# Design Intent — flutes rev A

- Master CAD: `CAD/flutes_family.scad` (sha256: da8ef2fa96771d89ffb48a29936026cc3f3fe4fb7997d9f78b5e01fbb8e4db68), driven by seed `CAD/design-table-seed.csv` (sha256: 6ed4ceb9d774c4f560a766ce802a76e79e68c5fdd5b87be7ef8ca6b55cc04e46) and historical workbook `Flutes.xlsx` (sha256: 3a58014cc2f502797e02126382682203d9d7711faf644c904f6b40cbbbca840d)
- Function: Native American style six-hole wooden flutes (NAF-6H) plus PVC training and legacy-SolidWorks families. Duct flutes with an effectively open-open long playing chamber: L_eff = c/(2f); L_geom = L_eff − end_correction. NAF-specific corrections and voicing (slow-air chamber, flue, true sound hole, bird block, six finger holes) live in the historical workbook as evidence, not re-derived here.
- Environment: L1 concept/explorer scaffold on top of a strong historical archive (150+ serial-numbered builds, workbook, FEM wood-species study, legacy SolidWorks). Nothing is build-ready until family rows are extracted from the workbook and checked against current measured tuning.
- Target qty: 1 (per selected key). Deadline: TBD. Budget/unit ceiling: TBD.

## Critical dimensions (carry tolerances)

| Feature | Nominal | Tolerance | Why critical | Source |
| --- | --- | --- | --- | --- |
| NAF-6H F4 predicted geometric length | 432.562 mm | measure current fundamental before authority | fundamental pitch (F4 = 349.23 Hz) | family-spec.csv NAF-6H-F4 (measurement_required) |
| NAF-6H A4 predicted geometric length | 337.490 mm | measure current A4 tuning | fundamental pitch (A4 = 440.00 Hz) | family-spec.csv NAF-6H-A4 (measurement_required) |
| NAF-6H C5 predicted geometric length | 285.318 mm | reconcile built-log chamber mismatch | fundamental pitch (C5 = 523.25 Hz) | family-spec.csv NAF-6H-C5 (measurement_required) |
| NAF-6H A4 bore ID | 19.050 mm | measure fired/turned bore | bore governs pitch/response | family-spec.csv NAF-6H-A4 (measurement_required) |
| Hole count | 6 | ergonomic + tuning gate | six-hole tuning log required | family-spec.csv (measurement_required) |
| PVC-TRAIN bore ID | measurement_required | measure stock before computing | planning row only | family-spec.csv PVC-TRAIN-A4 |

## Incidental (free for DFM)

- Wood species/figure, bird/fetish block style, lacing/decoration, exterior body profile, finish — all documented historically but not dimension-controlling.

## Must-nots (DFM may never violate)

- Do not treat extracted workbook rows as CAD/DXF or tuning authority until logged against current measured fundamental + six-hole tuning (design.md evidence boundary; family-spec next_measurement_gate).
- Voicing geometry (flue/true sound hole/bird block) is tuning-sensitive: refine by hand, do not freeze from a scaffold or lossy export.
- Do not derive PVC-TRAIN dimensions from the wooden NAF table without measuring actual PVC stock (family-spec PVC-TRAIN).
- Legacy SolidWorks archive is not current CAD authority until normalized and reviewed (family-spec LEGACY-SW).

## Material intent

- Preferred: wood (NAF-6H) per historical build registry; PVC proof stock for training family (family-spec material_system).
- Acceptable subs: per sourcing.csv / bom.csv (spec-first; live prices unverified).
- Forbidden: none recorded (mouth-safe finishes on played bodies).

## Stage status

Stage 0 intake complete 2026-07-01. Gate A (Alpha shop compile) NOT yet run — no concessions logged, nothing presented as shippable. L1 concept scaffold; authority remains measurement-gated.
