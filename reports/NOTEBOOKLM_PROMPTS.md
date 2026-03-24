# NotebookLM Ueberarbeitungsmodus — Animations-Prompts pro Slide
> Lade deine PowerPoint-Datei als Quelle in NotebookLM hoch.
> Oeffne dann den Notebook-Bereich und kopiere den jeweiligen Prompt fuer jede Slide.
> Die Prompts beziehen sich auf den tatsaechlichen Inhalt deiner Folien — keine hardcodierten Zahlen.

---

## Anleitung: So nutzt du diese Prompts in NotebookLM

1. **Quelle hochladen:** Lade deine PowerPoint (.pptx) in NotebookLM als Quelle hoch
2. **Notebook oeffnen:** Klicke auf "Notebook" (Ueberarbeitungsmodus)
3. **Slide auswaehlen:** Kopiere den passenden Prompt unten und fuege ihn ein
4. **Ergebnis uebernehmen:** NotebookLM generiert Animationsanweisungen basierend auf dem echten Slide-Inhalt

---

## Slide 1: Titelfolie

```
Schau dir Slide 1 (Titelfolie) meiner Praesentation an.
Erstelle detaillierte Animationsanweisungen fuer diese Folie:
- Das Logo soll von 0% auf 100% Opacity faden (0.8s ease-out)
- Der Haupttitel soll von unten hereinsliden (0.5s, 30px Offset)
- Der Untertitel mit dem Zeitraum blendet mit 0.3s Verzoegerung ein
- Das Datum blendet zuletzt ein (0.5s Delay)
- Hintergrund: Subtiler Gradient-Shift von hell nach etwas dunkler (5s Loop)
Stil: Professionell, Corporate Dashboard. Farben: Dunkelblau #1e326e, Gruen #009b91.
Gib mir die exakten Texte von der Folie in deiner Antwort wieder.
```

---

## Slide 2: Executive Summary / KPI-Karten

```
Schau dir Slide 2 (Executive Summary) meiner Praesentation an.
Lies die KPI-Karten/Kennzahlen auf dieser Folie aus und erstelle Animationsanweisungen:
- Jede KPI-Karte: Scale 0.8→1.0 + Fade-In (0.5s ease-out), staggered mit 0.2s Versatz
- Die Zahlen sollen einen Count-Up-Effekt haben (von 0 hochzaehlen, 1.5s)
- Karten: weisser Hintergrund, abgerundete Ecken (10px), dezenter Schatten
- Zahlen in Gruen #009b91, Labels in Dunkelblau #1e326e
Nenne mir die exakten KPI-Werte, die auf der Folie stehen, und ordne sie den Animationen zu.
```

---

## Slide 3: Traffic & Akquisition

```
Schau dir Slide 3 (Traffic & Akquisition) meiner Praesentation an.
Lies alle Traffic-Quellen und Zahlen von der Folie und erstelle Animationsanweisungen:
- Horizontales Balkendiagramm: Balken wachsen von links nach rechts (staggered 0.3s)
- Jeder Balken zeigt die exakte Zahl am Ende, die mit dem Balken einslided
- Balkenfarbe: #009b91 (Gruen) und #1e326e (Dunkelblau) alternierend
- Falls eine Channel-Performance-Tabelle vorhanden ist: Diese faded als Block ein (0.5s Delay)
Liste alle Traffic-Quellen mit ihren exakten Werten von der Folie auf.
```

---

## Slide 4: Neue vs. Wiederkehrende Nutzer

```
Schau dir Slide 4 (Neue vs. Wiederkehrende Nutzer) meiner Praesentation an.
Lies die Segmente und Kennzahlen aus und erstelle Animationsanweisungen:
- Donut-Diagramm zeichnet sich im Uhrzeigersinn (1.2s ease-in-out)
- Jedes Segment bekommt seine eigene Farbe (Neue: #1e326e, Returning: #009b91)
- Prozent-Label erscheint in der Mitte (Fade + Scale)
- KPI-Karten darunter staggered (je 0.15s Versatz)
- KEY INSIGHT hervorheben: Falls Returning-Nutzer ueberproportional viel Umsatz machen, bekommt deren Karte einen gruenen Glow-Pulse (1x)
Nenne alle exakten Werte von der Folie.
```

---

## Slide 5: Top-Seiten & Engagement

