---
name: parametric-design-table
domain: instrument design
description: |
  Build a spreadsheet or table that takes one musical target and derives the
  rest of an instrument's geometry from it in a reproducible way.
status: validated across 150+ Native American style flute builds
canonical-location: tonykoop/flutes/skills/parametric-design-table.md
also-referenced-from:
  - tonykoop/flutes/SKILLS.md
  - tonykoop/flutes/README.md
  - tonykoop/fujara/README.md
provenance: |
  Derived from the Native American style flute design table and build
  registry documented in this repository.
audience: human (instrument makers, recruiters) + agent
maintainer: Tony Koop
license: CC-BY 4.0
---

# Parametric Design Table

> *Take one musical target note, then let a controlled table derive the body dimensions, hole positions, and material requirements instead of re-solving the whole instrument by hand every time.*

## When to use this skill

Use this when:

- the instrument family varies mainly by scale
- a small set of geometry rules can be reused across many target notes
- you want build records and design rules to live in the same artifact

## Core method

1. Choose the one input that matters most, usually the target fundamental note.
2. Define the stable geometric relationships that do not need to be rediscovered every build.
3. Let the table derive every downstream dimension that should change with the target note.
4. Track actual builds against the same table so the design tool and the yield history stay connected.
5. Revise the table based on failure modes, not just on successful builds.

## Why this matters

- It turns craft intuition into something reproducible.
- It makes scaling across keys practical.
- It creates a natural place to compare design intent with build reality.
- It is one of the cleanest bridges between handcraft and engineering thinking in this portfolio.

## Failure modes I watch for

- Treating the table as finished when the build registry is still surfacing yield problems.
- Mixing user-set inputs with derived values so thoroughly that the table becomes hard to reason about.
- Forgetting that material behavior can still move the outcome even when the geometry is correct.

## Cross-references

- [`flutes/README.md`](../README.md)
- [`fujara`](https://github.com/tonykoop/fujara)
- [`WSS-2019`](https://github.com/tonykoop/WSS-2019)
