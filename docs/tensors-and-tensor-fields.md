# Tensors and Tensor Fields

A velocity has different components when we rotate our axes, but the particle's motion does not change. General relativity extends this distinction to arbitrary smooth coordinates. We need objects whose components change in a controlled way, so that an equation describes the same measurement in every chart.

## Tangent Vectors

A **tangent vector** at a point specifies a direction and magnitude of an infinitesimal displacement. For a curve $x^\mu(\lambda)$, its tangent has components $V^\mu=dx^\mu/d\lambda$. Here $\lambda$ is a parameter labeling points on the curve.

Apply the chain rule under $x^\mu\to x'^\mu(x)$:

$$V'^\mu=\frac{\partial x'^\mu}{\partial x^\nu}V^\nu.$$

This defines the transformation of an upper, or **contravariant**, index. Write the vector itself as $V=V^\mu\partial_\mu$, where $\partial_\mu=\partial/\partial x^\mu$ is a coordinate basis vector. The basis changes inversely to the components.

## Covectors and Gradients

A **scalar** has the same value at a given event in every coordinate system: $f'(x')=f(x)$. A scalar temperature field $f(x)$ assigns such a number to each point. Its change along a displacement is $df=(\partial_\mu f)dx^\mu$. To keep $df$ independent of coordinates, the gradient components must transform inversely to displacement components:

$$\omega'_\mu=\frac{\partial x^\nu}{\partial x'^\mu}\omega_\nu.$$

A **covector**, or one-form, is an object with this rule. It takes a vector as input and returns a scalar, $\omega(V)=\omega_\mu V^\mu$. The gradient $df$ is a covector; converting it to a vector requires a metric.

<details>
<summary>Why the contraction is invariant</summary>

Insert both rules:

$$\omega'_\mu V'^\mu=\frac{\partial x^\alpha}{\partial x'^\mu}\frac{\partial x'^\mu}{\partial x^\beta}\omega_\alpha V^\beta=\delta^\alpha{}_\beta\omega_\alpha V^\beta.$$

The symbol $\delta^\alpha{}_\beta$ is the identity matrix. The two Jacobian matrices are inverses, so their product removes the coordinate change.

</details>

## Tensors and Index Rules

A **tensor** combines vector and covector transformation rules. Its type $(r,s)$ counts upper and lower indices. For example,

$$T'^{\mu\nu}=\frac{\partial x'^\mu}{\partial x^\alpha}\frac{\partial x'^\nu}{\partial x^\beta}T^{\alpha\beta}.$$

Each index transforms separately. A two-index array is not automatically a tensor; its transformation rule matters.

In an equation, a **free index** occurs on both sides and labels components. A **dummy index** occurs once up and once down within a term and is summed. Thus $A^\mu=T^{\mu\nu}\omega_\nu$ has free index $\mu$ and dummy index $\nu$. We may rename $\nu$ without changing the expression.

Tensor equations have the same free indices on both sides. This keeps their validity independent of coordinates, but it does not by itself establish that they correctly describe nature.

## Raising and Lowering Indices

The metric $g_{\mu\nu}$ compares two vectors. Its inverse satisfies $g^{\mu\alpha}g_{\alpha\nu}=\delta^\mu{}_\nu$. Use them to convert between vector and covector components:

$$V_\mu=g_{\mu\nu}V^\nu,\qquad V^\mu=g^{\mu\nu}V_\nu.$$

In Cartesian Minkowski coordinates, $V_\mu=(V^0,-V^1,-V^2,-V^3)$. In general coordinates, lowering an index can mix components and introduce position-dependent factors.

Consider the Euclidean plane in polar coordinates. Its spatial metric is $d\ell^2=dr^2+r^2d\phi^2$. Then $V_\phi=r^2V^\phi$, and the squared length is $(V^r)^2+r^2(V^\phi)^2$. Treating the angular component as a Cartesian length would give the wrong measurement.

## Fields and Differentiation

A **tensor field** assigns a tensor to each point. The metric and the stress–energy tensor are examples. Differentiating a scalar gives a covector, but differentiating vector components also differentiates the coordinate transformation matrix. Ordinary partial derivatives of vectors therefore fail to transform as tensors in general.

[Connections and curvature](curvature.md) will correct this derivative. First, [Riemannian Spaces and the Metric Tensor](riemannian-spaces-and-metric-tensor.md) introduces geometric measurements. [Curves and Motion](curves-and-motion.md) supplies supporting material on trajectories.