```
Schau dir Slide 5 (Top-Seiten & Engagement) meiner Praesentation an.
Lies die Seiten-Rangliste aus und erstelle Animationsanweisungen:
- Rangliste zeilenweise von oben nach unten (staggered 0.1s pro Zeile)
- Jede Zeile slided von links herein mit Fade
- Views-Spalte hat einen Mini-Balken, der proportional waechst
- Engagement-Werte als farbige Badges: gruen >70%, gelb 50-70%, rot <50%
- Falls eine Landing-Pages-Tabelle vorhanden ist: Diese faded danach ein
Gib alle Seiten mit ihren exakten Metriken wieder.
```

---

## Slide 6: E-Commerce Ueberblick

```
Schau dir Slide 6 (E-Commerce Ueberblick) meiner Praesentation an.
Lies den Gesamt-Umsatz und alle E-Commerce-Kennzahlen aus:
- Grosse Umsatz-KPI zaehlt von 0 hoch (2s, ease-out), Schriftfarbe wechselt grau → #009b91
- Kleinere KPIs (Kaeufe, Avg. Warenkorb, Abbruchrate) fade-in darunter (staggered 0.2s)
- Abbruchrate in Rot #af0f09 mit Warn-Pulse
- Balkendiagramm "Umsatz nach Quelle" baut sich von unten auf (staggered 0.2s)
- Balkenfarbe: #009b91
Nenne alle exakten Umsatz- und Transaktionswerte von der Folie.
```

---

## Slide 7: Produkt-Performance

```
Schau dir Slide 7 (Produkt-Performance) meiner Praesentation an.
Lies die Produkt-Rangliste aus und erstelle Animationsanweisungen:
- Produkt-Karten gleiten von links herein (staggered 0.15s)
- Jede Karte: Produktname (Fade-In), Umsatz-Balken waechst 0→Ziel (0.8s), Anzahl-Badge poppt ein (bounce)
- Top-Produkt bekommt einen Gold-Rahmen
- Balkenfarbe: #009b91
Nenne alle Produkte mit exakten Umsatz- und Mengen-Werten.
```

---

## Slide 8: Warenkorb-Analyse / Funnel

```
Schau dir Slide 8 (Warenkorb-Analyse) meiner Praesentation an.
Lies die Funnel-Stufen aus und erstelle Animationsanweisungen:
- Trichter-Diagramm stufenweise von oben nach unten (0.4s Delay pro Stufe)
- Obere Stufe (Sessions): volle Breite, hellgrau #e8eaf0
- Mittlere Stufe (Warenkorb): schmaler, Gruen #009b91
- Untere Stufe (Kauf): schmalste Stufe, Dunkelgruen
- Drop-off-Prozente zwischen Stufen blinken rot ein (#af0f09)
- Abbruchrate erscheint GROSS in Rot mit Pulse-Effekt (2x)
- Badge "Optimierungspotenzial!" slided von rechts herein
Nenne die exakten Zahlen jeder Funnel-Stufe.
```

---

## Slide 9: Erstakquise-Kanaele

```
Schau dir Slide 9 (Erstakquise-Kanaele) meiner Praesentation an.
Lies die Kanal-Daten aus und erstelle Animationsanweisungen:
- Horizontale Balken nach Umsatz, wachsen von links (staggered 0.2s)
- Farbe: Dunkelblau #1e326e
- CHF/User-Wert erscheint als kleine Zahl am Balkenende (Fade-In nach Balken-Wachstum)
- Insight-Box unten slided ein mit einer Zusammenfassung des besten Kanals
Nenne alle Kanaele mit exakten Werten.
```

---

## Slide 10: Produktkategorie-Performance

```
Schau dir Slide 10 (Produktkategorie-Performance) meiner Praesentation an.
Lies die Kategorien aus und erstelle Animationsanweisungen:
- Treemap-Bloecke staggered (0.2s), jeder Block skaliert von 0 auf Zielgroesse
- Groesste Kategorie bekommt Farbe #c8338a, weitere: #009b91, #4664af, #1e326e
- Cart/View-Rate als Overlay-Badge pro Block (Fade-In nach Block)
Nenne alle Kategorien mit exakten Umsatz- und Mengenwerten.
```

---

## Slide 11: Conversion Funnel

