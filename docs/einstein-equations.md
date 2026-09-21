# The Einstein Field Equations

A metric determines clock readings and free-fall paths, but we still need to calculate which metric a star or a distribution of matter produces. Einstein's equations connect spacetime curvature to the local energy, momentum, and stresses of matter.

## Matter as a Source

The **stress–energy tensor** $T_{\mu\nu}$ describes energy density, momentum density, energy flux, and stress. In a local orthonormal rest frame, $T^{00}=\epsilon$ is energy per volume. Pressure contributes spatial stress, so gravity depends on more than rest mass.

For an isotropic **perfect fluid**, with no viscosity or heat flux,

$$T^{\mu\nu}=(\epsilon+p)\frac{u^\mu u^\nu}{c^2}-p\,g^{\mu\nu}.$$

Here $p$ is pressure and $u^\mu u_\mu=c^2$. In its rest frame the diagonal components are $(\epsilon,p,p,p)$.

## A Curvature Equation

The Einstein tensor is

$$G_{\mu\nu}=R_{\mu\nu}-\frac12g_{\mu\nu}R.$$

Its covariant divergence vanishes by the contracted Bianchi identity. This makes it compatible with the matter equation $\nabla_\mu T^{\mu\nu}=0$.

With our $(+,-,-,-)$ signature and the [curvature convention](spacetime.md) already defined, write the field equations as

$$G_{\mu\nu}-\Lambda g_{\mu\nu}=\frac{8\pi G}{c^4}T_{\mu\nu}.$$

$G$ is Newton's constant. We define positive $\Lambda$ to produce accelerated de Sitter expansion. The minus sign in this convention differs from texts that use $(-,+,+,+)$ with the same definition of the Riemann tensor. Mixing their metric and curvature conventions without changing the equation gives incorrect signs.

These equations are a dynamical model supported by experiment. Covariance and the equivalence principle motivate their structure but do not alone prove that nature must obey them.

## Constructing the Action

An **action** assigns a number to a field configuration; physical configurations make its first variation vanish under the allowed variations. With $x^0=ct$, a compatible action is

$$S=-\frac{c^3}{16\pi G}\int d^4x\sqrt{-g}\,(R+2\Lambda)+S_m.$$

Define matter stress–energy through $\delta S_m=(1/2c)\int\sqrt{-g}\,T_{\mu\nu}\delta g^{\mu\nu}d^4x$. The overall gravitational sign follows our signature and this definition.

<details>
<summary>Varying the metric</summary>

The determinant variation is $\delta\sqrt{-g}=-\tfrac12\sqrt{-g}g_{\mu\nu}\delta g^{\mu\nu}$. The curvature variation gives

$$\delta(\sqrt{-g}R)=\sqrt{-g}G_{\mu\nu}\delta g^{\mu\nu}+\text{boundary terms}.$$

We quote this identity without expanding the variation of every connection coefficient. For compactly supported variations, boundary terms vanish; a variational problem with a physical boundary requires an appropriate boundary term and boundary data.

The cosmological term contributes $-\sqrt{-g}\Lambda g_{\mu\nu}\delta g^{\mu\nu}$. Combining the gravitational and matter variations gives $G_{\mu\nu}-\Lambda g_{\mu\nu}=8\pi G T_{\mu\nu}/c^4$.

</details>

## Recovering Newtonian Gravity

For weak, slowly varying fields and nonrelativistic matter, set $\Lambda=0$ and $g_{00}\simeq1+2\Phi/c^2$. The trace-reversed equation is

$$R_{\mu\nu}=\frac{8\pi G}{c^4}\left(T_{\mu\nu}-\frac12g_{\mu\nu}T\right),\qquad T=g^{\mu\nu}T_{\mu\nu}.$$

Using $R_{00}\simeq\nabla^2\Phi/c^2$ and $T_{00}\simeq T\simeq\rho c^2$ gives $\nabla^2\Phi=4\pi G\rho$. This recovers Poisson's equation and fixes the coupling normalization.

## Conservation and Solutions

$\nabla_\mu T^{\mu\nu}=0$ expresses local energy–momentum balance. It does not generally supply a single conserved total energy for an arbitrary expanding spacetime; global conserved quantities require suitable symmetries and boundary conditions.

Solving the field equations requires a matter model, initial or boundary data, and coordinate choices. In vacuum with $\Lambda=0$, $R_{\mu\nu}=0$, but tidal curvature can remain. The earlier geodesic and black-hole chapters applied this dynamics to test motion and spherical geometry. [Gravitational Waves](gravitational-waves.md) now linearizes the equations to calculate traveling perturbations.

For the action and field equations in the alternative signature, see [Tong, Einstein equations](https://davidtong.org/teaching/general-relativity/grhtml/S4).
