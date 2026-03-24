"""
Slide Deck Prompt-Paket Generator fuer labtec-safety.ch

Liest GA4-Reports (SUMMARY.md + CSV-Dateien) und generiert:
  - reports/SLIDE_DECK_PROMPT.md  (Prompt-Paket fuer NotebookLM)
  - reports/slide_preview.html    (HTML-Vorschau, optional)

Voraussetzung: GA4-Daten muessen existieren:
  python3 ga4_analytics.py --all --csv --summary

Nutzung:
  python3 slide_deck_generator.py              # Nur Prompt-Paket
  python3 slide_deck_generator.py --html       # + HTML-Vorschau
"""

import argparse
import csv
import os
import re
from datetime import datetime

REPORTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'reports')

LABTEC_COLORS = {
    'logo_dunkelblau': '#1e326e',
    'logo_gruen': '#009b91',
    'alkoholgeraete': '#eb640a',
    'drogentest': '#c8338a',
    'geschwindigkeitsanzeigen': '#ffcd00',
    'arbeitskleider': '#b9dc00',
    'schutzausruestung': '#4664af',
    'sicherheitsmesser': '#00a0e1',
    'feuerwehrbedarf': '#af0f09',
    'spezialeinsaetze': '#464646',
    'notduschen': '#00823c',
    'personalisierung': '#aabed2',
}

SCREENSHOT_PROMPTS = {
    'homepage': (
        'Screenshot of labtec-safety.ch homepage, professional Swiss safety '
        'equipment e-commerce shop, clean modern design with dark blue '
        '(#1e326e) and green (#009b91) branding, hero section with product '
        'categories'
    ),
    'top_pages': (
        'Screenshot of labtec-safety.ch product category page, professional '
        'grid layout showing safety equipment products with prices, Swiss '
        'e-commerce shop'
    ),
    'products': (
        'Screenshot of labtec-safety.ch product detail page, professional '
        'product image with description, price, and add-to-cart button, '
        'Swiss safety equipment shop'
    ),
    'cart': (
        'Screenshot of labtec-safety.ch shopping cart page, clean checkout '
        'layout with product list, quantities, and total, Swiss e-commerce'
    ),
    'mobile_desktop': (
        'Side-by-side comparison of labtec-safety.ch on mobile phone and '
        'desktop monitor, responsive design, Swiss safety equipment shop'
    ),
    'problems': (
        'Screenshot of labtec-safety.ch page with UX issues highlighted, '
        'annotated with red circles showing problem areas, professional '
        'audit style'
    ),
}


