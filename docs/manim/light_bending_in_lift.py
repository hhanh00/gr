from manim import *
import numpy as np


class LightBendingInLift(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        ink = BLACK
        beam_color = "#2563eb"
        vec_color = "#dc2626"
        ref_color = "#9ca3af"

        def make_lift():
            box = Rectangle(width=3.4, height=2.4, color=ink, stroke_width=3)
            floor = Line(box.get_corner(DL), box.get_corner(DR), color=ink, stroke_width=5)
            entry = box.get_left() + UP * 0.75
            exit_point = box.get_right() + DOWN * 0.45
            reference = DashedLine(
                entry, box.get_right() + UP * 0.75, color=ref_color, stroke_width=3,
            )
            beam = CurvedArrow(
                entry, exit_point, angle=-0.8, color=beam_color, stroke_width=6,
            )
            entry_dot = Dot(entry, color=beam_color, radius=0.06)
            return VGroup(box, floor, reference, beam, entry_dot)

        # Left panel: lift accelerating upward through empty space
        left_lift = make_lift()
        accel_arrow = Arrow(
            ORIGIN, UP * 1.0, color=vec_color, stroke_width=6,
        ).next_to(left_lift, RIGHT, buff=0.5)
        accel_label = MathTex("a", color=vec_color, font_size=40).next_to(accel_arrow, RIGHT, buff=0.15)
        left_diagram = VGroup(left_lift, accel_arrow, accel_label)
        left_caption = Text("accelerating through empty space", font_size=26, color=ink)
        left_caption.next_to(left_diagram, DOWN, buff=0.4)
        left_panel = VGroup(left_diagram, left_caption)

        # Right panel: lift at rest on a planet's surface
        right_lift = make_lift()
        ground = Line(LEFT * 2.0, RIGHT * 2.0, color=ink, stroke_width=3)
        hatches = VGroup(*[
            Line(
                ground.point_from_proportion(t),
                ground.point_from_proportion(t) + DOWN * 0.22 + LEFT * 0.14,
                color=ink, stroke_width=2,
            )
            for t in np.linspace(0.05, 0.95, 12)
        ])
        ground_group = VGroup(ground, hatches).next_to(right_lift, DOWN, buff=0.0)
        gravity_arrow = Arrow(
            ORIGIN, DOWN * 1.0, color=vec_color, stroke_width=6,
        ).next_to(right_lift, RIGHT, buff=0.5).align_to(right_lift, UP)
        gravity_label = MathTex("g", color=vec_color, font_size=40).next_to(gravity_arrow, RIGHT, buff=0.15)
        right_diagram = VGroup(right_lift, ground_group, gravity_arrow, gravity_label)
        right_caption = Text("at rest above a planet", font_size=26, color=ink)
        right_caption.next_to(VGroup(right_lift, ground_group), DOWN, buff=0.4)
        right_panel = VGroup(right_diagram, right_caption)

        panels = VGroup(left_panel, right_panel).arrange(RIGHT, buff=1.8)
        panels.move_to(ORIGIN).shift(UP * 0.3)

        equiv = MathTex("\\equiv", color=ink, font_size=56).move_to(
            (left_panel.get_right() + right_panel.get_left()) / 2
        )

        title = Text("Light bending in a lift", font_size=32, color=ink)
        title.next_to(panels, UP, buff=0.6)

        self.add(panels, equiv, title)
