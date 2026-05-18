# Flutes Packet Risks

## Overclaiming Historical Evidence

The repository has real build history, but the public packet does not yet expose a row-by-row, non-private build registry. Treat the history as strong provenance, not as automatic V5 build readiness.

Mitigation: publish selected non-private build IDs with key, species, measured result, and failure mode before raising readiness.

## Mixed Family Drift

Wooden NAF rows, PVC proof rows, legacy SolidWorks files, and songbook assets can look like one family if they are blended too early.

Mitigation: keep `family_split` explicit in every CSV. PVC and legacy CAD rows remain `unknown_requires_measurement` until their own measurements or exports exist.

## Formula Misuse

NAF correction factors and K2-style empirical adjustments are family-specific. Applying them to PVC, other duct flutes, or archived CAD without checking bore and voicing geometry can create plausible but wrong dimensions.

Mitigation: use `dimension_provenance=measurement_required` until the row is extracted and checked against measured stock or built flutes.

## Visual Authority Drift

Photos, screenshots, SVG diagrams, and generated explorer views can become accidental dimensional authority.

Mitigation: keep `visual-output-register.csv` current. Only CAD, DXF, design tables, measured templates, or reviewed drawings may control fabrication.

## Cultural Framing

The repo documents Native American style flutes by a non-Indigenous maker. Packet language must keep attribution and cultural boundaries visible.

Mitigation: preserve the README cultural attribution in explorer and packet summaries.
