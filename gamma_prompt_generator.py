#!/usr/bin/env python3
"""
Gamma.app Prompt Generator fuer labtec-safety.ch

Liest GA4-Reports (SUMMARY.md + CSV-Dateien) und generiert:
  - reports/GAMMA_PROMPT.md       (Volldokument zum Upload als Quelle in Gamma)
  - reports/GAMMA_PASTE_PROMPT.txt (Kurzprompt zum Einfuegen in Gamma's Generate-Feld)

Voraussetzung: GA4-Daten muessen existieren:
  python3 ga4_analytics.py --all --csv --summary

Nutzung:
  python3 gamma_prompt_generator.py
"""

import os
from datetime import datetime
from slide_deck_generator import SlideDeckGenerator, LABTEC_COLORS


class GammaPromptGenerator:

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

    # ── Full document for Gamma upload ────────────────────────────────

    def generate_gamma_prompt(self):
        """Generate both GAMMA_PROMPT.md and GAMMA_PASTE_PROMPT.txt."""
        tage = self._zeitraum()
        datum = self._datum()

        # -- Build the full upload document --
        sections = []

        # Design note at the very top
        sections.append(
            'Design-Stil: Professionell, modern, datenfokussiert. '
            'Farben: Dunkelblau #1e326e, Gruen #009b91, Hintergrund hell. '
            'Schrift: Clean Sans-Serif.'
        )
        sections.append('')

        # Color palette
        sections.append('### Farbpalette Labtec')
        sections.append('| Kategorie | Farbe |')
        sections.append('|-----------|-------|')
        for name, color in LABTEC_COLORS.items():
            sections.append(f'| {name} | `{color}` |')
        sections.append('')

        # Title
        sections.append(f'# Web-Analytics Report — labtec-safety.ch')
        sections.append(
            f'Datenbasierte Analyse der letzten {tage} Tage | Datum: {datum}'
        )
        sections.append('')

        # Executive Summary
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

        # Traffic & Akquisition
        sections.append('## Traffic & Akquisition')
        sections.append('### Traffic-Quellen (Top 10)')
        sections.append(self.deck._csv_to_markdown('traffic_sources.csv', max_rows=10))
        sections.append('')
        sections.append('### Channel-Performance')
        sections.append(self.deck._csv_to_markdown('channel_performance.csv'))
        sections.append('')

        # Neue vs. Wiederkehrende Nutzer
        sections.append('## Neue vs. Wiederkehrende Nutzer')
        sections.append(self.deck._csv_to_markdown('new_vs_returning.csv'))
        sections.append('')

        # Top-Seiten & Engagement
        sections.append('## Top-Seiten & Engagement')
        sections.append('### Top-Seiten')
        sections.append(self.deck._csv_to_markdown('top_pages.csv', max_rows=15))
        sections.append('')
        sections.append('### Landing Pages')
        sections.append(self.deck._csv_to_markdown('landing_pages.csv', max_rows=10))
        sections.append('')

        # E-Commerce Ueberblick
        sections.append('## E-Commerce Ueberblick')
        sections.append('### Transaktionen')
        sections.append(self.deck._csv_to_markdown('ecommerce_transactions.csv'))
        sections.append('')
        sections.append('### Umsatz nach Quelle')
        sections.append(
            self.deck._csv_to_markdown('ecommerce_revenue_by_source.csv', max_rows=10)
        )
        sections.append('')

        # Produkt-Performance
        sections.append('## Produkt-Performance')
        sections.append(
            self.deck._csv_to_markdown('product_performance.csv', max_rows=15)
        )
        sections.append('')

        # Warenkorb-Analyse
        sections.append('## Warenkorb-Analyse')
        sections.append(self.deck._csv_to_markdown('cart_abandonment.csv'))
        sections.append('')

        # Erstakquise-Kanaele
        sections.append('## Erstakquise-Kanaele')
        sections.append(
            self.deck._csv_to_markdown('first_touch_attribution.csv')
        )
        sections.append('')

        # Produktkategorie-Performance
        sections.append('## Produktkategorie-Performance')
        sections.append(
            self.deck._csv_to_markdown('product_category_performance.csv')
        )
        sections.append('')

        # Conversion Funnel
        sections.append('## Conversion Funnel')
        sections.append(self.deck._csv_to_markdown('conversion_funnel.csv'))
        sections.append('')

        # Kanal-Effizienz (ROI)
        sections.append('## Kanal-Effizienz (ROI)')
        sections.append(
            self.deck._csv_to_markdown('channel_revenue_efficiency.csv')
        )
        sections.append('')

        # Warenkorbwert-Trend (AOV)
        sections.append('## Warenkorbwert-Trend (AOV)')
        sections.append(self.deck._csv_to_markdown('aov_trend.csv'))
        sections.append('')

        # Wiederkaufrate
        sections.append('## Wiederkaufrate')
        sections.append(self.deck._csv_to_markdown('repeat_purchase_rate.csv'))
        sections.append('')

        # Landing-Page-Effizienz
        sections.append('## Landing-Page-Effizienz')
        sections.append(
            self.deck._csv_to_markdown('landing_page_efficiency.csv')
        )
        sections.append('')

        # Mobile Conversion Gap
        sections.append('## Mobile Conversion Gap')
        sections.append(
            self.deck._csv_to_markdown('mobile_conversion_gap.csv')
        )
        sections.append('')

        # Monatstrend & Saisonalitaet
        sections.append('## Monatstrend & Saisonalitaet')
        sections.append(self.deck._csv_to_markdown('monthly_trend.csv'))
        sections.append('')

        # Produkt-Stickiness
        sections.append('## Produkt-Stickiness')
        sections.append(
            self.deck._csv_to_markdown('product_stickiness.csv', max_rows=20)
        )
        sections.append('')

        # Geraete & Browser
        sections.append('## Geraete & Browser')
        sections.append('### Geraete')
        sections.append(self.deck._csv_to_markdown('device_split.csv'))
        sections.append('')
        sections.append('### Browser')
        sections.append(self.deck._csv_to_markdown('browser_stats.csv', max_rows=8))
        sections.append('')
        sections.append('### Betriebssysteme')
        sections.append(self.deck._csv_to_markdown('os_stats.csv', max_rows=8))
        sections.append('')

        # Geografie
        sections.append('## Geografie')
        sections.append('### Laender')
        sections.append(self.deck._csv_to_markdown('geo_countries.csv', max_rows=10))
        sections.append('')
        sections.append('### Staedte')
        sections.append(self.deck._csv_to_markdown('geo_cities.csv', max_rows=15))
        sections.append('')

        # Zeitliche Muster
        sections.append('## Zeitliche Muster')
        sections.append('### Wochentag')
        sections.append(self.deck._csv_to_markdown('day_of_week.csv'))
        sections.append('')
        sections.append('### Tageszeit')
        sections.append(self.deck._csv_to_markdown('hour_of_day.csv'))
        sections.append('')

        # Probleme & Empfehlungen
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

        # -- Build the short paste prompt --
        paste_prompt = self._build_paste_prompt(tage, datum)

        # -- Write files --
        os.makedirs(self.reports_dir, exist_ok=True)

        full_path = os.path.join(self.reports_dir, 'GAMMA_PROMPT.md')
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(full_doc)
        print(f'Gamma Upload-Dokument gespeichert: {full_path}')

        paste_path = os.path.join(self.reports_dir, 'GAMMA_PASTE_PROMPT.txt')
        with open(paste_path, 'w', encoding='utf-8') as f:
            f.write(paste_prompt)
        print(f'Gamma Paste-Prompt gespeichert:    {paste_path}')

        return full_path, paste_path

    def _build_paste_prompt(self, tage, datum):
        """Build a concise prompt (max ~2000 chars) for Gamma's Generate text field."""
        lines = [
            f'Erstelle eine professionelle Praesentation: '
            f'"Web-Analytics Report — labtec-safety.ch"',
            f'Zeitraum: Letzte {tage} Tage | Datum: {datum}',
            '',
            'Design: Modern, datenfokussiert, clean. '
            'Hauptfarben: Dunkelblau #1e326e, Gruen #009b91. '
            'Heller Hintergrund. Sans-Serif-Schrift.',
            '',
            'Folien-Struktur (Daten aus dem hochgeladenen Dokument):',
            '',
            '1. Titelfolie: "Web-Analytics Report — labtec-safety.ch"',
            '2. Executive Summary: 4 KPI-Karten mit Hauptmetriken '
            '(Sessions, Umsatz, Conversion-Rate, Avg. Warenkorbwert)',
            '3. Traffic & Akquisition: Top-10 Traffic-Quellen als '
            'Tabelle + Channel-Performance',
            '4. Neue vs. Wiederkehrende Nutzer: Vergleichstabelle',
            '5. Top-Seiten & Engagement: Meistbesuchte Seiten + Landing Pages',
            '6. E-Commerce Ueberblick: Transaktionen + Umsatz nach Quelle',
            '7. Produkt-Performance: Top-Produkte nach Umsatz',
            '8. Warenkorb-Analyse: Conversion-Funnel + Abbruchrate',
            '9. Erstakquise-Kanaele & Kanal-Effizienz',
            '10. Kategorie-Performance & Produkt-Stickiness',
            '11. Monatstrend & Saisonalitaet',
            '12. Geraete & Browser: Desktop/Mobile/Tablet-Split',
            '13. Geografie: Laender + Top-Staedte (DACH-Fokus)',
            '14. Zeitliche Muster: Wochentag + Tageszeit',
            '15. Probleme & Empfehlungen: High-Bounce-Seiten, UX-Issues',
            '',
            'Wichtig:',
            '- Alle Zahlen exakt aus dem Dokument uebernehmen',
            '- Tabellen und Daten visuell darstellen (Diagramme, Charts)',
            '- Schweizer E-Commerce-Kontext (CHF-Betraege)',
            '- Professioneller Business-Report-Stil',
        ]
        prompt = '\n'.join(lines)
        # Safety: truncate to 2000 chars if needed
        if len(prompt) > 2000:
            prompt = prompt[:1997] + '...'
        return prompt


def generate_gamma_prompt():
    """Convenience function to generate Gamma files."""
    gen = GammaPromptGenerator()
    return gen.generate_gamma_prompt()


if __name__ == '__main__':
    full_path, paste_path = generate_gamma_prompt()
    print(f'\nFertig! Zwei Dateien erstellt:')
    print(f'  1. {full_path}  (Upload als Quelle in Gamma)')
    print(f'  2. {paste_path}  (Text in Gamma Generate-Feld einfuegen)')
