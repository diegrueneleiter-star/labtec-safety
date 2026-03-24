# Animations-Prompts fuer Slide Deck — labtec-safety.ch
> Kopiere den jeweiligen Prompt beim Bearbeiten der Slide in NotebookLM / Gamma / Canva AI
> Basierend auf: SLIDE_DECK_PROMPT.md (Generiert: 24.03.2026, Zeitraum: 90 Tage)

---

## Slide 1: Titel

```
Animiere diese Titelfolie:
- Labtec-Logo faded von 0% auf 100% Opacity (0.8s ease-out)
- Titel "Web-Analytics Report — labtec-safety.ch" slided von unten herein (0.5s, 30px Offset)
- Untertitel "Datenbasierte Analyse der letzten 90 Tage" Fade-In mit 0.3s Delay
- Datum "24.03.2026" blendet zuletzt ein (0.5s Delay)
- Hintergrund: Subtiler Gradient-Shift #f8f9fc → #e8eaf0 (5s Loop)
Stil: Soft Corporate Dashboard. Farben: #1e326e (Dunkelblau), #009b91 (Gruen).
```

---

## Slide 2: Executive Summary (KPI-Karten)

```
Animiere 4 KPI-Karten nebeneinander (staggered, je 0.2s Versatz):
Jede Karte: Scale 0.8→1.0 + Fade-In (0.5s ease-out).
Zahlen zaehlen von 0 hoch (Count-Up, 1.5s):
  - Karte 1: "8'573 Sessions" (Gruen #009b91)
  - Karte 2: "126'317 CHF Umsatz" (Gruen #009b91)
  - Karte 3: "126 Kaeufe" (Gruen #009b91)
  - Karte 4: "1'003 CHF Avg. Warenkorb" (Gruen #009b91)
Karten: weiss, border-radius 10px, dezenter Schatten baut sich beim Erscheinen auf.
Labels unter den Zahlen in Dunkelblau #1e326e.
```

---

## Slide 3: Traffic & Akquisition

```
Animiere horizontales Balkendiagramm — Balken wachsen von links nach rechts (staggered 0.3s):
  1. google/cpc: 3'366 Sessions (volle Breite) — #009b91
  2. (direct)/(none): 2'132 Sessions — #1e326e
  3. google/organic: 1'901 Sessions — #009b91 heller
  4. bing/organic: 291 Sessions
  5. littlegiant-leitern.de/referral: 254 Sessions
  6. bailaho.ch/referral: 175 Sessions
  7. portal.socarretail.com/referral: 137 Sessions
Jeder Balken hat die Zahl am Ende, die mit dem Balken einslided.
Rechts daneben: Channel-Performance-Tabelle faded als Block ein (0.5s Delay):
  Paid Search: 3'170 Sess, 67.9% Engage, 140 Conv
  Organic Search: 2'257 Sess, 64.0% Engage, 198 Conv
  Direct: 2'132 Sess, 50.7% Engage, 334 Conv
  Referral: 662 Sess, 59.8% Engage, 494 Conv
  Display: 216 Sess, 28.7% Engage, 0 Conv
```

---

## Slide 4: Neue vs. Wiederkehrende Nutzer

```
Animiere Donut-Diagramm im Uhrzeigersinn (1.2s ease-in-out):
  - Segment "new": 66.1% (5'575 Sessions) — Dunkelblau #1e326e
  - Segment "returning": 29.1% (2'454 Sessions) — Gruen #009b91
  - Segment "(not set)": 4.8% (409 Sessions) — Hellgrau
Prozent-Label erscheint in der Mitte (Fade + Scale).
KPI-Karten darunter staggered (je 0.15s):
  - Neue: 5'575 Sessions, 18'679.21 CHF Umsatz, 41 Kaeufe, 455.59 CHF Avg.
  - Returning: 2'454 Sessions, 107'637.99 CHF Umsatz, 85 Kaeufe, 1'266.33 CHF Avg.
KEY INSIGHT: Returning-Karte bekommt gruenen Glow-Pulse (1x) —
Returning = 85.2% des Umsatzes bei nur 29% der Sessions!
```

