# Curvature

Two nearby falling particles can accelerate toward one another even though each accelerometer reads zero. To describe this relative motion, we need a derivative that compares vectors at neighboring points and a measure of the failure of that comparison to agree around a loop.

## 1. Covariant Differentiation

Ordinary differentiation changes vector components without correcting for a changing basis. A **connection** specifies that correction. For a vector and a covector,

$$\nabla_\mu V^\nu=\partial_\mu V^\nu+\Gamma^\nu{}_{\mu\rho}V^\rho,$$

$$\nabla_\mu\omega_\nu=\partial_\mu\omega_\nu-\Gamma^\rho{}_{\mu\nu}\omega_\rho.$$

The signs ensure that differentiation of a contraction follows the product rule. Each upper tensor index gets a plus correction, and each lower index gets a minus correction. For a scalar, $\nabla_\mu f=\partial_\mu f$.

The coefficients $\Gamma^\rho{}_{\mu\nu}$, often called **Christoffel symbols** for the metric connection, do not form a tensor. Their coordinate transformation includes the extra terms needed to make $\nabla_\mu V^\nu$ a tensor.

## 2. The Metric Connection

General relativity normally uses the **Levi-Civita connection**, which preserves the metric, $\nabla_\rho g_{\mu\nu}=0$, and has zero torsion, $\Gamma^\rho{}_{\mu\nu}=\Gamma^\rho{}_{\nu\mu}$ in a coordinate basis. These conditions determine

$$\Gamma^\rho{}_{\mu\nu}=\frac12g^{\rho\sigma}(\partial_\mu g_{\sigma\nu}+\partial_\nu g_{\sigma\mu}-\partial_\sigma g_{\mu\nu}).$$

<details>
<summary>Deriving the Christoffel formula</summary>

Metric compatibility gives

$$\partial_\mu g_{\nu\sigma}=\Gamma^\rho{}_{\mu\nu}g_{\rho\sigma}+\Gamma^\rho{}_{\mu\sigma}g_{\nu\rho}.$$

Add the equations with derivatives $\partial_\mu g_{\nu\sigma}$ and $\partial_\nu g_{\mu\sigma}$, then subtract the equation with $\partial_\sigma g_{\mu\nu}$. Symmetry in the two lower connection indices cancels four terms, leaving $2g_{\sigma\rho}\Gamma^\rho{}_{\mu\nu}$. Multiply by $g^{\lambda\sigma}/2$.

</details>

## 3. Parallel Transport

**Parallel transport** along $x^\mu(\lambda)$ keeps a vector covariantly constant:

$$\frac{DV^\mu}{d\lambda}=\frac{dV^\mu}{d\lambda}+\Gamma^\mu{}_{\alpha\beta}\frac{dx^\alpha}{d\lambda}V^\beta=0.$$

Metric compatibility preserves its inner products during transport. On a curved space, transporting along different routes can give different final vectors. This depends on the connection, rather than on how a drawing sits in an external space.

As a useful check, the flat polar-plane metric has $\Gamma^r{}_{\phi\phi}=-r$ and $\Gamma^\phi{}_{r\phi}=1/r$. The coefficients are nonzero, but its curvature vanishes. We therefore cannot identify gravity or curvature with the mere presence of Christoffel symbols.

## 4. The Riemann Tensor

Define curvature by the derivative commutator:

$$[\nabla_\mu,\nabla_\nu]V^\rho=R^\rho{}_{\sigma\mu\nu}V^\sigma.$$

Our convention is

$$R^\rho{}_{\sigma\mu\nu}=\partial_\mu\Gamma^\rho{}_{\nu\sigma}-\partial_\nu\Gamma^\rho{}_{\mu\sigma}+\Gamma^\rho{}_{\mu\lambda}\Gamma^\lambda{}_{\nu\sigma}-\Gamma^\rho{}_{\nu\lambda}\Gamma^\lambda{}_{\mu\sigma}.$$

The **Riemann tensor** measures infinitesimal path dependence. Its contractions are the Ricci tensor $R_{\mu\nu}=R^\rho{}_{\mu\rho\nu}$ and Ricci scalar $R=g^{\mu\nu}R_{\mu\nu}$. A zero Ricci tensor does not imply zero Riemann tensor; vacuum can contain tidal gravity and gravitational waves.

<details>
<summary>Computing curvature on a sphere and a flat plane</summary>

For the positive-definite sphere metric $g_{\theta\theta}=R_0^2$ and $g_{\phi\phi}=R_0^2\sin^2\theta$, the nonzero connection coefficients are

$$\Gamma^\theta{}_{\phi\phi}=-\sin\theta\cos\theta,\qquad \Gamma^\phi{}_{\theta\phi}=\Gamma^\phi{}_{\phi\theta}=\cot\theta.$$

Our Riemann formula gives

$$R^\theta{}_{\phi\theta\phi}=\partial_\theta(-\sin\theta\cos\theta)-\Gamma^\theta{}_{\phi\phi}\Gamma^\phi{}_{\theta\phi}=\sin^2\theta.$$

Thus $R_{\phi\phi}=\sin^2\theta$ and $R_{\theta\theta}=1$. Contracting gives the sphere's scalar curvature $R=2/R_0^2$. Its Gaussian curvature is $K=R/2=1/R_0^2$.

For the flat polar plane, the same component is

$$R^r{}_{\phi r\phi}=\partial_r(-r)-\Gamma^r{}_{\phi\phi}\Gamma^\phi{}_{r\phi}=-1-(-r)(1/r)=0.$$

The derivative and connection-product terms cancel. This calculation distinguishes intrinsic curvature from coordinate-dependent connection coefficients.

</details>

For neighboring geodesics with separation $\xi^\mu$ and tangent $u^\mu$, our convention gives

$$\frac{D^2\xi^\mu}{d\tau^2}=-R^\mu{}_{\alpha\nu\beta}u^\alpha\xi^\nu u^\beta.$$

This **geodesic-deviation equation** describes relative free-fall acceleration. We supply it without the full two-parameter-curve derivation here; the important distinction is between zero acceleration along each geodesic and nonzero acceleration between them.

[Geodesics](geodesics.md) uses this connection to derive free-fall paths. For the geometry calculation in a different signature convention, see [Tong, Riemannian geometry](https://davidtong.org/teaching/general-relativity/grhtml/S3).
