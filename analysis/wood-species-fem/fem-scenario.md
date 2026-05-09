# FEM Scenario — Coupled Structural-Acoustic Analysis

Analysis readiness: L3-frontier (methodology and inputs defined;
software execution requires COMSOL or Ansys licence on a workstation
with the Acoustic-Solid Interaction module).

---

## Instrument geometry

Fixed bore: A4 key (fundamental 440 Hz).

### Playing-chamber dimensions

| Parameter | Symbol | Value |
|-----------|--------|-------|
| Target fundamental | f₁ | 440 Hz |
| Speed of sound (20°C) | c | 343 m/s |
| Effective acoustic length | L_eff | c/(2f₁) = 390 mm |
| End correction per open end | δ | 0.6 × R_bore = 4.6 mm |
| Physical chamber length | L_chamber | 390 − 2×4.6 = 381 mm |
| Bore inner diameter | D_bore | 15.2 mm |
| Bore inner radius | R_bore | 7.60 mm |
| Wall thickness | h_wall | 5.10 mm |
| Outer diameter | D_outer | 25.4 mm |

Source: parametric design table
`design-table/flute-dimensions-parametric.xlsx`, column A4
(derived values; see README for design table description).

The SAC (slow air chamber), nest, and bird block are excluded from this
analysis; the playing chamber alone is modeled. The SAC–TSH junction
is treated as an open boundary condition for the air column (pressure-release
at the True Sound Hole end).

---

## Finite element model

### Geometry

- Cylindrical shell: hollow tube, L = 381 mm, D_inner = 15.2 mm,
  D_outer = 25.4 mm.
- Air domain: cylindrical volume, L = 381 mm, D = 15.2 mm.
- Two end caps: open (pressure-release) boundary conditions at both
  ends of the air domain (playing position with all holes covered
  except the foot opening is not modeled here; open-open is the
  conservative acoustic boundary).

### Mesh

- Solid (tube wall): 8-node hexahedral (SOLID186/C3D20R equivalent).
  Target max element size: h_wall/3 = 1.7 mm. Minimum 3 elements
  through wall thickness.
- Acoustic (air): 8-node acoustic hexahedral (FLUID30/AC3D8).
  Target max element size: c/(10 × f_max) = 343/(10×2200) = 15.6 mm.
  Adequate for 5-mode extraction to 2200 Hz.
- Acoustic–solid interface: conforming mesh with coupling DOFs
  at the shared surface.

### Boundary conditions

| Surface | Condition |
|---------|-----------|
| TSH end (top) | Acoustic: pressure-release (p = 0) |
| Foot end (bottom) | Acoustic: pressure-release (p = 0) |
| Tube outer surface | Structural: free (no constraint) |
| TSH end of tube | Structural: simply-supported (w = 0, θ = free) |
| Foot end of tube | Structural: simply-supported (w = 0, θ = free) |

### Material assignment

Each run uses one of the three species (isotropic approximation using E_L and ν_LR
from the wood property table; full orthotropic tensor available in [1]).
Isotropic approximation is the first-order model; orthotropic refinement is the
Phase 2 FEM update.

### Coupling physics

Acoustic-Solid Interaction multiphysics (COMSOL) or Fluid–Structure
Interaction (Ansys Harmonic Acoustics):
- Normal acceleration continuity at the solid–fluid interface:
  ∂²u_n/∂t² = (1/ρ_air) × ∂p/∂n
- Pressure load on solid from fluid:
  F_n = −p × n_hat (pressure acts inward on tube wall)

### Analysis type

Frequency-domain harmonic analysis (eigenfrequency extraction):
- Frequency range: 200–3000 Hz (captures 5 acoustic modes + structural modes)
- Solver: MUMPS or PARDISO direct solver; complex eigenvalue extraction
  for damped modes.
- Damping: structural loss factor η_L applied as isotropic loss factor
  in solid domain; fluid damping ignored (air is lightly damped at these
  frequencies).

---

## Mode identification protocol

Acoustic-dominated modes: pressure field shows clear standing-wave pattern
(n half-wavelengths along bore axis); wall displacement amplitude is small
relative to air particle displacement.

Structural-dominated modes: wall displacement pattern is dominant;
air-pressure perturbation is secondary. Identify by modal strain energy
fraction in solid domain > 50%.

Coupled modes (avoided crossings): energy shared between air and wall;
frequency splitting visible in the modal map. Flag for qualitative
species comparison.

---

## Output deliverables

1. Modal map: plot of all modes (structural + acoustic character)
   vs frequency for each species, 200–2500 Hz.
2. Modal table: 5 lowest acoustic-dominated modes per species
   (frequency, Q-factor, acoustic energy fraction).
3. Structural mode table: lowest 3 bending modes per species.
4. Q-weighted spectral centroid: tone-color metric per species.
5. Avoided-crossing proximity table: separation between each
   structural mode and the nearest acoustic harmonic.

---

## Validation plan

Compare predicted acoustic fundamentals against phone-mic FFT recordings
of three A4 registry flutes (one per species), single-blow methodology
consistent with `tongue-drum` measurement protocol. Empirical gate
deferred until recordings are available.
