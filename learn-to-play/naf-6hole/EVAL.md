# EVAL — sheet-music v0.1 against the production-ready NAF path

Evaluation of how cleanly the v0.1 `sheet-music` skill handled the
`naf-6hole` instrument — explicitly the v0.1 production-ready
target, per `SKILL.md`. Bugs surfaced here are **v0.1 fixes**, not
v0.2 expansion gaps.

Scope of this eval: the handoff at
`evals/handoffs/02-native-american-flute.md` — produce a complete
starter songbook for an A-tuned 6-hole NAF, deposit it into
`tonykoop/flutes`, and report honestly.

---

## What worked

The skill **did** deliver a complete songbook end-to-end without
fundamental rewrites of the engine. The strong points:

- **Registry-driven configuration.** `instruments/registry.yaml`
  carries enough information (range, scale, soundfont preset,
  fingering scheme, build-repo link) to drive every downstream
  script. Adding a tune or arrangement didn't require touching any
  Python — only ABC and Markdown.
- **Validator catches range violations cleanly.**
  `scripts/validate_arrangement.py --tune <abc> --instrument naf-6hole
  --strict` flagged out-of-range pitches the moment I authored a draft
  that strayed below A4. That tight loop saved real time.
- **Composer scaffolder is the right shape.** `compose_original.py`
  produced a header-correct stub with mood/form/range pre-filled and
  an explicit TODO marker for the LLM step. The
  scaffold-then-fill split kept determinism in the file and creativity
  in the model — exactly the workflow the skill description promises.
- **Pipeline degrades honestly.** With `lilypond` and `fluidsynth`
  absent, the pipeline produced 4-of-7 stages (ABC, MusicXML, MIDI,
  fingering SVG, songsheet PDF) and wrote a per-tune
  `render-summary.json` that documents which stages ran. No fake
  output, no silent skips. The SKILL.md "Fail honestly" rule held up
  under pressure.
- **Per-tune deliverables came out usable.** `tune.musicxml`,
  `tune.mid`, `tune-fingering.svg`, and `tune.pdf` all rendered for
  every tune. The MIDI uses GM preset 76 (Pan Flute) per the
  registry — the soundfont story is honored at the program-change
  level even when WAV rendering is skipped.
- **Catalog and arrangement separation is a sound model.** Storing
  PD tunes in `catalog/public-domain/<tradition>/<slug>/` and
  arrangements in `learn-to-play/<instrument>/...` lets one canonical
  tune feed many instruments. The model is right; what's missing is
  the *transposer* that the model implies (see "v0.1 fixes" below).
- **README append worked.** The build repo's `README.md` got a
  "Learn to play" section at the bottom without disturbing prior
  content, and the script's idempotent-section logic handles re-runs.

---

## What felt rough

These are real friction points encountered while running the handoff,
in roughly the order I hit them.

### 1. `deposit_songbook.py` repertoire selection is alphabetical, not curated

The handoff specified three exact tunes for `01-easy` (Amazing Grace,
Star of the County Down, What Wondrous Love Is This). The script's
`pick_repertoire()` simply takes the first three PD-tune folders in
alphabetical order, then the next two for intermediate, then the first
original alphabetically. After my catalog additions the auto-pick
landed on:

- easy: `simple-gifts, wondrous-love, auld-lang-syne`
- intermediate: `loch-lomond, scotland-the-brave`
- original: `drovers-path`

None of those match the handoff except `wondrous-love`. The two celtic
intermediate tunes are *bagpipe* arrangements in A mixolydian and
contain B and F# pitches that the A-NAF cannot play — but
`deposit_songbook.py` happily ran them through the full pipeline
without any compatibility check. I had to delete the deposit and
re-curate manually.

### 2. The deposited per-tune folders are missing `notes.md`

`render_pipeline.py` copies `tune.abc` into the destination but does
not copy the source folder's `notes.md`. Since the deposit's quality
gate (`validate_arrangement.py --target ... --strict`) requires
`notes.md` per tune, every clean v0.1 deposit fails its own validator
unless the orchestrator copies notes.md by hand. That's a one-line
fix: `shutil.copy2(tune_src/"notes.md", dest/"notes.md")` in
`run_pipeline()`.