```
Schau dir Slide 11 (Conversion Funnel) meiner Praesentation an.
Lies die Funnel-Daten aus und erstelle Animationsanweisungen:
- Vertikaler Trichter, jede Ebene faerbt sich nacheinander ein (0.5s pro Stufe)
- Conversion-Raten erscheinen als animierte Kreise zwischen den Stufen
- Gesamt-Conversion zaehlt von 0% hoch (1s) in grosser Schrift
- Umsatz-KPI pulst 1x gruen auf
- Drop-off-Raten in Rot #af0f09, Conversions in Gruen #009b91
Nenne die exakten Conversion-Werte.
```

---

## Slide 12: Kanal-Effizienz (ROI)

```
Schau dir Slide 12 (Kanal-Effizienz / ROI) meiner Praesentation an.
Lies die Effizienz-Rangliste aus und erstelle Animationsanweisungen:
- Ranking-Tabelle zeilenweise (staggered 0.15s)
- CHF/Session als horizontale Balken die wachsen
- Bester ROI-Kanal: Badge "Bester ROI" poppt ein (bounce, gruen)
- Schlechtester ROI: Badge in Rot/Orange
Nenne alle Kanaele mit exakten CHF/Session und Umsatz-Werten.
```

---

## Slide 13: Warenkorbwert-Trend (AOV)

```
Schau dir Slide 13 (Warenkorbwert-Trend / AOV) meiner Praesentation an.
Lies den Zeitverlauf aus und erstelle Animationsanweisungen:
- Liniendiagramm zeichnet sich von links nach rechts (2s, ease-in-out)
- Datenpunkte entlang der Linie einzeichnen
- Tiefstwert und Hoechstwert hervorheben
- KPI-Karten mit Durchschnittswerten fade-in nach Linie
- Falls eine Steigerung sichtbar: Pfeil-nach-oben mit Prozentwert (bounce, gruen)
- Trendlinie (gestrichelt) zeichnet sich ueber die Datenlinie
Nenne die exakten Werte und den Zeitraum.
```

---

## Slide 14: Wiederkaufrate

```
Schau dir Slide 14 (Wiederkaufrate) meiner Praesentation an.
Lies die Segmentierung aus und erstelle Animationsanweisungen:
- Donut-Diagramm (1s): Wiederkehrende in Gruen #009b91, Neukunden in Dunkelblau #1e326e
- Prozent erscheint in der Mitte (scale + fade, 0.3s Delay)
- Effizienz-Metriken (Kaeufe/User) fade-in
- Insight-Karte unten slided ein mit gruenem Rahmen
Nenne die exakten Prozentwerte und Kaufzahlen.
```

---

## Slide 15: Landing-Page-Effizienz

```
Schau dir Slide 15 (Landing-Page-Effizienz) meiner Praesentation an.
Lies die Rangliste aus und erstelle Animationsanweisungen:
- Rangliste nach Umsatz, Zeilen staggered von oben (0.12s)
- CHF/Session als proportionale Balken
- Top-Performer: Gold-Highlight
- Seiten mit 0 Kaeufen trotz Traffic in Rot markieren
Nenne alle Landing Pages mit exakten Werten.
```

---

## Slide 16: Mobile Conversion Gap

```
Schau dir Slide 16 (Mobile Conversion Gap) meiner Praesentation an.
Lies die Geraete-Vergleichsdaten aus und erstelle Animationsanweisungen:
- Desktop-Karte slided von links herein (gruener Rahmen #009b91)
- Mobile-Karte slided von rechts herein (roter Rahmen #af0f09)
- Alle Werte zaehlen hoch — Mobile-Werte in Rot, Desktop in Gruen
- Falls Tablet-Daten vorhanden: Kleine Karte unten in Grau
- Delta-Pfeile zwischen den Karten blinken rot (pulse 2x)
- CTA-Text zur Mobile-Optimierung faded ein
Nenne die exakten Conversion-Raten und Umsaetze.
```

---

## Slide 17: Monatstrend & Saisonalitaet

```
Schau dir Slide 17 (Monatstrend & Saisonalitaet) meiner Praesentation an.
Lies die Monatsdaten aus und erstelle Animationsanweisungen:
- Umsatz-Balken wachsen von unten (staggered 0.3s pro Monat)
- Sessions-Linie zeichnet sich darueber (1s, Dunkelblau #1e326e)
- Avg. Warenkorb als Datenpunkte einpoppen (bounce)
- Trend-Pfeil mit Prozent-Veraenderung in Gruen (falls positiv) oder Rot (falls negativ)
- Balkenfarbe: #009b91
Nenne alle Monatswerte exakt.
```

