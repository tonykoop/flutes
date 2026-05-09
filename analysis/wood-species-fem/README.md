# Wood-Species Coupled Structural-Acoustic FEM

**Issue:** `flutes#1` — Coupled structural-acoustic FEM: quantify wood-species
effect on tone (cedar vs walnut vs hard maple).

**Readiness:** L3-frontier analysis (methodology complete, analytical results
computed, FEM execution ready, empirical gate deferred).

---

## Summary

This analysis quantifies how wood species — Western Red Cedar, Black Walnut,
and Hard Maple — affects the tone of a Native American style flute with a fixed
A4-key bore geometry.

**Key finding:** At A4, the "forgiving vs demanding" character difference between
species is driven primarily by **wall damping** (η_L), not by structural-acoustic
mode coincidence.

| Species | η_L | f_QSC (Hz) | Tone |
|---------|-----|-----------|------|
| W. Red Cedar | 0.030 | **1141** | Warm, forgiving |
| Black Walnut | 0.020 | **1176** | Balanced |
| Hard Maple   | 0.014 | **1203** | Bright, demanding |

f_QSC is the Q-weighted spectral centroid — a scalar tone-brightness index.
Cedar's higher damping attenuates upper partials 2.1× faster than maple,
explaining the registry observation without requiring structural modes to
coincide with acoustic partials.

No structural-acoustic avoided crossing was found at < 5% separation for
any species at A4 key (smallest observed separation: 9.1%, Hard Maple
2nd bending mode vs acoustic n=3).

---

## Files in this directory

| File | Contents |
|------|---------|
| `README.md` | This summary |
| `wood-property-table.md` | E, ρ, η, Poisson ratios per species with FPL-GTR-190 citations |
| `fem-scenario.md` | Geometry, mesh, BCs, coupling physics, analysis type |
| `modal-results-table.md` | 5 acoustic modes + 3 structural modes per species; Q-factor tables |
| `tone-color-comparison.md` | f_QSC computation, spectrum ASCII plot, root-cause analysis |
| `capstone-design-table.md` | All parameters in one table; FEM execution status; next steps |
| `references.md` | Literature and software citations |

---

## Physics overview

### Air-column modes

Open-open cylindrical bore, L_eff = 390 mm (A4 key):

    f_n = n × 440 Hz    for n = 1, 2, 3, 4, 5

These are the same for all species. Wall compliance shifts modes < 1%
(bore is stiff relative to air pressure at these dimensions).

### Body bending modes

Hollow cylinder, simply-supported, L = 381 mm.

    f_body_n = n² × (π / 2L²) × √(EI / ρA)

| Species | f_body_1 | f_body_2 |
|---------|---------|---------|
| Cedar   | 388 Hz  | 1552 Hz |
| Walnut  | 371 Hz  | 1484 Hz |
| Maple   | 360 Hz  | 1440 Hz |

### Acoustic Q-factor

    1/Q_n = 1/Q_rad_n + 1/Q_wall
    Q_rad_n ≈ n × 15     (radiation loss, bore geometry)
    Q_wall = 1/η_L        (species-dependent wall damping)

### Tone color metric

    f_QSC = Σ(f_n × Q_n × A_n) / Σ(Q_n × A_n)
    A_n = 1/n   (fipple excitation amplitude model)

---

## Relationship to registry observations

The build registry records: "Cedar is forgiving; hard maple is demanding;
ambrosia maple has a high failure rate." This analysis provides the first
principled physical explanation: **cedar's 2.1× higher damping factor
attenuates upper partials faster**, reducing the sensitivity of the
instrument to embouchure variations and overblowing.

The analysis also rules out structural-acoustic mode coincidence as a
first-order explanation at A4 key — all species show body modes separated
from acoustic harmonics by > 9%.

---

## FEM execution status

Analytical pre-computation complete. Full FEM execution (COMSOL Acoustic-Solid
Interaction or Ansys Harmonic Acoustics) will refine:
- Exact body mode frequencies (cylindrical shell vs beam approximation)
- Orthotropic vs isotropic material response
- Radiation impedance at open ends

Empirical validation (FFT blow test on three A4 registry flutes)
is deferred; no measured spectral data exists in the repo yet.

**Do not claim L4 build-ready.** This is a frontier analysis; computed
FEM results and empirical comparison are required for L4.

---

## Cross-references

- `design-table/flute-dimensions-parametric.xlsx` — bore geometry source
- `built-log/` — build registry with species-resolved entries
- `tonykoop/WSS-2019` — Wolfram notebook: air-column acoustic model
- `tonykoop/tensile-testing` — orthotropic E-tensor measurement pipeline
- `tonykoop/tongue-drum` analysis `docs/study/fem-modal-validation.md`
  — FEM pipeline reused; FFT measurement protocol shared
