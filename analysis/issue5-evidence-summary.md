# Issue #5 Evidence Summary — Public Workbook Extraction + NAF Comparison

This file cross-references the artifacts that fulfill `tonykoop/flutes#5` scope:
"Extract sanitized public F4/A4/C5 workbook rows, compare vs. measured NAF logs."

## Artifact Map

| Artifact | Location | Status |
|---|---|---|
| Sanitized F4/A4/C5 workbook rows | `design-table/public-naf-workbook-rows.csv` | Present (`public_workbook_extract_unvalidated`) |
| Build-log comparison (F4/A4/C5) | `analysis/naf-workbook-measured-log-comparison.csv` | Present (`public_sanitized_build_log_aggregate`) |
| Comparison methodology and privacy notes | `analysis/naf-workbook-measured-log-notes.md` | Present |
| Family member rows with acoustic law | `family-spec.csv:2-6` | Present (`measurement_required` provenance) |
| Validator gate rows for comparison | `validation.csv:4-8` (VAL-003, VAL-004) | `public_extract_added`, `comparison_added_private_fields_omitted` |
| Promotion gates cross-reference | `design.md:34-40` | Present |
| Visual authority map | `visual-output-register.csv` | Present |

## Privacy Compliance

Verified present in all public artifacts:
- No per-flute owner, price, date, or recipient fields
- No private archive/source paths
- No full build-log row dumps — only sanitized aggregates (count, range, average)
- Master workbook (`Flutes.xlsx`) and full built registry remain private

## C5 Mismatch Caveat

The C5 public comparison shows a large delta (+6.517 in) between the workbook long-chamber
and the sanitized built-log aggregates. This is documented in both the comparison CSV and
`design.md:38`. The C5 row must remain `comparison-only` until the source-generation difference
is reconciled — it does not block the extraction from satisfying issue #5 scope.

## V5 Authority Boundaries

All public extraction artifacts use `public_workbook_extract_unvalidated` or
`public_sanitized_build_log_aggregate` authority. None are fabrication authority.
CAD/DXF or cut-list work from these rows requires current measured-flute data (fundamental
plus six-hole tuning trace) per `validation.csv` gate VAL-003.