---

## Slide 5: Top-Seiten & Engagement

```
Animiere Rangliste zeilenweise von oben nach unten (staggered 0.1s pro Zeile).
Jede Zeile slided von links herein mit Fade.
Views-Spalte hat Mini-Balken der proportional waechst:
  1. / (Homepage): 3'966 Views, 69.3% Engage, 77s Dauer
  2. /onlineshop/: 1'164 Views, 87.9% Engage, 56s
  3. /mein-konto/: 1'081 Views, 93.1% Engage, 67s
  4. /uber-uns/verkaufsladen/: 981 Views, 57.8% Engage, 77s
  5. /uber-uns/team/: 742 Views, 85.0% Engage, 104s
Engagement%-Werte als farbige Badges: gruen >70%, gelb 50-70%, rot <50%.
Zweite Tabelle "Landing Pages" faded danach ein:
  /: 2'785 Sess, 30.8% Bounce | /uber-uns/verkaufsladen: 669 Sess, 49.2% Bounce
```

---

## Slide 6: E-Commerce Ueberblick

```
Animiere grosse Umsatz-KPI "126'317.20 CHF" — zaehlt von 0 hoch (2s, ease-out).
Waehrend Count-Up: Schriftfarbe grau → #009b91.
3 kleinere KPIs fade-in darunter (staggered 0.2s):
  - "126 Kaeufe"
  - "1'003 CHF Avg. Warenkorb"
  - "85.6% Abbruchrate" in Rot #af0f09 mit Warn-Pulse
Balkendiagramm "Umsatz nach Quelle" baut sich von unten auf (staggered 0.2s):
  1. (direct)/(none): 55'403.28 CHF, 39 Kaeufe — groesster Balken
  2. google/organic: 51'898.56 CHF, 25 Kaeufe
  3. google/cpc: 8'993.19 CHF, 19 Kaeufe
  4. portal.socarretail.com/referral: 8'858.04 CHF, 39 Kaeufe
  5. statics.teams.cdn.office.net: 746.81 CHF, 1 Kauf
  6. bing/organic: 310.30 CHF, 2 Kaeufe
Balkenfarbe: #009b91.
```

---

## Slide 7: Produkt-Performance

```
Animiere Produkt-Rangliste als Karten von links hereingleitend (staggered 0.15s).
Jede Karte: Produktname (Fade-In), Umsatz-Balken waechst 0→Ziel (0.8s), Anzahl-Badge poppt ein (bounce).
  1. DrugWipe 6S+: 49'446.75 CHF, 1'575x gekauft, 95 Views → Gold-Rahmen
  2. Mundstuecke: 23'785.68 CHF, 182x gekauft, 113 Views
  3. DrugWipe 6S: 7'620.75 CHF, 225x gekauft, 51 Views
  4. Drogentest Urin Kreatinin 9 Par.: 6'567.21 CHF, 27x, 9 Views
  5. Lingette DrugWipe 6S: 6'270.00 CHF, 200x, 4 Views
  6. Embouchures: 4'643.84 CHF, 33x, 27 Views
  7. Drogenschnelltest Urin Pipettier 9 Par.: 3'648.45 CHF, 15x
Balkenfarbe: Labtec-Gruen #009b91. Top-Produkt mit Gold-Akzent.
```

---

## Slide 8: Warenkorb-Analyse

```
Animiere Trichter-Diagramm stufenweise von oben nach unten (0.4s Delay pro Stufe):
  1. Sessions: 8'573 (volle Breite, hellgrau #e8eaf0)
  2. Warenkorb: 875 (schmaler, Gruen #009b91) — "Drop-off 89.8%" blinkt rot ein
  3. Kauf: 126 (schmalste Stufe, Dunkelgruen) — "Drop-off 85.6%" blinkt rot ein
Rote Pfeile mit Drop-off-Prozent zwischen Stufen (fade-in).
Abbruchrate "85.6%" erscheint GROSS in Rot #af0f09 mit Pulse-Effekt (2x).
Tagesdetail als kleine Sparkline darunter (optional).
Badge "Optimierungspotenzial!" slided von rechts herein.
```
