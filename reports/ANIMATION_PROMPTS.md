# Animations-Prompts fuer Slide Deck — labtec-safety.ch
> Kopiere den jeweiligen Prompt beim Bearbeiten der Slide in NotebookLM / Gamma / Canva AI

---

## Slide 1: Titel

```
Animation: Das Labtec-Logo faded von 0% auf 100% Opacity (0.8s ease-out).
Danach slides der Titel "Web-Analytics Report" von unten herein (0.5s, 30px offset).
Der Untertitel "Datenbasierte Analyse der letzten 90 Tage" erscheint mit 0.3s Verzoegerung als Fade-In.
Das Datum blendet zuletzt ein (0.5s delay).
Hintergrund: Subtiler Gradient-Shift von #f8f9fc nach #e8eaf0 (5s Loop, sanft).
```

---

## Slide 2: Executive Summary (KPI-Karten)

```
Animation: 4 KPI-Karten erscheinen nacheinander von links nach rechts (staggered, je 0.2s Versatz).
Jede Karte: Scale von 0.8 auf 1.0 + Fade-In (0.5s ease-out).
Die Zahlen in den Karten zaehlen hoch (Count-Up Animation, 1.5s):
  - 8'578 Sessions (von 0 hochzaehlend)
  - 126'317 CHF Umsatz (von 0 hochzaehlend)
  - 126 Kaeufe (von 0 hochzaehlend)
  - 1'003 CHF Avg. Warenkorb (von 0 hochzaehlend)
Dezenter Schatten auf den Karten baut sich beim Erscheinen auf (box-shadow transition).
```

---

## Slide 3: Traffic & Akquisition

```
Animation: Horizontale Balken wachsen von links nach rechts (staggered, 0.3s pro Balken).
Reihenfolge nach Groesse:
  1. google/cpc: Balken waechst auf 3'370 (volle Breite) — Farbe #009b91
  2. (direct)/(none): Balken waechst auf 2'134 — Farbe #1e326e
  3. google/organic: Balken waechst auf 1'901 — Farbe #009b91 heller
  4. bing/organic: Balken waechst auf 291
  5. Weitere Quellen kleiner werdend
Jeder Balken hat eine Zahl am Ende, die mit dem Balken einslided.
Die Channel-Performance-Tabelle rechts daneben faded als Block ein (0.5s delay nach Balken).
```

---

## Slide 4: Neue vs. Wiederkehrende Nutzer

```
Animation: Donut-Diagramm zeichnet sich im Uhrzeigersinn (1.2s ease-in-out).
  - Segment 1 (new): 69.4% in Dunkelblau #1e326e
  - Segment 2 (returning): 30.6% in Gruen #009b91
Prozent-Label erscheint in der Mitte nach Abschluss der Animation (Fade + Scale).
KPI-Karten darunter staggered einblenden (je 0.15s Versatz):
  - Neue: 5'577 Sessions, 18'679 CHF (455 CHF Avg.)
  - Returning: 2'455 Sessions, 107'638 CHF (1'266 CHF Avg.)
Highlight-Effekt: Die Returning-Karte bekommt einen gruenen Glow-Pulse (1x),
weil Returning 85% des Umsatzes ausmacht — das ist die Key Insight.
```

---

## Slide 5: Top-Seiten & Engagement

```
Animation: Rangliste erscheint zeilenweise von oben nach unten (staggered, 0.1s pro Zeile).
Jede Zeile slided von links herein mit Fade.
Die Views-Spalte hat einen Mini-Balken der proportional waechst:
  - Homepage: 3'971 Views (volle Breite)
  - Onlineshop: 1'165 Views
  - Mein Konto: 1'081 Views
  - Verkaufsladen: 982 Views
  - Team: 743 Views
Engagement%-Werte erscheinen als farbige Badges (gruen > 70%, gelb 50-70%).
```

---

## Slide 6: E-Commerce Ueberblick

