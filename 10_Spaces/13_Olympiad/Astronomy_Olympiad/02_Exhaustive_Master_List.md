---
title: 02_Exhaustive_Master_List
course: ""
tags: []
aliases: ["02_Exhaustive_Master_List"]
created: "2026-05-11"
---
# Exhaustive Master List for IOAA Preparation

## 1. Mathematics & Data Analysis Toolkit
### 1.1 Spherical Trigonometry
*   [ ] **Concepts:** Great circles, small circles, poles, spherical triangles, dihedral angles.
*   [ ] **Formulas to Master:**
    *   [ ] Spherical Sine Rule: $\frac{\sin a}{\sin A} = \frac{\sin b}{\sin B} = \frac{\sin c}{\sin C}$
    *   [ ] Spherical Cosine Rule for Sides: $\cos a = \cos b \cos c + \sin b \sin c \cos A$
    *   [ ] Spherical Cosine Rule for Angles: $\cos A = -\cos B \cos C + \sin B \sin C \cos a$
    *   [ ] Four-Parts Rule (Cotangent formula).
    *   [ ] Haversine formula (for small angular distances to avoid precision loss).
*   [ ] **Applications:** Finding angular separation between two RA/Dec coordinates, converting between coordinate systems.

### 1.2 Geometry & Vectors
*   [ ] **Vector Algebra:** Addition, subtraction, dot product (finding angles between vectors), cross product (finding normal vectors, torque, angular momentum).
*   [ ] **Vector Calculus:** Geometric interpretation of a time derivative of a vector quantity (e.g., $\vec{v} = d\vec{r}/dt$, $\vec{a} = d\vec{v}/dt$).
*   [ ] **Conic Sections:** Properties of circles, ellipses, parabolas, and hyperbolas (foci, semi-major/minor axes, latus rectum, eccentricity).

### 1.3 Calculus & Numerical Methods
*   [ ] **Differentiation:** Product rule, quotient rule, chain rule for elementary functions (polynomials, exponentials, logarithms, trig functions).
*   [ ] **Integration:** Definite and indefinite integrals. Finding constants using initial conditions (e.g., given $v(t)$ and $r(0)$, find $r(t)$).
*   [ ] **Approximations:**
    *   [ ] Small angle: $\sin x \approx x$, $\tan x \approx x$, $\cos x \approx 1 - x^2/2$.
    *   [ ] Taylor series for $(1+x)^n \approx 1 + nx$ when $x \ll 1$.
    *   [ ] Natural log expansion $\ln(1+x) \approx x$.
*   [ ] **Numerical Methods:** Linearization of non-linear expressions, estimating area under curves (trapezoidal rule, graphical counting), finding roots iteratively.

### 1.4 Statistics & Error Analysis
*   [ ] **Descriptive Statistics:** Mean, weighted mean, median, mode, percentiles, quartiles, box plots.
*   [ ] **Uncertainty:** Standard deviation ($\sigma$), variance ($\sigma^2$), standard error of the mean ($\sigma / \sqrt{n}$).
*   [ ] **Error Propagation:**
    *   [ ] Addition/Subtraction: $Z = A \pm B \implies \delta Z = \sqrt{\delta A^2 + \delta B^2}$
    *   [ ] Multiplication/Division: $Z = AB \implies \frac{\delta Z}{Z} = \sqrt{\left(\frac{\delta A}{A}\right)^2 + \left(\frac{\delta B}{B}\right)^2}$
    *   [ ] Power laws: $Z = A^n \implies \frac{\delta Z}{Z} = |n| \frac{\delta A}{A}$
    *   [ ] Absolute vs. Relative errors. Maximum error estimations vs. Standard error.

### 1.5 Practical Graphing Skills
*   [ ] **Graph Types:** Linear, Polar, Semi-log (Log-Linear), Log-Log scales.
*   [ ] **Line Fitting:** Drawing a line of best fit by eye (balancing points above and below the line).
*   [ ] **Parameter Extraction:** Calculating slope (gradient) and y-intercept manually from a drawn line.
*   [ ] **Error Bars:** Drawing and interpreting error bars, estimating error margins from the scatter of data points around the best-fit line.

---

