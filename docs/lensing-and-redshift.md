# Lensing and Redshift

A light ray carries two kinds of information: its trajectory determines the apparent direction of a source, and its frequency records the relation between emitter and observer clocks. Gravity changes both. We calculate them separately so that coordinate effects do not become mistaken for local changes in light speed.

## The Frequency an Observer Measures

A photon has four-momentum $p^\mu$. An observer with four-velocity $u^\mu$ measures $E=p_\mu u^\mu=h\nu$, where $h$ here is Planck's constant.

In a static spacetime, the time-translation symmetry conserves $p_0$ along the ray. A stationary observer has $u^0=c/\sqrt{g_{00}}$, so the local frequency is proportional to $1/\sqrt{g_{00}}$. Thus

$$\frac{\nu_o}{\nu_e}=\sqrt{\frac{g_{00}(e)}{g_{00}(o)}}.$$

This relation assumes stationary emitter and observer in the static region. Their motion would add Doppler factors.

## Gravitational Redshift

For the Schwarzschild exterior,

$$\frac{\nu_o}{\nu_e}=\sqrt{\frac{1-r_s/r_e}{1-r_s/r_o}}.$$

A photon traveling upward from a smaller radius to a larger one is observed at lower frequency. For weak fields,

$$\frac{\nu_o-\nu_e}{\nu_e}\simeq\frac{\Phi_e-\Phi_o}{c^2}.$$

The locally measured photon energy changes between these observers, while the conserved quantity associated with static time translation remains constant. Energy measurement always includes the observer.

Cosmological redshift instead follows $1+z=a_o/a_e$. A general evolving FLRW spacetime has no corresponding static time-translation symmetry. Both effects arise from metric-dependent propagation and observer measurements, but their calculation uses different symmetries.

## Weak Deflection of Light

For a ray passing a spherical mass with impact parameter $b\gg r_s$, general relativity predicts

$$\alpha\simeq\frac{4GM}{bc^2}=\frac{2r_s}{b}.$$

The **impact parameter** describes the incoming ray's perpendicular offset from the center in the asymptotically flat region. The formula assumes weak deflection and distant source and observer.

<details>
<summary>Obtaining the leading deflection</summary>

For an equatorial Schwarzschild null geodesic, let $u=1/r$. The conserved quantities and null constraint give

$$\frac{d^2u}{d\phi^2}+u=\frac32r_su^2.$$

The undeflected trajectory is $u_0=\sin\phi/b$. Substituting it into the small correction gives a particular solution

$$\delta u=\frac{r_s}{4b^2}(3+\cos2\phi).$$

Near $\phi=0$, setting $u=0$ shifts the incoming asymptote by $-r_s/b$. Near $\phi=\pi$, the outgoing asymptote shifts by $+r_s/b$. Their difference gives $\alpha=2r_s/b$. Homogeneous corrections can fix the definition of the closest approach without changing this leading asymptotic angle.

</details>

## Images and the Einstein Radius

A lens can redirect more than one ray from a source toward an observer, producing multiple images. In the small-angle **thin-lens approximation**, a point mass obeys

$$\beta=\theta-\frac{\theta_E^2}{\theta},\qquad \theta_E^2=\frac{4GM}{c^2}\frac{D_{LS}}{D_LD_S}.$$

$\beta$ is the source's unlensed angular position, $\theta$ the image position, and the $D$ quantities are observer–lens, observer–source, and lens–source angular-diameter distances. In cosmology these distances require the expansion model.

Perfect alignment, $\beta=0$, produces an Einstein ring in the idealized point-lens model. Lensing preserves surface brightness in geometric optics but changes apparent solid angle, so it can magnify the received flux.

## Propagation Delay

A gravitational field also changes travel times. Different lensed paths have different geometric lengths and gravitational delays. In the solar system, the **Shapiro delay** is an excess radar travel time relative to a specified weak-field reference calculation.

Redshift, deflection, and delay test related parts of the metric using different measurements. [Tests of relativity](tests-of-relativity.md) connects those predictions to experimental comparisons and their assumptions.
