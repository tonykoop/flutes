# NAF Workbook Row Extraction and Public Log Comparison

Issue: `tonykoop/flutes#5`

Readiness: public comparison artifact only. This does not promote the packet to
build-ready, measured-current, or CAD/DXF fabrication authority.

## Public Extraction Scope

`design-table/public-naf-workbook-rows.csv` extracts the public F4, A4, and
C5 rows from the `Low to High Range` sheet of
`design-table/flute-dimensions-parametric.xlsx`. The extraction keeps only
engineering fields needed for acoustic comparison: target frequencies, bore,
wall, mouthpiece, slow-air chamber, spacing, long chamber, flue, true-sound-hole
length, and six hole diameters/positions.

The CSV intentionally does not publish private workbook/archive paths, owner
fields, price fields, recipient details, dates, or free-text build notes.

## Comparison Method

`analysis/naf-workbook-measured-log-comparison.csv` compares each extracted row
against sanitized aggregates from the workbook `Built` sheet:

- count of public rows for the key,
- count/range/average for logged long-chamber values when present,
- count/range/average for TSH width, track length, and nest width when present.

The comparison is useful evidence that the historical workbook and measured
build logs cover the target keys. It is not enough to claim final tuning
authority because the public log extract does not expose a complete measured
fundamental plus six-hole tuning trace for each selected key.

## Authority Boundary

- The workbook rows are `public_workbook_extract_unvalidated`.
- The log comparison is `public_sanitized_build_log_aggregate`.
- The F4/A4/C5 rows can now drive review and follow-up measurement planning.
- CAD/DXF, cut lists, or V5 tuning claims still require a current measured
  flute row with fundamental and finger-hole tuning evidence.

## Local Validation

Run this guard after editing the public extraction or comparison tables:

```bash
python3 scripts/check_public_naf_comparison.py
```

The check keeps the F4/A4/C5 public rows aligned with the comparison rows,
rejects local filesystem path leaks, rejects private/public-hostile CSV
headers, and confirms the family-spec rows still point at the public extract
while staying `measurement_required`.

## Private or Summarized Data

The following workbook fields were inspected only to produce public aggregates
and were not exported: owner, price, private notes, dates, recipient/disposition
context, and private source/archive paths. Historical row numbers were also
omitted from the published comparison table to avoid turning the public artifact
into a build registry dump.
