from manim import *
import numpy as np
from diagram_text import Text


class ParallelTransportSphere(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        ink = BLACK
        sphere_color = "#94a3b8"
        path_color = "#d97706"
        initial_color = "#2563eb"
        transport_color = "#7c3aed"
        returned_color = "#dc2626"

        title = Text("Parallel transport depends on the closed path", font_size=32, color=ink)
        title.to_edge(UP, buff=0.3)

        def make_panel(center, separation, rotation, area_label, rotation_label):
            radius = 1.65
            globe = Circle(radius=radius, color=ink, stroke_width=3).move_to(center)

            # Faint latitude and longitude lines suggest the spherical surface.
            latitude = Ellipse(
                width=2 * radius,
                height=0.55,
                color=sphere_color,
                stroke_width=2,
            ).move_to(center)
            longitude = Ellipse(
                width=0.75,
                height=2 * radius,
                color=sphere_color,
                stroke_width=2,
            ).move_to(center)

            north = center + UP * radius
            left_equator = center + np.array([-separation, 0, 0])
            right_equator = center + np.array([separation, 0, 0])

            left_meridian = CubicBezier(
                north,
                north + LEFT * separation * 0.75 + DOWN * 0.35,
                left_equator + UP * 0.65,
                left_equator,
                color=path_color,
                stroke_width=6,
            )
            equator_arc = ArcBetweenPoints(
                left_equator,
                right_equator,
                angle=-0.28,
                color=path_color,
                stroke_width=6,
            )
            right_meridian = CubicBezier(
                right_equator,
                right_equator + UP * 0.65,
                north + RIGHT * separation * 0.75 + DOWN * 0.35,
                north,
                color=path_color,
                stroke_width=6,
            )
            loop = VGroup(left_meridian, equator_arc, right_meridian)

            # Sample the same vector during transport. The arrows retain their
            # direction along a meridian and accumulate the loop's rotation
            # while crossing between the two meridians.
            transported_arrows = VGroup()
            samples = [
                (left_meridian.point_from_proportion(0.38), 0),
                (left_meridian.point_from_proportion(0.76), 0),
                (equator_arc.point_from_proportion(0.32), rotation * 0.32),
                (equator_arc.point_from_proportion(0.68), rotation * 0.68),
                (right_meridian.point_from_proportion(0.30), rotation),
                (right_meridian.point_from_proportion(0.68), rotation),
            ]
            for point, angle in samples:
                direction = np.array([np.cos(angle), np.sin(angle), 0])
                transported_arrows.add(
                    Arrow(
                        point,
                        point + direction * 0.42,
                        buff=0,
                        color=transport_color,
                        stroke_width=4,
                        max_tip_length_to_length_ratio=0.28,
                    )
                )

            start_dot = Dot(north, color=ink, radius=0.07)
            start_label = Text("start / finish", font_size=17, color=ink)
            start_label.next_to(north, UP, buff=0.12)

            arrow_length = 0.9
            arrow_origin = north + DOWN * 0.08
            initial_arrow = Arrow(
                arrow_origin,
                arrow_origin + RIGHT * arrow_length,
                buff=0,
                color=initial_color,
                stroke_width=6,
                max_tip_length_to_length_ratio=0.22,
            )
            returned_direction = np.array([np.cos(rotation), np.sin(rotation), 0])
            returned_arrow = Arrow(
                arrow_origin,
                arrow_origin + returned_direction * arrow_length,
                buff=0,
                color=returned_color,
                stroke_width=6,
                max_tip_length_to_length_ratio=0.22,
            )

            angle_arc = Arc(
                radius=0.42,
                start_angle=0,
                angle=rotation,
                arc_center=arrow_origin,
                color=returned_color,
                stroke_width=3,
            )
            delta = MathTex(r"\Delta\alpha", color=returned_color, font_size=28)
            delta.next_to(angle_arc, RIGHT, buff=0.05)

            area = Text(area_label, font_size=22, color=path_color)
            area.move_to(center + DOWN * 0.45)
            result = Text(rotation_label, font_size=22, color=returned_color)
            result.next_to(globe, DOWN, buff=0.28)

            return VGroup(
                globe,
                latitude,
                longitude,
                loop,
                transported_arrows,
                start_dot,
                start_label,
                initial_arrow,
                returned_arrow,
                angle_arc,
                delta,
                area,
                result,
            )

        small = make_panel(
            LEFT * 3.5 + DOWN * 0.15,
            separation=0.65,
            rotation=PI / 6,
            area_label="smaller enclosed area",
            rotation_label="smaller rotation",
        )
        large = make_panel(
            RIGHT * 3.5 + DOWN * 0.15,
            separation=1.25,
            rotation=PI / 2,
            area_label="larger enclosed area",
            rotation_label="larger rotation",
        )

        legend_initial = Line(ORIGIN, RIGHT * 0.45, color=initial_color, stroke_width=6)
        legend_initial_label = Text("initial vector", font_size=19, color=initial_color)
        legend_returned = Line(ORIGIN, RIGHT * 0.45, color=returned_color, stroke_width=6)
        legend_returned_label = Text("returned vector", font_size=19, color=returned_color)
        legend_transport = Line(ORIGIN, RIGHT * 0.45, color=transport_color, stroke_width=6)
        legend_transport_label = Text("during transport", font_size=19, color=transport_color)
        legend = VGroup(
            VGroup(legend_initial, legend_initial_label).arrange(RIGHT, buff=0.14),
            VGroup(legend_transport, legend_transport_label).arrange(RIGHT, buff=0.14),
            VGroup(legend_returned, legend_returned_label).arrange(RIGHT, buff=0.14),
        ).arrange(RIGHT, buff=0.48)
        legend.to_edge(DOWN, buff=0.18)

        relation = MathTex(
            r"\Delta\alpha=\frac{A}{R^2}",
            color=ink,
            font_size=35,
        )
        relation.next_to(title, DOWN, buff=0.18)

        self.add(title, relation, small, large, legend)