```
Animation: Grosse Umsatz-KPI "126'317 CHF" zaehlt von 0 hoch (2s, ease-out).
Waehrend des Hochzaehlens: Schriftfarbe geht von grau zu #009b91.
Darunter 3 kleinere KPIs fade-in (staggered 0.2s):
  - 126 Kaeufe
  - 1'003 CHF Avg. Warenkorb
  - 85.6% Abbruchrate (in Rot #af0f09, mit Warn-Pulse)
Balkendiagramm "Umsatz nach Quelle" baut sich von unten auf:
  - (direct)/(none): 55'403 CHF (groesster Balken)
  - google/organic: 51'899 CHF
  - google/cpc: 8'993 CHF
  - portal.socarretail.com: 8'858 CHF
Balken wachsen staggered (0.2s Versatz), Farbe #009b91.
```

---

## Slide 7: Produkt-Performance

```
Animation: Produkt-Rangliste erscheint als Karten von links hereingleitend (staggered 0.15s).
Jede Karte hat:
  - Produktname (Fade-In)
  - Umsatz-Balken der von 0 auf Zielwert waechst (0.8s)
  - Anzahl-Badge der einpoppt (scale 0 → 1, bounce)
Top-Produkt "DrugWipe 6S+" bekommt einen Gold-Rahmen und erscheint zuerst:
  49'447 CHF, 1'575x verkauft
Danach: Mundstuecke (23'786 CHF), DrugWipe 6S (7'621 CHF), etc.
```

---

## Slide 8: Warenkorb-Analyse & Abbruchrate

```
Animation: Trichter-Diagramm baut sich stufenweise von oben nach unten auf.
Jede Stufe erscheint mit 0.4s Verzoegerung:
  1. Sessions: 8'578 (volle Breite, hellgrau #e8eaf0)
  2. Warenkorb: 875 (schmaler, Gruen #009b91) — "Drop-off 89.8%" blinkt rot ein
  3. Kauf: 126 (schmalste Stufe, Dunkelgruen) — "Drop-off 85.6%" blinkt rot ein
Zwischen den Stufen: Rote Pfeile mit Drop-off-Prozent fade-in.
Die Abbruchrate "85.6%" erscheint gross in Rot #af0f09 mit einem Pulse-Effekt (2x).
Empfehlung-Badge am Ende: "Optimierungspotenzial!" slides von rechts herein.
```

---

## Slide 9: Conversion Funnel Detail

```
Animation: Funnel als vertikaler Trichter, jede Ebene faerbt sich nacheinander ein (0.5s pro Stufe).
  Sessions (8'578) → 10.2% → Warenkorb (875) → 14.4% → Kauf (126)
Conversion-Raten erscheinen als animierte Kreise zwischen den Stufen.
Gesamt-Conversion "1.47%" zaehlt von 0% hoch (1s) in grosser Schrift.
Umsatz-KPI "126'317 CHF" pulst einmal gruen auf.
```

---

## Slide 10: Kanal-Effizienz (ROI)

```
Animation: Ranking-Tabelle erscheint zeilenweise (staggered 0.15s).
CHF/Session als horizontale Balken die wachsen:
  - Direct: 25.96 CHF/Session (laengster Balken, Gruen)
  - Organic: 23.18 CHF/Session
  - Referral: 14.51 CHF/Session
  - Paid Search: 2.83 CHF/Session (kuerzester Balken, Orange als Warnung)
Badge "Bester ROI" poppt beim Direct-Kanal ein (bounce-animation).
Badge "Teuerster Kanal" poppt beim Paid Search ein (rot).
```

---

## Slide 11: Erstakquise-Attribution

```
Animation: Horizontale Balken nach Umsatz, wachsen von links (staggered 0.2s):
  - Paid Search: 43'356 CHF (laengster Balken)
  - Organic Search: 37'563 CHF
  - Direct: 36'189 CHF
  - Referral: 8'885 CHF
Sekundaer-Metrik "CHF/User" erscheint als kleine Zahl am Balkenende (Fade-In nach Balken-Wachstum).
Insight-Box: "Paid Search bringt den meisten Erstakquise-Umsatz" slided von unten ein.
```

---

## Slide 12: Produktkategorie-Performance

