# References — Wood-Species Coupled Structural-Acoustic FEM

## Primary material property sources

**[1] Wood Handbook — Wood as an Engineering Material**
Forest Products Laboratory. USDA Forest Service, Forest Products Laboratory.
General Technical Report FPL-GTR-190. Madison, WI, 2010.
Table 5-1 (orthotropic elastic constants for clear, straight-grained wood by species) and
Table 5-2 (strength properties).
URL: https://www.fpl.fs.usda.gov/documnts/fplgtr/fpl_gtr190.pdf

Species values used:
- Western Red Cedar (*Thuja plicata*): Table 5-1, moisture content 12%.
- Black Walnut (*Juglans nigra*): Table 5-1, moisture content 12%.
- Hard Maple (*Acer saccharum*): Table 5-1, moisture content 12%.

**[2] Haines, D. W.** "On musical instrument wood."
*Journal of the Catgut Acoustical Society*, Vol. 31, pp. 23–32, 1979.
Longitudinal loss factor (damping) measurements for spruce, cedar, maple, and walnut.

**[3] Schelleng, J. C.** "The bowed string and the player."
*Journal of the Acoustical Society of America*, Vol. 53, No. 1, pp. 26–41, 1973.
Discussion of Q-factor and damping in musical wood.

## Acoustic modeling references

**[4] Fletcher, N. H., and Rossing, T. D.**
*The Physics of Musical Instruments*, 2nd ed. Springer, New York, 1998.
Chapter 16: Flutes and flue instruments. Air-column mode theory, end corrections, open-hole cutoff frequency.

**[5] Nederveen, C. J.**
*Acoustical Aspects of Woodwind Instruments*. Northern Illinois University Press, 1998.
Detailed treatment of end corrections, tone-hole lattice, and inharmonicity for
open-cylindrical instruments.

**[6] Wolfe, J.** "Flute acoustics: an introduction."
UNSW School of Physics, Music Acoustics group, 2005.
URL: https://www.phys.unsw.edu.au/music/flute/

## Structural-acoustic coupling references

**[7] Fahy, F. J.**
*Sound and Structural Vibration: Radiation, Transmission and Response*.
Academic Press, London, 1985.
Chapters 4 and 5: radiation efficiency of cylindrical shells; vibroacoustic coupling loss factor.

**[8] Cremer, L., Heckl, M., and Ungar, E. E.**
*Structure-Borne Sound: Structural Vibrations and Sound Radiation at Audio Frequencies*.
Springer-Verlag, Berlin, 1988.
Chapter 9: Cylindrical shells, breathing modes, ring frequency.

**[9] Gough, C. E.** "Musical acoustics." In *Springer Handbook of Acoustics*,
T. D. Rossing, ed., Springer, New York, 2007, pp. 533–621.
Section 15.4: Wood and its acoustic properties; loss factor tables for instrument woods.

## FEM software references

**[10] COMSOL Multiphysics 6.x — Acoustics Module User's Guide.**
Acoustic-Solid Interaction multiphysics coupling; frequency-domain harmonic analysis.
Chapter 3: Acoustic-Structural Interaction.

**[11] Ansys Mechanical 2023 — Harmonic Acoustics Module.**
System coupling: Fluid–Structure Interaction for acoustic cavities and elastic shells.
Ansys Help Portal: Harmonic Acoustics documentation.

## Sister-repo cross-references

- `tonykoop/flutes` — build registry and parametric design table.
- `tonykoop/WSS-2019` — Wolfram Summer School notebook:
  *Properties of a Native American Flute.nb* (air-column acoustic model).
- `tonykoop/tensile-testing` — orthotropic elastic constant measurement pipeline,
  source of species-resolved E-tensor data.
- `tonykoop/tongue-drum` — FEM modal pipeline reused for this analysis;
  measurement protocol shared.
