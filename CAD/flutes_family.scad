// Flutes family scaffold for Round 31 issue #3.
// This is not a cut-ready flute model. Critical dimensions stay tied to
// cad/design-table-seed.csv and family-spec.csv until workbook rows and
// physical measurements are extracted.

$fn = 64;

show_family = "NAF-6H"; // NAF-6H, PVC-TRAIN, LEGACY-SW

naf_placeholder_length_mm = 390; // A4 analysis effective length reference only
naf_placeholder_bore_mm = 15.2;  // A4 FEM analysis row, not full packet authority
pvc_placeholder_length_mm = 390; // measurement_required
pvc_placeholder_bore_mm = 19.0;  // nominal placeholder, measure actual stock
body_wall_mm = 5.1;              // A4 FEM analysis row, measurement_required

module flute_body(length_mm, bore_mm, wall_mm) {
  difference() {
    cylinder(h = length_mm, d = bore_mm + 2 * wall_mm);
    translate([0, 0, -1])
      cylinder(h = length_mm + 2, d = bore_mm);
  }
}

module six_hole_markers(length_mm, bore_mm, wall_mm) {
  // Marker stations only. Real stations must come from workbook extraction.
  for (i = [1:6]) {
    translate([0, -(bore_mm / 2 + wall_mm + 1), length_mm * (0.28 + i * 0.075)])
      rotate([90, 0, 0])
        cylinder(h = 2, d = 4);
  }
}

module naf_scaffold() {
  color([0.55, 0.33, 0.18])
    flute_body(naf_placeholder_length_mm, naf_placeholder_bore_mm, body_wall_mm);
  color([0.1, 0.1, 0.1])
    six_hole_markers(naf_placeholder_length_mm, naf_placeholder_bore_mm, body_wall_mm);
}

module pvc_scaffold() {
  color([0.85, 0.85, 0.8])
    flute_body(pvc_placeholder_length_mm, pvc_placeholder_bore_mm, 2.5);
  color([0.1, 0.1, 0.1])
    six_hole_markers(pvc_placeholder_length_mm, pvc_placeholder_bore_mm, 2.5);
}

if (show_family == "PVC-TRAIN") {
  pvc_scaffold();
} else {
  naf_scaffold();
}
