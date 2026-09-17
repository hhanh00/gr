# The Equivalence Principle

Drop different test bodies in the same gravitational field and, after accounting for nongravitational forces, they follow the same trajectory from the same initial conditions. This universality makes a geometric description possible: the path can depend on spacetime and initial velocity rather than on the body's composition.

## 1. Newtonian Gravity and Free Fall

For a spherical source of mass $M$, Newton's gravitational force on a test body is

$$\mathbf F=-\frac{GMm_g}{r^2}\hat{\mathbf r}.$$

The Newtonian potential is $\Phi=-GM/r$, and gravitational acceleration is $\mathbf g=-\nabla\Phi$. For a general mass density $\rho$, Poisson's equation $\nabla^2\Phi=4\pi G\rho$ determines the potential with suitable boundary conditions.

Newtonian gravity treats this field as a force acting in space with a shared absolute time. We will retain its successful slow-motion predictions while replacing that spacetime description.


Newtonian mechanics distinguishes inertial mass $m_i$, the resistance to acceleration, from gravitational mass $m_g$, the coupling to a gravitational field:

$$m_i\mathbf a=m_g\mathbf g.$$

If $m_g/m_i$ is the same for all test bodies, they share the same acceleration. The **weak equivalence principle** states this universality for freely falling test bodies. A test body is small enough that its own gravity and finite-size effects can be neglected.

This principle does not assert that every extended object follows exactly the same motion. Spin, tidal deformation, and self-gravity require more detailed equations.

## 2. A Falling Laboratory

A freely falling laboratory and an unsupported object inside it have nearly the same gravitational acceleration. The object therefore floats relative to the laboratory. An accelerometer carried by the lab reads zero.

For an approximately uniform gravitational acceleration, write a body's position as $\mathbf x=\mathbf X(t)+\boldsymbol\xi$, where $\mathbf X$ is the laboratory's position and $\boldsymbol\xi$ is position relative to it. Then

$$\ddot{\boldsymbol\xi}=\mathbf g-\ddot{\mathbf X}.$$

If the laboratory falls with $\ddot{\mathbf X}=\mathbf g$, the relative acceleration vanishes. If it accelerates with $\mathbf a$ in a gravity-free region, the body has relative acceleration $-\mathbf a$. This is the Newtonian form of the local gravity–acceleration correspondence.

A laboratory supported on the ground behaves differently. The floor exerts a force, and an accelerometer records nonzero proper acceleration. Inside a sufficiently small region, this resembles a rocket accelerating through gravity-free spacetime.

The **Einstein equivalence principle** extends universal free fall: local nongravitational experiments in a freely falling laboratory have the special-relativistic form, independent of the laboratory's location and velocity. This motivates describing matter with a locally Minkowskian metric. It does not uniquely determine the Einstein field equations; alternative metric theories can also satisfy it.

## 3. The Limits of a Local Description

A freely falling coordinate system can remove the connection at one event. It cannot generally remove curvature over a finite region.

Two particles dropped at slightly different positions above a spherical body move toward its center. Their separation changes even though both fall freely. This **tidal effect** depends on the variation of the gravitational field, and in general relativity on the Riemann tensor.

The useful laboratory must be small in space and short in duration compared with the scales over which these effects become measurable. “Local” expresses this physical restriction; it does not imply that gravity disappears throughout an extended elevator.

## 4. Clock Rates in a Weak Field

An accelerating laboratory also connects free-fall physics with clock measurements. A light pulse sent upward toward a receiver a height $h$ above the emitter reaches it after roughly $h/c$. During that interval, a lab accelerating upward at $g$ changes velocity by $gh/c$.

The receiver therefore measures a first-order Doppler redshift of approximately $gh/c^2$. By local equivalence, stationary clocks and light signals in a weak gravitational field exhibit the corresponding effect.

With Newtonian potential $\Phi$, the weak static metric has

$$g_{00}\simeq1+\frac{2\Phi}{c^2},\qquad d\tau\simeq\left(1+\frac{\Phi}{c^2}\right)dt.$$

A supported clock higher in the potential records more proper time per unit of this coordinate time. For emission at $\Phi_e$ and reception at $\Phi_o$, stationary observers find

$$\frac{\nu_o-\nu_e}{\nu_e}\simeq\frac{\Phi_e-\Phi_o}{c^2}.$$

<details>
<summary>Expanding the clock-rate factor</summary>

For a stationary clock, $ds^2=g_{00}c^2dt^2=c^2d\tau^2$. Hence $d\tau/dt=\sqrt{1+2\Phi/c^2}$. Apply $\sqrt{1+\epsilon}=1+\epsilon/2+O(\epsilon^2)$ with $|\Phi|/c^2\ll1$.

</details>

The equivalence principle establishes how local free fall and clock measurements fit a metric description. [Tensors and Tensor Fields](tensors-and-tensor-fields.md) develops coordinate-independent notation. Chapter 9 later adds the dynamical law relating the metric to matter and energy.
