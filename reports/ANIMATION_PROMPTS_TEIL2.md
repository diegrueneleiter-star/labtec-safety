# Animations-Prompts Teil 2 — Slides 9–21

---

## Slide 9: Erstakquise-Kanaele

```
Animiere horizontale Balken nach Umsatz, wachsen von links (staggered 0.2s):
  1. Paid Search: 43'355.80 CHF, 24 Kaeufe, 17.89 CHF/User — laengster Balken
  2. Organic Search: 37'563.17 CHF, 26 Kaeufe, 24.58 CHF/User
  3. Direct: 36'188.69 CHF, 39 Kaeufe, 25.56 CHF/User
  4. Referral: 8'884.72 CHF, 36 Kaeufe, 31.51 CHF/User
  5. Unassigned: 324.82 CHF, 1 Kauf, 23.20 CHF/User
Farbe: Labtec-Dunkelblau #1e326e.
CHF/User erscheint als kleine Zahl am Balkenende (Fade-In nach Balken-Wachstum).
Insight-Box unten: "Paid Search bringt hoechsten Erstakquise-Umsatz, Referral besten CHF/User" slided ein.
```

---

## Slide 10: Produktkategorie-Performance

```
Animiere Treemap-Bloecke staggered (0.2s), jeder Block skaliert von 0 auf Zielgroesse:
  1. Speicheltest: 49'446.75 CHF, 1'575x gekauft — Farbe #c8338a (groesster Block)
  2. Verbrauchsmaterial: 18'576.14 CHF, 139x — Farbe #009b91
  3. Mehrfach Urintest: 17'591.20 CHF, 74x — Farbe #4664af
  4. Test salivaire: 13'890.75 CHF, 425x — Farbe #c8338a heller
  5. Medizin & Institution: 6'243.54 CHF, 35x — Farbe #1e326e
  6. Consommables: 4'027.48 CHF, 31x
  7. Privatanwender: 1'075.51 CHF, 11x
Cart/View-Rate als Overlay-Badge pro Block (Fade-In nach Block):
  Speicheltest: 2901.7% | Test salivaire: 873.1% | Mehrfach Urintest: 197.5%
```

---

## Slide 11: Conversion Funnel

```
Animiere vertikalen Trichter, jede Ebene faerbt sich nacheinander ein (0.5s pro Stufe):
  Sessions (8'573) → 10.2% Conv → Warenkorb (875) → 14.4% Conv → Kauf (126)
Conversion-Raten erscheinen als animierte Kreise zwischen den Stufen.
Gesamt-Conversion "1.47%" zaehlt von 0% hoch (1s) in grosser Schrift.
Umsatz-KPI "126'317.20 CHF" pulst 1x gruen auf.
Drop-off-Raten in Rot #af0f09: "89.8%" und "85.6%".
Gruen #009b91 fuer Conversions, Rot #af0f09 fuer Drop-offs.
```

---

## Slide 12: Kanal-Effizienz (ROI)

```
Animiere Ranking-Tabelle zeilenweise (staggered 0.15s).
CHF/Session als horizontale Balken die wachsen:
  1. Direct: 25.99 CHF/Session, 39.40 CHF/User, 55'403.28 CHF Umsatz — Gruen, laengster
  2. Organic Search: 23.18 CHF/Session, 32.66 CHF/User, 52'315.88 CHF
  3. Referral: 14.51 CHF/Session, 32.02 CHF/User, 9'604.85 CHF
  4. Paid Search: 2.84 CHF/Session, 3.61 CHF/User, 8'993.19 CHF — Orange/Warnung
  5. Cross-network: 0.00 CHF — Grau
  6. Display: 0.00 CHF — Grau
Badge "Bester ROI" poppt bei Direct ein (bounce). Badge "Niedrigster ROI" bei Paid Search (rot).
```

---

## Slide 13: Warenkorbwert-Trend (AOV)

```
Animiere Liniendiagramm von links nach rechts (2s, ease-in-out).
X-Achse: Jan 2026 – Maerz 2026. Y-Achse: CHF.
Datenpunkte zeichnen sich entlang der Linie ein. Starke Schwankungen sichtbar:
  Tiefstwert: 38.62 CHF (01.01.) | Hoechstwert: 6'448.16 CHF (16.03.)
Zwei KPI-Karten fade-in nach Linie:
  - "1. Haelfte Avg: 487 CHF" (Dunkelblau #1e326e)
  - "2. Haelfte Avg: 1'293 CHF" (Gruen #009b91)
Pfeil-nach-oben zwischen Karten: "+166% Steigerung" (bounce, gruen).
Trendlinie (gestrichelt) zeichnet sich ueber die Datenlinie.
```

---

## Slide 14: Wiederkaufrate

