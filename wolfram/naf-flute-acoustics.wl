(* Native American Style Flute — Open-Open Bore Acoustics Starter
   tonykoop/flutes
   Authority: first-order estimates from public workbook rows (F4/A4/C5).
   Dimension provenance = measurement_required for all rows.
   Manipulate block is CloudDeploy-ready (Public-Execute). *)

(* ── Open-Open Duct Flute Model ──
   L_eff = c / (2 * f)
   L_geom = L_eff - end_correction_total
   End correction (each open end): ΔL ≈ 0.6 × r
   Total end correction ≈ 1.2 × r (both ends) *)

OpenOpenFreq[Lgeom_Real, r_Real, c_Real : 343.0] :=
  c / (2 * (Lgeom + 1.2 * r))

EffectiveLength[f_Real, c_Real : 343.0] := c / (2 * f)

GeomLength[f_Real, r_Real, c_Real : 343.0] :=
  c / (2 * f) - 1.2 * r

(* Convert mm → m *)
MMToM[x_] := x / 1000.0

(* ── Workbook reference rows (public F4/A4/C5) ──
   From family-spec.csv; dimension_provenance = measurement_required *)
WorkbookRows = {
  <|"note" -> "F4", "f" -> 349.23, "Lgeom_mm" -> 432.562,
    "boreID_mm" -> 22.225, "holes" -> 6|>,
  <|"note" -> "A4", "f" -> 440.00, "Lgeom_mm" -> 337.490,
    "boreID_mm" -> 19.050, "holes" -> 6|>,
  <|"note" -> "C5", "f" -> 523.25, "Lgeom_mm" -> 285.318,
    "boreID_mm" -> 15.875, "holes" -> 6|>
}

(* Reference comparison table *)
Print["Workbook rows vs first-order model:"]
TableForm[
  Table[
    Module[{row = WorkbookRows[[i]], c = 343.0},
      {
        row["note"],
        NumberForm[row["f"], {5, 2}],
        NumberForm[row["Lgeom_mm"], {5, 1}],
        NumberForm[row["boreID_mm"], {4, 3}],
        NumberForm[
          1000 * EffectiveLength[row["f"]], {5, 1}],
        NumberForm[
          1000 * GeomLength[row["f"], MMToM[row["boreID_mm"]/2]], {5, 1}]
      }
    ],
    {i, 1, 3}
  ],
  TableHeadings -> {None,
    {"Note", "Target Hz", "Workbook L_geom (mm)", "Bore ID (mm)",
     "L_eff model (mm)", "L_geom model (mm)"}
  }
]

(* ── Interactive Manipulate ── *)

flutesExplorer = Manipulate[
  Module[
    {
      r_m   = MMToM[boreID_mm / 2],
      Lg_m  = MMToM[Lgeom_mm],
      f_est = OpenOpenFreq[MMToM[Lgeom_mm], MMToM[boreID_mm / 2]],
      L_eff = EffectiveLength[targetHz],
      L_geom_calc = 1000 * GeomLength[targetHz, MMToM[boreID_mm / 2]]
    },
    Grid[{
      {"Target note frequency (Hz)", NumberForm[targetHz, {5, 2}]},
      {"Bore ID (mm)", NumberForm[boreID_mm, {4, 1}]},
      {"End correction total (mm)", NumberForm[1000 * 1.2 * MMToM[boreID_mm/2], {4, 1}]},
      {"Model L_eff (mm)", NumberForm[1000 * EffectiveLength[targetHz], {5, 1}]},
      {"Model L_geom (mm)", NumberForm[L_geom_calc, {5, 1}]},
      {"Actual chamber (mm)", NumberForm[Lgeom_mm, {5, 1}]},
      {"Estimated pitch from actual (Hz)", NumberForm[f_est, {5, 2}]},
      {"Pitch error (cents)",
        NumberForm[1200 * Log2[f_est / targetHz], {4, 1}]},
      {"Note", "measurement_required — workbook rows, not measured data."}
    },
    Frame -> All,
    Background -> {{GrayLevel[0.88], White}, None}]
  ],

  (* Controls *)
  {{targetHz, 440.0, "Target frequency (Hz)"}, 260.0, 600.0, 1.0,
    Appearance -> "Labeled"},
  {{boreID_mm, 19.05, "Bore ID (mm)"}, 10.0, 30.0, 0.25,
    Appearance -> "Labeled"},
  {{Lgeom_mm, 337.5, "Actual chamber length (mm)"}, 200.0, 550.0, 1.0,
    Appearance -> "Labeled"},

  ControlPlacement -> Left,
  TrackedSymbols :> {targetHz, boreID_mm, Lgeom_mm}
]
