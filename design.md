# Flutes V5 Packet Scaffold

## Design Intent

This packet promotes the `flutes` repository from a historical engineering archive toward a V5 packet/explorer scaffold. The repo already has unusually strong evidence for Native American style wooden flutes: a parametric workbook, build photos, historical SolidWorks files, learning material, and a wood-species FEM study. Round 31 does not convert that history into a build-ready packet by assertion. It makes the family split explicit and records the measurement gates needed before any row can be treated as current fabrication authority.

## Family Split

| Family | Scope | Current authority | Measurement gate |
| --- | --- | --- | --- |
| `NAF-6H` | Six-hole Native American style wooden flutes from the historical workbook | Workbook and build-registry evidence exist, but exact public-row extraction is still required | Extract each key row from `design-table/flute-dimensions-parametric.xlsx`, compare to a built flute, and log measured fundamental plus finger-hole tuning |
| `PVC-TRAIN` | PVC training or proof flute using the same open-open acoustic law | Planning family only | Select bore stock, measure actual ID, then compute and drill a proof flute before publishing dimensions |
| `LEGACY-SW` | Historical SolidWorks body/nest/fetish/jig assets | Archived source files exist under `legacy/` and stashed CAD paths, but they are not normalized into V5 CAD | Recover the chosen model, export clean neutral geometry, and map dimensions back to family rows |
| `SONGBOOK` | Learn-to-play assets for the 6-hole NAF family | Documentation/playability support | Keep separate from fabrication authority; fingering charts do not validate geometry |

## Governing Acoustic Model

The target rows are duct flutes with an effectively open-open long playing chamber. The first-order model is:

```text
L_eff = c / (2f)
L_geom = L_eff - end_correction
```

The historical design table also includes NAF-specific corrections and voicing geometry for the slow-air chamber, flue, true sound hole, bird block, and six finger holes. Those corrections are design-table evidence, not something this scaffold re-derives by hand. Any row that has not been extracted and checked stays `dimension_provenance=measurement_required`.

## Evidence Boundary

- The workbook and build registry support an L1 packet scaffold and justify a future L2 shop-packet candidate after row extraction.
- The FEM analysis is a study artifact for wood-species behavior. It does not replace per-flute pitch, decay, or hole-tuning measurements.
- The new OpenSCAD, SVG, and DXF files are family-split scaffolds. They show packet organization and authority routing, not a complete production flute.
- Photos are documentation and provenance support only. They are not dimensional authority.

## Next Promotion Gates

1. Export selected workbook rows for F4, A4, C5, and PVC proof rows into `family-spec.csv`.
2. Add a design-table extraction CSV with bore ID, physical length, SAC length, TSH size, flue depth, flue width, and all six hole positions.
3. Compare at least one built flute per chosen key against the extracted row.
4. Replace scaffold CAD/DXF with checked geometry generated from the extracted design table.
5. Add MCP provenance entries only when an actual OpenSCAD, Blender, Illustrator, or Photoshop MCP session produces a repo artifact.
