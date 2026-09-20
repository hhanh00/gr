# Black Holes: Falling In and Formation

A horizon is a boundary in the set of possible signal paths. To determine whether light can escape, we must examine future-directed trajectories rather than infer physical behavior from a diverging metric component.

## The Event Horizon

In an asymptotically flat spacetime, a **black-hole region** contains events from which no future-directed causal signal can reach future null infinity, the idealized destination of escaping light. Its boundary is the **event horizon**.

This definition is global. Identifying an event horizon requires the spacetime's future causal structure, rather than just one local measurement. Apparent horizons, which concern trapped surfaces on chosen spatial slices, are useful in evolving spacetimes but are not identical to event horizons in general.

For a Schwarzschild black hole, the event horizon is $r=r_s$. A star with surface radius larger than $r_s$ can have a Schwarzschild exterior without having a horizon.

## Coordinates That Cross the Horizon

Define the **tortoise coordinate**

$$r_*=r+r_s\ln\left|\frac{r}{r_s}-1\right|,$$

and ingoing time coordinate $v=t+r_*/c$. The metric becomes

$$ds^2=f(r)c^2dv^2-2c\,dv\,dr-r^2d\Omega^2.$$

These **ingoing Eddington–Finkelstein coordinates** have no divergent metric coefficients at $r_s$.

<details>
<summary>Transforming the radial metric</summary>

Since $dr_*/dr=1/f$, substitute $dt=dv-dr/(cf)$ into $fc^2dt^2-dr^2/f$. The two $dr^2/f$ terms cancel, leaving $fc^2dv^2-2c\,dv\,dr$.

Radial null curves then have either $dv=0$, the ingoing family, or

$$\frac{dr}{dv}=\frac c2f(r),$$

the outgoing family. This transformation makes their behavior at the horizon explicit.

</details>

At the horizon the outgoing family stays at fixed radius. Inside it, even these future-directed outgoing rays move toward smaller $r$. This causal restriction prevents escape; it is not a failure of an engine to exceed a Newtonian escape speed.

## Kruskal Coordinates

The ingoing chart crosses the future horizon, but a chart covering both horizon families makes the eternal solution's causal structure clearer. In the exterior, define dimensionless coordinates

$$U=-\exp\left[-\frac{ct-r_*}{2r_s}\right],\qquad V=\exp\left[\frac{ct+r_*}{2r_s}\right].$$

They obey

$$-UV=\left(\frac r{r_s}-1\right)e^{r/r_s}.$$

The metric becomes

$$ds^2=\frac{4r_s^3}{r}e^{-r/r_s}\,dU\,dV-r^2d\Omega^2.$$

Its coefficient is finite and nonzero at $r=r_s$. Radial null lines have constant $U$ or constant $V$, and horizons occur at $UV=0$. **Kruskal coordinates** extend the chart smoothly across those horizons by treating this metric and the implicit equation for $r$ as the continuation.

<details>
<summary>Deriving the Kruskal metric coefficient</summary>

Let $q=ct-r_*$ and $p=ct+r_*$. The radial metric is $f\,dq\,dp$. Since $dq=-2r_s\,dU/U$ and $dp=2r_s\,dV/V$,

$$f\,dq\,dp=-\frac{4r_s^2f}{UV}\,dU\,dV.$$

Use $UV=-(r/r_s-1)e^{r/r_s}$ and $f=(r/r_s-1)/(r/r_s)$. The factor $r/r_s-1$ cancels, leaving $4r_s^3e^{-r/r_s}/r$. No coefficient diverges at the horizon.

If we define $T=(V+U)/2$ and $X=(V-U)/2$, then $dU\,dV=dT^2-dX^2$. Light rays appear at $45^\circ$ in the $(T,X)$ diagram. The surface $r=0$ corresponds to $UV=1$ and remains singular.

</details>

## Falling and Observing

A freely falling observer crosses a regular Schwarzschild horizon in finite proper time. Schwarzschild coordinate time tends to infinity for that crossing, but that chart does not extend smoothly through it.

A distant observer receives increasingly delayed and redshifted signals from the falling object. The object's clock does not stop locally. The distinction concerns the falling worldline, the received signals, and the chosen coordinates.

Horizon-crossing tidal forces depend on the mass. The curvature invariant at $r_s$ scales as $1/r_s^4$, so large black holes can have small tidal curvature at the horizon even though their centers remain singular in the classical solution.

## Singularities and Extensions

A coordinate singularity can disappear in another chart. A physical singularity cannot be removed that way. More generally, singularity theorems concern **geodesic incompleteness**: a causal geodesic ends after a finite affine parameter without continuation within the spacetime. Curvature divergence is an important diagnostic, but it is not the complete definition.

The maximally extended eternal Schwarzschild solution contains additional exterior and white-hole regions. A black hole formed by stellar collapse does not automatically contain that entire eternal extension; its past includes collapsing matter.

## Falling In and Gravitational Collapse

For a radial timelike geodesic, the conserved quantity $e=f\,dt/d\tau$ and the normalization give

$$\left(\frac{dr}{d\tau}\right)^2=c^2(e^2-f).$$

A particle released from rest at infinity has $e=1$. On its inward path,

$$\frac{dr}{d\tau}=-c\sqrt{\frac{r_s}{r}}.$$

Starting at a finite radius $r_0$, the proper time along this particular infalling trajectory down to radius $r$ is

$$\tau(r)-\tau(r_0)=\frac{2}{3c\sqrt{r_s}}(r_0^{3/2}-r^{3/2}).$$

It crosses the horizon in finite proper time. From $r_s$ to $0$, this geodesic has remaining proper time $2r_s/(3c)$. Starting at infinity itself takes infinite proper time; the finite-radius expression avoids treating infinity as an ordinary release event.

A real black hole can form when an object's internal support fails to halt collapse. A model calculation must solve the matter interior, follow its surface, and match it to the exterior geometry. An idealized spherical pressureless fluid gives the Oppenheimer–Snyder collapse model. Its interior is a contracting homogeneous dust solution, while its exterior is Schwarzschild by spherical vacuum symmetry. We describe the model's structure without deriving the matching conditions.

As collapse proceeds, trapped spheres can form: both future-directed ingoing and outgoing null expansions are negative. The resulting event horizon is identified from which rays ultimately escape. Because that definition depends on the whole future, the horizon can extend into the matter before the surface crosses its final Schwarzschild radius.

The collapse spacetime has one physical exterior and a collapsing interior. It does not require the second exterior or past white-hole region of the eternal Kruskal extension. A coordinate extension establishes how the idealized eternal solution continues; a formation model establishes which spacetime the matter actually generates.

## Rotation and Quantum Effects

Astrophysical black holes generally rotate. The stationary vacuum solution for rotation is the Kerr metric. Its **ergoregion** contains points where an observer cannot remain stationary relative to infinity; its boundary differs from the event horizon. Deriving Kerr requires mathematics beyond this spherical chapter.

Quantum field theory on a stationary black-hole background predicts Hawking radiation. For a Schwarzschild black hole,

$$T_H=\frac{\hbar c^3}{8\pi G M k_B}.$$

We state this result without deriving it; classical Einstein equations alone do not produce the quantum radiation. The next chapter, [The Einstein Field Equations](einstein-equations.md), derives the dynamics underlying these geometries. [Cosmology](cosmology.md) develops the homogeneous fluid metrics used in expansion and idealized collapse models.

For horizon extensions and black-hole causal structure, see [Tong, Black holes](https://davidtong.org/teaching/general-relativity/grhtml/S6).
