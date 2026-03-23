"""
GA4 Shop-Analyse-Suite
Umfassende Analytics fuer den labtec-safety Online-Shop.

Module:
  A) Traffic & Akquisition
  B) Nutzerverhalten & Engagement
  C) E-Commerce Performance
  D) Geraete & Technologie
  E) Geografie
  F) Zeitliche Muster
  G) Problem-Erkennung

Nutzung:
  python ga4_analytics.py --all
  python ga4_analytics.py --module traffic
  python ga4_analytics.py --module ecommerce --days 90 --csv
"""

import argparse
import csv
import os
from datetime import datetime

from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange, Dimension, Filter, FilterExpression, Metric, NumericValue, OrderBy,
    RunReportRequest,
)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'ga4-credentials.json'
)

PROPERTY_ID = '499885493'
REPORTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'reports')


class GA4Analytics:

    def __init__(self, property_id=PROPERTY_ID, days=90):
        self.property_id = property_id
        self.days = days
        self.client = BetaAnalyticsDataClient()
        self.summary_sections = []

    # ── Helpers ──────────────────────────────────────────────────────

    def _run_report(self, dimensions, metrics, limit=None, order_by=None,
                    dimension_filter=None, metric_filter=None):
        kwargs = dict(
            property=f'properties/{self.property_id}',
            dimensions=[Dimension(name=d) for d in dimensions],
            metrics=[Metric(name=m) for m in metrics],
            date_ranges=[DateRange(
                start_date=f'{self.days}daysAgo', end_date='today'
            )],
        )
        if limit:
            kwargs['limit'] = limit
        if order_by:
            kwargs['order_bys'] = order_by
        if dimension_filter:
            kwargs['dimension_filter'] = dimension_filter
        if metric_filter:
            kwargs['metric_filter'] = metric_filter
        return self.client.run_report(RunReportRequest(**kwargs))

    def _rows_to_list(self, response, dim_count, metric_names):
        rows = []
        for row in response.rows:
            dims = [row.dimension_values[i].value for i in range(dim_count)]
            vals = []
            for i, name in enumerate(metric_names):
                raw = row.metric_values[i].value
                if 'rate' in name.lower() or 'Rate' in name:
                    vals.append(f'{float(raw) * 100:.1f}%')
                elif 'revenue' in name.lower() or 'Revenue' in name:
                    vals.append(f'{float(raw):,.2f}')
                elif 'duration' in name.lower() or 'Duration' in name:
                    vals.append(f'{float(raw):.0f}s')
                else:
                    val = float(raw)
                    vals.append(str(int(val)) if val == int(val) else f'{val:.2f}')
            rows.append(dims + vals)
        return rows

    def _print_table(self, title, headers, rows):
        print(f'\n{"=" * 60}')
        print(f'  {title}')
        print(f'  Zeitraum: letzte {self.days} Tage')
        print(f'{"=" * 60}')
        if not rows:
            print('  Keine Daten verfuegbar.')
            return
        widths = [max(len(str(h)), max((len(str(r[i])) for r in rows), default=0))
                  for i, h in enumerate(headers)]
        fmt = '  '.join(f'{{:<{w}}}' if i == 0 else f'{{:>{w}}}'
                        for i, w in enumerate(widths))
        print(fmt.format(*headers))
        print('-' * sum(widths) + '-' * (2 * (len(widths) - 1)))
        for row in rows:
            print(fmt.format(*row))

    def _export_csv(self, filename, headers, rows):
        os.makedirs(REPORTS_DIR, exist_ok=True)
        path = os.path.join(REPORTS_DIR, filename)
        with open(path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            writer.writerows(rows)
        print(f'  → CSV: {path}')

    def _add_summary(self, title, insights):
        self.summary_sections.append((title, insights))

    def _write_summary(self):
        os.makedirs(REPORTS_DIR, exist_ok=True)
        path = os.path.join(REPORTS_DIR, 'SUMMARY.md')
        with open(path, 'w', encoding='utf-8') as f:
            f.write(f'# GA4 Analyse-Report: labtec-safety\n')
            f.write(f'**Zeitraum:** Letzte {self.days} Tage\n')
            f.write(f'**Erstellt:** {datetime.now().strftime("%Y-%m-%d %H:%M")}\n\n')
            f.write('---\n\n')
            for title, insights in self.summary_sections:
                f.write(f'## {title}\n')
                for insight in insights:
                    f.write(f'- {insight}\n')
                f.write('\n')
        print(f'\n{"=" * 60}')
        print(f'  SUMMARY gespeichert: {path}')
        print(f'{"=" * 60}')

    # ── Modul A: Traffic & Akquisition ───────────────────────────────

    def traffic_sources(self, export_csv=False):
        metrics = ['sessions', 'totalUsers', 'engagementRate', 'averageSessionDuration']
        resp = self._run_report(
            ['sessionSource', 'sessionMedium'], metrics,
            limit=20,
            order_by=[OrderBy(metric=OrderBy.MetricOrderBy(metric_name='sessions'), desc=True)],
        )
        headers = ['Quelle', 'Medium', 'Sessions', 'Users', 'Engage%', 'Dauer']
        rows = self._rows_to_list(resp, 2, metrics)
        self._print_table('Traffic-Quellen (Top 20)', headers, rows)
        if export_csv:
            self._export_csv('traffic_sources.csv', headers, rows)
        if rows:
            top = rows[0]
            self._add_summary('Traffic-Quellen', [
                f'Top-Quelle: {top[0]}/{top[1]} mit {top[2]} Sessions',
                f'{len(rows)} verschiedene Quellen/Medien aktiv',
                f'Engagement-Rate der Top-Quelle: {top[4]}',
            ])

    def channel_performance(self, export_csv=False):
        metrics = ['sessions', 'totalUsers', 'engagementRate', 'conversions']
        resp = self._run_report(
            ['sessionDefaultChannelGroup'], metrics,
            order_by=[OrderBy(metric=OrderBy.MetricOrderBy(metric_name='sessions'), desc=True)],
        )
        headers = ['Kanal', 'Sessions', 'Users', 'Engage%', 'Conversions']
        rows = self._rows_to_list(resp, 1, metrics)
        self._print_table('Kanal-Performance', headers, rows)
        if export_csv:
            self._export_csv('channel_performance.csv', headers, rows)
        if rows:
            insights = [f'{r[0]}: {r[1]} Sessions, {r[4]} Conversions' for r in rows[:5]]
            self._add_summary('Kanal-Performance', insights)

    def new_vs_returning(self, export_csv=False):
        metrics = ['sessions', 'totalUsers', 'screenPageViews', 'engagementRate']
        resp = self._run_report(['newVsReturning'], metrics)
        headers = ['Typ', 'Sessions', 'Users', 'PageViews', 'Engage%']
        rows = self._rows_to_list(resp, 1, metrics)
        self._print_table('Neue vs. Wiederkehrende Nutzer', headers, rows)
        if export_csv:
            self._export_csv('new_vs_returning.csv', headers, rows)
        if rows:
            self._add_summary('Neue vs. Wiederkehrende', [
                f'{r[0]}: {r[1]} Sessions, {r[3]} PageViews, Engagement {r[4]}' for r in rows
            ])

    def landing_pages(self, export_csv=False):
        metrics = ['sessions', 'bounceRate', 'averageSessionDuration', 'engagementRate']
        resp = self._run_report(
            ['landingPage'], metrics, limit=20,
            order_by=[OrderBy(metric=OrderBy.MetricOrderBy(metric_name='sessions'), desc=True)],
        )
        headers = ['Landing Page', 'Sessions', 'Bounce%', 'Dauer', 'Engage%']
        rows = self._rows_to_list(resp, 1, metrics)
        self._print_table('Landing Pages (Top 20)', headers, rows)
        if export_csv:
            self._export_csv('landing_pages.csv', headers, rows)
        if rows:
            self._add_summary('Landing Pages', [
                f'Top Landing Page: {rows[0][0]} ({rows[0][1]} Sessions, Bounce {rows[0][2]})',
                f'Beste Engagement-Rate: {min(rows, key=lambda r: r[0])[0]} mit {min(rows, key=lambda r: r[0])[4]}',
            ])

    def run_traffic(self, export_csv=False):
        self.traffic_sources(export_csv)
        self.channel_performance(export_csv)
        self.new_vs_returning(export_csv)
        self.landing_pages(export_csv)

    # ── Modul B: Nutzerverhalten & Engagement ────────────────────────

    def top_pages(self, export_csv=False):
        metrics = ['screenPageViews', 'engagementRate', 'averageSessionDuration']
        resp = self._run_report(
            ['pagePath', 'pageTitle'], metrics, limit=20,
            order_by=[OrderBy(metric=OrderBy.MetricOrderBy(metric_name='screenPageViews'), desc=True)],
        )
        headers = ['Seite', 'Titel', 'Views', 'Engage%', 'Dauer']
        rows = self._rows_to_list(resp, 2, metrics)
        self._print_table('Top-Seiten (Top 20)', headers, rows)
        if export_csv:
            self._export_csv('top_pages.csv', headers, rows)
        if rows:
            self._add_summary('Top-Seiten', [
                f'{rows[i][1]}: {rows[i][2]} Views' for i in range(min(5, len(rows)))
            ])

    def high_bounce_pages(self, export_csv=False):
        metrics = ['sessions', 'bounceRate', 'engagementRate']
        resp = self._run_report(
            ['pagePath'], metrics, limit=20,
            order_by=[OrderBy(metric=OrderBy.MetricOrderBy(metric_name='bounceRate'), desc=True)],
            metric_filter=FilterExpression(filter=Filter(
                field_name='sessions',
                numeric_filter=Filter.NumericFilter(
                    operation=Filter.NumericFilter.Operation.GREATER_THAN,
                    value=NumericValue(int64_value=10),
                ),
            )),
        )
        headers = ['Seite', 'Sessions', 'Bounce%', 'Engage%']
        rows = self._rows_to_list(resp, 1, metrics)
        self._print_table('Seiten mit hoher Bounce-Rate (min. 10 Sessions)', headers, rows)
        if export_csv:
            self._export_csv('high_bounce_pages.csv', headers, rows)
        if rows:
            self._add_summary('Hohe Bounce-Raten', [
                f'PROBLEM: {rows[i][0]} hat {rows[i][2]} Bounce-Rate ({rows[i][1]} Sessions)'
                for i in range(min(5, len(rows)))
            ])

    def event_tracking(self, export_csv=False):
        metrics = ['eventCount', 'totalUsers']
        resp = self._run_report(
            ['eventName'], metrics, limit=20,
            order_by=[OrderBy(metric=OrderBy.MetricOrderBy(metric_name='eventCount'), desc=True)],
        )
        headers = ['Event', 'Anzahl', 'Users']
        rows = self._rows_to_list(resp, 1, metrics)
        self._print_table('Event-Tracking (Top 20)', headers, rows)
        if export_csv:
            self._export_csv('event_tracking.csv', headers, rows)
        if rows:
            self._add_summary('Events', [
                f'{rows[i][0]}: {rows[i][1]}x von {rows[i][2]} Nutzern'
                for i in range(min(5, len(rows)))
            ])

    def run_behavior(self, export_csv=False):
        self.top_pages(export_csv)
        self.high_bounce_pages(export_csv)
        self.event_tracking(export_csv)

    # ── Modul C: E-Commerce ──────────────────────────────────────────

    def revenue_by_source(self, export_csv=False):
        metrics = ['ecommercePurchases', 'purchaseRevenue', 'totalUsers']
        try:
            resp = self._run_report(
                ['sessionSource', 'sessionMedium'], metrics, limit=20,
                order_by=[OrderBy(metric=OrderBy.MetricOrderBy(metric_name='purchaseRevenue'), desc=True)],
            )
        except Exception as e:
            print(f'\n  E-Commerce: Umsatz nach Quelle nicht verfuegbar ({e})')
            return
        headers = ['Quelle', 'Medium', 'Kaeufe', 'Umsatz', 'Users']
        rows = self._rows_to_list(resp, 2, metrics)
        # Filter: nur Zeilen mit Kaeufen
        rows = [r for r in rows if r[2] != '0']
        self._print_table('Umsatz nach Traffic-Quelle', headers, rows)
        if export_csv and rows:
            self._export_csv('ecommerce_revenue_by_source.csv', headers, rows)
        if rows:
            self._add_summary('Umsatz nach Quelle', [
                f'Top: {rows[0][0]}/{rows[0][1]} = {rows[0][3]} EUR ({rows[0][2]} Kaeufe)'
            ] + [f'{r[0]}/{r[1]}: {r[3]} EUR' for r in rows[1:4]])

    def transaction_summary(self, export_csv=False):
        metrics = ['ecommercePurchases', 'purchaseRevenue', 'averagePurchaseRevenue']
        try:
            resp = self._run_report(
                ['date'], metrics,
                order_by=[OrderBy(dimension=OrderBy.DimensionOrderBy(dimension_name='date'), desc=True)],
            )
        except Exception as e:
            print(f'\n  E-Commerce: Transaktionen nicht verfuegbar ({e})')
            return
        headers = ['Datum', 'Kaeufe', 'Umsatz', 'Avg. Warenkorb']
        rows = self._rows_to_list(resp, 1, metrics)
        # Datum formatieren
        for r in rows:
            d = r[0]
            if len(d) == 8:
                r[0] = f'{d[:4]}-{d[4:6]}-{d[6:]}'
        self._print_table('Transaktions-Uebersicht (pro Tag)', headers, rows)
        if export_csv:
            self._export_csv('ecommerce_transactions.csv', headers, rows)
        # Gesamtberechnung
        total_purchases = sum(int(r[1]) for r in rows)
        total_revenue = sum(float(r[2].replace(',', '')) for r in rows)
        if total_purchases > 0:
            avg_order = total_revenue / total_purchases
            self._add_summary('Transaktionen Gesamt', [
                f'Gesamt-Umsatz: {total_revenue:,.2f} EUR',
                f'Anzahl Kaeufe: {total_purchases}',
                f'Durchschn. Warenkorbwert: {avg_order:,.2f} EUR',
            ])

    def product_performance(self, export_csv=False):
        metrics = ['itemsViewed', 'itemsAddedToCart', 'itemsPurchased', 'itemRevenue']
        try:
            resp = self._run_report(
                ['itemName'], metrics, limit=30,
                order_by=[OrderBy(metric=OrderBy.MetricOrderBy(metric_name='itemRevenue'), desc=True)],
            )
        except Exception as e:
            print(f'\n  E-Commerce: Produkt-Daten nicht verfuegbar ({e})')
            return
        headers = ['Produkt', 'Views', 'In Warenkorb', 'Gekauft', 'Umsatz']
        rows = self._rows_to_list(resp, 1, metrics)
        rows = [r for r in rows if r[3] != '0' or r[1] != '0']
        self._print_table('Produkt-Performance (Top 30)', headers, rows)
        if export_csv and rows:
            self._export_csv('product_performance.csv', headers, rows)
        if rows:
            self._add_summary('Produkt-Performance', [
                f'Bestseller: {rows[0][0]} ({rows[0][4]} EUR, {rows[0][3]}x gekauft)'
            ] + [f'{r[0]}: {r[4]} EUR Umsatz' for r in rows[1:5]])

    def cart_abandonment(self, export_csv=False):
        metrics = ['addToCarts', 'ecommercePurchases']
        try:
            resp = self._run_report(
                ['date'], metrics,
                order_by=[OrderBy(dimension=OrderBy.DimensionOrderBy(dimension_name='date'), desc=True)],
            )
        except Exception as e:
            print(f'\n  E-Commerce: Warenkorb-Daten nicht verfuegbar ({e})')
            return
        headers = ['Datum', 'In Warenkorb', 'Kaeufe']
        rows = self._rows_to_list(resp, 1, metrics)
        for r in rows:
            d = r[0]
            if len(d) == 8:
                r[0] = f'{d[:4]}-{d[4:6]}-{d[6:]}'
        self._print_table('Warenkorb vs. Kaeufe (pro Tag)', headers, rows)
        if export_csv:
            self._export_csv('cart_abandonment.csv', headers, rows)
        total_cart = sum(int(r[1]) for r in rows)
        total_purchase = sum(int(r[2]) for r in rows)
        if total_cart > 0:
            abandon_rate = (1 - total_purchase / total_cart) * 100
            self._add_summary('Warenkorb-Abbruch', [
                f'In Warenkorb gelegt: {total_cart}',
                f'Tatsaechlich gekauft: {total_purchase}',
                f'Abbruchrate: {abandon_rate:.1f}%',
                f'{"PROBLEM: Hohe Abbruchrate!" if abandon_rate > 70 else "Abbruchrate im normalen Bereich"}'
            ])

    def conversion_by_channel(self, export_csv=False):
        metrics = ['sessions', 'ecommercePurchases', 'purchaseRevenue']
        try:
            resp = self._run_report(
                ['sessionDefaultChannelGroup'], metrics,
                order_by=[OrderBy(metric=OrderBy.MetricOrderBy(metric_name='purchaseRevenue'), desc=True)],
            )
        except Exception as e:
            print(f'\n  E-Commerce: Conversion nach Kanal nicht verfuegbar ({e})')
            return
        headers = ['Kanal', 'Sessions', 'Kaeufe', 'Umsatz']
        rows = self._rows_to_list(resp, 1, metrics)
        # Conversion-Rate berechnen
        headers.append('Conv%')
        for r in rows:
            sessions = int(r[1])
            purchases = int(r[2])
            rate = (purchases / sessions * 100) if sessions > 0 else 0
            r.append(f'{rate:.2f}%')
        self._print_table('Conversion nach Kanal', headers, rows)
        if export_csv:
            self._export_csv('conversion_by_channel.csv', headers, rows)
        if rows:
            self._add_summary('Conversion nach Kanal', [
                f'{r[0]}: {r[4]} Conversion-Rate, {r[3]} EUR Umsatz' for r in rows if r[2] != '0'
            ][:5])

    def run_ecommerce(self, export_csv=False):
        self.revenue_by_source(export_csv)
        self.transaction_summary(export_csv)
        self.product_performance(export_csv)
        self.cart_abandonment(export_csv)
        self.conversion_by_channel(export_csv)

    # ── Modul D: Geraete & Technologie ───────────────────────────────

    def device_split(self, export_csv=False):
        metrics = ['sessions', 'totalUsers', 'engagementRate', 'bounceRate']
        resp = self._run_report(
            ['deviceCategory'], metrics,
            order_by=[OrderBy(metric=OrderBy.MetricOrderBy(metric_name='sessions'), desc=True)],
        )
        headers = ['Geraet', 'Sessions', 'Users', 'Engage%', 'Bounce%']
        rows = self._rows_to_list(resp, 1, metrics)
        self._print_table('Geraete-Verteilung', headers, rows)
        if export_csv:
            self._export_csv('device_split.csv', headers, rows)
        if rows:
            self._add_summary('Geraete', [
                f'{r[0]}: {r[1]} Sessions, Bounce {r[4]}, Engagement {r[3]}' for r in rows
            ])

    def browser_stats(self, export_csv=False):
        metrics = ['sessions', 'bounceRate', 'engagementRate']
        resp = self._run_report(
            ['browser'], metrics, limit=10,
            order_by=[OrderBy(metric=OrderBy.MetricOrderBy(metric_name='sessions'), desc=True)],
        )
        headers = ['Browser', 'Sessions', 'Bounce%', 'Engage%']
        rows = self._rows_to_list(resp, 1, metrics)
        self._print_table('Browser (Top 10)', headers, rows)
        if export_csv:
            self._export_csv('browser_stats.csv', headers, rows)

    def os_stats(self, export_csv=False):
        metrics = ['sessions', 'totalUsers']
        resp = self._run_report(
            ['operatingSystem'], metrics, limit=10,
            order_by=[OrderBy(metric=OrderBy.MetricOrderBy(metric_name='sessions'), desc=True)],
        )
        headers = ['Betriebssystem', 'Sessions', 'Users']
        rows = self._rows_to_list(resp, 1, metrics)
        self._print_table('Betriebssysteme (Top 10)', headers, rows)
        if export_csv:
            self._export_csv('os_stats.csv', headers, rows)

    def run_devices(self, export_csv=False):
        self.device_split(export_csv)
        self.browser_stats(export_csv)
        self.os_stats(export_csv)

    # ── Modul E: Geografie ───────────────────────────────────────────

    def geo_countries(self, export_csv=False):
        metrics = ['sessions', 'totalUsers', 'engagementRate']
        resp = self._run_report(
            ['country'], metrics, limit=20,
            order_by=[OrderBy(metric=OrderBy.MetricOrderBy(metric_name='sessions'), desc=True)],
        )
        headers = ['Land', 'Sessions', 'Users', 'Engage%']
        rows = self._rows_to_list(resp, 1, metrics)
        self._print_table('Laender (Top 20)', headers, rows)
        if export_csv:
            self._export_csv('geo_countries.csv', headers, rows)
        if rows:
            self._add_summary('Geografie', [
                f'{r[0]}: {r[1]} Sessions, {r[2]} Users' for r in rows[:5]
            ])

    def geo_cities(self, export_csv=False):
        metrics = ['sessions', 'totalUsers']
        resp = self._run_report(
            ['city'], metrics, limit=20,
            order_by=[OrderBy(metric=OrderBy.MetricOrderBy(metric_name='sessions'), desc=True)],
        )
        headers = ['Stadt', 'Sessions', 'Users']
        rows = self._rows_to_list(resp, 1, metrics)
        self._print_table('Staedte (Top 20)', headers, rows)
        if export_csv:
            self._export_csv('geo_cities.csv', headers, rows)

    def run_geo(self, export_csv=False):
        self.geo_countries(export_csv)
        self.geo_cities(export_csv)

    # ── Modul F: Zeitliche Muster ────────────────────────────────────

    def day_of_week(self, export_csv=False):
        metrics = ['sessions', 'totalUsers', 'screenPageViews']
        resp = self._run_report(
            ['dayOfWeek'], metrics,
            order_by=[OrderBy(dimension=OrderBy.DimensionOrderBy(dimension_name='dayOfWeek'))],
        )
        headers = ['Wochentag', 'Sessions', 'Users', 'PageViews']
        day_names = {'0': 'Sonntag', '1': 'Montag', '2': 'Dienstag', '3': 'Mittwoch',
                     '4': 'Donnerstag', '5': 'Freitag', '6': 'Samstag'}
        rows = self._rows_to_list(resp, 1, metrics)
        for r in rows:
            r[0] = day_names.get(r[0], r[0])
        self._print_table('Sessions nach Wochentag', headers, rows)
        if export_csv:
            self._export_csv('day_of_week.csv', headers, rows)
        if rows:
            best = max(rows, key=lambda r: int(r[1]))
            worst = min(rows, key=lambda r: int(r[1]))
            self._add_summary('Zeitliche Muster', [
                f'Staerkster Tag: {best[0]} ({best[1]} Sessions)',
                f'Schwaechster Tag: {worst[0]} ({worst[1]} Sessions)',
            ])

    def hour_of_day(self, export_csv=False):
        metrics = ['sessions', 'totalUsers']
        resp = self._run_report(
            ['hour'], metrics,
            order_by=[OrderBy(dimension=OrderBy.DimensionOrderBy(dimension_name='hour'))],
        )
        headers = ['Stunde', 'Sessions', 'Users']
        rows = self._rows_to_list(resp, 1, metrics)
        for r in rows:
            r[0] = f'{int(r[0]):02d}:00'
        self._print_table('Sessions nach Uhrzeit', headers, rows)
        if export_csv:
            self._export_csv('hour_of_day.csv', headers, rows)
        if rows:
            peak = max(rows, key=lambda r: int(r[1]))
            self._add_summary('Peak-Stunde', [f'Meister Traffic um {peak[0]} ({peak[1]} Sessions)'])

    def daily_trend(self, export_csv=False):
        metrics = ['sessions', 'totalUsers', 'screenPageViews', 'engagementRate']
        resp = self._run_report(
            ['date'], metrics,
            order_by=[OrderBy(dimension=OrderBy.DimensionOrderBy(dimension_name='date'), desc=True)],
        )
        headers = ['Datum', 'Sessions', 'Users', 'PageViews', 'Engage%']
        rows = self._rows_to_list(resp, 1, metrics)
        for r in rows:
            d = r[0]
            if len(d) == 8:
                r[0] = f'{d[:4]}-{d[4:6]}-{d[6:]}'
        self._print_table('Tages-Trend', headers, rows)
        if export_csv:
            self._export_csv('daily_trend.csv', headers, rows)

    def run_time(self, export_csv=False):
        self.day_of_week(export_csv)
        self.hour_of_day(export_csv)
        self.daily_trend(export_csv)

    # ── Modul H: UX-Design-Insights ────────────────────────────────

    def ux_mobile_vs_desktop(self, export_csv=False):
        metrics = ['sessions', 'engagementRate', 'bounceRate', 'averageSessionDuration',
                   'screenPageViews', 'conversions']
        resp = self._run_report(
            ['deviceCategory'], metrics,
            order_by=[OrderBy(metric=OrderBy.MetricOrderBy(metric_name='sessions'), desc=True)],
        )
        headers = ['Geraet', 'Sessions', 'Engage%', 'Bounce%', 'Dauer', 'PageViews', 'Conversions']
        rows = self._rows_to_list(resp, 1, metrics)
        self._print_table('UX: Mobile vs. Desktop', headers, rows)
        if export_csv:
            self._export_csv('ux_mobile_vs_desktop.csv', headers, rows)
        if rows:
            insights = []
            device_map = {r[0]: r for r in rows}
            mobile = device_map.get('mobile')
            desktop = device_map.get('desktop')
            if mobile and desktop:
                insights.append(f'Desktop: Engagement {desktop[2]}, Bounce {desktop[3]}, Dauer {desktop[4]}')
                insights.append(f'Mobile: Engagement {mobile[2]}, Bounce {mobile[3]}, Dauer {mobile[4]}')
                m_eng = float(mobile[2].rstrip('%'))
                d_eng = float(desktop[2].rstrip('%'))
                gap = d_eng - m_eng
                if gap > 10:
                    insights.append(f'PROBLEM: Mobile Engagement {gap:.0f}pp niedriger als Desktop')
                else:
                    insights.append('Mobile und Desktop UX auf aehnlichem Niveau')
            self._add_summary('UX: Mobile vs. Desktop', insights)

    def ux_screen_resolution(self, export_csv=False):
        metrics = ['sessions', 'bounceRate', 'engagementRate']
        resp = self._run_report(
            ['screenResolution', 'deviceCategory'], metrics, limit=20,
            order_by=[OrderBy(metric=OrderBy.MetricOrderBy(metric_name='sessions'), desc=True)],
        )
        headers = ['Aufloesung', 'Geraet', 'Sessions', 'Bounce%', 'Engage%']
        rows = self._rows_to_list(resp, 2, metrics)
        self._print_table('UX: Bildschirmaufloesung (Top 20)', headers, rows)
        if export_csv:
            self._export_csv('ux_screen_resolution.csv', headers, rows)
        if rows:
            problem_resolutions = [r for r in rows if int(r[2]) > 20
                                   and float(r[3].rstrip('%')) > 60]
            insights = [f'Haeufigste Aufloesung: {rows[0][0]} ({rows[0][1]}, {rows[0][2]} Sessions)']
            for r in problem_resolutions[:3]:
                insights.append(f'Hohe Bounce bei {r[0]} ({r[1]}): {r[3]}')
            self._add_summary('UX: Bildschirmaufloesungen', insights)

    def ux_engagement_per_page(self, export_csv=False):
        metrics = ['userEngagementDuration', 'engagementRate', 'screenPageViews']
        resp = self._run_report(
            ['pagePath', 'pageTitle'], metrics, limit=30,
            order_by=[OrderBy(metric=OrderBy.MetricOrderBy(metric_name='screenPageViews'), desc=True)],
        )
        headers = ['Seite', 'Titel', 'Engage-Zeit', 'Engage%', 'Views']
        rows = self._rows_to_list(resp, 2, metrics)
        self._print_table('UX: Engagement pro Seite (Top 30)', headers, rows)
        if export_csv:
            self._export_csv('ux_engagement_per_page.csv', headers, rows)
        if rows:
            best = max(rows, key=lambda r: float(r[2].rstrip('s'))) if rows else None
            worst = min((r for r in rows if int(r[4]) > 10),
                        key=lambda r: float(r[2].rstrip('s')), default=None)
            insights = []
            if best:
                insights.append(f'Hoechstes Engagement: {best[1]} ({best[2]} aktive Zeit)')
            if worst:
                insights.append(f'Niedrigstes Engagement: {worst[1]} ({worst[2]} aktive Zeit, {worst[4]} Views)')
            self._add_summary('UX: Engagement pro Seite', insights)

    def ux_exit_pages(self, export_csv=False):
        # Sessions pro Seite vs. PageViews gibt einen Hinweis auf Exit-Verhalten
        metrics = ['sessions', 'screenPageViews', 'bounceRate', 'engagementRate']
        resp = self._run_report(
            ['pagePath'], metrics, limit=20,
            order_by=[OrderBy(metric=OrderBy.MetricOrderBy(metric_name='sessions'), desc=True)],
        )
        headers = ['Seite', 'Sessions', 'PageViews', 'Bounce%', 'Engage%']
        rows = self._rows_to_list(resp, 1, metrics)
        # Sortiere nach hoher Bounce-Rate (= Exit-Indikator)
        rows_sorted = sorted(rows, key=lambda r: float(r[3].rstrip('%')), reverse=True)
        self._print_table('UX: Exit-Seiten (nach Bounce-Rate)', headers, rows_sorted)
        if export_csv:
            self._export_csv('ux_exit_pages.csv', headers, rows_sorted)
        if rows_sorted:
            self._add_summary('UX: Exit-Seiten', [
                f'{r[0]}: Bounce {r[3]}, {r[1]} Sessions' for r in rows_sorted[:5]
            ])

    def ux_landing_to_purchase(self, export_csv=False):
        metrics = ['sessions', 'addToCarts', 'ecommercePurchases']
        try:
            resp = self._run_report(
                ['landingPage'], metrics, limit=20,
                order_by=[OrderBy(metric=OrderBy.MetricOrderBy(metric_name='sessions'), desc=True)],
            )
        except Exception as e:
            print(f'\n  UX Landing-to-Purchase nicht verfuegbar ({e})')
            return
        headers = ['Landing Page', 'Sessions', 'Warenkorb', 'Kaeufe', 'Conv%']
        rows = self._rows_to_list(resp, 1, metrics)
        for r in rows:
            sessions = int(r[1])
            purchases = int(r[3])
            r.append(f'{(purchases / sessions * 100):.2f}%' if sessions > 0 else '0%')
        self._print_table('UX: Landing Page → Kauf Funnel', headers, rows)
        if export_csv:
            self._export_csv('ux_landing_to_purchase.csv', headers, rows)
        if rows:
            converting = [r for r in rows if r[3] != '0']
            non_converting = [r for r in rows if r[3] == '0' and int(r[1]) > 20]
            insights = []
            for r in converting[:3]:
                insights.append(f'Konvertiert: {r[0]} ({r[4]} Conv-Rate, {r[3]} Kaeufe)')
            for r in non_converting[:3]:
                insights.append(f'Kein Kauf trotz Traffic: {r[0]} ({r[1]} Sessions, 0 Kaeufe)')
            self._add_summary('UX: Landing Page Funnel', insights)

    def ux_new_vs_returning(self, export_csv=False):
        metrics = ['engagementRate', 'bounceRate', 'averageSessionDuration']
        resp = self._run_report(
            ['newVsReturning', 'deviceCategory'], metrics,
            order_by=[OrderBy(dimension=OrderBy.DimensionOrderBy(dimension_name='newVsReturning'))],
        )
        headers = ['Nutzer-Typ', 'Geraet', 'Engage%', 'Bounce%', 'Dauer']
        rows = self._rows_to_list(resp, 2, metrics)
        self._print_table('UX: Neue vs. Wiederkehrende nach Geraet', headers, rows)
        if export_csv:
            self._export_csv('ux_new_vs_returning.csv', headers, rows)
        if rows:
            self._add_summary('UX: Neue vs. Wiederkehrende', [
                f'{r[0]} auf {r[1]}: Engagement {r[2]}, Bounce {r[3]}' for r in rows
            ])

    def ux_product_funnel(self, export_csv=False):
        metrics = ['itemsViewed', 'itemsAddedToCart', 'itemsPurchased']
        try:
            resp = self._run_report(
                ['itemName'], metrics, limit=20,
                order_by=[OrderBy(metric=OrderBy.MetricOrderBy(metric_name='itemsViewed'), desc=True)],
            )
        except Exception as e:
            print(f'\n  UX Produkt-Funnel nicht verfuegbar ({e})')
            return
        headers = ['Produkt', 'Views', 'Warenkorb', 'Gekauft', 'View→Cart%', 'Cart→Buy%']
        rows = self._rows_to_list(resp, 1, metrics)
        for r in rows:
            views = int(r[1])
            cart = int(r[2])
            bought = int(r[3])
            r.append(f'{(cart / views * 100):.1f}%' if views > 0 else '0%')
            r.append(f'{(bought / cart * 100):.1f}%' if cart > 0 else '0%')
        self._print_table('UX: Produkt-Interaktions-Funnel', headers, rows)
        if export_csv:
            self._export_csv('ux_product_funnel.csv', headers, rows)
        if rows:
            insights = []
            for r in rows[:3]:
                insights.append(f'{r[0]}: {r[1]} Views → {r[2]} Warenkorb ({r[4]}) → {r[3]} Kauf ({r[5]})')
            low_cart = [r for r in rows if int(r[1]) > 10 and r[4] != '0%'
                        and float(r[4].rstrip('%')) < 5]
            for r in low_cart[:2]:
                insights.append(f'Niedriger View→Cart: {r[0]} nur {r[4]} bei {r[1]} Views')
            self._add_summary('UX: Produkt-Funnel', insights)

    def run_ux(self, export_csv=False):
        self.ux_mobile_vs_desktop(export_csv)
        self.ux_screen_resolution(export_csv)
        self.ux_engagement_per_page(export_csv)
        self.ux_exit_pages(export_csv)
        self.ux_landing_to_purchase(export_csv)
        self.ux_new_vs_returning(export_csv)
        self.ux_product_funnel(export_csv)

    # ── Modul G: Problem-Erkennung ───────────────────────────────────

    def problem_detection(self, export_csv=False):
        print(f'\n{"=" * 60}')
        print('  PROBLEM-ERKENNUNG')
        print(f'{"=" * 60}')
        problems = []

        # 1. Hohe Bounce-Rate Seiten
        try:
            metrics_b = ['sessions', 'bounceRate']
            resp = self._run_report(
                ['pagePath'], metrics_b, limit=10,
                order_by=[OrderBy(metric=OrderBy.MetricOrderBy(metric_name='bounceRate'), desc=True)],
                metric_filter=FilterExpression(filter=Filter(
                    field_name='sessions',
                    numeric_filter=Filter.NumericFilter(
                        operation=Filter.NumericFilter.Operation.GREATER_THAN,
                        value=Filter.NumericFilter.NumericValue(int64_value=20),
                    ),
                )),
            )
            for row in resp.rows:
                bounce = float(row.metric_values[1].value)
                if bounce > 0.7:
                    page = row.dimension_values[0].value
                    sessions = row.metric_values[0].value
                    problems.append(f'Hohe Bounce-Rate: {page} ({bounce*100:.0f}%, {sessions} Sessions)')
        except Exception:
            pass

        # 2. Mobile vs Desktop Gap
        try:
            resp = self._run_report(
                ['deviceCategory'], ['engagementRate', 'bounceRate'],
            )
            device_data = {}
            for row in resp.rows:
                device_data[row.dimension_values[0].value] = {
                    'engagement': float(row.metric_values[0].value),
                    'bounce': float(row.metric_values[1].value),
                }
            mobile = device_data.get('mobile', {})
            desktop = device_data.get('desktop', {})
            if mobile and desktop:
                eng_gap = desktop.get('engagement', 0) - mobile.get('engagement', 0)
                if eng_gap > 0.1:
                    problems.append(
                        f'Mobile-Gap: Desktop Engagement {desktop["engagement"]*100:.0f}% vs '
                        f'Mobile {mobile["engagement"]*100:.0f}% (Differenz: {eng_gap*100:.0f}pp)'
                    )
                bounce_gap = mobile.get('bounce', 0) - desktop.get('bounce', 0)
                if bounce_gap > 0.1:
                    problems.append(
                        f'Mobile Bounce hoeher: Mobile {mobile["bounce"]*100:.0f}% vs '
                        f'Desktop {desktop["bounce"]*100:.0f}%'
                    )
        except Exception:
            pass

        # 3. Warenkorb-Abbruch
        try:
            resp = self._run_report(['date'], ['addToCarts', 'ecommercePurchases'])
            total_cart = sum(int(r.metric_values[0].value) for r in resp.rows)
            total_buy = sum(int(r.metric_values[1].value) for r in resp.rows)
            if total_cart > 0:
                abandon = (1 - total_buy / total_cart) * 100
                if abandon > 70:
                    problems.append(f'Hohe Warenkorb-Abbruchrate: {abandon:.1f}% ({total_cart} in Warenkorb, {total_buy} gekauft)')
        except Exception:
            pass

        if problems:
            for i, p in enumerate(problems, 1):
                print(f'  {i}. {p}')
            self._add_summary('Erkannte Probleme', problems)
        else:
            print('  Keine kritischen Probleme erkannt.')
            self._add_summary('Erkannte Probleme', ['Keine kritischen Probleme erkannt.'])

    # ── Alle Module ──────────────────────────────────────────────────

    def run_all(self, export_csv=False):
        self.run_traffic(export_csv)
        self.run_behavior(export_csv)
        self.run_ecommerce(export_csv)
        self.run_devices(export_csv)
        self.run_geo(export_csv)
        self.run_time(export_csv)
        self.run_ux(export_csv)
        self.problem_detection(export_csv)
        self._write_summary()


def main():
    parser = argparse.ArgumentParser(description='GA4 Shop-Analyse-Suite fuer labtec-safety')
    parser.add_argument('--all', action='store_true', help='Alle Module ausfuehren')
    parser.add_argument('--module', choices=['traffic', 'behavior', 'ecommerce', 'devices', 'geo', 'time', 'ux', 'problems'],
                        help='Einzelnes Modul ausfuehren')
    parser.add_argument('--days', type=int, default=90, help='Zeitraum in Tagen (Standard: 90)')
    parser.add_argument('--csv', action='store_true', help='CSV-Export aktivieren')
    args = parser.parse_args()

    if not args.all and not args.module:
        parser.print_help()
        print('\nBeispiele:')
        print('  python ga4_analytics.py --all')
        print('  python ga4_analytics.py --all --csv')
        print('  python ga4_analytics.py --module traffic')
        print('  python ga4_analytics.py --module ecommerce --days 30 --csv')
        return

    analytics = GA4Analytics(days=args.days)

    if args.all:
        analytics.run_all(export_csv=args.csv)
    elif args.module == 'traffic':
        analytics.run_traffic(export_csv=args.csv)
        analytics._write_summary()
    elif args.module == 'behavior':
        analytics.run_behavior(export_csv=args.csv)
        analytics._write_summary()
    elif args.module == 'ecommerce':
        analytics.run_ecommerce(export_csv=args.csv)
        analytics._write_summary()
    elif args.module == 'devices':
        analytics.run_devices(export_csv=args.csv)
        analytics._write_summary()
    elif args.module == 'geo':
        analytics.run_geo(export_csv=args.csv)
        analytics._write_summary()
    elif args.module == 'time':
        analytics.run_time(export_csv=args.csv)
        analytics._write_summary()
    elif args.module == 'ux':
        analytics.run_ux(export_csv=args.csv)
        analytics._write_summary()
    elif args.module == 'problems':
        analytics.problem_detection(export_csv=args.csv)
        analytics._write_summary()


if __name__ == '__main__':
    main()
