# Manifolds

A globe has no preferred flat map. Every map introduces coordinates that work over some region and fail elsewhere, while distances and routes on the Earth remain well defined. Spacetime requires the same distinction between a geometric space and the coordinates used to describe it.

## Local Coordinates

A smooth **manifold** is a space that locally admits coordinates like those of ordinary Euclidean space, with smooth coordinate changes between overlapping regions. General relativity describes spacetime with a four-dimensional manifold $M$.

A **chart** maps an open region $U\subset M$ to an open subset of $\mathbb R^4$:

$$\varphi:U\longrightarrow\varphi(U)\subset\mathbb R^4.$$

Its four coordinate functions label events. A collection of compatible charts covering the manifold is an **atlas**. The usual definition also imposes separation and countability conditions, which exclude pathological spaces; we will work with ordinary smooth manifolds satisfying those conditions.

The manifold alone has no clock readings, distances, or light cones. Those require a metric. Four-dimensional coordinates also do not imply an external fifth dimension containing spacetime.

## Overlapping Charts

Suppose $\varphi$ and $\psi$ cover the same event. Their **transition map** converts its labels:

$$x'=\psi\circ\varphi^{-1}(x).$$

Smooth transitions let us take derivatives consistently. Their Jacobian matrices produce the [vector and tensor transformation rules](tensors-and-tensor-fields.md).

On a sphere, latitude and longitude fail at the poles, where longitude has no unique value. A second chart can cover a pole without that failure. The bad coordinates do not imply a damaged sphere.

<details>
<summary>A sphere described without polar coordinates</summary>

For a unit sphere embedded in Euclidean three-space, project from the north pole onto the equatorial plane. Away from the north pole, define

$$X=\frac{x}{1-z},\qquad Y=\frac{y}{1-z}.$$

The inverse map is

$$x=\frac{2X}{1+X^2+Y^2},\quad y=\frac{2Y}{1+X^2+Y^2},\quad z=\frac{X^2+Y^2-1}{1+X^2+Y^2}.$$

Projection from the south pole covers the point missing from this chart. On the overlap the transition functions are smooth. The embedding makes the example easy to visualize, but the charts define the surface intrinsically.

</details>

## Tangent Spaces

At each point $p$, the tangent directions form a vector space $T_pM$, the **tangent space**. One intrinsic definition treats a vector as a directional derivative acting on smooth scalar functions:

$$V[f]=V^\mu\partial_\mu f.$$

A curve through $p$ supplies such an operation by differentiating $f$ along the curve. Different curves with the same tangent define the same vector at that point.

Vectors at different points belong to different tangent spaces. Adding them requires an additional comparison rule, a connection. A common coordinate label does not supply a coordinate-independent identification of those spaces.

## Local and Global Structure

Local coordinates do not determine global **topology**, the pattern of connectedness and continuity. A plane and a cylinder both have locally two-dimensional charts, but a loop around the cylinder cannot contract to a point on its surface.

Curvature is a separate concept. A cylinder with its usual surface metric is locally flat even though its topology differs from the plane. We must specify both the underlying manifold and the metric rather than infer either from a sketch.

This distinction matters for [Black holes](black-holes-ii.md): a coordinate chart can stop at a horizon while a larger spacetime continues smoothly. A physical singularity requires more than a diverging coordinate component.

[Metrics](riemannian-spaces-and-metric-tensor.md) now introduces the tensor field that turns the manifold into a geometry where clocks and rulers have definite readings.
