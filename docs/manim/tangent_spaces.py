from manim import *
import numpy as np
from diagram_text import Text


class TangentSpaces(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        ink = BLACK
        surface_color = "#93c5fd"
        tangent_color = "#7c3aed"
        point_color = "#dc2626"
        muted = "#64748b"

        title = Text("Tangent spaces are attached point by point", font_size=32, color=ink)
        title.to_edge(UP, buff=0.3)

        # Left panel: a flat surface and its tangent plane have the same direction.
        plane_center = LEFT * 3.65 + DOWN * 0.25
        plane_corners = [
            plane_center + LEFT * 2.15 + DOWN * 0.85,
            plane_center + RIGHT * 2.15 + DOWN * 0.85,
            plane_center + RIGHT * 1.55 + UP * 0.85,
            plane_center + LEFT * 1.55 + UP * 0.85,
        ]
        plane = Polygon(
            *plane_corners,
            color=surface_color,
            fill_color="#dbeafe",
            fill_opacity=0.72,
            stroke_width=3,
        )
        plane_grid = VGroup()
        for alpha in [0.25, 0.5, 0.75]:
            lower = interpolate(plane_corners[0], plane_corners[1], alpha)
            upper = interpolate(plane_corners[3], plane_corners[2], alpha)
            plane_grid.add(Line(lower, upper, color=surface_color, stroke_width=2))
        for alpha in [0.33, 0.66]:
            left = interpolate(plane_corners[0], plane_corners[3], alpha)
            right = interpolate(plane_corners[1], plane_corners[2], alpha)
            plane_grid.add(Line(left, right, color=surface_color, stroke_width=2))

        p = plane_center + LEFT * 0.25 + UP * 0.05
        tangent_patch = Polygon(
            p + LEFT * 1.05 + DOWN * 0.40,
            p + RIGHT * 1.05 + DOWN * 0.40,
            p + RIGHT * 0.78 + UP * 0.40,
            p + LEFT * 0.78 + UP * 0.40,
            color=tangent_color,
            fill_color="#ede9fe",
            fill_opacity=0.48,
            stroke_width=4,
        )
        tangent_patch.set_stroke(opacity=0.95)
        p_dot = Dot(p, color=point_color, radius=0.075)
        p_label = MathTex("p", color=point_color, font_size=30).next_to(p_dot, DOWN, buff=0.08)
        flat_vectors = VGroup(
            Arrow(p, p + RIGHT * 0.78, buff=0, color=tangent_color, stroke_width=5),
            Arrow(p, p + LEFT * 0.28 + UP * 0.55, buff=0, color=tangent_color, stroke_width=5),
        )
        flat_tangent_label = MathTex("T_pM", color=tangent_color, font_size=34)
        flat_tangent_label.next_to(tangent_patch, UP, buff=0.12)
        flat_heading = Text("flat surface", font_size=26, color=ink)
        flat_heading.next_to(plane, DOWN, buff=0.32)
        flat_note = Text("same direction at every point", font_size=20, color=muted)
        flat_note.next_to(flat_heading, DOWN, buff=0.12)

        # Right panel: tangent planes at two points on a sphere differ.
        sphere_center = RIGHT * 3.5 + DOWN * 0.25
        radius = 1.55
        sphere = Circle(radius=radius, color=ink, stroke_width=3).move_to(sphere_center)
        sphere_grid = VGroup(
            Ellipse(width=2 * radius, height=0.55, color=surface_color, stroke_width=2).move_to(sphere_center),
            Ellipse(width=0.78, height=2 * radius, color=surface_color, stroke_width=2).move_to(sphere_center),
        )

        top_point = sphere_center + UP * radius
        top_plane = Polygon(
            top_point + LEFT * 1.0 + DOWN * 0.22,
            top_point + RIGHT * 1.0 + DOWN * 0.22,
            top_point + RIGHT * 0.72 + UP * 0.22,
            top_point + LEFT * 0.72 + UP * 0.22,
            color=tangent_color,
            fill_color="#ede9fe",
            fill_opacity=0.62,
            stroke_width=4,
        )
        top_dot = Dot(top_point, color=point_color, radius=0.07)
        top_vectors = VGroup(
            Arrow(top_point, top_point + RIGHT * 0.70, buff=0, color=tangent_color, stroke_width=5),
            Arrow(top_point, top_point + LEFT * 0.22 + UP * 0.32, buff=0, color=tangent_color, stroke_width=5),
        )
        top_label = MathTex("T_pM", color=tangent_color, font_size=31)
        top_label.next_to(top_plane, UP, buff=0.08)
        top_point_label = MathTex("p", color=point_color, font_size=28).next_to(top_dot, LEFT, buff=0.08)

        side_point = sphere_center + RIGHT * radius
        side_plane = Polygon(
            side_point + LEFT * 0.22 + DOWN * 0.92,
            side_point + RIGHT * 0.22 + DOWN * 0.68,
            side_point + RIGHT * 0.22 + UP * 0.92,
            side_point + LEFT * 0.22 + UP * 0.68,
            color=tangent_color,
            fill_color="#ede9fe",
            fill_opacity=0.62,
            stroke_width=4,
        )
        side_dot = Dot(side_point, color=point_color, radius=0.07)
        side_vectors = VGroup(
            Arrow(side_point, side_point + UP * 0.65, buff=0, color=tangent_color, stroke_width=5),
            Arrow(side_point, side_point + RIGHT * 0.30 + DOWN * 0.38, buff=0, color=tangent_color, stroke_width=5),
        )
        side_label = MathTex("T_qM", color=tangent_color, font_size=31)
        side_label.next_to(side_plane, RIGHT, buff=0.08)
        side_point_label = MathTex("q", color=point_color, font_size=28).next_to(side_dot, DOWN, buff=0.08)

        curved_heading = Text("curved surface", font_size=26, color=ink)
        curved_heading.next_to(sphere, DOWN, buff=0.32)
        curved_note = Text("different points, different tangent spaces", font_size=20, color=muted)
        curved_note.next_to(curved_heading, DOWN, buff=0.12)

        divider = DashedLine(UP * 2.5, DOWN * 3.15, color="#cbd5e1", stroke_width=2)

        self.add(
            title,
            divider,
            plane,
            plane_grid,
            tangent_patch,
            p_dot,
            p_label,
            flat_vectors,
            flat_tangent_label,
            flat_heading,
            flat_note,
            sphere,
            sphere_grid,
            top_plane,
            top_dot,
            top_vectors,
            top_label,
            top_point_label,
            side_plane,
            side_dot,
            side_vectors,
            side_label,
            side_point_label,
            curved_heading,
            curved_note,
        )
