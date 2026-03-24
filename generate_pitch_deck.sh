#!/bin/bash
# ─────────────────────────────────────────────────────────────
# Pitch Deck Generator fuer labtec-safety.ch
# Generiert GA4-Daten, erstellt Slide Deck Prompt + HTML-Vorschau
# + Gamma.app Prompt-Paket
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
echo "[1/4] GA4-Daten werden erhoben (alle Module inkl. Business Insights)..."
echo ""
python3 ga4_analytics.py --all --csv

echo ""
echo "[2/4] Slide Deck Prompt-Paket + HTML-Vorschau werden erstellt..."
echo ""
python3 slide_deck_generator.py --html

echo ""
echo "[3/4] Gamma.app Prompt-Paket wird erstellt..."
echo ""
python3 gamma_prompt_generator.py

echo ""
echo "=================================================="
echo "  FERTIG!"
echo "=================================================="
echo ""
echo "  Erstellte Dateien:"
echo "  ─────────────────"
echo "  NotebookLM:"
echo "    reports/SLIDE_DECK_PROMPT.md  → In NotebookLM hochladen"
echo "    reports/slide_preview.html    → HTML-Vorschau im Browser"
echo ""
echo "  Gamma.app:"
echo "    reports/GAMMA_PROMPT.md       → In Gamma hochladen (Import)"
echo "    reports/GAMMA_PASTE_PROMPT.txt→ Prompt ins Textfeld einfuegen"
echo ""
echo "  Rohdaten:"
echo "    reports/SUMMARY.md            → Zusammenfassung aller Daten"
echo "    reports/*.csv                 → Rohdaten"
echo ""

# Schritt 4: HTML-Vorschau oeffnen
if [[ "$OSTYPE" == "darwin"* ]]; then
    echo "[4/4] HTML-Vorschau wird geoeffnet..."
    open "$SCRIPT_DIR/reports/slide_preview.html"
elif command -v xdg-open &>/dev/null; then
    echo "[4/4] HTML-Vorschau wird geoeffnet..."
    xdg-open "$SCRIPT_DIR/reports/slide_preview.html"
else
    echo "[4/4] Oeffne manuell: $SCRIPT_DIR/reports/slide_preview.html"
fi

echo ""
echo "  Naechste Schritte:"
echo "  ─────────────────"
echo ""
echo "  Option A — NotebookLM:"
echo "  1. Oeffne notebooklm.google.com"
echo "  2. Neues Notebook erstellen"
echo "  3. reports/SLIDE_DECK_PROMPT.md als Quelle hochladen"
echo "  4. Prompt eingeben:"
echo "     Erstelle ein professionelles Pitch Deck basierend auf"
echo "     den GA4-Daten. Folge den Design-Richtlinien und der"
echo "     Slide-Struktur im Dokument. Alle Zahlen sind echte"
echo "     GA4-Daten in CHF — woertlich uebernehmen."
echo ""
echo "  Option B — Gamma.app:"
echo "  1. Oeffne gamma.app/create/generate"
echo "  2. reports/GAMMA_PROMPT.md als Dokument importieren"
echo "  3. Inhalt von reports/GAMMA_PASTE_PROMPT.txt ins Textfeld"
echo "  4. Generate klicken"
echo ""
