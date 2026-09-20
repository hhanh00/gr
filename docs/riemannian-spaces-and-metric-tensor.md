# Riemannian Spaces and the Metric Tensor

Coordinates identify an event but do not state how far apart two nearby events are or how much time a moving clock records. A metric supplies that measurement rule. In general relativity it also determines which directions light can follow.

## Riemannian and Lorentzian Geometry

A smooth manifold supplies local coordinates; a metric supplies measurements. A **Riemannian space** has a positive-definite metric, so every nonzero tangent vector has positive squared length. On a spatial surface, a path's length is

$$\ell=\int\sqrt{g_{ab}\frac{dx^a}{d\lambda}\frac{dx^b}{d\lambda}}\,d\lambda.$$

Here $a,b$ label the surface's coordinates. A round sphere of radius $R_0$ has $d\ell^2=R_0^2(d\theta^2+\sin^2\theta\,d\phi^2)$. A meridian from pole to equator therefore has length $\pi R_0/2$. These measurements are intrinsic; an embedding picture is optional.

Spacetime instead uses Lorentzian geometry, where timelike, null, and spacelike vectors have different signs of squared norm. We use the same tensor methods, but spatial-distance intuition does not apply to every spacetime interval. [Manifolds](manifolds.md) provides additional background on charts and tangent spaces.

## The Line Element

A **metric** is a symmetric, nondegenerate bilinear form on each tangent space. Its components give

$$ds^2=g_{\mu\nu}(x)dx^\mu dx^\nu.$$

Bilinear means linear in each of its two vector arguments. Nondegenerate means that the matrix has an inverse. A spacetime metric has **Lorentzian signature** $(+,-,-,-)$: one positive and three negative directions in a diagonal basis.

The components depend on coordinates, while $ds^2$ does not. A term written as $2g_{0r}c\,dt\,dr$ represents both symmetric off-diagonal contributions. Reading the coefficient of the cross term as $g_{0r}$ would introduce a factor-of-two error.

## Coordinates Can Change the Components

Flat spacetime in spherical spatial coordinates has

$$ds^2=c^2dt^2-dr^2-r^2d\theta^2-r^2\sin^2\theta\,d\phi^2.$$

Some components vary with position, but the spacetime remains flat. Position dependence alone does not demonstrate curvature.

<details>
<summary>Obtaining the angular factors</summary>

Write $x=r\sin\theta\cos\phi$, $y=r\sin\theta\sin\phi$, and $z=r\cos\theta$. Differentiate and substitute into $dx^2+dy^2+dz^2$. The mixed terms cancel, leaving

$$d\ell^2=dr^2+r^2d\theta^2+r^2\sin^2\theta\,d\phi^2.$$

Insert this into $ds^2=c^2dt^2-d\ell^2$. The factors of $r$ convert angular changes into physical lengths.

</details>

## Clock Readings and Light Cones

Along a timelike curve,

$$\tau=\frac1c\int\sqrt{g_{\mu\nu}\frac{dx^\mu}{d\lambda}\frac{dx^\nu}{d\lambda}}\,d\lambda.$$

This integral gives a clock reading independent of the curve's parameter or coordinates. For a static diagonal metric and a clock at fixed spatial coordinates, $d\tau=\sqrt{g_{00}}\,dt$, where $g_{00}>0$ in that region. Such a clock may require support to remain stationary.

Null directions satisfy $g_{\mu\nu}dx^\mu dx^\nu=0$. For a radial metric $ds^2=A(r)c^2dt^2-B(r)dr^2$, a light ray has coordinate speed $dr/dt=\pm c\sqrt{A/B}$. A nearby observer using local rulers and clocks still measures $c$. Coordinate speed is not a local measurement.

## Local Inertial Coordinates

Near any regular event, suitable coordinates give

$$g_{\mu\nu}(p)=\eta_{\mu\nu},\qquad \partial_\alpha g_{\mu\nu}(p)=0.$$

These are **local inertial coordinates** for the metric's Levi-Civita connection. They reproduce special relativity at the event and remove first-derivative gravitational effects there. Curvature generally remains in second derivatives, so the same construction cannot make an extended curved region Minkowskian.

An orthonormal frame is a basis that gives the Minkowski inner products at a point. Such a basis need not arise from one coordinate chart over a region. We will distinguish local measurements in these frames from coordinate components.

## Volume and Geometry

Coordinate boxes also require a geometric volume factor. With $g=\det(g_{\mu\nu})$, the invariant four-volume is

$$dV_4=\sqrt{-g}\,d^4x.$$

The minus sign reflects our Lorentzian signature in four dimensions. In flat spherical coordinates, $\sqrt{-g}=r^2\sin\theta$ with $x^0=ct$. Integrating only $d^4x$ would omit the spherical-coordinate volume factor.

The metric now supplies inner products, clock readings, null directions, and volume. [Connections and curvature](curvature.md) uses its derivatives to compare vectors at different events and measure tidal geometry.
