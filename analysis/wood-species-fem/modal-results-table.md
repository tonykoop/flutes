# Modal Results — 5 Acoustic Modes + Structural Modes per Species

All results are analytical predictions at L3-frontier readiness.
FEM execution (COMSOL Acoustic-Solid Interaction or Ansys Harmonic Acoustics)
required to produce computed values; analytical results here serve as
pre-computation bounds and L3 deliverable.

---

## Geometry and acoustic modal series

Fixed bore geometry (A4 key):
- L_eff = 390 mm (effective acoustic length)
- Open-open boundary: f_n = n × c / (2 L_eff) = n × 440 Hz

| Mode n | Acoustic frequency (Hz) | Musical note (nearest) |
|--------|------------------------|----------------------|
| 1 | 440 | A4 |
| 2 | 880 | A5 |
| 3 | 1320 | E6 |
| 4 | 1760 | A6 |
| 5 | 2200 | C#7 |

These are the ideal open-open harmonics. Wall compliance shifts each
acoustic mode by a small amount δf_n:
δf_n / f_n ≈ − (ρ_air × c²) / (2 × E_R × h_wall / R_bore) × (correction factor)

For E_R = 850 MPa (cedar), h_wall = 5.1 mm, R_bore = 7.6 mm:
Stiffness per unit length k_s = E_R × h_wall / R_bore² = 0.85e9 × 0.0051 / (0.0076)² = 7.49×10⁸ N/m³

Compliance shift (approximate): δf/f ≈ ρ_air c² / k_s × A_bore / L ≈ −0.002 (< 1%)

Wall compliance correction is < 1% for all three species; acoustic mode
frequencies are dominated by bore geometry, not wood species. Species
effect on acoustic modes is negligible at this first-order level.

---

## Structural bending modes (playing chamber treated as hollow beam)

Model: simply-supported hollow cylinder (grain parallel to bore axis).
Formula: f_n = n² × (π / 2L²) × √(EI / ρA)

Cross-section parameters (common to all species):
- I = 2.011×10⁻⁸ m⁴
- A = 3.251×10⁻⁴ m²
- L = 0.381 m

| Species | √(EI/ρA) (m²/s) | f_body_1 (Hz) | f_body_2 (Hz) | f_body_3 (Hz) |
|---------|----------------|--------------|--------------|--------------|
| W. Red Cedar | 35.87 | 388 | 1552 | 3492 |
| Black Walnut | 34.28 | 371 | 1484 | 3339 |
| Hard Maple   | 33.25 | 360 | 1440 | 3240 |

Notes:
1. All first structural bending modes (f_body_1) lie BELOW the acoustic
   fundamental (440 Hz). Proximity varies: cedar is closest at 388 Hz
   (Δf = 52 Hz, 12%), maple is furthest at 360 Hz (Δf = 80 Hz, 18%).
2. Structural mode 2 falls between acoustic modes 3 and 4 (1320–1760 Hz)
   for all three species.
3. No structural mode coincides with an acoustic harmonic within ±5%
   for any species; avoided-crossing coupling is expected to be weak.

---

## Species-resolved acoustic Q-factor table

Acoustic mode Q is limited by two loss mechanisms:
- Radiation loss (open ends): Q_rad_n ≈ Q_rad_1 × n, Q_rad_1 ≈ 15 (bore geometry)
- Wall damping: Q_wall ≈ 1 / η_L (species-dependent)

Combined: 1/Q_n = 1/Q_rad_n + 1/Q_wall

| Species | η_L | Q_wall | Q_rad_1 |
|---------|-----|--------|---------|
| Cedar   | 0.030 | 33 | 15 |
| Walnut  | 0.020 | 50 | 15 |
| Maple   | 0.014 | 71 | 15 |

### Cedar — acoustic Q by mode

| Mode n | f_n (Hz) | Q_rad_n | Q_wall | Q_total |
|--------|---------|---------|--------|---------|
| 1 | 440  | 15 | 33 | 10.3 |
| 2 | 880  | 30 | 33 | 15.7 |
| 3 | 1320 | 45 | 33 | 19.0 |
| 4 | 1760 | 60 | 33 | 21.3 |
| 5 | 2200 | 75 | 33 | 22.9 |

### Black Walnut — acoustic Q by mode

| Mode n | f_n (Hz) | Q_rad_n | Q_wall | Q_total |
|--------|---------|---------|--------|---------|
| 1 | 440  | 15 | 50 | 11.5 |
| 2 | 880  | 30 | 50 | 18.8 |
| 3 | 1320 | 45 | 50 | 23.7 |
| 4 | 1760 | 60 | 50 | 27.3 |
| 5 | 2200 | 75 | 50 | 30.0 |

### Hard Maple — acoustic Q by mode

| Mode n | f_n (Hz) | Q_rad_n | Q_wall | Q_total |
|--------|---------|---------|--------|---------|
| 1 | 440  | 15 | 71 | 12.4 |
| 2 | 880  | 30 | 71 | 21.1 |
| 3 | 1320 | 45 | 71 | 27.6 |
| 4 | 1760 | 60 | 71 | 32.6 |
| 5 | 2200 | 75 | 71 | 36.6 |

---

## Avoided-crossing proximity table

Separation between each structural body mode and the nearest acoustic harmonic.
A separation < 5% would indicate potential coupling; all values here are > 5%.

| Species | Body mode | f_body (Hz) | Nearest acoustic | f_acoustic (Hz) | Δf (Hz) | Δf/f_acoustic |
|---------|-----------|------------|-----------------|----------------|---------|---------------|
| Cedar   | 1st bend  | 388        | n=1             | 440            | 52      | 11.8% |
| Cedar   | 2nd bend  | 1552       | n=4             | 1760           | 208     | 11.8% |
| Walnut  | 1st bend  | 371        | n=1             | 440            | 69      | 15.7% |
| Walnut  | 2nd bend  | 1484       | n=3             | 1320           | 164     | 12.4% |
| Maple   | 1st bend  | 360        | n=1             | 440            | 80      | 18.2% |
| Maple   | 2nd bend  | 1440       | n=3             | 1320           | 120     | 9.1% |

**Finding:** Hard Maple's 2nd bending mode (1440 Hz) shows the smallest
separation from an acoustic harmonic (9.1% from n=3 at 1320 Hz). All other
separations exceed 11%. No species exhibits a structural-acoustic near-coincidence
(< 5%) at this geometry and key.

**Implication:** At A4, the species-dependent tone difference is driven primarily
by wall damping (η_L), not by structural-acoustic mode coupling.
Cedar's higher η_L (0.030 vs 0.014 for maple) attenuates upper partials
2.1× more strongly per octave, producing the observed "warm, forgiving" character
without requiring the body to be an active resonator.