## 2. Fundamental Physics
### 2.1 Classical Mechanics
*   [ ] **Kinematics:** 1D, 2D, and 3D motion, rotational kinematics (angular velocity, angular acceleration).
*   [ ] **Dynamics:** Newton's Three Laws, momentum, impulse, torque.
*   [ ] **Energy:** Kinetic, Potential, Conservation of Energy, Work-Energy theorem.
*   [ ] **Angular Momentum:** Conservation of angular momentum, moment of inertia for simple shapes.

### 2.2 Thermodynamics & Statistical Mechanics
*   [ ] **Ideal Gas Law:** $PV = nRT = NkT$.
*   [ ] **Thermodynamic Processes:** Isothermal, adiabatic ($PV^\gamma = \text{const}$), isobaric, isochoric.
*   [ ] **Energy Transfer:** Conduction, Convection, Radiation.
*   [ ] Thermodynamic equilibrium vs. Local Thermodynamic Equilibrium (LTE).

### 2.3 Electromagnetism & Quantum Physics
*   [ ] **Electromagnetic Spectrum:** Wavelength/frequency boundaries for Radio, Microwave, IR, Visible, UV, X-ray, Gamma-ray.
*   [ ] **Blackbody Radiation:**
    *   [ ] Planck's Law (understanding the shape of the spectral radiance curve).
    *   [ ] Wien’s Displacement Law: $\lambda_{max} T = 2.898 \times 10^{-3} \text{ m K}$.
    *   [ ] Stefan-Boltzmann Law: $L = A \sigma T^4$ and flux $F = \sigma T^4$.
*   [ ] **Atomic Physics:**
    *   [ ] Bohr model of Hydrogen, energy levels: $E_n = -13.6 \text{ eV} / n^2$.
    *   [ ] Rydberg formula for spectral lines (Lyman, Balmer, Paschen series).
    *   [ ] Ionization energy.
*   [ ] **Nuclear Physics:** Mass defect ($E = mc^2$), binding energy per nucleon. Fusion processes (p-p chain, CNO cycle). Radioactivity (alpha, beta, gamma decay half-lives). Qualitative understanding of neutrinos.

---

## 3. Positional Astronomy & Time
### 3.1 Celestial Sphere & Coordinates
*   [ ] **Horizontal System (Alt-Az):** Altitude ($h$), Azimuth ($A$, $0^\circ \to 360^\circ$ N $\to$ E), Zenith, Nadir, Meridian.
*   [ ] **Equatorial System (RA-Dec):** Right Ascension ($\alpha$), Declination ($\delta$), Celestial Equator, North/South Celestial Poles, Vernal/Autumnal Equinox. Hour Angle ($H$).
*   [ ] **Ecliptic System:** Ecliptic Longitude ($\lambda$), Ecliptic Latitude ($\beta$), Obliquity of the ecliptic ($\epsilon \approx 23.5^\circ$).
*   [ ] **Galactic System:** Galactic Longitude ($l$), Galactic Latitude ($b$).
*   [ ] **Coordinate Transformations:** Spherical trig derivations between Horizontal/Equatorial and Equatorial/Ecliptic systems.
*   [ ] Circumpolar stars (conditions for never setting: $\delta > 90^\circ - \phi$ or never rising).
*   [ ] Constellations, Zodiac, asterisms.

### 3.2 Time Systems
*   [ ] **Solar Time:** Apparent Solar Time (sundial time), Mean Solar Time (clock time).
*   [ ] **Equation of Time:** $\text{EoT} = \text{Apparent} - \text{Mean}$ (understanding the Analemma shape due to orbital eccentricity and axial obliquity).
*   [ ] **Sidereal Time:** Local Sidereal Time (LST), Greenwich Sidereal Time (GST).
    *   [ ] Fundamental relation: $\text{LST} = H + \alpha$.
    *   [ ] Difference in length between mean solar day (24h) and sidereal day (~23h 56m 4s).
*   [ ] Time Zones, Universal Time (UT1, UTC), Local Mean Time (LMT).
*   [ ] **Julian Date (JD):** Calculating days elapsed since Jan 1, 4713 BC. Modified Julian Date (MJD = JD - 2400000.5). Heliocentric Julian Date (HJD) correction for binary star observations.
*   [ ] Definitions of a year: Tropical, Sidereal, Anomalistic, Draconic.

