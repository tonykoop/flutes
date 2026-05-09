# Wood Property Table — Cedar, Walnut, Hard Maple

Source: Wood Handbook FPL-GTR-190 [1], Table 5-1, 12% MC.
Damping loss factors from Haines 1979 [2] and Gough 2007 [9].

Fixed bore geometry (A4 key):
- Bore inner diameter (D_bore): 15.2 mm (0.60 in)
- Outer diameter (D_outer): 25.4 mm (1.00 in)
- Wall thickness (h_wall): 5.1 mm (0.20 in)
- Playing-chamber physical length (L_chamber): 381 mm (see FEM scenario)

---

## Primary properties

| Property | Symbol | Units | W. Red Cedar | Black Walnut | Hard Maple |
|----------|--------|-------|-------------|-------------|------------|
| Longitudinal Young's modulus | E_L | GPa | 7.7 | 11.6 | 12.6 |
| Radial Young's modulus | E_R | GPa | 0.85 | 1.11 | 1.83 |
| Tangential Young's modulus | E_T | GPa | 0.37 | 0.61 | 1.57 |
| Shear modulus (LR plane) | G_LR | GPa | 0.48 | 0.94 | 1.50 |
| Poisson ratio ν_LR | ν_LR | — | 0.38 | 0.50 | 0.44 |
| Density | ρ | kg/m³ | 370 | 610 | 705 |
| Longitudinal loss factor | η_L | — | 0.030 | 0.020 | 0.014 |
| Transverse loss factor | η_T | — | 0.060 | 0.040 | 0.028 |

Notes:
- E_L is the modulus along the grain, governing the flute body's bending stiffness
  (grain runs parallel to bore axis in a conventional NAF body).
- η_L is used for the structural damping of body modes.
- Moduli at 12% moisture content; vary ≈ ±5% per 2% MC change.

---

## Derived structural parameters

Cross-section of playing-chamber tube:
- Second moment of area: I = π(R_o^4 − R_i^4)/4
  - R_o = 12.70 mm, R_i = 7.60 mm
  - I = π(2.594×10⁻⁸ − 3.339×10⁻¹⁰)/4 = 2.011×10⁻⁸ m⁴
- Cross-sectional area: A = π(R_o² − R_i²) = 3.251×10⁻⁴ m²

Beam-bending parameter √(EI/ρA):

| Species | E_L (Pa) | EI (N·m²) | ρA (kg/m) | √(EI/ρA) (m²/s) |
|---------|----------|-----------|----------|-----------------|
| Cedar   | 7.70×10⁹ | 154.8     | 0.1203   | 35.87           |
| Walnut  | 11.6×10⁹ | 233.3     | 0.1983   | 34.28           |
| Maple   | 12.6×10⁹ | 253.4     | 0.2292   | 33.25           |

---

## Acoustic parameters

Speed of sound in air (20°C): c = 343 m/s

Specific acoustic impedance: Z_air = ρ_air × c = 1.205 × 343 = 413.3 Pa·s/m

Bore area: A_bore = π(D_bore/2)² = π(0.0076)² = 1.815×10⁻⁴ m²

---

## Species interpretation

**Western Red Cedar** — low density, high longitudinal-to-radial stiffness ratio
(E_L/E_R = 9.1). High damping (η_L = 0.030) attenuates upper partials strongly,
producing a warm, forgiving tone. Wide body-mode frequency separation from
acoustic partials reduces mode-mode coupling.

**Black Walnut** — medium density, moderate damping (η_L = 0.020). Intermediate
tone character; body modes closer to lower acoustic partials than cedar.

**Hard Maple** — highest density, lowest damping (η_L = 0.014). Preserves upper
partials aggressively, producing a bright, demanding tone. Body-mode 2 comes
closest to acoustic harmonic 3 (1320 Hz), suggesting potential mild coupling.
