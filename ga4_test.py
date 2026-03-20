"""
GA4 API Test Script
Teste die Verbindung zur Google Analytics Data API.

Voraussetzungen:
  pip install google-analytics-data

Nutzung:
  python ga4_test.py
"""

from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    RunReportRequest, DateRange, Metric, Dimension
)
import os

# Pfad zur Credentials-Datei
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'ga4-credentials.json'
)

PROPERTY_ID = '499885493'


def test_connection():
    client = BetaAnalyticsDataClient()

    request = RunReportRequest(
        property=f'properties/{PROPERTY_ID}',
        dimensions=[Dimension(name='date')],
        metrics=[
            Metric(name='sessions'),
            Metric(name='totalUsers'),
            Metric(name='screenPageViews'),
        ],
        date_ranges=[DateRange(start_date='30daysAgo', end_date='today')],
    )

    response = client.run_report(request)

    print(f'Verbindung OK! {response.row_count} Tage mit Daten.\n')
    print(f'{"Datum":<12} {"Sessions":>10} {"Users":>10} {"PageViews":>10}')
    print('-' * 44)

    rows = sorted(
        response.rows,
        key=lambda r: r.dimension_values[0].value,
        reverse=True
    )

    for row in rows:
        date = row.dimension_values[0].value
        date_fmt = f'{date[:4]}-{date[4:6]}-{date[6:]}'
        sessions = row.metric_values[0].value
        users = row.metric_values[1].value
        views = row.metric_values[2].value
        print(f'{date_fmt:<12} {sessions:>10} {users:>10} {views:>10}')


if __name__ == '__main__':
    try:
        test_connection()
    except Exception as e:
        print(f'Fehler: {e}')
        print('\nMögliche Ursachen:')
        print('  1. ga4-credentials.json nicht im selben Ordner')
        print('  2. Google Analytics Data API nicht aktiviert')
        print('  3. Service Account nicht in GA4 als Betrachter hinzugefügt')
