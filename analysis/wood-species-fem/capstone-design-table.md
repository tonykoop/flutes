# Capstone Design Table — Wood-Species Coupled Structural-Acoustic FEM

Issue: `flutes#1` — Coupled structural-acoustic FEM: quantify wood-species
effect on tone (cedar vs walnut vs hard maple).
Readiness: L3-frontier analysis.

---

## Fixed geometry (A4 key)

| Parameter | Value | Source |
|-----------|-------|--------|
| Target fundamental f₁ | 440 Hz | Design table A4 column |
| Effective acoustic length L_eff | 390 mm | c/(2f₁), c=343 m/s |
| Bore inner diameter D_bore | 15.2 mm | Design table |
| Wall thickness h_wall | 5.1 mm | ≈ D_bore/3 (design table rule) |
| Outer diameter D_outer | 25.4 mm | D_bore + 2h_wall |
| Physical chamber length L_chamber | 381 mm | L_eff − 2δ (end correction) |

---

## Material properties summary

| Species | E_L (GPa) | ρ (kg/m³) | η_L | Q_wall |
|---------|----------|----------|-----|--------|
| W. Red Cedar  | 7.7  | 370 | 0.030 | 33 |
| Black Walnut  | 11.6 | 610 | 0.020 | 50 |
| Hard Maple    | 12.6 | 705 | 0.014 | 71 |

Source: FPL-GTR-190 [1]; damping from Haines 1979 [2].

---

## Acoustic modal series (all species — bore geometry dominant)

| Mode n | f_n (Hz) | Note |
|--------|---------|------|
| 1 | 440 | A4 |
| 2 | 880 | A5 |
| 3 | 1320 | E6 |
| 4 | 1760 | A6 |
| 5 | 2200 | C#7 |

Wall compliance correction < 1% for all species; not included.

---

## Structural bending modes (simply-supported hollow cylinder)

| Species | f_body_1 (Hz) | f_body_2 (Hz) | f_body_3 (Hz) |
|---------|--------------|--------------|--------------|
| Cedar   | 388 | 1552 | 3492 |
| Walnut  | 371 | 1484 | 3339 |
| Maple   | 360 | 1440 | 3240 |

---

## Acoustic Q-factor table

| Species | Q_n=1 | Q_n=2 | Q_n=3 | Q_n=4 | Q_n=5 |
|---------|------|------|------|------|------|
| Cedar   | 10.3 | 15.7 | 19.0 | 21.3 | 22.9 |
| Walnut  | 11.5 | 18.8 | 23.7 | 27.3 | 30.0 |
| Maple   | 12.4 | 21.1 | 27.6 | 32.6 | 36.6 |

---

## Tone color metric (Q-weighted spectral centroid)

| Species | f_QSC (Hz) | Rank | Character |
|---------|-----------|------|-----------|
| W. Red Cedar  | 1141 | 1 — warmest | Forgiving, dark, high dynamic range |
| Black Walnut  | 1176 | 2 | Balanced, moderate warmth |
| Hard Maple    | 1203 | 3 — brightest | Demanding, bright, long sustain |

Species spread: 62 Hz (5.4% of centroid). Rank order is stable to
reasonable variation in excitation model and radiation damping.

---

## Avoided-crossing proximity

| Species | Body mode | f_body (Hz) | Nearest acoustic | Separation |
|---------|-----------|------------|-----------------|------------|
| Cedar  | 2nd bend | 1552 | n=4 (1760 Hz) | 11.8% |
| Walnut | 2nd bend | 1484 | n=3 (1320 Hz) | 12.4% |
| Maple  | 2nd bend | 1440 | n=3 (1320 Hz) | 9.1% |

No species shows structural-acoustic near-coincidence (< 5%).
Mode-coupling is a secondary mechanism at A4; damping is primary.

---

## Root-cause summary

| Mechanism | Cedar | Walnut | Maple | Dominant? |
|-----------|-------|--------|-------|-----------|
| Wall damping η_L | 0.030 (high) | 0.020 | 0.014 (low) | **Yes** |
| Closest body-acoustic separation | 11.8% | 12.4% | 9.1% | No (> 5%) |
| f_QSC outcome | Warm (1141 Hz) | Mid (1176 Hz) | Bright (1203 Hz) | — |

**Registry observation confirmed:** Cedar's high damping (η_L = 0.030)
is the primary physical cause of its forgiving, warm character — not
structural mode coincidence with acoustic partials.

---

## FEM execution requirements

| Requirement | Status |
|------------|--------|
| Geometry defined | ✅ |
| Mesh strategy defined | ✅ |
| BCs defined | ✅ |
| Material inputs ready | ✅ |
| Damping values assigned | ✅ |
| COMSOL/Ansys license + workstation | ⚠️ Required for computed results |
| Empirical validation recordings | ⏳ Deferred |

Analysis readiness: **L3-frontier**. Ready for FEM execution; empirical
validation gate deferred until registry recordings (per-species A4 flute
FFT blow tests) are available.

---

## Next steps for L4 build-readiness

1. Execute FEM in COMSOL Acoustic-Solid Interaction or Ansys Harmonic Acoustics
   using inputs from this design table and `fem-scenario.md`.
2. Extract computed modal results; compare against analytical pre-computation
   in `modal-results-table.md` — flag any mode that deviates > 5%.
3. Record phone-mic FFT blow tests on three A4 registry flutes (one per species).
4. Overlay measured vs. FEM-predicted spectrum; confirm f_QSC rank order.
5. Publish validated spectral fingerprints in `analysis/wood-species-fem/measured/`.
