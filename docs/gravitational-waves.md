# Gravitational Waves

A changing distribution of matter can produce traveling tidal disturbances. A passing disturbance changes the separation of freely falling test masses, which makes interferometers useful detectors. To calculate the effect, first approximate the metric near a flat background.

## Linearizing the Geometry

Write

$$g_{\mu\nu}=\eta_{\mu\nu}+h_{\mu\nu},\qquad |h_{\mu\nu}|\ll1.$$

Keep only first-order terms in the **metric perturbation** $h_{\mu\nu}$. Define its trace $h=\eta^{\mu\nu}h_{\mu\nu}$ and trace-reversed perturbation $\bar h_{\mu\nu}=h_{\mu\nu}-\tfrac12\eta_{\mu\nu}h$.

A small coordinate change alters $h_{\mu\nu}$ without changing the physical geometry. This **gauge freedom** means that a component oscillation alone is not evidence of a measurable wave.

In harmonic gauge, $\partial^\mu\bar h_{\mu\nu}=0$, and with negligible $\Lambda$ the linearized field equation is

$$\Box\bar h_{\mu\nu}=-\frac{16\pi G}{c^4}T_{\mu\nu},\qquad \Box=\frac1{c^2}\partial_t^2-\nabla^2.$$

In vacuum the right-hand side vanishes. Plane-wave solutions propagate at $c$.

<details>
<summary>Linearizing and solving the vacuum field equation</summary>

To first order, raise indices using $\eta^{\mu\nu}$. The connection is

$$\Gamma^\rho{}_{\mu\nu}=\frac12\eta^{\rho\sigma}(\partial_\mu h_{\sigma\nu}+\partial_\nu h_{\sigma\mu}-\partial_\sigma h_{\mu\nu}).$$

The quadratic connection products in the Riemann tensor are second order and can be dropped. Contract its derivative terms to obtain

$$R^{(1)}_{\mu\nu}=\frac12(\partial_\rho\partial_\mu h^\rho{}_\nu+\partial_\rho\partial_\nu h^\rho{}_\mu-\Box h_{\mu\nu}-\partial_\mu\partial_\nu h).$$

Harmonic gauge gives $\partial_\rho h^\rho{}_\nu=\tfrac12\partial_\nu h$, so the mixed derivatives cancel. Hence $R^{(1)}_{\mu\nu}=-\tfrac12\Box h_{\mu\nu}$ and $G^{(1)}_{\mu\nu}=-\tfrac12\Box\bar h_{\mu\nu}$. Substitution in Einstein's equations gives the linear wave equation stated above.

In vacuum, try $\bar h_{\mu\nu}=\operatorname{Re}[A_{\mu\nu}e^{ik_\rho x^\rho}]$. Then

$$\Box\bar h_{\mu\nu}=0\quad\Rightarrow\quad k_\rho k^\rho=0,\qquad k^\mu A_{\mu\nu}=0.$$

For $k^\mu=(\omega/c,\mathbf k)$, the first condition is $\omega=c|\mathbf k|$. The second is the harmonic-gauge constraint. Residual coordinate freedom then removes unphysical components, leaving the two TT polarizations described next. A monochromatic example is $h_+=a_+\cos[\omega(t-z/c)]$ and $h_\times=a_\times\cos[\omega(t-z/c)+\varphi_0]$, with dimensionless amplitudes $a_+,a_\times$.

</details>

## Two Physical Polarizations

For a vacuum plane wave traveling along $z$, we can use **transverse-traceless gauge**, or TT gauge. The physical spatial perturbation has the form

$$h^{\rm TT}_{ij}=\begin{pmatrix}h_+&h_\times&0\\h_\times&-h_+&0\\0&0&0\end{pmatrix},\qquad h_+,h_\times=h_+,h_\times(t-z/c).$$

The plus polarization changes the transverse separations along $x$ and $y$ oppositely. The cross polarization acts on axes rotated by $45^\circ$. The two functions describe the two propagating polarization modes of vacuum general relativity.

Here $h_{ij}$ is the perturbation of a metric with background $g_{ij}=-\delta_{ij}$. The commonly drawn positive stretch convention can therefore have the opposite sign from our spatial metric perturbation. The measured magnitude is unaffected.

## An Interferometer Measurement

For nearby test masses initially at rest in TT coordinates, their coordinates stay fixed to first order while their proper separation changes. Along a short $x$ arm,

$$L_x\simeq L_0\left(1-\frac12h_+\right),\qquad L_y\simeq L_0\left(1+\frac12h_+\right).$$

The differential fractional change is $\delta(L_x-L_y)/L_0\simeq-h_+$. **Strain** denotes a fractional change in length.

<details>
<summary>Obtaining the arm-length change</summary>

At fixed time along the $x$ direction, $d\ell^2=-g_{xx}dx^2=(1-h_+)dx^2$. If the wave varies negligibly across the arm, integrate to get $L_x=L_0\sqrt{1-h_+}\simeq L_0(1-h_+/2)$. Repeat with $g_{yy}=-1-h_+$.

A real interferometer measures round-trip light phase, rather than one instantaneous spatial length. This short-arm expression captures the leading response when the arm is much shorter than the gravitational wavelength; the full response includes light travel time and orientation.

</details>

## Producing Waves

Conservation removes leading monopole and dipole gravitational radiation from an isolated slowly moving source. The leading contribution depends on its changing **quadrupole moment**, the trace-free second moment of mass:

$$Q_{ij}=\int\rho\left(x_ix_j-\frac13\delta_{ij}r^2\right)d^3x.$$

The far-zone wave amplitude scales as $G\ddot Q/(c^4D)$, where $D$ is distance. The leading emitted power is

$$P=\frac{G}{5c^5}\left\langle\dddot Q_{ij}\dddot Q_{ij}\right\rangle.$$

We state this quadrupole formula without deriving the retarded field and its energy flux. It assumes weak radiation, a slowly moving source, and observation in the radiation zone. Compact-binary merger requires stronger methods near coalescence.

A binary loses orbital energy through radiation. Its orbital frequency and emitted wave frequency rise as the orbit contracts, producing a **chirp**. This connects the tidal signal to source dynamics and to the [Tests of relativity](tests-of-relativity.md).

For linearized gravity and wave production, see [Tong, When gravity is weak](https://davidtong.org/teaching/general-relativity/grhtml/S5).