```
Animiere Donut-Diagramm (1s):
  - Wiederkehrende: 67.5% (85 Kaeufe) — Gruen #009b91
  - Neukunden: 32.5% (41 Kaeufe) — Dunkelblau #1e326e
Prozent "67.5%" erscheint in der Mitte (scale + fade, 0.3s Delay).
Effizienz-Metriken fade-in:
  - Returning: 0.09 Kaeufe/User
  - New: 0.01 Kaeufe/User
Insight-Karte unten: "Stammkunden = 85% des Umsatzes" slided ein mit gruenem Rahmen.
```

---

## Slide 15: Landing-Page-Effizienz

```
Animiere Rangliste nach Umsatz, Zeilen staggered von oben (0.12s):
  1. /: 46'391.75 CHF, 2.41% Conv, 16.66 CHF/Sess — Gruen
  2. /fr/produkt/drugwipe-6s-2: 15'923.13 CHF, 17.65% Conv, 936.65 CHF/Sess — Gold-Highlight
  3. /onlineshop: 15'743.41 CHF, 7.14% Conv, 86.50 CHF/Sess
  4. /de/Login.27.html: 15'456.03 CHF, 150% Conv, 7'728 CHF/Sess — Sonderfall-Badge
  5. /mein-konto: 11'062.74 CHF, 9.16% Conv, 84.45 CHF/Sess
CHF/Session als proportionale Balken.
Seiten mit 0 Kaeufen trotz Traffic in Rot markieren: /uber-uns/verkaufsladen (669 Sess, 0 Kaeufe).
```

---

## Slide 16: Mobile Conversion Gap

```
Animiere Vergleichs-Karten Desktop vs. Mobile (slide-in von links/rechts):
Desktop-Karte (links, gruener Rahmen #009b91):
  - Conv-Rate: 2.24% (zaehlt hoch)
  - CHF/Session: 23.62 (zaehlt hoch)
  - Umsatz: 125'514.24 CHF
  - Bounce: 36.4%
Mobile-Karte (rechts, roter Rahmen #af0f09):
  - Conv-Rate: 0.23% (zaehlt hoch — rot!)
  - CHF/Session: 0.26 (zaehlt hoch — rot!)
  - Umsatz: 802.96 CHF
  - Bounce: 40.5%
Tablet-Karte (klein, unten): 0.00% Conv, 0 CHF — Grau
Delta-Pfeile: "-2.01pp Conv" und "-23.36 CHF/Sess" blinken rot (pulse 2x).
CTA: "Mobile-Optimierung = groesstes Umsatzpotenzial" faded ein.
```

---

## Slide 17: Monatstrend & Saisonalitaet

```
Animiere Kombinations-Diagramm:
  1. Umsatz-Balken wachsen von unten (staggered 0.3s):
     - Dez 2025: 0 CHF, 453 Sessions (kein Balken)
     - Jan 2026: 31'209.96 CHF, 48 Kaeufe, 3'115 Sessions
     - Feb 2026: 50'105.90 CHF, 49 Kaeufe, 2'949 Sessions (hoechster)
     - Maerz 2026: 45'001.34 CHF, 29 Kaeufe, 2'056 Sessions
  2. Sessions-Linie zeichnet sich darueber (1s, Dunkelblau #1e326e)
  3. Avg. Warenkorb als Datenpunkte einpoppen (bounce):
     Jan: 650.21 CHF → Feb: 1'022.57 CHF → Maerz: 1'551.77 CHF
Trend-Pfeil "AOV steigt +139%!" gruen.
Balkenfarbe: #009b91.
```

---

## Slide 18: Produkt-Stickiness

```
Animiere Scatter-Plot/Bubble-Chart:
X-Achse: View→Cart%, Y-Achse: Cart→Buy%, Bubble-Groesse: Views.
Bubbles poppen nacheinander ein (staggered 0.15s, bounce):
  GRUEN (Top-Performer, #009b91):
    - DrugWipe 6S+: 3634.7% V→C, 45.6% C→B, 95 Views — groesste Bubble
    - DrugWipe 6S: 784.3% V→C, 56.2% C→B, 51 Views
    - Mundstuecke: 365.5% V→C, 44.1% C→B, 113 Views
  ROT (Preishuerde, #af0f09):
    - AlcoTrue P: 0.0% V→C bei 177 Views — grosse rote Bubble!
    - Alcotest AlcoTrue P: 0.0% bei 93 Views
    - Traffic Counter: 0.0% bei 78 Views
    - AlcoTrue C Set: 2.2% V→C bei 138 Views
  ORANGE (Checkout-Problem):
    - Test rapide depistage salive: 21.8% V→C aber 0.0% C→B, 55 Views
    - AlcoTrue M: 6.9% V→C aber nur 25.0% C→B
Legende erscheint zuletzt (fade-in).
```