---

## Slide 18: Produkt-Stickiness

```
Schau dir Slide 18 (Produkt-Stickiness) meiner Praesentation an.
Lies die Produkt-Metriken aus und erstelle Animationsanweisungen:
- Scatter-Plot/Bubble-Chart: X=View→Cart%, Y=Cart→Buy%, Bubble-Groesse=Views
- Bubbles poppen nacheinander ein (staggered 0.15s, bounce)
- Top-Performer in Gruen #009b91 (hohe Conversion)
- Problematische Produkte (0% Conversion trotz Views) in Rot #af0f09
- Produkte mit Checkout-Problem (hohe View→Cart aber 0% Cart→Buy) in Orange
- Legende erscheint zuletzt (fade-in)
Nenne alle Produkte mit exakten Stickiness-Werten.
```

---

## Slide 19: Geraete & Browser

```
Schau dir Slide 19 (Geraete & Browser) meiner Praesentation an.
Lies die Verteilung aus und erstelle Animationsanweisungen:
- Donut-Diagramm Geraete (1s): Desktop #1e326e, Mobile #009b91, Tablet Hellgrau
- Browser-Balken daneben (staggered 0.1s)
- OS-Verteilung als kleine Icons (fade-in)
- Warnhinweis-Badge falls grosser Mobile-Desktop Conversion Gap
Nenne alle exakten Geraete-, Browser- und OS-Zahlen.
```

---

## Slide 20: Geografie

```
Schau dir Slide 20 (Geografie) meiner Praesentation an.
Lies die Laender- und Staedte-Daten aus und erstelle Animationsanweisungen:
- Karte der DACH-Region faded ein (0.8s)
- Laender-Punkte poppen staggered auf (0.2s) mit Ripple-Effekt
- Punktgroesse proportional zu Sessions
- Farbintensitaet nach Sessions: Dunkelblau #1e326e Abstufungen
- Top-Staedte Rangliste rechts (zeilenweise fade-in)
Nenne alle Laender und Staedte mit exakten Werten.
```

---

## Slide 21: Probleme & Handlungsempfehlungen

```
Schau dir die letzte Slide (Probleme & Empfehlungen) meiner Praesentation an.
Lies alle Probleme und Empfehlungen aus und erstelle Animationsanweisungen:
- Zweispaltig: Links Probleme, Rechts Empfehlungen
- LINKS: Rote Karten von oben (staggered 0.2s, #af0f09)
  - Groesstes Problem: Shake-Animation (1x)
  - Weitere: Roter Badge
- RECHTS: Gruene Karten (staggered, 0.3s Delay nach Problemen, #009b91)
  - Jede mit Checkmark-Icon das einpoppt
- Gruener Rahmen um gesamte Slide pulst 1x zum Abschluss
Nenne alle exakten Probleme und Empfehlungen von der Folie.
```

---

## Allgemeine Richtlinien (einmalig in NotebookLM einfuegen)

```
Fuer alle Animationsanweisungen gelten folgende Richtlinien:

TIMING:
- Subtil und professionell, nicht verspielt
- Dauer pro Element: 0.3–0.8s
- Stagger zwischen Elementen: 0.1–0.2s
- Easing: ease-out (Einblendungen), ease-in-out (Diagramme)

FARBEN (Labtec Corporate Identity):
- Primaer: #1e326e (Dunkelblau), #009b91 (Gruen)
- Warnung/Problem: #af0f09 (Rot)
- Hintergrund: #f8f9fc
- Karten: Weiss, border-radius 10px, dezenter Schatten
- Kategoriefarben: #c8338a (Drogentest), #eb640a (Alkohol), #ffcd00 (Geschwindigkeit)

EFFEKTE:
- Count-Up fuer alle Zahlen/KPIs
- Balken wachsen proportional zur Datenmenge
- Donut/Pie zeichnen sich im Uhrzeigersinn
- Linien-Diagramme: Links nach Rechts
- Probleme: Pulse/Shake (1-2x, dezent)
- Highlights: Kurzer Glow-Effekt
- Badges: Scale 0→1 mit leichtem Bounce

WICHTIG: Verwende immer die exakten Zahlen und Texte von der jeweiligen Folie.
Runde oder schaetze keine Werte — alle Daten sind echte GA4-Analysen.
```
