# Curves and Motion

A particle's trajectory is a sequence of events, not just a line through space. Describing it as a spacetime curve keeps the clock carried by the particle in the calculation. We can then separate a coordinate acceleration from an acceleration that an instrument actually measures.

## 1. Parameterizing a Worldline

A **worldline** is a particle's path through spacetime:

$$\gamma:\lambda\mapsto x^\mu(\lambda).$$

The parameter $\lambda$ orders points along the curve. Replacing it by a smooth monotonic parameter changes the tangent's magnitude, but leaves the path unchanged.

For a massive particle, use proper time $\tau$. The **four-velocity** is

$$u^\mu=\frac{dx^\mu}{d\tau},\qquad g_{\mu\nu}u^\mu u^\nu=c^2.$$

In an inertial Minkowski frame, $u^\mu=\gamma(c,\mathbf v)$. Its time component accounts for the difference between coordinate time and the particle's clock reading.

## 2. Acceleration and Forces

In flat Cartesian coordinates, define four-acceleration $a^\mu=du^\mu/d\tau$. Differentiate the normalization:

$$0=\frac{d}{d\tau}(u^\mu u_\mu)=2u_\mu a^\mu.$$

Four-acceleration is orthogonal to four-velocity. In the instantaneous rest frame, $u^\mu=(c,0,0,0)$, so $a^0=0$. The spatial components describe the acceleration recorded by an accelerometer.

For constant rest mass $m$, the four-momentum is $p^\mu=mu^\mu$, and four-force is $f^\mu=dp^\mu/d\tau$. A force-free particle has $a^\mu=0$ in these coordinates.

In curved spacetime or curvilinear coordinates, replace the ordinary derivative with a covariant derivative:

$$a^\mu=\frac{Du^\mu}{d\tau}=\frac{du^\mu}{d\tau}+\Gamma^\mu{}_{\alpha\beta}u^\alpha u^\beta.$$

The connection coefficients $\Gamma^\mu{}_{\alpha\beta}$ correct for changes in the basis. We derive them in [Connections and curvature](curvature.md).

## 3. Coordinate Acceleration in Flat Space

Even a straight trajectory can have changing coordinate velocity. On a Euclidean plane, a free particle's polar-coordinate equations are

$$\ddot r-r\dot\phi^2=0,\qquad \ddot\phi+\frac{2}{r}\dot r\dot\phi=0.$$

Dots here mean derivatives with respect to ordinary time. The nonzero second derivatives do not establish that a force acts on the particle.

<details>
<summary>Recovering the polar equations</summary>

Use the kinetic Lagrangian $L=\tfrac12m(\dot r^2+r^2\dot\phi^2)$. Its Euler–Lagrange equation for $r$ gives $m\ddot r-mr\dot\phi^2=0$. For $\phi$, it gives

$$\frac{d}{dt}(mr^2\dot\phi)=0\quad\Rightarrow\quad r^2\ddot\phi+2r\dot r\dot\phi=0.$$

These equations describe straight Cartesian motion expressed with a changing polar basis.

</details>

## 4. Light and Null Parameters

Light follows a **null curve**, with $g_{\mu\nu}dx^\mu dx^\nu=0$. Its proper-time increment vanishes, so proper time cannot parameterize its motion.

Instead choose an **affine parameter** $\lambda$, a parameter for which a freely propagating ray obeys

$$\frac{d^2x^\mu}{d\lambda^2}+\Gamma^\mu{}_{\alpha\beta}\frac{dx^\alpha}{d\lambda}\frac{dx^\beta}{d\lambda}=0.$$

Affine parameters remain affine under $\lambda\to A\lambda+B$ with constant $A\ne0$. An arbitrary reparameterization generally adds a term proportional to the tangent on the right-hand side. Affine therefore describes the parameter choice, not a particular shape of path.

## 5. Measurements Along a Curve

For a photon with four-momentum $p^\mu$, an observer with four-velocity $u^\mu$ measures energy $E=p_\mu u^\mu$ in our $(+,-,-,-)$ convention. Different observers can measure different energies for the same photon. This includes ordinary Doppler shifts and, later, gravitational redshift.

To calculate any of these quantities in curved spacetime, we need both a curve and a geometry. [Manifolds](manifolds.md) supplies the space of events; [Metrics](riemannian-spaces-and-metric-tensor.md) supplies the measurement rule.
