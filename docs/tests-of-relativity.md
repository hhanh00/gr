# Tests of Relativity

To test a geometric theory, calculate an observable and compare it with a measurement under the same conditions. Clock readings, image positions, orbital angles, and signal travel times provide different comparisons. No single successful measurement establishes every part of general relativity.

## 1. Free Fall and Clock Comparisons

Universality-of-free-fall experiments compare the accelerations of bodies with different composition. A common measure is the **Eötvös parameter**

$$\eta=\frac{2|a_A-a_B|}{|a_A+a_B|}.$$

The weak equivalence principle predicts $\eta=0$ for ideal test bodies in the same field. An experimental bound must include control of nongravitational forces and instrumental uncertainties.

Clock comparisons test the predicted weak-field rate difference $\Delta\nu/\nu\simeq\Delta\Phi/c^2$, with a stated convention for comparing the clocks. Frequency transfer also includes motion, atmospheric effects, and the signal path. Satellite timekeeping combines gravitational shifts with special-relativistic velocity shifts rather than treating either in isolation.

## 2. Perihelion Precession

A bound orbit in Schwarzschild spacetime is not a closed Kepler ellipse. For a weak-field orbit with semimajor axis $a$ and eccentricity $e$, the additional perihelion advance per orbit is

$$\Delta\phi=\frac{6\pi GM}{a(1-e^2)c^2}.$$

The **perihelion** is the point of closest approach to the Sun. This expression assumes a test body and a nearly Newtonian orbit.

<details>
<summary>Connecting the orbit correction to precession</summary>

For a timelike equatorial geodesic, $u=1/r$ obeys

$$u''+u=\frac{GM}{\ell^2}+\frac{3GM}{c^2}u^2.$$

At zeroth order, $u=(1+e\cos\phi)/p$, where $p=\ell^2/(GM)=a(1-e^2)$. The correction contains a resonant term proportional to $\cos\phi$. Absorb it into a shifted frequency:

$$u\simeq\frac1p[1+e\cos((1-\delta)\phi)],\qquad \delta=\frac{3GM}{pc^2}.$$

One radial cycle then spans $2\pi/(1-\delta)$, giving extra angle $2\pi\delta$ to first order. Nonresonant terms also perturb the orbit but do not set the leading secular precession.

</details>

Comparing this prediction with a planetary orbit requires subtracting or fitting other contributions, including perturbations from planets and the Sun's nonspherical mass distribution.

## 3. Light Deflection and Radar Delay

Light bending probes the spacetime geometry along a null path. In a weak static parameterization, the **post-Newtonian parameter** $\gamma_{\rm PPN}$ measures spatial curvature relative to the Newtonian potential. It is unrelated to the Lorentz factor used in special relativity.

At leading order,

$$\alpha=(1+\gamma_{\rm PPN})\frac{2GM}{bc^2}.$$

General relativity predicts $\gamma_{\rm PPN}=1$. Time dilation alone does not supply the full deflection; the spatial metric contributes too.

For a radar signal passing a mass, the leading one-way Shapiro delay in a standard weak-field coordinate treatment is

$$\Delta t\simeq(1+\gamma_{\rm PPN})\frac{GM}{c^3}\ln\frac{r_e+r_o+R}{r_e+r_o-R}.$$

$r_e$ and $r_o$ are the endpoint radii, and $R$ is their Euclidean separation at leading order. A round-trip measurement includes the return path and conversion to the observing clock's proper time.

## 4. Binary Motion and Radiation

Binary pulsar timing tests orbital dynamics and the energy loss predicted by gravitational radiation. Interpreting an orbital-period change also requires corrections for relative acceleration and other astrophysical effects.

Gravitational-wave observations test the waveform's phase and amplitude evolution. Inspiral calculations, numerical merger solutions, and final black-hole oscillations probe different regimes. Agreement with a fitted waveform must be assessed alongside noise, source parameters, and possible competing models.

These comparisons extend the weak-field tests to relativistic motion and strong gravitational fields. They do not establish a quantum theory of gravity or eliminate every possible modification outside the tested regime.

## 5. Connecting the Sequence

The chapters began with invariant intervals and clock readings, developed tensors and curvature, and introduced Einstein's dynamical equations. Schwarzschild and FLRW supplied concrete solutions. Light propagation and gravitational waves then supplied observables.

When evaluating a new claim, identify the metric and matter assumptions, the trajectory or field calculation, and the actual measured quantity. That chain connects a statement about geometry to an experimental prediction.
