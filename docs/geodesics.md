# Geodesics

An unsupported particle follows a path with zero proper acceleration. Its coordinate position can still accelerate near a gravitating body. A geodesic expresses this motion through the connection, so that the same free-fall law holds in every coordinate system.

## Parallel Transport of the Tangent

A **geodesic** transports its own tangent parallel to itself. With an affine parameter $\lambda$,

$$\frac{D\dot x^\mu}{d\lambda}=0\quad\Rightarrow\quad\ddot x^\mu+\Gamma^\mu{}_{\alpha\beta}\dot x^\alpha\dot x^\beta=0.$$

Dots in this chapter mean $d/d\lambda$. For a timelike geodesic, proper time is affine. For a null geodesic, use another affine parameter and impose $g_{\mu\nu}\dot x^\mu\dot x^\nu=0$.

An accelerometer records the covariant acceleration. Thus a freely falling satellite has zero proper acceleration even while its coordinates describe an orbit. A supported observer at fixed radius generally has nonzero proper acceleration.

## A Variational Derivation

For a massive particle, the physical action is $S=-mc^2\int d\tau$. Its extremals are timelike geodesics. For an affine parameter, a convenient equivalent way to derive their paths uses

$$L=\frac12g_{\mu\nu}\dot x^\mu\dot x^\nu.$$

This quadratic Lagrangian also yields null geodesics when we separately impose the null constraint. It is not the proper-time action of a photon, since that action would vanish.

<details>
<summary>Deriving the coordinate equation</summary>

The Euler–Lagrange equation for $x^\rho$ gives

$$\frac{d}{d\lambda}(g_{\rho\nu}\dot x^\nu)-\frac12\partial_\rho g_{\alpha\beta}\dot x^\alpha\dot x^\beta=0.$$

Expand the derivative:

$$g_{\rho\nu}\ddot x^\nu+\partial_\alpha g_{\rho\beta}\dot x^\alpha\dot x^\beta-\frac12\partial_\rho g_{\alpha\beta}\dot x^\alpha\dot x^\beta=0.$$

Symmetrize the middle coefficient in $\alpha,\beta$, because the velocity product is symmetric. Multiplication by the inverse metric produces the Christoffel formula and hence the geodesic equation.

</details>

A timelike geodesic locally maximizes proper time between sufficiently nearby fixed endpoints. We should not extend that statement to arbitrary distant endpoints, where conjugate points and multiple geodesics can occur.

## Conserved Quantities from Symmetry

If the metric does not depend on one coordinate, that coordinate is **cyclic** in $L$. Its conjugate momentum is constant:

$$p_\rho=\frac{\partial L}{\partial\dot x^\rho}=g_{\rho\nu}\dot x^\nu.$$

Time-translation symmetry gives an energy-like constant; rotational symmetry gives angular momentum. These quantities reduce second-order trajectory equations to first-order equations.

More generally a **Killing vector** $K^\mu$ generates a continuous metric-preserving symmetry and obeys $\nabla_\mu K_\nu+\nabla_\nu K_\mu=0$. Then $K_\mu\dot x^\mu$ is constant along an affine geodesic. Its derivative contracts the antisymmetric part of $\nabla K$ with the symmetric tangent product, giving zero.

## The Newtonian Limit

For a weak static field, $g_{00}\simeq1+2\Phi/c^2$ and $g_{ij}\simeq-\delta_{ij}$. Then

$$\Gamma^i{}_{00}\simeq\frac{\partial_i\Phi}{c^2}.$$

For slow motion, $dx^0/d\tau\simeq c$ and $d\tau\simeq dt$. The spatial geodesic equation becomes

$$\frac{d^2x^i}{dt^2}\simeq-\partial_i\Phi.$$

The familiar gravitational acceleration is therefore the slow-motion coordinate description of zero covariant acceleration.

Geodesics describe test bodies and light when nongravitational forces, self-force, and finite-size effects are negligible. They do not describe every possible trajectory. [Metric for a Gravitational Field](metric-for-a-gravitational-field.md) now constructs metrics in which we can calculate these paths.