class SlideDeckGenerator:

    def __init__(self, reports_dir=REPORTS_DIR):
        self.reports_dir = reports_dir
        self._summary = None
        self._csv_cache = {}

    # ── Daten laden ──────────────────────────────────────────────────

    def _read_summary(self):
        if self._summary is not None:
            return self._summary
        path = os.path.join(self.reports_dir, 'SUMMARY.md')
        if not os.path.exists(path):
            self._summary = ''
            return ''
        with open(path, encoding='utf-8') as f:
            self._summary = f.read()
        return self._summary

    def _read_csv(self, filename):
        if filename in self._csv_cache:
            return self._csv_cache[filename]
        path = os.path.join(self.reports_dir, filename)
        if not os.path.exists(path):
            self._csv_cache[filename] = []
            return []
        with open(path, encoding='utf-8') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        self._csv_cache[filename] = rows
        return rows

    def _discover_csvs(self):
        if not os.path.isdir(self.reports_dir):
            return []
        return sorted(f for f in os.listdir(self.reports_dir) if f.endswith('.csv'))

    def _csv_to_markdown(self, filename, max_rows=None):
        rows = self._read_csv(filename)
        if not rows:
            return f'*{filename} nicht vorhanden oder leer.*'
        headers = list(rows[0].keys())
        display = rows[:max_rows] if max_rows else rows
        lines = ['| ' + ' | '.join(headers) + ' |']
        lines.append('|' + '|'.join(' --- ' for _ in headers) + '|')
        for row in display:
            lines.append('| ' + ' | '.join(str(row.get(h, '')) for h in headers) + ' |')
        if max_rows and len(rows) > max_rows:
            lines.append(f'*... und {len(rows) - max_rows} weitere Zeilen (siehe Anhang)*')
        return '\n'.join(lines)

    def _extract_summary_section(self, section_title):
        summary = self._read_summary()
        if not summary:
            return ''
        pattern = rf'## {re.escape(section_title)}\n(.*?)(?=\n## |\Z)'
        match = re.search(pattern, summary, re.DOTALL)
        return match.group(1).strip() if match else ''

    def _extract_zeitraum(self):
        summary = self._read_summary()
        match = re.search(r'Letzte (\d+) Tage', summary)
        return match.group(1) if match else '90'

    def _infsh_command(self, key):
        prompt = SCREENSHOT_PROMPTS.get(key, '')
        if not prompt:
            return ''
        return (
            f"```bash\n"
            f"infsh app run google/gemini-3-1-flash-image-preview --input '{{\n"
            f'  "prompt": "{prompt}",\n'
            f'  "enable_google_search": true,\n'
            f'  "aspect_ratio": "16:9",\n'
            f'  "resolution": "2K"\n'
            f"}}'\n"
            f"```"
        )

    # ── Slides ───────────────────────────────────────────────────────

    def _slide_title(self):
        tage = self._extract_zeitraum()
        return (
            f'## Slide 1: Titel\n\n'
            f'### Anweisung\n'
            f'Erstelle eine Titelfolie im Stil "Soft Corporate Dashboard". '
            f'Hintergrund: helles Blaugrau (#f8f9fc). Zentriert: '
            f'Labtec-Logo (dunkelblau #1e326e), darunter Titel und Untertitel.\n\n'
            f'### Daten\n'
            f'- **Titel:** Web-Analytics Report — labtec-safety.ch\n'
            f'- **Untertitel:** Datenbasierte Analyse der letzten {tage} Tage\n'
            f'- **Datum:** {datetime.now().strftime("%d.%m.%Y")}\n\n'
            f'### Screenshot-Platzhalter\n'
            f'[SCREENSHOT: Homepage labtec-safety.ch — Hero-Bereich als Hintergrundbild]\n\n'
            f'{self._infsh_command("homepage")}\n'
        )

    def _slide_executive_summary(self):
        summary = self._read_summary()
        sections = []
        for title in ['Traffic & Akquisition', 'Nutzerverhalten & Engagement',
                       'E-Commerce Performance', 'Geraete & Technologie']:
            content = self._extract_summary_section(title)
            if content:
                sections.append(f'**{title}:**\n{content}')

        return (
            f'## Slide 2: Executive Summary\n\n'
            f'### Anweisung\n'
            f'Erstelle 4 KPI-Karten nebeneinander (weiss, abgerundete Ecken 10px, '
            f'dezenter Schatten). Jede Karte zeigt eine Hauptmetrik gross in '
            f'Labtec-Gruen (#009b91) mit Label darunter in Dunkelblau (#1e326e). '
            f'Titel der Folie in Dunkelblau.\n\n'
            f'### Daten\n'
            + ('\n\n'.join(sections) if sections else '*Keine Summary-Daten verfuegbar.*')
            + '\n'
        )

    def _slide_traffic(self):
        return (
            f'## Slide 3: Traffic & Akquisition\n\n'
            f'### Anweisung\n'
            f'Zeige ein horizontales Balkendiagramm der Top-10 Traffic-Quellen '
            f'(Labtec-Gruen #009b91 fuer Balken). Daneben eine kleine Tabelle '
            f'mit Channel-Performance. Alle Werte exakt uebernehmen.\n\n'
            f'### Daten\n'
            f'#### Traffic-Quellen (Top 10)\n'
            f'{self._csv_to_markdown("traffic_sources.csv", max_rows=10)}\n\n'
            f'#### Channel-Performance\n'
            f'{self._csv_to_markdown("channel_performance.csv")}\n'
        )

    def _slide_users(self):
        return (
            f'## Slide 4: Neue vs. Wiederkehrende Nutzer\n\n'
            f'### Anweisung\n'
            f'Erstelle ein Donut-Diagramm (Dunkelblau #1e326e fuer neue, '
            f'Gruen #009b91 fuer wiederkehrende Nutzer). Daneben die '
            f'wichtigsten Metriken als KPI-Karten. Zeige zusaetzlich den '
            f'Umsatz-Split (Umsatz, Kaeufe, Avg. Warenkorbwert) pro Nutzertyp '
            f'als separate KPI-Zeile.\n\n'
            f'### Daten\n'
            f'{self._csv_to_markdown("new_vs_returning.csv")}\n'
        )

    def _slide_pages(self):
        return (
            f'## Slide 5: Top-Seiten & Engagement\n\n'
            f'### Anweisung\n'
            f'Zeige eine Rangliste der meistbesuchten Seiten als Tabelle mit '
            f'farbigen Balken fuer Views. Landing Pages als zweite kleine '
            f'Tabelle. Screenshots der Top-Seiten einbinden.\n\n'
            f'### Daten\n'
            f'#### Top-Seiten\n'
            f'{self._csv_to_markdown("top_pages.csv", max_rows=15)}\n\n'
            f'#### Landing Pages\n'
            f'{self._csv_to_markdown("landing_pages.csv", max_rows=10)}\n\n'
            f'### Screenshot-Platzhalter\n'
            f'[SCREENSHOT: Top-Kategorieseite von labtec-safety.ch]\n\n'
            f'{self._infsh_command("top_pages")}\n'
        )

    def _slide_ecommerce(self):
        transactions = self._read_csv('ecommerce_transactions.csv')
        revenue_by_source = self._read_csv('ecommerce_revenue_by_source.csv')
        if not transactions and not revenue_by_source:
            return (
                f'## Slide 6: E-Commerce Ueberblick\n\n'
                f'*Keine E-Commerce-Daten verfuegbar. Slide wird uebersprungen.*\n'
            )
        return (
            f'## Slide 6: E-Commerce Ueberblick\n\n'
            f'### Anweisung\n'
            f'Zeige Umsatz-KPIs als grosse Karten (Gruen #009b91). '
            f'Darunter ein Balkendiagramm der Revenue nach Quelle. '
            f'Alle Betraege exakt uebernehmen.\n\n'
            f'### Daten\n'
            f'#### Transaktionen\n'
            f'{self._csv_to_markdown("ecommerce_transactions.csv")}\n\n'
            f'#### Umsatz nach Quelle\n'
            f'{self._csv_to_markdown("ecommerce_revenue_by_source.csv", max_rows=10)}\n'
        )

    def _slide_products(self):
        products = self._read_csv('product_performance.csv')
        if not products:
            return (
                f'## Slide 7: Produkt-Performance\n\n'
                f'*Keine Produktdaten verfuegbar. Slide wird uebersprungen.*\n'
            )
        return (
            f'## Slide 7: Produkt-Performance\n\n'
            f'### Anweisung\n'
            f'Zeige die Top-Produkte als Rangliste mit kleinen Produkt-'
            f'Thumbnails. Umsatz als Balken in Labtec-Gruen. '
            f'Produktseiten-Screenshots einbinden.\n\n'
            f'### Daten\n'
            f'{self._csv_to_markdown("product_performance.csv", max_rows=15)}\n\n'
            f'### Screenshot-Platzhalter\n'
            f'[SCREENSHOT: Produktseite von labtec-safety.ch]\n\n'
            f'{self._infsh_command("products")}\n'
        )

    def _slide_cart(self):
        cart = self._read_csv('cart_abandonment.csv')
        if not cart:
            return (
                f'## Slide 8: Warenkorb-Analyse\n\n'
                f'*Keine Warenkorb-Daten verfuegbar. Slide wird uebersprungen.*\n'
            )
        return (
            f'## Slide 8: Warenkorb-Analyse\n\n'
            f'### Anweisung\n'
            f'Zeige einen Conversion-Funnel (Trichter-Diagramm): '
            f'Warenkorb → Checkout → Kauf. Abbruchrate prominent in '
            f'Warnfarbe (#af0f09). Screenshot des Warenkorbs einbinden.\n\n'
            f'### Daten\n'
            f'{self._csv_to_markdown("cart_abandonment.csv")}\n\n'
            f'### Screenshot-Platzhalter\n'
            f'[SCREENSHOT: Warenkorb-Seite von labtec-safety.ch]\n\n'
            f'{self._infsh_command("cart")}\n'
        )

    def _slide_devices(self):
        return (
            f'## Slide 9: Geraete & Browser\n\n'
            f'### Anweisung\n'
            f'Zeige ein Donut-Diagramm der Geraete-Verteilung '
            f'(Desktop/Mobile/Tablet). Daneben Browser-Statistiken als '
            f'kleine Balken. Screenshot: Mobile vs. Desktop Vergleich.\n\n'
            f'### Daten\n'
            f'#### Geraete\n'
            f'{self._csv_to_markdown("device_split.csv")}\n\n'
            f'#### Browser\n'
            f'{self._csv_to_markdown("browser_stats.csv", max_rows=8)}\n\n'
            f'#### Betriebssysteme\n'
            f'{self._csv_to_markdown("os_stats.csv", max_rows=8)}\n\n'
            f'### Screenshot-Platzhalter\n'
            f'[SCREENSHOT: Mobile vs. Desktop Ansicht von labtec-safety.ch]\n\n'
            f'{self._infsh_command("mobile_desktop")}\n'
        )

    def _slide_geography(self):
        return (
            f'## Slide 10: Geografie\n\n'
            f'### Anweisung\n'
            f'Zeige eine Karte der DACH-Region mit Farbintensitaet nach '
            f'Nutzerzahl. Daneben Top-Staedte als Rangliste. '
            f'Farbe: Labtec-Dunkelblau (#1e326e) Abstufungen.\n\n'
            f'### Daten\n'
            f'#### Laender\n'
            f'{self._csv_to_markdown("geo_countries.csv", max_rows=10)}\n\n'
            f'#### Staedte\n'
            f'{self._csv_to_markdown("geo_cities.csv", max_rows=15)}\n'
        )

    def _slide_time_patterns(self):
        return (
            f'## Slide 11: Zeitliche Muster\n\n'
            f'### Anweisung\n'
            f'Zeige zwei Diagramme nebeneinander: '
            f'(1) Balkendiagramm Sessions nach Wochentag, '
            f'(2) Liniendiagramm Sessions nach Tageszeit. '
            f'Farbe: Labtec-Gruen (#009b91).\n\n'
            f'### Daten\n'
            f'#### Wochentag\n'
            f'{self._csv_to_markdown("day_of_week.csv")}\n\n'
            f'#### Tageszeit\n'
            f'{self._csv_to_markdown("hour_of_day.csv")}\n'
        )

    def _slide_problems(self):
        problems = self._extract_summary_section('Problem-Erkennung')
        ux = self._extract_summary_section('UX-Analyse')
        content = problems or ux or '*Keine Probleme erkannt.*'
        return (
            f'## Slide 12: Probleme & Empfehlungen\n\n'
            f'### Anweisung\n'
            f'Erstelle eine zweispaltige Folie: Links Probleme '
            f'(rote Badges #af0f09), rechts Empfehlungen (gruene Badges '
            f'#009b91). Jeder Punkt als Karte mit Icon. '
            f'Screenshots der Problemseiten einbinden.\n\n'
            f'### Daten\n'
            f'{content}\n\n'
            f'#### High-Bounce-Seiten\n'
            f'{self._csv_to_markdown("high_bounce_pages.csv", max_rows=10)}\n\n'
            f'### Screenshot-Platzhalter\n'
            f'[SCREENSHOT: Problemseiten mit UX-Annotationen]\n\n'
            f'{self._infsh_command("problems")}\n'
        )

    # ── Business Insight Slides ─────────────────────────────────────

    def _slide_first_touch(self):
        data = self._read_csv('first_touch_attribution.csv')
        if not data:
            return (
                f'## Slide: Erstakquise-Kanaele\n\n'
                f'*Keine Erstakquise-Daten verfuegbar.*\n'
            )
        return (
            f'## Slide: Erstakquise-Kanaele\n\n'
            f'### Anweisung\n'
            f'Horizontales Balkendiagramm: Welche Kanaele bringen zahlende '
            f'Kunden? Sortiert nach Umsatz. Farbe: Labtec-Dunkelblau (#1e326e). '
            f'CHF/User als sekundaere Metrik hervorheben.\n\n'
            f'### Daten\n'
            f'{self._csv_to_markdown("first_touch_attribution.csv")}\n'
        )

    def _slide_category_performance(self):
        data = self._read_csv('product_category_performance.csv')
        if not data:
            return (
                f'## Slide: Produktkategorie-Performance\n\n'
                f'*Keine Kategorie-Daten verfuegbar.*\n'
            )
        return (
            f'## Slide: Produktkategorie-Performance\n\n'
            f'### Anweisung\n'
            f'Treemap oder gestapeltes Balkendiagramm der Produktkategorien '
            f'nach Umsatz. Verwende die Labtec-Kategoriefarben. '
            f'Cart/View-Rate als Effizienz-Indikator hervorheben.\n\n'
            f'### Daten\n'
            f'{self._csv_to_markdown("product_category_performance.csv")}\n'
        )

    def _slide_conversion_funnel(self):
        data = self._read_csv('conversion_funnel.csv')
        if not data:
            return (
                f'## Slide: Conversion Funnel\n\n'
                f'*Keine Funnel-Daten verfuegbar.*\n'
            )
        return (
            f'## Slide: Conversion Funnel\n\n'
            f'### Anweisung\n'
            f'Trichter-Diagramm: Sessions → Warenkorb → Kauf. '
            f'Drop-off-Raten zwischen jeder Stufe prominent anzeigen. '
            f'Gruen (#009b91) fuer Conversions, Rot (#af0f09) fuer Drop-offs. '
            f'Gesamtumsatz als grosse KPI-Karte.\n\n'
            f'### Daten\n'
            f'{self._csv_to_markdown("conversion_funnel.csv")}\n'
        )

    def _slide_channel_efficiency(self):
        data = self._read_csv('channel_revenue_efficiency.csv')
        if not data:
            return (
                f'## Slide: Kanal-Effizienz\n\n'
                f'*Keine Effizienz-Daten verfuegbar.*\n'
            )
        return (
            f'## Slide: Kanal-Effizienz (ROI)\n\n'
            f'### Anweisung\n'
            f'Ranking-Tabelle der Kanaele nach CHF/Session und CHF/User. '
            f'Beste Kanaele mit gruenen Badges (#009b91) hervorheben. '
            f'Zeigt welche Kanaele den hoechsten ROI liefern.\n\n'
            f'### Daten\n'
            f'{self._csv_to_markdown("channel_revenue_efficiency.csv")}\n'
        )

    def _slide_aov_trend(self):
        data = self._read_csv('aov_trend.csv')
        if not data:
            return (
                f'## Slide: Warenkorbwert-Trend\n\n'
                f'*Keine AOV-Daten verfuegbar.*\n'
            )
        return (
            f'## Slide: Warenkorbwert-Trend (AOV)\n\n'
            f'### Anweisung\n'
            f'Liniendiagramm des durchschnittlichen Warenkorbwerts ueber Zeit. '
            f'Trendlinie einzeichnen. Farbe: Labtec-Gruen (#009b91). '
            f'Vergleich erste vs. zweite Haelfte als KPI-Karten.\n\n'
            f'### Daten\n'
            f'{self._csv_to_markdown("aov_trend.csv")}\n'
        )

    def _slide_repeat_purchase(self):
        data = self._read_csv('repeat_purchase_rate.csv')
        if not data:
            return (
                f'## Slide: Wiederkaufrate\n\n'
                f'*Keine Wiederkauf-Daten verfuegbar.*\n'
            )
        return (
            f'## Slide: Wiederkaufrate\n\n'
            f'### Anweisung\n'
            f'Donut-Diagramm: Anteil Neukunden vs. Wiederkehrende an '
            f'Gesamtkaeufen. Kaeufe/User als Effizienz-Metrik. '
            f'Dunkelblau (#1e326e) fuer Neukunden, Gruen (#009b91) fuer '
            f'Wiederkehrende. Zeigt ob das Geschaeft von Stammkunden lebt.\n\n'
            f'### Daten\n'
            f'{self._csv_to_markdown("repeat_purchase_rate.csv")}\n'
        )

    def _slide_landing_efficiency(self):
        data = self._read_csv('landing_page_efficiency.csv')
        if not data:
            return (
                f'## Slide: Landing-Page-Effizienz\n\n'
                f'*Keine Landing-Page-Umsatz-Daten verfuegbar.*\n'
            )
        return (
            f'## Slide: Landing-Page-Effizienz\n\n'
            f'### Anweisung\n'
            f'Rangliste der Landing Pages nach Umsatz. CHF/Session und '
            f'Conversion-Rate als Balken. Seiten mit hohem Traffic aber '
            f'niedrigem Umsatz rot markieren (#af0f09) = Optimierungspotenzial.\n\n'
            f'### Daten\n'
            f'{self._csv_to_markdown("landing_page_efficiency.csv")}\n'
        )

    def _slide_mobile_gap(self):
        data = self._read_csv('mobile_conversion_gap.csv')
        if not data:
            return (
                f'## Slide: Mobile Conversion Gap\n\n'
                f'*Keine Mobile-Gap-Daten verfuegbar.*\n'
            )
        return (
            f'## Slide: Mobile Conversion Gap\n\n'
            f'### Anweisung\n'
            f'Vergleichstabelle Mobile vs. Desktop: Conversion-Rate, '
            f'CHF/Session, Bounce-Rate. Gap als Delta hervorheben. '
            f'Wenn Mobile deutlich schlechter: Warnfarbe (#af0f09). '
            f'Zeigt wie viel Umsatz durch Mobile-Optimierung moeglich waere.\n\n'
            f'### Daten\n'
            f'{self._csv_to_markdown("mobile_conversion_gap.csv")}\n'
        )

    def _slide_monthly_trend(self):
        data = self._read_csv('monthly_trend.csv')
        if not data:
            return (
                f'## Slide: Monatstrend\n\n'
                f'*Keine Monatstrend-Daten verfuegbar.*\n'
            )
        return (
            f'## Slide: Monatstrend & Saisonalitaet\n\n'
            f'### Anweisung\n'
            f'Kombinations-Diagramm: Balken fuer Umsatz (Gruen #009b91), '
            f'Linie fuer Sessions (Dunkelblau #1e326e). '
            f'Zeigt saisonale Schwankungen und Wachstumstrend. '
            f'Avg. Warenkorbwert als zweite Achse.\n\n'
            f'### Daten\n'
            f'{self._csv_to_markdown("monthly_trend.csv")}\n'
        )

    def _slide_product_stickiness(self):
        data = self._read_csv('product_stickiness.csv')
        if not data:
            return (
                f'## Slide: Produkt-Stickiness\n\n'
                f'*Keine Stickiness-Daten verfuegbar.*\n'
            )
        return (
            f'## Slide: Produkt-Stickiness\n\n'
            f'### Anweisung\n'
            f'Bubble-Chart oder Scatter-Plot: X=View→Cart%, Y=Cart→Buy%, '
            f'Groesse=Views. Produkte mit hohen Views aber niedrigem '
            f'View→Cart in Rot markieren (Preishuerde). Produkte mit hohem '
            f'Cart aber niedrigem Buy in Orange markieren (Checkout-Problem). '
            f'Top-Performer in Gruen (#009b91).\n\n'
            f'### Daten\n'
            f'{self._csv_to_markdown("product_stickiness.csv", max_rows=20)}\n'
        )

    # ── Output generieren ────────────────────────────────────────────

    def generate_prompt_package(self):
        tage = self._extract_zeitraum()
        now = datetime.now().strftime('%d.%m.%Y %H:%M')

        slides = [
            self._slide_title(),
            self._slide_executive_summary(),
            self._slide_traffic(),
            self._slide_users(),
            self._slide_pages(),
            self._slide_ecommerce(),
            self._slide_products(),
            self._slide_cart(),
            self._slide_first_touch(),
            self._slide_category_performance(),
            self._slide_conversion_funnel(),
            self._slide_channel_efficiency(),
            self._slide_aov_trend(),
            self._slide_repeat_purchase(),
            self._slide_landing_efficiency(),
            self._slide_mobile_gap(),
            self._slide_monthly_trend(),
            self._slide_product_stickiness(),
            self._slide_devices(),
            self._slide_geography(),
            self._slide_problems(),
        ]

        colors_table = '\n'.join(
            f'| {name} | `{color}` |' for name, color in LABTEC_COLORS.items()
        )

        header = (
            f'# Slide Deck: labtec-safety.ch Analytics\n'
            f'> Generiert: {now} | Zeitraum: {tage} Tage\n\n'
            f'---\n\n'
            f'## DATENINTEGRITAET\n'
            f'- ALLE Zahlen in diesem Dokument sind ECHTE GA4-Daten\n'
            f'- Werte WOERTLICH uebernehmen, NICHT runden oder schaetzen\n'
            f'- Bei ungewoehnlichen Zahlen: trotzdem korrekt darstellen\n'
            f'- Keine eigenen Berechnungen durchfuehren\n\n'
            f'## Design-Richtlinien: Soft Corporate Dashboard\n'
            f'- **Hintergrund:** #f8f9fc (helles Blaugrau)\n'
            f'- **Karten:** Weiss #ffffff, border-radius: 10px, dezenter Schatten\n'
            f'- **Primaerfarbe (Titel/Header):** #1e326e (Labtec Dunkelblau)\n'
            f'- **Akzentfarbe (KPIs/Highlights):** #009b91 (Labtec Gruen)\n'
            f'- **Warnfarbe (Probleme):** #af0f09 (Feuerwehr-Rot)\n'
            f'- **Schrift:** Inter oder Source Sans Pro (clean sans-serif)\n'
            f'- **Ecken:** 10px auf Karten, 6px auf Badges\n'
            f'- **Stil:** Schlicht, modern, professionell, datenfokussiert\n\n'
            f'### Farbpalette\n'
            f'| Kategorie | Farbe |\n'
            f'|-----------|-------|\n'
            f'{colors_table}\n\n'
            f'---\n\n'
        )

        # Anhang: alle CSVs als Markdown-Tabellen
        appendix_parts = ['\n---\n\n## Anhang: Rohdaten\n']
        for csv_file in self._discover_csvs():
            appendix_parts.append(f'\n### {csv_file}\n')
            appendix_parts.append(self._csv_to_markdown(csv_file))
            appendix_parts.append('')

        content = header + '\n'.join(slides) + '\n'.join(appendix_parts)

        os.makedirs(self.reports_dir, exist_ok=True)
        path = os.path.join(self.reports_dir, 'SLIDE_DECK_PROMPT.md')
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Prompt-Paket gespeichert: {path}')
        return path

    def generate_html_preview(self):
        tage = self._extract_zeitraum()
        now = datetime.now().strftime('%d.%m.%Y %H:%M')

        slide_methods = [
            ('Titel', self._slide_title),
            ('Executive Summary', self._slide_executive_summary),
            ('Traffic & Akquisition', self._slide_traffic),
            ('Neue vs. Wiederkehrende', self._slide_users),
            ('Top-Seiten', self._slide_pages),
            ('E-Commerce', self._slide_ecommerce),
            ('Produkte', self._slide_products),
            ('Warenkorb', self._slide_cart),
            ('Erstakquise-Kanaele', self._slide_first_touch),
            ('Kategorie-Performance', self._slide_category_performance),
            ('Conversion Funnel', self._slide_conversion_funnel),
            ('Kanal-Effizienz', self._slide_channel_efficiency),
            ('Warenkorbwert-Trend', self._slide_aov_trend),
            ('Wiederkaufrate', self._slide_repeat_purchase),
            ('Landing-Page-Effizienz', self._slide_landing_efficiency),
            ('Mobile Conversion Gap', self._slide_mobile_gap),
            ('Monatstrend', self._slide_monthly_trend),
            ('Produkt-Stickiness', self._slide_product_stickiness),
            ('Geraete & Browser', self._slide_devices),
            ('Geografie', self._slide_geography),
            ('Probleme', self._slide_problems),
        ]

        slides_html = []
        for i, (title, method) in enumerate(slide_methods, 1):
            md_content = method()
            # Convert markdown tables to HTML
            html_content = self._md_to_html(md_content)
            slides_html.append(
                f'<div class="slide" id="slide-{i}">'
                f'<div class="slide-number">Slide {i}</div>'
                f'{html_content}'
                f'</div>'
            )

        html = f'''<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Slide Deck Vorschau — labtec-safety.ch</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');

  * {{ margin: 0; padding: 0; box-sizing: border-box; }}

  body {{
    font-family: 'Inter', -apple-system, sans-serif;
    background: #e8eaf0;
    color: #333;
    padding: 2rem;
  }}

  .header {{
    text-align: center;
    margin-bottom: 2rem;
    color: #1e326e;
  }}
  .header h1 {{ font-size: 1.8rem; font-weight: 700; }}
  .header p {{ color: #666; margin-top: 0.3rem; }}

  .slide {{
    background: #f8f9fc;
    border-radius: 12px;
    padding: 2.5rem;
    margin-bottom: 2rem;
    max-width: 960px;
    margin-left: auto;
    margin-right: auto;
    box-shadow: 0 2px 12px rgba(30, 50, 110, 0.08);
    position: relative;
  }}

  .slide-number {{
    position: absolute;
    top: 1rem;
    right: 1.5rem;
    background: #1e326e;
    color: white;
    font-size: 0.75rem;
    font-weight: 600;
    padding: 0.25rem 0.75rem;
    border-radius: 6px;
  }}

  .slide h2 {{
    color: #1e326e;
    font-size: 1.4rem;
    margin-bottom: 1rem;
    padding-bottom: 0.5rem;
    border-bottom: 2px solid #009b91;
  }}

  .slide h3 {{
    color: #009b91;
    font-size: 1rem;
    margin: 1.2rem 0 0.5rem;
    font-weight: 600;
  }}

  .slide h4 {{
    color: #1e326e;
    font-size: 0.9rem;
    margin: 1rem 0 0.4rem;
  }}

  .slide p, .slide li {{
    font-size: 0.9rem;
    line-height: 1.6;
    color: #444;
  }}

  .slide ul {{ padding-left: 1.2rem; }}

  .slide table {{
    width: 100%;
    border-collapse: collapse;
    margin: 0.8rem 0;
    font-size: 0.82rem;
  }}

  .slide th {{
    background: #1e326e;
    color: white;
    padding: 0.5rem 0.7rem;
    text-align: left;
    font-weight: 600;
  }}

  .slide th:first-child {{ border-radius: 6px 0 0 0; }}
  .slide th:last-child {{ border-radius: 0 6px 0 0; }}

  .slide td {{
    padding: 0.45rem 0.7rem;
    border-bottom: 1px solid #e8eaf0;
  }}

  .slide tr:nth-child(even) td {{ background: #f0f2f8; }}
  .slide tr:hover td {{ background: #e3f0ef; }}

  .screenshot-placeholder {{
    background: linear-gradient(135deg, #e8eaf0, #d5dae6);
    border: 2px dashed #009b91;
    border-radius: 10px;
    padding: 2rem;
    text-align: center;
    color: #009b91;
    font-weight: 600;
    margin: 1rem 0;
  }}

  .code-block {{
    background: #1e326e;
    color: #a8d8d0;
    padding: 1rem;
    border-radius: 8px;
    font-family: 'SF Mono', Monaco, monospace;
    font-size: 0.78rem;
    overflow-x: auto;
    margin: 0.5rem 0;
    white-space: pre-wrap;
    word-break: break-all;
  }}

  .skip-notice {{
    background: #fff3e0;
    border-left: 4px solid #eb640a;
    padding: 1rem;
    border-radius: 0 8px 8px 0;
    color: #b85000;
    font-style: italic;
  }}

  .nav {{
    position: fixed;
    top: 50%;
    right: 1rem;
    transform: translateY(-50%);
    display: flex;
    flex-direction: column;
    gap: 0.3rem;
  }}

  .nav a {{
    display: block;
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background: #1e326e;
    opacity: 0.3;
    transition: opacity 0.2s;
  }}
  .nav a:hover {{ opacity: 1; }}
</style>
</head>
<body>

<div class="header">
  <h1>Slide Deck Vorschau</h1>
  <p>labtec-safety.ch Analytics | {tage} Tage | {now}</p>
</div>

<nav class="nav">
''' + '\n'.join(f'  <a href="#slide-{i}" title="Slide {i}"></a>' for i in range(1, 13)) + '''
</nav>

''' + '\n'.join(slides_html) + '''

</body>
</html>'''

        os.makedirs(self.reports_dir, exist_ok=True)
        path = os.path.join(self.reports_dir, 'slide_preview.html')
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f'HTML-Vorschau gespeichert: {path}')
        return path

    def _md_to_html(self, md):
        lines = md.split('\n')
        html_parts = []
        in_table = False
        in_code = False
        table_rows = []

        for line in lines:
            # Code blocks
            if line.strip().startswith('```'):
                if in_code:
                    in_code = False
                    html_parts.append('</div>')
                else:
                    in_code = True
                    html_parts.append('<div class="code-block">')
                continue
            if in_code:
                html_parts.append(line)
                continue

            # Screenshot placeholders
            if line.strip().startswith('[SCREENSHOT:'):
                desc = line.strip().strip('[]')
                html_parts.append(f'<div class="screenshot-placeholder">{desc}</div>')
                continue

            # Skip notices
            if line.strip().startswith('*Keine') or line.strip().startswith('*...'):
                text = line.strip().strip('*')
                html_parts.append(f'<div class="skip-notice">{text}</div>')
                continue

            # Tables
            if '|' in line and line.strip().startswith('|'):
                cells = [c.strip() for c in line.strip().strip('|').split('|')]
                if all(c.replace('-', '').replace(' ', '') == '' for c in cells):
                    continue  # separator row
                if not in_table:
                    in_table = True
                    html_parts.append('<table><thead><tr>')
                    html_parts.extend(f'<th>{c}</th>' for c in cells)
                    html_parts.append('</tr></thead><tbody>')
                else:
                    html_parts.append('<tr>')
                    html_parts.extend(f'<td>{c}</td>' for c in cells)
                    html_parts.append('</tr>')
                continue
            elif in_table:
                in_table = False
                html_parts.append('</tbody></table>')

            # Headers
            if line.startswith('#### '):
                html_parts.append(f'<h4>{line[5:]}</h4>')
            elif line.startswith('### '):
                html_parts.append(f'<h3>{line[4:]}</h3>')
            elif line.startswith('## '):
                html_parts.append(f'<h2>{line[3:]}</h2>')
            elif line.startswith('- **'):
                # Bold list items
                html_parts.append(f'<li>{line[2:]}</li>')
            elif line.startswith('- '):
                html_parts.append(f'<li>{line[2:]}</li>')
            elif line.strip():
                html_parts.append(f'<p>{line}</p>')

        if in_table:
            html_parts.append('</tbody></table>')

        return '\n'.join(html_parts)


