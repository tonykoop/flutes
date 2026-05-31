# Flutes V5 Packet Scaffold

## Design Intent

This packet promotes the `flutes` repository from a historical engineering archive toward a V5 packet/explorer scaffold. The repo already has unusually strong evidence for Native American style wooden flutes: a parametric workbook, build photos, historical SolidWorks files, learning material, and a wood-species FEM study. Round 31 does not convert that history into a build-ready packet by assertion. It makes the family split explicit and records the measurement gates needed before any row can be treated as current fabrication authority.

## Family Split

| Family | Scope | Current authority | Measurement gate |
| --- | --- | --- | --- |
| `NAF-6H` | Six-hole Native American style wooden flutes from the historical workbook | Public F4/A4/C5 workbook rows and sanitized build-log aggregates now exist, but they are comparison evidence only | Log current measured fundamental plus six-hole tuning for each selected key before treating the rows as CAD/DXF or build authority |
| `PVC-TRAIN` | PVC training or proof flute using the same open-open acoustic law | Planning family only | Select bore stock, measure actual ID, then compute and drill a proof flute before publishing dimensions |
| `LEGACY-SW` | Historical SolidWorks body/nest/fetish/jig assets | Archived source files exist under `legacy/` and stashed CAD paths, but they are not normalized into V5 CAD | Recover the chosen model, export clean neutral geometry, and map dimensions back to family rows |
| `SONGBOOK` | Learn-to-play assets for the 6-hole NAF family | Documentation/playability support | Keep separate from fabrication authority; fingering charts do not validate geometry |

## Governing Acoustic Model

The target rows are duct flutes with an effectively open-open long playing chamber. The first-order model is:

```text
L_eff = c / (2f)
L_geom = L_eff - end_correction
```

The historical design table also includes NAF-specific corrections and voicing geometry for the slow-air chamber, flue, true sound hole, bird block, and six finger holes. Those corrections are design-table evidence, not something this scaffold re-derives by hand. The extracted F4/A4/C5 rows stay `dimension_provenance=measurement_required` until checked against current measured tuning traces.

## Evidence Boundary

- The workbook extraction and sanitized build-log comparison support an L1 packet scaffold and justify a future L2 shop-packet candidate after current measured tuning checks.
- The FEM analysis is a study artifact for wood-species behavior. It does not replace per-flute pitch, decay, or hole-tuning measurements.
- The new OpenSCAD, SVG, and DXF files are family-split scaffolds. They show packet organization and authority routing, not a complete production flute.
- Photos are documentation and provenance support only. They are not dimensional authority.

## Next Promotion Gates

1. Capture current measured fundamental plus six-hole tuning for the F4, A4, and C5 public workbook rows.
2. Reconcile the C5 historical chamber-length mismatch before using that row for CAD/DXF or cut-list authority.
3. Keep the A4 FEM simplification analysis-only until it is reconciled with the workbook row and measured logs.
4. Replace scaffold CAD/DXF with checked geometry generated from reviewed design-table rows.
5. Add MCP provenance entries only when an actual OpenSCAD, Blender, Illustrator, or Photoshop MCP session produces a repo artifact.
