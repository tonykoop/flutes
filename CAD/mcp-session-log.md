# Flutes MCP Session Log

This is the provenance landing zone for future V5 OpenSCAD, Blender, Illustrator, Photoshop, and image-generation sessions.

Round 31 created a conservative scaffold without running an MCP tool session. The row below records that boundary so future V5 work can append real session IDs without implying that this scaffold was MCP-verified.

| timestamp | tool | artifact | claude_session_id | notes |
| --- | --- | --- | --- | --- |
| 2026-05-18 | none-used | CAD/flutes_family.scad; drawings/flutes-family-layout.svg; drawings/flutes-family-layout.dxf; explorer.html | n/a | Local scaffold only. Not a measured or MCP-verified V5 build packet. |
| 2026-07-01 | claude-code (Fable 5) | CAD/design-table-seed.csv; CAD/flutes_family.scad; Flutes.xlsx | fable-v5-refresh-2026-07-01 | V5 refresh pass (packet_refresh, authority_result=fabrication, review_status=self_checked). Reviewed seed design table + scaffold against workbook; no dimension changes. Provenance row added to satisfy V5 fabrication-artifact logging for CAD/design-table-seed.csv. |
| 2026-07-01 | claude-code (Fable 5) + OpenSCAD CLI | CAD/flutes_family.scad | fable-v5-refresh-2026-07-01 | Existing family-layout OpenSCAD master (kept, not rewritten; cad_authoring, authority_result=pending_measurement, review_status=self_checked). openscad render check: pass (openscad -o STL, exit 0). |
| 2026-07-01 | claude-code (Fable 5) | wolfram/naf-flute-acoustics.wl | fable-v5-refresh-2026-07-01 | Wolfram NAF acoustics model; source-only (not executed; analysis_source, authority_result=derived_preview, review_status=unreviewed). L2 evidence. |