```
Animation: Treemap-Bloecke erscheinen staggered (0.2s), jeder Block skaliert von 0 auf Zielgroesse:
  - Speicheltest: 49'447 CHF (groesster Block, Farbe #c8338a)
  - Verbrauchsmaterial: 18'576 CHF
  - Mehrfach Urintest: 17'591 CHF
  - Test salivaire: 13'891 CHF
  - Medizin & Institution: 6'244 CHF
Cart/View-Rate als Overlay-Badge pro Block (Fade-In nach Block-Animation).
```

---

## Slide 13: Warenkorbwert-Trend (AOV)

```
Animation: Liniendiagramm zeichnet sich von links nach rechts (2s, ease-in-out).
X-Achse: Zeitverlauf (Jan–Maerz 2026).
Y-Achse: CHF-Wert.
Die Linie waechst visuell und zeigt den steigenden Trend.
Zwei KPI-Karten fade-in nach der Linie:
  - "1. Haelfte: 487 CHF" (Dunkelblau)
  - "2. Haelfte: 1'293 CHF" (Gruen)
Pfeil-nach-oben-Icon zwischen den Karten mit "+166% Steigerung" (bounce-animation, gruen).
```

---

## Slide 14: Wiederkaufrate

```
Animation: Donut-Diagramm zeichnet sich (1s):
  - Wiederkehrende: 67.5% (85 Kaeufe) in Gruen #009b91
  - Neukunden: 32.5% (41 Kaeufe) in Dunkelblau #1e326e
Prozent-Label "67.5%" erscheint in der Mitte (scale + fade, 0.3s delay).
Insight-Karte: "Stammkunden = 85% des Umsatzes" slided von unten ein mit gruenem Rahmen.
```

---

## Slide 15: Monatstrend

```
Animation: Kombinations-Diagramm baut sich auf:
  1. Zuerst: Umsatz-Balken wachsen von unten (staggered 0.3s pro Monat):
     - Dez 2025: 0 CHF (kein Balken)
     - Jan 2026: 31'210 CHF
     - Feb 2026: 50'106 CHF (hoechster Balken)
     - Maerz 2026: 45'001 CHF
  2. Dann: Sessions-Linie zeichnet sich darueber (1s, Dunkelblau #1e326e)
  3. Zuletzt: Avg. Warenkorb als Datenpunkte einpoppen (bounce):
     - Jan: 650 CHF → Feb: 1'023 CHF → Maerz: 1'552 CHF
Trend-Pfeil "Avg. Warenkorb steigt!" erscheint mit gruener Farbe.
```

---

## Slide 16: Geraete & Browser

```
Animation: Donut-Diagramm der Geraete zeichnet sich (1s):
  - Desktop: 62.6% (5'318 Sessions) — Dunkelblau
  - Mobile: 36.3% (3'086 Sessions) — Gruen
  - Tablet: 1.1% (93 Sessions) — Hellgrau
Daneben: Browser-Statistiken als kleine Balken (staggered fade-in, 0.1s).
Warnhinweis: "Mobile Conv. 0.23% vs. Desktop 2.24%" erscheint als rote Badge (#af0f09).
```

---

## Slide 17: Mobile Conversion Gap

```
Animation: Vergleichs-Karten Desktop vs. Mobile erscheinen nebeneinander (slide-in von links/rechts).
Desktop-Karte (links, gruener Rahmen):
  - Conv-Rate: 2.24% (zaehlt hoch)
  - CHF/Session: 23.60 (zaehlt hoch)
  - Bounce: 36.4%
Mobile-Karte (rechts, roter Rahmen):
  - Conv-Rate: 0.23% (zaehlt hoch — rot!)
  - CHF/Session: 0.26 (zaehlt hoch — rot!)
  - Bounce: 40.4%
Delta-Pfeile zwischen den Karten: "-2.0pp" und "-23.34 CHF" blinken rot (pulse 2x).
Call-to-Action: "Mobile-Optimierung = groesstes Umsatzpotenzial" faded ein.
```

---

## Slide 18: Geografie