### 3.3 Earth-Moon-Sun Geometry
*   [ ] Seasons: Causes (obliquity), dates of equinoxes and solstices, variations in insolation (sunlight intensity based on latitude).
*   [ ] Earth's Motions: Precession of the equinoxes (~26,000 yr period), Nutation (18.6 yr period).
*   [ ] Lunar Phases: Synodic month (29.53 days, phase cycle) vs. Sidereal month (27.32 days, true orbit). Phase angle and illuminated fraction.
*   [ ] Eclipses: Umbra and penumbra geometry. Angular sizes of Sun and Moon. Nodes of lunar orbit, eclipse seasons, Saros cycle.
*   [ ] Libration of the Moon (optical/geometric and physical).

---

## 4. Celestial Mechanics
### 4.1 Two-Body Problem & Orbits
*   [ ] Newton’s Law of Universal Gravitation: $F = G m_1 m_2 / r^2$.
*   [ ] Kepler’s Laws (qualitative and mathematical formulations):
    *   [ ] 1st: Elliptical orbits (Polar equation: $r = a(1-e^2)/(1+e\cos\theta)$).
    *   [ ] 2nd: Equal areas in equal times ($dA/dt = L/2m = \text{const}$).
    *   [ ] 3rd: $P^2 = \frac{4\pi^2}{G(m_1+m_2)} a^3$.
*   [ ] Orbital Velocity & Energy:
    *   [ ] Vis-Viva Equation: $v^2 = G(m_1+m_2) \left(\frac{2}{r} - \frac{1}{a}\right)$.
    *   [ ] Escape velocity: $v_{esc} = \sqrt{2GM/R}$.
    *   [ ] Circular velocity: $v_c = \sqrt{GM/R}$.
*   [ ] Barycenter (Center of Mass) calculation: $r_1 = a \frac{m_2}{m_1+m_2}$.

### 4.2 Multi-Body & Advanced Orbital Dynamics
*   [ ] **Tidal Forces:** Derivation showing $F_{tidal} \propto 1/r^3$.
*   [ ] **Roche Limit:** Distance at which tidal forces overcome self-gravity ($d \approx 2.44 R (\rho_M / \rho_m)^{1/3}$).
*   [ ] **Lagrange Points:** Location and stability of L1 through L5. Deriving L1/L2 distances using binomial expansions.
*   [ ] **Space Exploration Mechanics:**
    *   [ ] Hohmann Transfer Orbit: Delta-v calculations for periapsis and apoapsis burns, transfer time.
    *   [ ] Gravitational Slingshot (Gravity Assist): Vector velocity addition, maximum delta-v gained.
    *   [ ] Satellite trajectories, geosynchronous and geostationary orbital altitudes.
*   [ ] Retrograde motion: Synodic period relation ($1/S = 1/P_{inner} - 1/P_{outer}$), determining the geometry of when retrograde motion begins/ends.

---

## 5. Stellar Astrophysics
### 5.1 Photometry and Distance
*   [ ] **Distances:** Trigonometric Parallax ($d (\text{pc}) = 1 / p (\text{arcsec})$), Distance Modulus ($m - M = 5 \log_{10} d - 5$).
*   [ ] **Magnitudes:** Apparent ($m$) and Absolute ($M$), Pogson’s formula ($m_1 - m_2 = -2.5 \log_{10}(F_1/F_2)$).
*   [ ] **Extinction:** Interstellar absorption ($m_\lambda - M_\lambda = 5 \log_{10} d - 5 + A_\lambda$).
*   [ ] **Color Index:** (B-V), (U-B), intrinsic color, color excess ($E(B-V) = (B-V) - (B-V)_0$).
*   [ ] Bolometric magnitude ($M_{bol}$) and Bolometric Correction (BC).

### 5.2 Spectroscopy and Stellar Atmospheres
*   [ ] **Doppler Effect:** Radial velocity $v_r = c (\Delta\lambda / \lambda)$ (non-relativistic).
*   [ ] Spectral classification (O, B, A, F, G, K, M) and relating lines to temperature.
*   [ ] Line broadening mechanisms:
    *   [ ] Thermal (Doppler) broadening: $\Delta\lambda \propto \sqrt{T}$.
    *   [ ] Rotational broadening: $\Delta\lambda \propto v_{rot} \sin i$.
    *   [ ] Pressure/Collisional broadening (used to differentiate Giants vs. Main Sequence Dwarfs).