### 3. No combined `fingering-charts.svg` is auto-generated

The starter-songbook spec lists `fingering-charts.svg` at the top
level as a quality gate. The deposit pipeline produces *per-tune*
fingering SVGs but never concatenates / unions them into a top-level
chart. I generated one manually by feeding a synthetic
"all NAF pitches" ABC into `render_fingering_svg.py`. This should be a
final pipeline step in `deposit_songbook.py`.

### 4. No top-level `songsheet.pdf` is auto-generated

Same shape of problem as #3. Each tune folder gets its own one-page
`tune.pdf`, but the spec calls for a single top-level `songsheet.pdf`
that summarizes the whole songbook. I wrote one with ReportLab in
~40 lines; this should ship as a script in the skill.

### 5. `generate_scales.py` ignores the instrument's `scale` field

For a `naf-6hole` row whose `scale: minor-pentatonic`, the auto-
generated `range-walk.abc` came out as `K:A` (major) and walked the
**diatonic** range (`A B c d e f g a b c' d'`) — including B, F, b, f,
which the NAF cannot play with standard fingerings. I overwrote the
generated file with an A-min-pent walk by hand. The fix is small:
`generate_scales.py` should read the registry's `scale` field and emit
only in-scale pitches.

### 6. `compose_original.py` produces `K:A` instead of `K:Am` for minor scales

The scaffold for `pre-dawn-field` came out as `K:A` (A major) even
though the registry says `scale: minor-pentatonic`. ABC tools (and
music21 in particular) apply key-signature accidentals, so `K:A` would
silently sharp every C, F, G in playback if I hadn't fixed it. The
right behavior is to map `minor-pentatonic` → `K:Am`,
`major-pentatonic` → `K:C` (or the major-key equivalent),
`mixolydian-A` → `K:Amix`, etc. — registry-driven, not hard-coded.

### 7. `compose_original.py` mangles the title hyphen

I asked for slug `pre-dawn-field` and got `T:Pre Dawn Field` (no
hyphen) in the scaffold. The slug→title transform splits on `-` and
then joins on space, dropping any intentional hyphenation. The fix is
to preserve hyphens: split on `-` only for word capitalization, then
re-join with `-`. (Or just accept the hyphen in the slug as part of
the displayed title.)

### 8. The arrangement step that the catalog model implies doesn't exist

The catalog stores tunes at "concert pitch" with the expectation that
arrangement-for-instrument happens at deposit. In practice
`deposit_songbook.py` just `cp`s the canonical ABC into the deposit
folder unmodified. So:

- `catalog/public-domain/hymn/amazing-grace/tune.abc` is at G
  (low-D below NAF range A4).
- Depositing it for `naf-6hole` produces a "tune" with pitches the
  flute literally cannot play.
- The validator does catch it (with `--strict`), but only after the
  pipeline has produced incorrect MIDI/MusicXML/PDF.

I worked around this by writing the A-NAF arrangement of Amazing
Grace directly into the deposit folder and tagging it as an
arrangement (provenance line in the ABC + explanation in
`notes.md`). The skill should ship a `transpose_for_instrument(abc,
target_row)` step that reads the registry, picks a target key the
instrument can actually play, and rewrites the ABC accordingly.
`flute-family.md` already specifies this step in arrangement
workflow #2; it just isn't implemented in code.

### 9. `validate_arrangement.py --target` only checks structure, not content

The directory-mode validation checks for the existence of required
folders and files but doesn't run the per-tune range/header
validation across every tune in the deposited folder. Combined with
issue #1, this means a bad auto-pick can produce a "valid" deposit
that contains tunes the instrument cannot play. The fix: `--target`
mode should walk every `*/tune.abc` and run the per-tune validator
recursively, accumulating issues.

### 10. The README append's link is generic, not instrument-specific

