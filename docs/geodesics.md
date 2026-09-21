# Geodesics

A freely falling particle follows the spacetime version of a straight line: its tangent stays parallel to itself as it moves. This definition works in both flat and curved spacetime. It also explains why a particle can accelerate in some coordinates while an accelerometer travelling with it reads zero.

We use signature $(+,-,-,-)$ and the metric-compatible, torsion-free **Levi-Civita connection**. In inertial coordinates, $x^0=ct$.

## Parallel Transport

Vectors at different points belong to different tangent spaces. To compare them along a curve $x^\mu(\lambda)$, we need a rule for carrying a vector from one tangent space to the next. The connection supplies this rule.

Let $v^\mu=dx^\mu/d\lambda$ be the curve's tangent and $V^\mu(\lambda)$ a vector along it. Its covariant derivative along the curve is

$$\frac{DV^\mu}{d\lambda}=v^\nu\nabla_\nu V^\mu=\frac{dV^\mu}{d\lambda}+\Gamma^\mu{}_{\alpha\beta}v^\alpha V^\beta.$$

The vector is **parallel transported** when

$$\frac{DV^\mu}{d\lambda}=0.$$

Its coordinate components need not be constant: the connection term accounts for the changing coordinate basis. Given an initial vector and a specified path, this equation determines the transported vector along the path.

Metric compatibility, $\nabla_\alpha g_{\mu\nu}=0$, means parallel transport preserves inner products. If $V$ and $W$ are both parallel transported, then

$$\frac{d}{d\lambda}g(V,W)=g\left(\frac{DV}{d\lambda},W\right)+g\left(V,\frac{DW}{d\lambda}\right)=0.$$

