# Black Holes (I)

Outside a spherical body, Newtonian gravity depends only on its total mass. General relativity has a corresponding vacuum geometry. It predicts the familiar weak-field motion and additional effects on clocks, orbits, and light.

## 1. The Exterior Metric

Assume spherical symmetry, vacuum, and $\Lambda=0$. The Schwarzschild line element is

$$ds^2=f(r)c^2dt^2-\frac{dr^2}{f(r)}-r^2(d\theta^2+\sin^2\theta\,d\phi^2),\qquad f(r)=1-\frac{r_s}{r},\quad r_s=\frac{2GM}{c^2}.$$

$r$ is the **areal radius**: symmetry spheres have area $4\pi r^2$. It is not radial proper distance. The coordinate $t$ agrees with proper time for stationary observers at infinity.

Birkhoff's theorem states that any spherically symmetric vacuum region is locally Schwarzschild under these assumptions. We use the theorem without proof. A spherical pulsating star can have a time-independent vacuum exterior; the star's interior still requires a matter solution.

The [preceding chapter](metric-for-a-gravitational-field.md) derived this metric from the spherical vacuum equations and matched its mass parameter to the Newtonian field. We now use that geometry to calculate measurements and motion. For an ordinary star, the exterior formula applies outside its surface; the interior requires a matter solution.

## 2. Static Clocks and Radial Distance

A clock held at fixed $r,\theta,\phi$ outside $r_s$ records

$$d\tau=\sqrt{f(r)}\,dt.$$

Its clock rate relative to infinity decreases as it approaches $r_s$. Holding it stationary requires proper acceleration

$$a=\frac{GM}{r^2\sqrt{f(r)}}.$$

This diverges at the horizon. It describes the force required to hover, not an acceleration experienced by a freely falling observer crossing the horizon.

At fixed Schwarzschild time, radial proper distance is $d\ell=dr/\sqrt{f(r)}$. Clock rate and radial distance both matter when we calculate light propagation.

## 3. Orbits from Conserved Quantities

Choose an equatorial timelike geodesic, $\theta=\pi/2$. Time and rotational symmetries give constants

$$e=f(r)\frac{dt}{d\tau},\qquad \ell=r^2\frac{d\phi}{d\tau}.$$

Here $e$ is energy per unit rest energy, and $\ell$ is angular momentum per unit mass. Using $u^\mu u_\mu=c^2$ gives

$$\left(\frac{dr}{d\tau}\right)^2+f(r)\left(c^2+\frac{\ell^2}{r^2}\right)=e^2c^2.$$

The second term is an **effective potential**, a function used to identify radial turning points and circular orbits. Its expansion contains the Newtonian terms and an additional $-r_s\ell^2/r^3$ contribution. That correction produces orbital precession and changes stability.

For timelike circular geodesics, the innermost stable orbit is $r=3r_s=6GM/c^2$. Null circular geodesics lie at $r=3r_s/2$ and are unstable. These results follow by differentiating the corresponding effective potentials; they are not the horizon radius.

## 4. Horizon and Curvature

If the vacuum geometry extends inward to form a black hole, $r=r_s$ is the **event horizon**, the boundary beyond which future-directed causal signals cannot escape to distant observers. Outside it, stationary worldlines are timelike. At it, the stationary direction becomes null; inside, fixed-radius worldlines cannot describe physical stationary observers.

For a star whose surface lies outside $r_s$, this radius is outside the vacuum metric's physical domain and there is no Schwarzschild black-hole horizon in the stellar exterior.

The displayed chart becomes singular at $r_s$, but the invariant

$$R_{\alpha\beta\gamma\delta}R^{\alpha\beta\gamma\delta}=\frac{12r_s^2}{r^6}$$

is finite there. It diverges at $r=0$. [Black holes](black-holes-ii.md) introduces coordinates that cross the horizon and distinguishes these two cases.

For the vacuum geometry and its extensions, see [Tong, Black holes](https://davidtong.org/teaching/general-relativity/grhtml/S6).
