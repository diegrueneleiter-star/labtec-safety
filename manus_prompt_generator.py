#!/usr/bin/env python3
"""
Manus AI Prompt Generator fuer labtec-safety.ch

Liest GA4-Reports (SUMMARY.md + CSV-Dateien) und generiert:
  - reports/MANUS_PROMPT.md  (Vollstaendiger Prompt mit allen Daten fuer Manus AI)

Manus AI kann Dokumente direkt verarbeiten und daraus Praesentationen,
Analysen und Berichte erstellen. Der Prompt enthaelt alle Daten inline,
da Manus keine separaten Datei-Uploads als Quelle unterstuetzt.

Voraussetzung: GA4-Daten muessen existieren:
  python3 ga4_analytics.py --all --csv --summary

Nutzung:
  python3 manus_prompt_generator.py
"""

import os
from datetime import datetime
from slide_deck_generator import SlideDeckGenerator, LABTEC_COLORS


class ManusPromptGenerator:

    def __init__(self, reports_dir=None):
        if reports_dir is None:
            reports_dir = os.path.join(
                os.path.dirname(os.path.abspath(__file__)), 'reports'
            )
        self.reports_dir = reports_dir
        self.deck = SlideDeckGenerator(reports_dir)

    def _zeitraum(self):
        return self.deck._extract_zeitraum()

    def _datum(self):
        return datetime.now().strftime('%d.%m.%Y')

    def generate_manus_prompt(self):
        """Generate MANUS_PROMPT.md with full inline data for Manus AI."""
        tage = self._zeitraum()
        datum = self._datum()

        sections = []

        # ── Task description for Manus ──────────────────────────────
        sections.append('# Aufgabe fuer Manus AI')
        sections.append('')
        sections.append(
            'Erstelle ein professionelles Pitch Deck / Web-Analytics Report '
            'als **PDF-Praesentation** basierend auf den folgenden echten GA4-Daten '
            'von labtec-safety.ch.'
        )
        sections.append('')
        sections.append('## Anforderungen')
        sections.append('')
        sections.append('1. **Format:** PDF-Praesentation (Querformat, 16:9)')
        sections.append('2. **Sprache:** Deutsch')
        sections.append(f'3. **Zeitraum:** Letzte {tage} Tage (Stand: {datum})')
        sections.append('4. **Design-Vorgaben:**')
        sections.append('   - Modern, datenfokussiert, clean')
        sections.append('   - Hauptfarben: Dunkelblau `#1e326e`, Gruen `#009b91`')
        sections.append('   - Heller Hintergrund (weiss oder sehr helles Grau)')
        sections.append('   - Sans-Serif-Schrift (z.B. Inter, Helvetica, Arial)')
        sections.append('   - Daten visuell darstellen: Charts, Diagramme, KPI-Karten')
        sections.append('5. **Wichtig:**')
        sections.append('   - Alle Zahlen exakt uebernehmen (echte GA4-Daten)')
        sections.append('   - Waehrung: CHF (Schweizer Franken)')
        sections.append('   - DACH-Markt / Schweizer E-Commerce-Kontext')
        sections.append('   - Professioneller Business-Report-Stil')
        sections.append('')

        # ── Slide structure ─────────────────────────────────────────
        sections.append('## Folien-Struktur (15 Slides)')
        sections.append('')
        slides = [
            ('Titelfolie', 'Web-Analytics Report — labtec-safety.ch'),
            ('Executive Summary', '4 KPI-Karten: Sessions, Umsatz, Conversion-Rate, Avg. Warenkorbwert'),
            ('Traffic & Akquisition', 'Top-10 Traffic-Quellen als Tabelle + Channel-Performance-Chart'),
            ('Neue vs. Wiederkehrende Nutzer', 'Vergleichstabelle mit Metriken'),
            ('Top-Seiten & Engagement', 'Meistbesuchte Seiten + Landing Pages'),
            ('E-Commerce Ueberblick', 'Transaktionen, Umsatz nach Quelle'),
            ('Produkt-Performance', 'Top-Produkte nach Umsatz als Balkendiagramm'),
            ('Warenkorb-Analyse', 'Conversion-Funnel + Abbruchrate'),
            ('Erstakquise-Kanaele & Kanal-Effizienz', 'ROI pro Kanal'),
            ('Kategorie-Performance & Produkt-Stickiness', 'Produktkategorien im Vergleich'),
            ('Monatstrend & Saisonalitaet', 'Liniendiagramm ueber Zeit'),
            ('Geraete & Browser', 'Desktop/Mobile/Tablet-Split als Donut-Chart'),
            ('Geografie', 'Laender + Top-Staedte (DACH-Fokus)'),
            ('Zeitliche Muster', 'Wochentag + Tageszeit Heatmap'),
            ('Probleme & Empfehlungen', 'High-Bounce-Seiten, UX-Issues, Handlungsempfehlungen'),
        ]
        for i, (title, desc) in enumerate(slides, 1):
            sections.append(f'{i}. **{title}:** {desc}')
        sections.append('')

        # ── Color palette ───────────────────────────────────────────
        sections.append('## Farbpalette Labtec')
        sections.append('| Kategorie | Farbe |')
        sections.append('|-----------|-------|')
        for name, color in LABTEC_COLORS.items():
            sections.append(f'| {name} | `{color}` |')
        sections.append('')

        # ── Separator ───────────────────────────────────────────────
        sections.append('---')
        sections.append('')
        sections.append('# GA4-Daten (alle Zahlen exakt uebernehmen)')
        sections.append('')

        # ── Executive Summary from SUMMARY.md ───────────────────────
        sections.append('## Executive Summary')
        for title in [
            'Traffic & Akquisition',
            'Nutzerverhalten & Engagement',
            'E-Commerce Performance',
            'Geraete & Technologie',
        ]:
            content = self.deck._extract_summary_section(title)
            if content:
                sections.append(f'**{title}:**')
                sections.append(content)
                sections.append('')
        sections.append('')

        # ── All data sections ───────────────────────────────────────
        data_sections = [
            ('Traffic & Akquisition', [
                ('Traffic-Quellen (Top 10)', 'traffic_sources.csv', 10),
                ('Channel-Performance', 'channel_performance.csv', None),
            ]),
            ('Neue vs. Wiederkehrende Nutzer', [
                (None, 'new_vs_returning.csv', None),
            ]),
            ('Top-Seiten & Engagement', [
                ('Top-Seiten', 'top_pages.csv', 15),
                ('Landing Pages', 'landing_pages.csv', 10),
            ]),
            ('E-Commerce Ueberblick', [
                ('Transaktionen', 'ecommerce_transactions.csv', None),
                ('Umsatz nach Quelle', 'ecommerce_revenue_by_source.csv', 10),
            ]),
            ('Produkt-Performance', [
                (None, 'product_performance.csv', 15),
            ]),
            ('Warenkorb-Analyse', [
                (None, 'cart_abandonment.csv', None),
            ]),
            ('Erstakquise-Kanaele', [
                (None, 'first_touch_attribution.csv', None),
            ]),
            ('Produktkategorie-Performance', [
                (None, 'product_category_performance.csv', None),
            ]),
            ('Conversion Funnel', [
                (None, 'conversion_funnel.csv', None),
            ]),
            ('Kanal-Effizienz (ROI)', [
                (None, 'channel_revenue_efficiency.csv', None),
            ]),
            ('Warenkorbwert-Trend (AOV)', [
                (None, 'aov_trend.csv', None),
            ]),
            ('Wiederkaufrate', [
                (None, 'repeat_purchase_rate.csv', None),
            ]),
            ('Landing-Page-Effizienz', [
                (None, 'landing_page_efficiency.csv', None),
            ]),
            ('Mobile Conversion Gap', [
                (None, 'mobile_conversion_gap.csv', None),
            ]),
            ('Monatstrend & Saisonalitaet', [
                (None, 'monthly_trend.csv', None),
            ]),
            ('Produkt-Stickiness', [
                (None, 'product_stickiness.csv', 20),
            ]),
            ('Geraete & Browser', [
                ('Geraete', 'device_split.csv', None),
                ('Browser', 'browser_stats.csv', 8),
                ('Betriebssysteme', 'os_stats.csv', 8),
            ]),
            ('Geografie', [
                ('Laender', 'geo_countries.csv', 10),
                ('Staedte', 'geo_cities.csv', 15),
            ]),
            ('Zeitliche Muster', [
                ('Wochentag', 'day_of_week.csv', None),
                ('Tageszeit', 'hour_of_day.csv', None),
            ]),
        ]

        for section_title, csvs in data_sections:
            sections.append(f'## {section_title}')
            for sub_title, csv_file, max_rows in csvs:
                if sub_title:
                    sections.append(f'### {sub_title}')
                sections.append(
                    self.deck._csv_to_markdown(csv_file, max_rows=max_rows)
                    if max_rows
                    else self.deck._csv_to_markdown(csv_file)
                )
                sections.append('')
            sections.append('')

        # ── Probleme & Empfehlungen ─────────────────────────────────
        sections.append('## Probleme & Empfehlungen')
        problems = self.deck._extract_summary_section('Problem-Erkennung')
        ux = self.deck._extract_summary_section('UX-Analyse')
        content = problems or ux or '*Keine Probleme erkannt.*'
        sections.append(content)
        sections.append('')
        sections.append('### High-Bounce-Seiten')
        sections.append(
            self.deck._csv_to_markdown('high_bounce_pages.csv', max_rows=10)
        )
        sections.append('')

        full_doc = '\n'.join(sections)

        # ── Write file ──────────────────────────────────────────────
        os.makedirs(self.reports_dir, exist_ok=True)
        out_path = os.path.join(self.reports_dir, 'MANUS_PROMPT.md')
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(full_doc)
        print(f'Manus AI Prompt gespeichert: {out_path}')

        return out_path


def generate_manus_prompt():
    """Convenience function to generate Manus AI prompt file."""
    gen = ManusPromptGenerator()
    return gen.generate_manus_prompt()


if __name__ == '__main__':
    out_path = generate_manus_prompt()
    print(f'\nFertig! Datei erstellt:')
    print(f'  {out_path}')
    print(f'\nNutzung:')
    print(f'  1. Oeffne manus.im')
    print(f'  2. Neuen Chat starten')
    print(f'  3. Inhalt von {out_path} einfuegen')
    print(f'  4. Manus erstellt die Praesentation als PDF')