In curved geometry the result can depend on the path. Carrying a vector around a small closed loop can change its direction; curvature measures this failure to return unchanged. See [Tong, parallel transport](https://www.davidtong.org/teaching/general-relativity/grhtml/S3#S3.SS3) for the covariant formulation.

## Tangent Vectors and Geodesics

A **geodesic** parallel transports its own tangent. With an affine parameter $\lambda$, its defining equation is

$$\nabla_vv=0,$$

or, in coordinates,

$$\boxed{\frac{d^2x^\mu}{d\lambda^2}+\Gamma^\mu{}_{\alpha\beta}\frac{dx^\alpha}{d\lambda}\frac{dx^\beta}{d\lambda}=0.}$$

This is a second-order equation: an initial event and initial tangent determine a local solution. Because the tangent is parallel transported, $g(v,v)$ is constant. A geodesic therefore retains its timelike, null, or spacelike character.

For a massive particle, proper time $\tau$ is an affine parameter. Its tangent is the four-velocity $u^\mu=dx^\mu/d\tau$, with $g(u,u)=c^2$, and its four-acceleration is

$$a^\mu=\frac{Du^\mu}{d\tau}.$$

Free fall means $a^\mu=0$. This does not require $d^2x^\mu/d\tau^2=0$: coordinate acceleration can be cancelled by the connection term.

For light, $g(v,v)=0$ and proper time cannot parameterize the path. Use another affine parameter. Affine parameters can be rescaled and shifted, $\lambda\mapsto A\lambda+B$, with constant $A\ne0$. A general parameter $s$ instead gives

$$\frac{d^2x^\mu}{ds^2}+\Gamma^\mu{}_{\alpha\beta}\frac{dx^\alpha}{ds}\frac{dx^\beta}{ds}=f(s)\frac{dx^\mu}{ds},$$

where the tangent term reflects the parameter choice, not a force.

## Minkowski Space

In inertial Cartesian coordinates $(ct,x,y,z)$, the metric is

$$ds^2=c^2dt^2-dx^2-dy^2-dz^2.$$

All connection coefficients vanish, so affine geodesics are straight coordinate lines:

$$x^\mu(\lambda)=b^\mu+v^\mu\lambda.$$

A massive free particle has constant ordinary velocity; a light ray travels at $c$. Flatness, however, does not require the metric components to be constant in every coordinate system.

To see this, introduce **hyperbolic coordinates** in the right wedge $x>|ct|$:

$$ct=\rho\sinh\eta,\qquad x=\rho\cosh\eta,\qquad \rho>0.$$

Here $\rho$ is a length and $\eta$ is dimensionless. Curves with fixed $\rho$ satisfy $x^2-c^2t^2=\rho^2$, so they are hyperbolas in a spacetime diagram. Substitution gives

$$c^2dt^2-dx^2=\rho^2d\eta^2-d\rho^2,$$

and hence

$$ds^2=\rho^2d\eta^2-d\rho^2-dy^2-dz^2.$$

These are Rindler coordinates. The nonzero connection coefficients are

$$\Gamma^\rho{}_{\eta\eta}=\rho,\qquad \Gamma^\eta{}_{\rho\eta}=\Gamma^\eta{}_{\eta\rho}=\frac1\rho.$$

The spacetime is still flat: its Riemann tensor vanishes. Nonzero connection coefficients alone do not establish curvature.

## Uniform Acceleration

Relativistic **uniform acceleration** means constant proper acceleration: the magnitude measured by an accelerometer. For motion along one spatial direction, introduce rapidity $\chi$ through

$$u^\mu=(c\cosh\chi,c\sinh\chi,0,0),\qquad v=c\tanh\chi.$$

Differentiating with respect to proper time gives

$$\alpha=\sqrt{-a_\mu a^\mu}=c\left|\frac{d\chi}{d\tau}\right|.$$

For constant acceleration $\alpha>0$ toward increasing $x$, choose $\chi=\alpha\tau/c$. Integrating the four-velocity, with the particle initially at rest at $x=c^2/\alpha$, gives

$$ct=\frac{c^2}{\alpha}\sinh\left(\frac{\alpha\tau}{c}\right),\qquad x=\frac{c^2}{\alpha}\cosh\left(\frac{\alpha\tau}{c}\right).$$

Thus a fixed-$\rho$ Rindler observer has proper acceleration $\alpha=c^2/\rho$ and proper time $d\tau=\rho\,d\eta/c$. These hyperbolas are accelerated worldlines, not geodesics.

The inertial-frame velocity and acceleration are

$$v(t)=\frac{\alpha t}{\sqrt{1+(\alpha t/c)^2}},\qquad \frac{dv}{dt}=\frac{\alpha}{[1+(\alpha t/c)^2]^{3/2}}.$$

Although the accelerometer reading stays constant, coordinate acceleration decreases and the speed approaches $c$ without reaching it. The null boundaries $x=\pm ct$ delimit the Rindler wedge; the coordinate chart does not cover all of Minkowski spacetime.

## Uniform Gravitational Field

To describe an accelerating laboratory, choose a reference acceleration $g>0$ and define

$$\rho=\frac{c^2}{g}+z,\qquad \eta=\frac{gT}{c}.$$

Here $z$ replaces the longitudinal coordinate $\rho$; call the two transverse coordinates $X,Y$. The metric becomes

$$\boxed{ds^2=N(z)^2c^2dT^2-dz^2-dX^2-dY^2,\qquad N(z)=1+\frac{gz}{c^2}>0.}$$

The reference observer at $z=0$ has proper acceleration $g$, and $T$ is that observer's proper time. For another observer fixed in the laboratory,

$$d\tau=N(z)dT,\qquad \alpha(z)=\frac{g}{N(z)}.$$

Clocks higher in the laboratory accumulate more proper time per unit $T$. Observers at different heights require different proper accelerations to maintain fixed proper separations. An extended rigid accelerating laboratory therefore cannot have the same proper acceleration everywhere.

Near $z=0$, where $|gz|/c^2\ll1$, the metric reads

$$ds^2\simeq\left(1+\frac{2gz}{c^2}\right)c^2dT^2-dz^2-dX^2-dY^2.$$

Comparing with $g_{00}\simeq1+2\Phi/c^2$ identifies the Newtonian potential $\Phi=gz$ and downward acceleration $-g$. This is the sense in which the laboratory simulates a uniform gravitational field.

The exact Rindler metric remains flat. It describes the apparent field of accelerated observers, while a real gravitating body generally also produces tidal curvature. The [equivalence principle](equivalence-principle.md) relates the two descriptions locally; it does not remove those tidal effects over an extended region.

## Motion of a Particle

For a massive test particle subject to a nongravitational four-force $f^\mu$, constant rest mass $m$ gives

$$m\left(\frac{d^2x^\mu}{d\tau^2}+\Gamma^\mu{}_{\alpha\beta}\frac{dx^\alpha}{d\tau}\frac{dx^\beta}{d\tau}\right)=f^\mu.$$

Setting $f^\mu=0$ gives free fall. Holding a particle at a fixed position in the accelerating laboratory instead requires a force: it follows one of the accelerated hyperbolas above.

For vertical free fall in the Rindler metric, use coordinates $(T,z)$ and let dots denote $d/d\tau$. The relevant connection coefficients are

$$\Gamma^z{}_{TT}=gN,\qquad \Gamma^T{}_{Tz}=\Gamma^T{}_{zT}=\frac{g}{c^2N}.$$

The geodesic equations and four-velocity normalization become

$$\ddot z+gN\dot T^2=0,\qquad \ddot T+\frac{2g}{c^2N}\dot T\dot z=0,$$

$$N^2c^2\dot T^2-\dot z^2=c^2.$$

The time equation integrates to $N^2\dot T=\mathcal E$, a constant associated with time-translation symmetry. Substituting it into the normalization gives a first-order equation:

$$\dot z^2=c^2\left(\frac{\mathcal E^2}{N^2}-1\right).$$

A particle released from rest at $z=z_0$ has $\mathcal E=N(z_0)$. It begins to move downward in laboratory coordinates even though its proper acceleration is zero.

<details>
<summary>An exact falling trajectory</summary>

Write the inertial longitudinal coordinate as $x$. The coordinate transformation is

$$ct=\left(\frac{c^2}{g}+z\right)\sinh\frac{gT}{c},\qquad x=\left(\frac{c^2}{g}+z\right)\cosh\frac{gT}{c}.$$

At $T=0$, the laboratory observers are instantaneously at rest in the inertial frame. A particle released then at $z_0$ remains at constant inertial position $x=c^2/g+z_0$. Its laboratory trajectory is therefore

$$z(T)=\left(\frac{c^2}{g}+z_0\right)\operatorname{sech}\frac{gT}{c}-\frac{c^2}{g}.$$

For release at $z_0=0$ and $|gT|/c\ll1$, expansion gives $z(T)\simeq-\tfrac12gT^2$. Ordinary free fall emerges from a straight inertial worldline viewed by an accelerating laboratory.

</details>

The same method applies when curvature is present: determine the metric, compute its connection, and solve the geodesic equation with the appropriate initial conditions. [Metric for a Gravitational Field](metric-for-a-gravitational-field.md) develops the weak-field and Schwarzschild geometries used for those calculations.