*   [ ] Zeeman effect (magnetic field splitting).
*   [ ] Boundary conditions and interpreting stellar atmospheric spectra.

### 5.3 Stellar Structure & Evolution
*   [ ] **Hydrostatic Equilibrium:** $dP/dr = -G M_r \rho / r^2$.
*   [ ] **Star Formation:** Jeans Mass and Jeans Radius conditions for cloud collapse. Pre-Main Sequence tracks (Hayashi, Henyey).
*   [ ] **Main Sequence (MS):** Mass-Luminosity relation ($L \propto M^{3.5}$), MS lifetime approximation ($t \propto M/L \propto M^{-2.5}$).
*   [ ] **Nucleosynthesis:** p-p chain (low mass), CNO cycle (high mass), Triple-Alpha process (red giants).
*   [ ] **Post-Main Sequence:** Red Giant Branch (RGB), Asymptotic Giant Branch (AGB), Helium Flash.
*   [ ] **End States:**
    *   [ ] White Dwarfs: Electron degeneracy pressure, Chandrasekhar limit (~1.4 $M_\odot$), cooling curves.
    *   [ ] Neutron Stars: Neutron degeneracy pressure, Tolman-Oppenheimer-Volkoff limit (~2-3 $M_\odot$), Pulsars.
    *   [ ] Black Holes: Schwarzschild radius ($R_s = 2GM/c^2$).
    *   [ ] Supernovae (Type Ia standard candles, Type II core-collapse), Planetary nebulae remnants.

### 5.4 Binary Stars and Variables
*   [ ] **Binary Types:** Visual, Astrometric, Spectroscopic, Eclipsing.
*   [ ] **Mass Determination:**
    *   [ ] Visual: Using Kepler’s 3rd and parallax to find sum of masses.
    *   [ ] Spectroscopic: Mass function $f(m) = \frac{m_2^3 \sin^3 i}{(m_1+m_2)^2} = \frac{P v_{1r}^3}{2\pi G}$.
*   [ ] **Eclipsing Binaries:** Analyzing light curves (primary/secondary eclipses) to find the ratio of radii, ratio of temperatures, and orbital inclination.
*   [ ] **Interacting Binaries:** Roche lobes, accretion disks, Eddington luminosity (radiation pressure vs. gravity).
*   [ ] **Variable Stars:** Cepheids, RR Lyrae. Period-Luminosity relation for distance ($M = a \log P + b$). Physics of pulsation (Kappa-mechanism) (Qualitative).

---

## 6. The Solar System
### 6.1 The Sun
*   [ ] Structure: Core, Radiative Zone, Convective Zone, Photosphere, Chromosphere, Corona.
*   [ ] Solar radiation, Solar constant ($1361 \text{ W/m}^2$) and calculating Earth's equilibrium temperature.
*   [ ] Solar activities: Sunspots, 11-year cycle, Solar flares, Coronal Mass Ejections (CMEs).
*   [ ] Role of magnetic fields, Zeeman effect in sunspots (Qualitative).
*   [ ] Solar wind, radiation pressure on dust/comets, Heliosphere, Earth's Magnetosphere and Aurorae (Qualitative).

### 6.2 Solar System Objects
*   [ ] Formation of the Solar System (Nebular hypothesis) (Qualitative).
*   [ ] Terrestrial vs. Jovian planets (structure, internal composition differences).
*   [ ] Minor bodies: Dwarf planets, Asteroid belt, Kuiper belt, Oort cloud.
*   [ ] Comets (distinguishing ion tail pointing directly away from the Sun vs. curved dust tail). Meteor showers and radiants.
*   [ ] Climate factors, planetary atmospheres, greenhouse effect calculations, albedo.

---

## 7. Galaxies, Interstellar Medium, and Cosmology
### 7.1 The Interstellar Medium (ISM)
*   [ ] Composition: Gas and Dust ratios (Qualitative).
*   [ ] HII regions (Stromgren spheres calculation for ionization radius).
*   [ ] 21-cm radiation (hyperfine transition of neutral hydrogen) for mapping spiral arms.
*   [ ] Pulsar dispersion measure (time delay of varying radio frequencies $\implies$ electron column density).
*   [ ] Faraday rotation (rotation of polarization plane in magnetic fields).

