# Spacetime

A clock measures the time between events along its own path. Two clocks that separate and reunite can record different elapsed times, even when both work correctly. To describe this without choosing a preferred observer, we combine space and time into spacetime and distinguish coordinate labels from measurements.

## 1. Events and Reference Frames

An **event** is a particular occurrence at a place and time. In an inertial frame, where force-free particles move at constant velocity, assign it coordinates

$$x^\mu=(ct,x,y,z),\qquad \mu=0,1,2,3.$$

The index $\mu$ labels spacetime components; it is not a power. Coordinates depend on the observer. The event itself does not.

Special relativity assumes that all inertial observers measure the same vacuum light speed $c$. For frames with relative velocity $v$ along $x$, the **Lorentz transformation** is

$$ct'=\gamma(ct-\beta x),\qquad x'=\gamma(x-\beta ct),\qquad \beta=v/c,\quad \gamma=(1-\beta^2)^{-1/2}.$$

The transverse coordinates stay unchanged. Since $t'$ depends on $x$, observers can disagree about the simultaneity of separated events. This disagreement does not imply that a clock has changed its rate through a coordinate transformation.

## 2. The Invariant Interval

To compare descriptions, form a quantity that remains unchanged under the transformation:

$$ds^2=c^2dt^2-dx^2-dy^2-dz^2=\eta_{\mu\nu}dx^\mu dx^\nu.$$

We use the signature $(+,-,-,-)$, matching the Phyz special-relativity chapter, so $\eta_{\mu\nu}=\operatorname{diag}(1,-1,-1,-1)$. Repeated paired upper and lower indices mean a sum. Later chapters retain this convention and write $x^0=ct$ unless they explicitly set $c=1$.

| Interval | Sign | Physical connection |
| --- | --- | --- |
| Timelike | $ds^2>0$ | A massive particle can follow this direction. |
| Null | $ds^2=0$ | Light in vacuum follows this direction. |
| Spacelike | $ds^2<0$ | No causal signal can follow this direction. |

<details>
<summary>Checking invariance for a boost</summary>

Substitute the coordinate differences into the interval:

$$c^2dt'^2-dx'^2=\gamma^2[(c\,dt-\beta\,dx)^2-(dx-\beta c\,dt)^2].$$

The cross terms cancel. The remaining factor is $\gamma^2(1-\beta^2)=1$, giving $c^2dt^2-dx^2$. Adding the unchanged transverse terms completes the check.

</details>

## 3. Proper Time and Moving Clocks

**Proper time** $\tau$ is the time recorded by a clock following a timelike path. Since that clock has no spatial displacement in its instantaneous rest frame,

$$c^2d\tau^2=ds^2,\qquad d\tau=dt\sqrt{1-v^2/c^2}.$$

For a path with changing speed, integrate this expression. Coordinate time describes a frame's assignment of times; proper time describes one clock's accumulated reading.

For example, suppose one clock remains at rest while another travels out and back at speed $v$, neglecting the short turnaround. If the stationary clock records total duration $T$, the traveler records $T\sqrt{1-v^2/c^2}$. Their paths differ, so their readings differ. The turnaround prevents treating both complete journeys as inertial motion in one frame.

## 4. Light Cones and Causality

In a diagram with $ct$ vertical and $x$ horizontal, light rays satisfy $x=\pm ct$. These lines bound the **light cone**, the set of lightlike directions from an event. Future-directed timelike paths lie inside the future cone.

Observers can reverse the coordinate-time order of spacelike-separated events. They cannot reverse the causal order of timelike-separated events while preserving the choice of future. This distinction prevents coordinate disagreements from becoming disagreements about which signal caused a response.

In general relativity, the interval becomes $ds^2=g_{\mu\nu}(x)dx^\mu dx^\nu$. Light cones and clock readings can then vary with position. Before studying that geometry, [Vectors and tensors](tensors-and-tensor-fields.md) develops the transformation rules needed to express the same physical law in different coordinates.
