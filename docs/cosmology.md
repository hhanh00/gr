# Cosmology

On sufficiently large scales, we can model the universe as spatially homogeneous and isotropic. These assumptions reduce the geometry to a time-dependent scale factor. Einstein's equations then relate expansion to matter, radiation, pressure, and a cosmological constant.

## 1. The Expanding Metric

The **Friedmann–Lemaître–Robertson–Walker metric**, abbreviated FLRW, is

$$ds^2=c^2dt^2-a^2(t)\left[\frac{d\chi^2}{1-k\chi^2}+\chi^2d\Omega^2\right].$$

Here $\chi$ is a dimensionless comoving radial coordinate, $k=0,\pm1$ describes spatial curvature, and $a(t)$ has units of length in this convention. A **comoving observer** stays at fixed spatial coordinates and records proper time $t$.

Homogeneity means the spatial geometry has no preferred location; isotropy means no preferred direction. These describe an idealized large-scale background. Galaxies and other structures require perturbations around it.

The **Hubble parameter** is $H=\dot a/a$. For comoving objects at fixed spatial separation in the flat case, their proper separation on a constant-$t$ slice satisfies $\dot D=HD$. This recession rate is not a local relative velocity between objects meeting at one event.

## 2. The Friedmann Equations

For a perfect fluid of mass-equivalent density $\rho=\epsilon/c^2$ and pressure $p$, our field-equation convention gives

$$H^2=\frac{8\pi G}{3}\rho-\frac{kc^2}{a^2}+\frac{\Lambda c^2}{3},$$

$$\frac{\ddot a}{a}=-\frac{4\pi G}{3}\left(\rho+\frac{3p}{c^2}\right)+\frac{\Lambda c^2}{3}.$$

We provide these symmetry-reduced equations without computing every FLRW curvature component. Positive ordinary pressure contributes to deceleration. Positive $\Lambda$ contributes to acceleration.

Energy–momentum conservation gives

$$\dot\rho+3H\left(\rho+\frac p{c^2}\right)=0.$$

An **equation of state** relates pressure to density, completing the fluid model. For constant $w$ defined by $p=w\rho c^2$, this gives $\rho\propto a^{-3(1+w)}$.

## 3. Matter and Radiation

Pressureless matter has $w=0$ and $\rho_m\propto a^{-3}$. Radiation has $w=1/3$ and $\rho_r\propto a^{-4}$. Expansion dilutes the number of photons per volume and decreases each photon's energy, producing the additional inverse power of $a$.

<details>
<summary>Solving single-fluid expansion</summary>

Take $k=\Lambda=0$ and constant $w>-1$. With $\rho\propto a^{-3(1+w)}$, the first Friedmann equation gives

$$\dot a\propto a^{1-3(1+w)/2}.$$

Integrating from the idealized initial singularity yields $a(t)\propto t^{2/[3(1+w)]}$. Thus matter domination gives $a\propto t^{2/3}$ and radiation domination gives $a\propto t^{1/2}$. These are single-component limits, rather than the expansion history at all times.

</details>

A pure positive-$\Lambda$ flat solution has constant $H=\sqrt{\Lambda c^2/3}$ and exponential expansion. Treating $\Lambda$ as a fluid instead would give $w=-1$; do not count it both as a separate fluid and as the explicit cosmological term.

## 4. Redshift and Horizons

Light emitted at $t_e$ and observed at $t_o$ has

$$1+z=\frac{a(t_o)}{a(t_e)}.$$

The **redshift** $z$ measures the observed fractional increase in wavelength. At small distances and small redshift, $cz\simeq H_oD$. At large distances, calculating distance requires the expansion history and a specified distance definition.

For radial light, define comoving radial distance using $d\chi/\sqrt{1-k\chi^2}$. The particle-horizon distance in these units is $\int_{t_{\rm start}}^t c\,dt'/a(t')$, if finite. An event horizon instead concerns the future integral $\int_t^{t_{\rm end}}c\,dt'/a(t')$. A Hubble radius $c/H$ is not automatically either horizon.

FLRW establishes the background expansion. [Gravitational waves](gravitational-waves.md) turns to traveling perturbations of spacetime, while [Lensing and redshift](lensing-and-redshift.md) connects light propagation to observations.