### 7.2 The Milky Way & Galaxies
*   [ ] Milky Way structure: Bulge, Thin/Thick Disk, Halo, Globular Clusters (halo), Open Clusters (disk).
*   [ ] Rotation Curves: Rigid body vs. Keplerian vs. Flat rotation curves (empirical evidence for Dark Matter halo).
*   [ ] Galaxy Classification: Hubble Tuning Fork (E0-E7, Sa-Sc, SBa-SBc, Irregulars).
*   [ ] Distance Indicators: Cepheids (intra-galactic/nearby), Type Ia Supernovae (deep space).
*   [ ] Scaling relations: Tully-Fisher (Spirals, $L \propto v_{max}^4$), Faber-Jackson (Ellipticals, $L \propto \sigma^4$).
*   [ ] Active Galaxies: Quasars, Seyferts, Blazars (unified model and accretion qualitative understanding).

### 7.3 Cosmology
*   [ ] **Expansion:** Hubble-Lemaître Law ($v = H_0 d$).
*   [ ] **Redshift:** Cosmological redshift $z = \frac{\lambda_{obs} - \lambda_{rest}}{\lambda_{rest}} \approx \frac{v}{c}$ (for low $z$), $1+z = \frac{a(t_0)}{a(t_e)}$ (scale factor relationship).
*   [ ] Age of the Universe estimation ($t \approx 1/H_0$ in a flat universe).
*   [ ] **Cosmological Distances:** Lookback time, comoving distance, luminosity distance (understanding that $F = L / 4\pi d_L^2$ relies on luminosity distance, which changes with $z$).
*   [ ] **Components:** Dark Matter, Dark Energy (Accelerating universe) (Qualitative).
*   [ ] Cosmic Microwave Background (CMB): $T \approx 2.7 \text{ K}$, recombination era.
*   [ ] Big Bang nucleosynthesis, large-scale structure (filaments, voids), Gravitational Lensing (Einstein rings).

---

## 8. Practical Instrumentation & Observation
### 8.1 Optics and Telescopes
*   [ ] **Lenses & Mirrors:** Lensmaker's equation, focal length, focal plane geometry.
*   [ ] **Telescope Designs:** Refractor, Newtonian, Cassegrain, Schmidt-Cassegrain.
*   [ ] **Key Formulas:**
    *   [ ] Magnification: $M = f_{obj} / f_{eye}$.
    *   [ ] Focal Ratio (F-number): $F = f / D$.
    *   [ ] Resolving Power (Rayleigh Criterion): $\theta = 1.22 \lambda / D$ (in radians).
    *   [ ] Light Gathering Power (LGP): $\propto D^2$.
    *   [ ] Plate Scale: $s = 206265 / f_{obj}$ (arcsec/mm).
    *   [ ] Field of View (FOV): $\text{FOV} = d \times s$ (where $d$ is detector size).
*   [ ] Adaptive optics vs. Active optics (compensating for atmospheric seeing vs. mirror deformation).
*   [ ] Interferometry baseline and resolving power ($\theta \approx \lambda / B$).

### 8.2 Detectors & Observational Setup
*   [ ] Photometry: Signal-to-noise ratio (Poisson statistics $\text{SNR} \approx \sqrt{N}$), exposure time calculations.
*   [ ] CCD Cameras: Pixel size, binning, quantum efficiency, readout noise, dark current, calibration (bias, dark, flat-fielding).
*   [ ] Spectroscopy: Gratings, resolving power of a spectrograph ($R = \lambda / \Delta\lambda$).
*   [ ] Astrometry: Determining precise positions and proper motions.
*   [ ] Artificial light and electromagnetic pollution.

### 8.3 Field Skills (Practical Exam)
*   [ ] Using a Planisphere or Star Map.
*   [ ] Naked-eye angular estimations using hands (1°, 5°, 10°, 15°, 25° rules).
*   [ ] Magnitude estimation (comparing an unknown object to known reference stars by interpolation).
*   [ ] Operation of a generic equatorial/alt-azimuth telescope mount.
*   [ ] Familiarity with IAU-approved star names (brightest stars).

*(Note: Items marked "Qualitative" (Q) in the syllabus mean you only need conceptual understanding without complex mathematical derivations. However, you should still be able to reason logically about them during a theoretical exam.)*