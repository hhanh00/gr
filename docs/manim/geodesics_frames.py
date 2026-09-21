from manim import *
import numpy as np
from diagram_text import Text


INK = BLACK
BLUE = "#2563eb"
RED = "#dc2626"
GRAY = "#94a3b8"


class MinkowskiSpace(Scene):
    """Light cone and hyperbolic coordinates in flat spacetime."""
    def construct(self):
        self.camera.background_color = WHITE
        axes = Axes(
            x_range=[-4, 4, 1], y_range=[-3, 3, 1],
            x_length=7.4, y_length=5.2,
            axis_config={"color": INK, "stroke_width": 2},
            tips=False,
        )
        xlab = MathTex("x", color=INK).next_to(axes.x_axis, RIGHT)
        tlab = MathTex("ct", color=INK).next_to(axes.y_axis, UP)
        light_right = DashedLine(axes.c2p(-3, -3), axes.c2p(3, 3), color=RED, stroke_width=3)
        light_left = DashedLine(axes.c2p(-3, 3), axes.c2p(3, -3), color=RED, stroke_width=3)
        hyperbolas = VGroup(*[
            ParametricFunction(
                lambda q, r=r: axes.c2p(r * np.cosh(q), r * np.sinh(q)),
                t_range=[-1.25, 1.25], color=BLUE, stroke_width=3,
            ) for r in [0.8, 1.35, 1.9, 2.45]
        ])
        inertial = Line(axes.c2p(-1.05, -2.7), axes.c2p(1.05, 2.7), color=INK, stroke_width=5)
        inertial_label = Text("inertial worldline", font_size=20, color=INK)
        inertial_label.next_to(inertial, LEFT, buff=0.18).shift(UP * 0.8)
        title = Text("Minkowski space", font_size=32, color=INK).to_edge(UP, buff=0.3)
        caption = MathTex("x^2-(ct)^2=\\rho^2", font_size=30, color=BLUE)
        caption.next_to(axes, DOWN, buff=0.25)
        self.add(axes, xlab, tlab, light_right, light_left, hyperbolas,
                 inertial, inertial_label, title, caption)


class UniformAcceleration(Scene):
    """A Rindler congruence: fixed-rho hyperbolas have different accelerations."""
    def construct(self):
        self.camera.background_color = WHITE
        axes = Axes(
            x_range=[0, 5.8, 1], y_range=[-2.8, 2.8, 1],
            x_length=8.0, y_length=4.5,
            axis_config={"color": INK, "stroke_width": 2}, tips=False,
        ).shift(DOWN * 0.15)
        xlab = MathTex("x", color=INK).next_to(axes.x_axis, RIGHT)
        tlab = MathTex("ct", color=INK).next_to(axes.y_axis, UP)
        curves = VGroup(*[
            ParametricFunction(
                lambda q, r=r: axes.c2p(r * np.cosh(q), r * np.sinh(q)),
                t_range=[-0.82, 0.82], color=BLUE, stroke_width=4,
            ) for r in [0.8, 1.45, 2.1, 2.75, 3.4]
        ])
        eta = 0.45
        simult = DashedLine(axes.c2p(0, 0), axes.c2p(4.8, 4.8 * np.tanh(eta)), color=RED, stroke_width=3)
        labels = Text("constant eta: simultaneous in the comoving inertial frame", font_size=19, color=RED)
        labels.to_edge(DOWN, buff=0.25)
        accel = MathTex("\\alpha = c^2/\\rho", color=BLUE, font_size=32)
        accel.move_to(axes.c2p(4.55, 2.35))
        title = Text("Uniform acceleration", font_size=32, color=INK).to_edge(UP, buff=0.55)
        self.add(axes, xlab, tlab, curves, simult, labels, accel, title)


class UniformGravitationalField(Scene):
    """Local accelerating-laboratory picture of a uniform gravitational field."""
    def construct(self):
        self.camera.background_color = WHITE
        box = Rectangle(width=5.2, height=3.3, color=INK, stroke_width=4)
        floor = Line(box.get_corner(DL), box.get_corner(DR), color=INK, stroke_width=6)
        ceiling = Line(box.get_corner(UL), box.get_corner(UR), color=INK, stroke_width=3)
        particle = Dot(box.get_center() + RIGHT * 0.8 + UP * 0.35, color=BLUE, radius=0.1)
        fall = Arrow(particle.get_center(), particle.get_center() + DOWN * 0.85, color=BLUE, stroke_width=5)
        g = Arrow(box.get_center() + LEFT * 2.8, box.get_center() + LEFT * 2.8 + DOWN * 1.1, color=RED, stroke_width=6)
        glabel = MathTex("g", color=RED, font_size=38).next_to(g, LEFT, buff=0.15)
        accel = Arrow(box.get_center() + RIGHT * 3.0, box.get_center() + RIGHT * 3.0 + UP * 1.0, color=RED, stroke_width=6)
        alabel = MathTex("a=g", color=RED, font_size=32).next_to(accel, RIGHT, buff=0.15)
        metric = MathTex("ds^2\\simeq(1+2gz/c^2)c^2dT^2-dz^2", color=INK, font_size=28)
        metric.next_to(box, DOWN, buff=0.55)
        title = Text("Uniform gravitational field", font_size=32, color=INK).to_edge(UP, buff=0.3)
        caption = Text("accelerating laboratory: free particles fall toward the floor", font_size=22, color=INK)
        caption.next_to(metric, DOWN, buff=0.2)
        self.add(box, floor, ceiling, particle, fall, g, glabel, accel, alabel, metric, caption, title)


class GeodesicsOnSphere(Scene):
    """Great circles are geodesics; latitude circles generally are not."""
    def construct(self):
        self.camera.background_color = WHITE
        sphere = Circle(radius=1.75, color=INK, stroke_width=3)
        great_circle = Ellipse(
            width=3.5, height=0.62, color=BLUE, stroke_width=6,
        ).rotate(25 * DEGREES)
        # Choose two visibly non-equatorial points directly from the tilted
        # great-circle curve.
        point_a = Dot(great_circle.point_from_proportion(0.16), color=BLUE, radius=0.09)
        point_b = Dot(great_circle.point_from_proportion(0.63), color=BLUE, radius=0.09)
        label_a = MathTex("A", color=BLUE, font_size=30).next_to(point_a, DOWN + LEFT, buff=0.12)
        label_b = MathTex("B", color=BLUE, font_size=30).next_to(point_b, UP + RIGHT, buff=0.12)
        latitude = ArcBetweenPoints(
            np.array([-1.35, 0.52, 0]), np.array([1.35, 0.52, 0]),
            angle=-0.62, color=GRAY, stroke_width=5,
        )
        geo_label = Text("great circle: geodesic through A and B", font_size=22, color=BLUE)
        geo_label.next_to(sphere, LEFT, buff=0.35).shift(DOWN * 0.85)
        steer_label = Text("latitude circle: not a geodesic (must turn)", font_size=22, color=RED)
        steer_label.next_to(sphere, RIGHT, buff=0.35).shift(UP * 0.8)
        title = Text("Geodesics on a sphere", font_size=32, color=INK).to_edge(UP, buff=0.3)
        caption = Text("along the blue path, the tangent is parallel transported", font_size=22, color=INK)
        caption.next_to(sphere, DOWN, buff=0.45)
        self.add(sphere, great_circle, point_a, point_b, label_a, label_b,
                 latitude, geo_label, steer_label, title, caption)