---

## Slide 19: Geraete & Browser

```
Animiere Donut-Diagramm Geraete (1s):
  - Desktop: 62.5% (5'314 Sessions) — Dunkelblau #1e326e
  - Mobile: 36.3% (3'085 Sessions) — Gruen #009b91
  - Tablet: 1.1% (93 Sessions) — Hellgrau
Browser-Balken daneben (staggered 0.1s):
  Chrome: 4'301 Sess, 61.1% Engage | Safari: 1'804 Sess, 55.1%
  Edge: 1'604 Sess, 70.6% | Firefox: 345 Sess, 68.4%
  Samsung Internet: 307 Sess, 63.5%
OS-Verteilung als kleine Icons (fade-in):
  Windows: 4'444 | iOS: 1'734 | Android: 1'484 | Mac: 560
Warnhinweis-Badge: "Mobile Conv 0.23% vs Desktop 2.24%" rot #af0f09.
```

---

## Slide 20: Geografie

```
Animiere Karte DACH-Region (fade-in 0.8s).
Laender-Punkte poppen staggered auf (0.2s), mit Ripple-Effekt:
  1. Switzerland: 5'853 Sessions, 4'009 Users, 66.4% Engage — groesster Punkt
  2. Germany: 905 Sessions, 358 Users, 59.2%
  3. France: 558 Sessions, 510 Users, 65.8%
  4. United States: 410 Sessions, 5.6% Engage (niedrig!)
  5. Singapore: 127 Sessions, 67.7% Engage
  6. Romania: 109 Sessions, 67.9% Engage
  7. Austria: 102 Sessions, 54.9% Engage
Farbintensitaet nach Sessions: Dunkelblau #1e326e Abstufungen.
Top-Staedte Rangliste rechts (zeilenweise fade-in):
  Zurich: 1'092 | Bern: 222 | Frick: 192 | Lausanne: 178 | Villmergen: 171
```

---

## Slide 21: Probleme & Handlungsempfehlungen

```
Animiere zweispaltig: Links Probleme, Rechts Empfehlungen.
LINKS — Rote Karten von oben (staggered 0.2s, #af0f09):
  1. "Warenkorb-Abbruch 85.6%" — Shake-Animation (1x)
  2. "Mobile Conv Gap: Desktop 2.24% vs Mobile 0.23%" — roter Badge
  3. "High-Bounce Produktseiten: Fischermuetze 80%, Tragekoffer 71.4%" — roter Badge
  4. "Display-Kanal: 216 Sessions, 0 Conversions, 0 CHF" — roter Badge
  5. "AlcoTrue P: 177 Views, 0% View→Cart" — roter Badge
RECHTS — Gruene Karten (staggered, 0.3s Delay nach Problemen, #009b91):
  1. "Checkout-Prozess vereinfachen (85.6% Abbruch!)" — Checkmark-Icon poppt
  2. "Mobile UX ueberarbeiten (nur 802 CHF vs 125'514 CHF Desktop)"
  3. "Produktseiten: Bessere Bilder, Preise, Call-to-Actions"
  4. "Display-Budget → Referral umschichten (6.04% Conv vs 0%)"
  5. "AlcoTrue P Produktseite optimieren (Preishuerde?)"
Gruener Rahmen um gesamte Slide pulst 1x zum Abschluss.
```

---

## Allgemeine Animations-Richtlinien (fuer alle Slides)

```
TIMING:
- Subtil und professionell, nicht verspielt
- Dauer pro Element: 0.3–0.8s
- Stagger zwischen Elementen: 0.1–0.2s
- Easing: ease-out (Einblendungen), ease-in-out (Diagramme)

FARBEN:
- Primaer: #1e326e (Dunkelblau), #009b91 (Gruen)
- Warn/Problem: #af0f09 (Rot)
- Hintergrund: #f8f9fc
- Karten: Weiss, border-radius 10px, dezenter Schatten
- Kategorien: #c8338a (Drogentest), #eb640a (Alkohol), #ffcd00 (Geschwindigkeit)

EFFEKTE:
- Count-Up fuer alle Zahlen/KPIs
- Balken wachsen proportional zur Datenmenge
- Donut/Pie zeichnen sich im Uhrzeigersinn
- Linien-Diagramme zeichnen sich von links nach rechts
- Probleme: Pulse/Shake (1-2x, dezent)
- Highlights: Kurzer Glow-Effekt
- Badges: Scale 0→1 mit leichtem Bounce

DATENINTEGRITAET:
- Alle Zahlen sind echte GA4-Daten — NICHT runden oder schaetzen
- Werte woertlich uebernehmen
```
