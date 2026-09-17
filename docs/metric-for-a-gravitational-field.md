# Metric for a Gravitational Field

A gravitational field changes the relation between coordinates and clock or ruler readings. To construct its metric, first recover the Newtonian limit, then use symmetry to reduce the unknown components. This chapter develops the weak static field and the exact spherical vacuum field. Chapter 9 will derive the field equations used in the exact calculation.

## 1. The Relativistic Interval

With $x^0=ct$ and signature $(+,-,-,-)$, write

$$ds^2=g_{00}c^2dt^2+2g_{0i}c\,dt\,dx^i+g_{ij}dx^idx^j.$$

Spatial indices $i,j$ run from 1 to 3. Off-diagonal time–space terms can occur in rotating or moving-source geometries. A static field admits coordinates with no such terms and no time dependence.

For a massive particle, $ds^2=c^2d\tau^2$; for a light ray, $ds^2=0$. The same metric determines both trajectories and measurements, but a source model is still necessary to determine its components.

## 2. Recovering the Newtonian Potential

For a weak static field and slow particle motion, the spatial geodesic equation gives

$$\frac{d^2x^i}{dt^2}\simeq-c^2\Gamma^i{}_{00}\simeq-\frac{c^2}{2}\partial_i g_{00}.$$

Compare this with $d^2x^i/dt^2=-\partial_i\Phi$. Normalize time so that $g_{00}\to1$ where the potential tends to zero. Then

$$g_{00}\simeq1+\frac{2\Phi}{c^2}.$$

This determines the leading time component from Newtonian motion. It does not determine every spatial component. Light bending and other relativistic effects require the remaining field equations.

For a stationary clock, $d\tau=\sqrt{g_{00}}dt$. Thus clocks at different gravitational potentials accumulate different proper times relative to this common static time coordinate.

## 3. The Weak Static Metric

For a weak isolated source with negligible pressure and anisotropic stress, solving the linearized Einstein equations in isotropic spatial coordinates gives

$$ds^2\simeq\left(1+\frac{2\Phi}{c^2}\right)c^2dt^2-\left(1-\frac{2\Phi}{c^2}\right)(dx^2+dy^2+dz^2).$$

We supply the spatial coefficient from the linearized equations here; Chapters 9 and 10 develop their dynamical origin. Terms of order $(\Phi/c^2)^2$ are omitted. For a spherical source, $\Phi=-GM/r$ at leading order outside the matter.

A radial null ray has coordinate speed approximately $c(1+2\Phi/c^2)$. For negative $\Phi$, this is smaller than $c$ in these coordinates. Dividing local proper distance by local clock time still gives $c$.

## 4. Exact Spherical Vacuum Geometry

Spherical symmetry and staticity give the ansatz

$$ds^2=A(r)c^2dt^2-B(r)dr^2-r^2d\Omega^2.$$

Choose $r$ as areal radius. Outside the source, with $\Lambda=0$, the equations introduced fully in [The Einstein Field Equations](einstein-equations.md) reduce to $R_{\mu\nu}=0$.

<details>
<summary>Integrating the spherical vacuum equations</summary>

Substitution of the ansatz into the Ricci tensor gives two independent combinations:

$$\frac{d}{dr}\left[r\left(1-B^{-1}\right)\right]=0,\qquad \frac{A'}A=\frac{B-1}{r}.$$

The first integrates to $B^{-1}=1-C/r$. Insert that in the second to obtain $A'/A=C/[r(r-C)]$. Integration gives $A=A_0(1-C/r)$.

Asymptotic flatness and normalization of $t$ set $A_0=1$. Matching the weak time component to $1-2GM/(rc^2)$ sets $C=r_s=2GM/c^2$. The remaining vacuum equation is then satisfied.

</details>

The result is the Schwarzschild metric:

$$ds^2=\left(1-\frac{r_s}{r}\right)c^2dt^2-\frac{dr^2}{1-r_s/r}-r^2d\Omega^2.$$

It describes a vacuum region, not the material interior of a star. In the absence of rotation, spherical symmetry fixes this exterior even if the interior evolves.

## 5. Coordinate Choice and Approximation

The weak isotropic metric and the Schwarzschild metric use different radial coordinates. To compare their spatial components, introduce isotropic radius $\varrho$ through

$$r=\varrho\left(1+\frac{r_s}{4\varrho}\right)^2.$$

The exact metric becomes

$$ds^2=\left(\frac{1-r_s/(4\varrho)}{1+r_s/(4\varrho)}\right)^2c^2dt^2-\left(1+\frac{r_s}{4\varrho}\right)^4(d\varrho^2+\varrho^2d\Omega^2).$$

Expanding for $r_s/\varrho\ll1$ reproduces the weak isotropic coefficients with $\Phi=-GM/\varrho$. Different coordinate components can therefore describe the same geometry.

[Black Holes (I)](black-holes-i.md) applies the exact metric to clocks, orbits, and horizons. For the spherical vacuum solution, see [Tong, Schwarzschild geometry](https://davidtong.org/teaching/general-relativity/grhtml/S6).
