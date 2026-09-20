from manim import *
import numpy as np
from diagram_text import Text


class GradientCurvedSurface(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        ink = BLACK
        contour_color = "#2563eb"
        gradient_color = "#dc2626"
        surface_color = "#93c5fd"
        muted = "#64748b"

        title = Text("The metric determines the gradient vector", font_size=32, color=ink)
        title.to_edge(UP, buff=0.28)

        divider = DashedLine(UP * 2.5, DOWN * 3.2, color="#cbd5e1", stroke_width=2)

        # A flat Euclidean plane with f=y.
        plane_center = LEFT * 3.5 + DOWN * 0.05
        plane = Rectangle(width=4.2, height=3.2, color=ink, stroke_width=3).move_to(plane_center)
        plane_contours = VGroup()
        for y in [-1.05, -0.35, 0.35, 1.05]:
            plane_contours.add(
                Line(
                    plane_center + LEFT * 2.1 + UP * y,
                    plane_center + RIGHT * 2.1 + UP * y,
                    color=contour_color,
                    stroke_width=3,
                )
            )
        flat_arrows = VGroup()
        for x in [-1.1, 0, 1.1]:
            start = plane_center + RIGHT * x + DOWN * 0.35
            flat_arrows.add(Arrow(start, start + UP * 0.95, buff=0, color=gradient_color, stroke_width=6))
        flat_heading = Text("flat Euclidean plane", font_size=26, color=ink)
        flat_heading.next_to(plane, UP, buff=0.24)
        flat_function = MathTex("f=y", color=contour_color, font_size=34)
        flat_function.next_to(flat_heading, DOWN, buff=0.12)
        flat_formula = MathTex(r"df=dy,\qquad \operatorname{grad}f=\partial_y", color=gradient_color, font_size=31)
        flat_formula.next_to(plane, DOWN, buff=0.28)
        flat_note = Text("same direction and magnitude everywhere", font_size=20, color=muted)
        flat_note.next_to(flat_formula, DOWN, buff=0.12)

        # A sphere with f=cos(theta): latitude contours and tangent gradients.
        sphere_center = RIGHT * 3.5 + DOWN * 0.05
        radius = 1.62
        sphere = Circle(radius=radius, color=ink, stroke_width=3).move_to(sphere_center)
        latitudes = VGroup(
            Ellipse(width=2 * radius * 0.78, height=0.36, color=contour_color, stroke_width=3).move_to(sphere_center + UP * 0.75),
            Ellipse(width=2 * radius, height=0.52, color=contour_color, stroke_width=3).move_to(sphere_center),
            Ellipse(width=2 * radius * 0.78, height=0.36, color=contour_color, stroke_width=3).move_to(sphere_center + DOWN * 0.75),
        )
        meridian = Ellipse(width=0.72, height=2 * radius, color=surface_color, stroke_width=2).move_to(sphere_center)

        left_p = sphere_center + LEFT * 1.25 + UP * 0.95
        right_q = sphere_center + RIGHT * 1.25 + UP * 0.95
        left_arrow = Arrow(
            left_p,
            left_p + RIGHT * 0.42 + UP * 0.58,
            buff=0,
            color=gradient_color,
            stroke_width=6,
        )
        right_arrow = Arrow(
            right_q,
            right_q + LEFT * 0.42 + UP * 0.58,
            buff=0,
            color=gradient_color,
            stroke_width=6,
        )
        points = VGroup(Dot(left_p, color=ink, radius=0.065), Dot(right_q, color=ink, radius=0.065))
        point_labels = VGroup(
            MathTex("p", color=ink, font_size=28).next_to(left_p, LEFT, buff=0.08),
            MathTex("q", color=ink, font_size=28).next_to(right_q, RIGHT, buff=0.08),
        )
        sphere_heading = Text("sphere of radius R", font_size=26, color=ink)
        sphere_heading.next_to(sphere, UP, buff=0.24)
        sphere_function = MathTex(r"f=\cos\theta", color=contour_color, font_size=34)
        sphere_function.next_to(sphere_heading, DOWN, buff=0.12)
        sphere_formula = MathTex(
            r"\operatorname{grad}f=-\frac{\sin\theta}{R^2}\partial_\theta",
            color=gradient_color,
            font_size=31,
        )
        sphere_formula.next_to(sphere, DOWN, buff=0.28)
        sphere_note = Text("tangent direction and magnitude vary with position", font_size=20, color=muted)
        sphere_note.next_to(sphere_formula, DOWN, buff=0.12)

        legend = VGroup(
            Line(ORIGIN, RIGHT * 0.48, color=contour_color, stroke_width=5),
            Text("level curve", font_size=20, color=contour_color),
            Arrow(ORIGIN, RIGHT * 0.48, buff=0, color=gradient_color, stroke_width=5),
            Text("gradient vector", font_size=20, color=gradient_color),
        )
        legend.arrange(RIGHT, buff=0.18)
        legend.to_edge(DOWN, buff=0.15)

        self.add(
            title,
            divider,
            plane,
            plane_contours,
            flat_arrows,
            flat_heading,
            flat_function,
            flat_formula,
            flat_note,
            sphere,
            latitudes,
            meridian,
            left_arrow,
            right_arrow,
            points,
            point_labels,
            sphere_heading,
            sphere_function,
            sphere_formula,
            sphere_note,
            legend,
        )