```
Animation: Karte der DACH-Region faded ein (0.8s).
Laender-Punkte poppen nacheinander auf (staggered 0.2s):
  1. Switzerland: 5'858 Sessions (groesster Punkt, Dunkelblau)
  2. Germany: 907 Sessions
  3. France: 558 Sessions
  4. United States: 410 Sessions (kleiner Punkt)
  5. Singapore: 127 Sessions
Jeder Punkt hat einen Ripple-Effekt beim Erscheinen.
Rangliste rechts daneben baut sich parallel auf (zeilenweise fade-in).
```

---

## Slide 19: Zeitliche Muster

```
Animation: Zwei Diagramme erscheinen nebeneinander:
Links — Wochentag-Balken (wachsen von unten, staggered 0.15s):
  - Montag: 1'477 (hoechster, gruener Highlight)
  - Dienstag: 1'422
  - Mittwoch: 1'400
  - ...
  - Sonntag: 738 (niedrigster, roter Highlight)
Rechts — Tageszeit-Linie zeichnet sich (1.5s):
  Peak bei 10:00 Uhr (723 Sessions) — Punkt pulst gruen.
  Zweiter Peak bei 11:00 (704 Sessions).
Insight-Badge: "Peak: Mo 10 Uhr" poppt ein.
```

---

## Slide 20: Probleme & Handlungsempfehlungen

```
Animation: Zweispaltig, Links (Probleme) und Rechts (Empfehlungen).
Links — Probleme erscheinen als rote Karten von oben (staggered 0.2s):
  1. "Warenkorb-Abbruch 85.6%" — roter Badge, Shake-Animation (1x)
  2. "Mobile Conv. Gap: -2.0pp" — roter Badge
  3. "High-Bounce Produktseiten (bis 80%)" — roter Badge
  4. "Display-Kanal: 0 Conversions" — roter Badge
Rechts — Empfehlungen erscheinen als gruene Karten (staggered, 0.3s delay nach Problemen):
  1. "Checkout-Prozess vereinfachen" — gruener Badge, Checkmark-Icon poppt ein
  2. "Mobile UX ueberarbeiten" — gruener Badge
  3. "Produktseiten mit besseren Bildern/Beschreibungen" — gruener Badge
  4. "Display-Budget umverteilen auf Referral/Organic" — gruener Badge
Abschluss: Gruener Rahmen um gesamte Slide pulst 1x.
```

---

## Slide 21: Zusammenfassung & Naechste Schritte

```
Animation: 3 Saeulen erscheinen nacheinander (slide-up, 0.3s staggered):
  Saeule 1 — "Staerken" (Gruen #009b91):
    - Starke Stammkunden (67.5% Wiederkauf)
    - Steigender AOV (+166%)
    - Hoher Referral-ROI (14.51 CHF/Session)
  Saeule 2 — "Schwaechen" (Rot #af0f09):
    - Warenkorb-Abbruch 85.6%
    - Mobile Gap
    - Display ohne Conversions
  Saeule 3 — "Aktionen" (Dunkelblau #1e326e):
    - Checkout optimieren (Quick Win)
    - Mobile Redesign (Mittelfristig)
    - Kanalbudget umverteilen (Strategisch)
Zum Schluss: "Danke" und Labtec-Logo fade-in in der Mitte.
```

---

## Allgemeine Animations-Richtlinien

```
Timing:
- Alle Animationen subtil und professionell (nicht verspielt)
- Dauer pro Element: 0.3–0.8s
- Stagger zwischen Elementen: 0.1–0.2s
- Easing: ease-out fuer Einblendungen, ease-in-out fuer Diagramme

Farben:
- Primaer: #1e326e (Dunkelblau), #009b91 (Gruen)
- Warn/Problem: #af0f09 (Rot)
- Hintergrund: #f8f9fc
- Karten: Weiss mit dezenten Schatten

Effekte:
- Count-Up fuer alle Zahlen/KPIs
- Balken wachsen proportional zur Datenmenge
- Donut/Pie zeichnen sich im Uhrzeigersinn
- Linien-Diagramme zeichnen sich von links nach rechts
- Probleme: Pulse/Shake (1-2x, dezent)
- Highlights: Kurzer Glow-Effekt
```