`append_to_build_readme()` writes a single "Learn to play" section
linking to `learn-to-play/`. When multiple instruments share a build
repo (NAF and PVC both ship from `flutes`, per the registry), the
real content lives at `learn-to-play/naf-6hole/` not `learn-to-play/`.
I rewrote the section by hand to list each instrument explicitly. The
fix: when `instrument != target.name` (the multi-instrument-repo case
the script already detects for the deposit path), the README section
should also link to the instrument-specific subfolder.

### 11. `tune.pdf` (per-tune songsheet) is a placeholder, not engraved

The ReportLab fallback in `build_songsheet_pdf.py` draws two empty
rectangles labeled "Engraved notation: open tune.svg" and "Fingering
chart: see tune-fingering.svg" — i.e., the songsheet PDF doesn't
actually embed the staff or the fingering chart. This is documented
in the script's source (`references/adobe-handoff.md` for the polished
path), but the v0.1 fallback PDF isn't useful as a printed reference
yet. Either embed the SVGs into the ReportLab canvas (svglib +
reportlab.graphics) or document this clearly in the songsheet output
itself ("for the engraved notation, render with LilyPond and reprint
this page").

---

## v0.1 fixes (ranked by impact)

These should land before v0.2 expands the family coverage. Roughly
ordered by how badly the v0.1 NAF path was broken without them.

1. **Add a transposer.** The catalog-vs-arrangement model is right,
   but without `transpose_for_instrument(abc, target_row)` the
   deposit produces unplayable output for any instrument whose key
   doesn't match the canonical entry. Probably 50–80 lines using
   music21's `.transpose()`.
2. **Fix `deposit_songbook.py` repertoire selection.** Either accept
   `--easy/--intermediate/--original` flags with explicit slug lists
   *or* make `pick_repertoire()` instrument-aware (filter PD tunes
   for in-range / in-scale before alphabetical fallback). Today it's
   alphabetical only, and that's how my deposit ended up with
   bagpipe tunes in the NAF intermediate slot.
3. **Have `render_pipeline.py` copy `notes.md`.** One-line fix; closes
   the gap that makes the structural validator fail on a clean run.
4. **Auto-generate combined `fingering-charts.svg` and top-level
   `songsheet.pdf` in `deposit_songbook.py`.** Both are listed in the
   spec and required by the structural validator; today both are
   missing on a fresh deposit.
5. **Fix `generate_scales.py` to honor the `scale` field.** The
   range-walk for a pentatonic instrument should be pentatonic, not
   diatonic. Same for the intervals drill.
6. **Fix `compose_original.py`'s `K:` line.** Map registry `scale`
   to ABC `K:` correctly (`minor-pentatonic` → `Am`, etc.). Today
   it's emitting major-key signatures for minor-pent instruments.
7. **Make `compose_original.py` preserve the slug hyphen in the
   title** (or accept titles in a separate flag).
8. **Make `validate_arrangement.py --target` walk every tune file**
   and run per-tune range/header validation on each, not just the
   structural folder check.
9. **Fix the README-append link** to point to the instrument-specific
   subfolder when the build repo hosts multiple instruments.
10. **Embed the SVGs in the per-tune songsheet PDF** (or document the
    placeholder loudly).

---

## Bottom line

The v0.1 `naf-6hole` path is **not yet clean end-to-end**, even though
it's labeled production-ready. Most of the gaps are small and
mechanical (issues 3, 5, 6, 7, 9 are each ≤10 lines of Python). A few
are structural (issues 1, 2, 4 require modest additions to the
deposit pipeline). One is a UX miss (issue 10/songsheet placeholder).

What's encouraging: the **shape of the skill is right**. The
catalog/registry/family-reference split, the scaffold-then-fill
composition flow, the "fail honestly" rendering pipeline, and the
deposit-to-build-repo deliverable model are all correct. The bugs are
in implementation density, not architecture.

Realistic v0.1.1 milestone: fix issues 1–7. After that, the NAF path
deposits cleanly without the orchestrator having to hand-edit anything.
