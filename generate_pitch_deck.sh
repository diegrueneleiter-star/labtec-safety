#!/bin/bash
# ─────────────────────────────────────────────────────────────
# Pitch Deck Generator fuer labtec-safety.ch
# Generiert GA4-Daten, erstellt Slide Deck Prompt + HTML-Vorschau
# ─────────────────────────────────────────────────────────────

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

echo ""
echo "=================================================="
echo "  labtec-safety.ch — Pitch Deck Generator"
echo "=================================================="
echo ""

# Schritt 1: GA4-Daten erheben
echo "[1/3] GA4-Daten werden erhoben (alle Module inkl. Business Insights)..."
echo ""
python3 ga4_analytics.py --all --csv

echo ""
echo "[2/3] Slide Deck Prompt-Paket + HTML-Vorschau werden erstellt..."
echo ""
python3 slide_deck_generator.py --html

echo ""
echo "=================================================="
echo "  FERTIG!"
echo "=================================================="
echo ""
echo "  Erstellte Dateien:"
echo "  ─────────────────"
echo "  reports/SLIDE_DECK_PROMPT.md  → In NotebookLM hochladen"
echo "  reports/slide_preview.html    → HTML-Vorschau im Browser"
echo "  reports/SUMMARY.md            → Zusammenfassung aller Daten"
echo "  reports/*.csv                 → Rohdaten"
echo ""

# Schritt 3: HTML-Vorschau oeffnen
if [[ "$OSTYPE" == "darwin"* ]]; then
    echo "[3/3] HTML-Vorschau wird geoeffnet..."
    open "$SCRIPT_DIR/reports/slide_preview.html"
elif command -v xdg-open &>/dev/null; then
    echo "[3/3] HTML-Vorschau wird geoeffnet..."
    xdg-open "$SCRIPT_DIR/reports/slide_preview.html"
else
    echo "[3/3] Oeffne manuell: $SCRIPT_DIR/reports/slide_preview.html"
fi

echo ""
echo "  Naechster Schritt:"
echo "  1. Oeffne notebooklm.google.com"
echo "  2. Neues Notebook erstellen"
echo "  3. reports/SLIDE_DECK_PROMPT.md als Quelle hochladen"
echo "  4. Prompt eingeben:"
echo ""
echo "     Erstelle ein professionelles Pitch Deck basierend auf"
echo "     den GA4-Daten. Folge den Design-Richtlinien und der"
echo "     Slide-Struktur im Dokument. Alle Zahlen sind echte"
echo "     GA4-Daten in CHF — woertlich uebernehmen."
echo ""