def main():
    parser = argparse.ArgumentParser(
        description='Slide Deck Prompt-Paket Generator fuer labtec-safety.ch'
    )
    parser.add_argument(
        '--html', action='store_true',
        help='Zusaetzlich HTML-Vorschau generieren'
    )
    parser.add_argument(
        '--reports-dir', default=REPORTS_DIR,
        help=f'Verzeichnis mit GA4-Reports (Standard: {REPORTS_DIR})'
    )
    args = parser.parse_args()

    gen = SlideDeckGenerator(reports_dir=args.reports_dir)

    # Check if data exists
    summary_path = os.path.join(args.reports_dir, 'SUMMARY.md')
    csvs = gen._discover_csvs()
    if not os.path.exists(summary_path) and not csvs:
        print('FEHLER: Keine GA4-Daten gefunden.')
        print('Zuerst ausfuehren: python3 ga4_analytics.py --all --csv --summary')
        return

    print(f'Gefunden: SUMMARY.md={os.path.exists(summary_path)}, {len(csvs)} CSV-Dateien')

    gen.generate_prompt_package()

    if args.html:
        gen.generate_html_preview()

    print('\nFertig! Naechste Schritte:')
    print('  1. reports/SLIDE_DECK_PROMPT.md in NotebookLM hochladen')
    print('  2. Screenshots mit infsh-Befehlen generieren (siehe Prompt-Paket)')
    print('  3. Screenshots ebenfalls in NotebookLM hochladen')


if __name__ == '__main__':
    main()
