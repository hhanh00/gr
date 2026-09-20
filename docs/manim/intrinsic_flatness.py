from manim import *
import numpy as np
from diagram_text import Text


class IntrinsicFlatness(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        ink = BLACK
        flat_color = "#2563eb"
        curved_color = "#d97706"
        grid_color = "#93c5fd"
        muted = "#6b7280"

        title = Text("Bending and intrinsic curvature", font_size=32, color=ink)
        title.to_edge(UP, buff=0.28)

        # A rectangular sheet and a cylinder carry the same square grid.
        sheet_outline = Rectangle(width=3.4, height=2.0, color=ink, stroke_width=3)
        sheet_grid = VGroup()
        for x in np.linspace(-1.7, 1.7, 6)[1:-1]:
            sheet_grid.add(Line([x, -1.0, 0], [x, 1.0, 0], color=grid_color, stroke_width=2))
        for y in np.linspace(-1.0, 1.0, 5)[1:-1]:
            sheet_grid.add(Line([-1.7, y, 0], [1.7, y, 0], color=grid_color, stroke_width=2))
        sheet = VGroup(sheet_outline, sheet_grid).move_to(LEFT * 4.0 + UP * 1.35)
        sheet_label = Text("flat sheet", font_size=24, color=ink).next_to(sheet, DOWN, buff=0.18)

        cylinder_top = Ellipse(width=2.8, height=0.65, color=ink, stroke_width=3)
        cylinder_bottom = Ellipse(width=2.8, height=0.65, color=ink, stroke_width=3).shift(DOWN * 2.0)
        cylinder_sides = VGroup(
            Line(cylinder_top.get_left(), cylinder_bottom.get_left(), color=ink, stroke_width=3),
            Line(cylinder_top.get_right(), cylinder_bottom.get_right(), color=ink, stroke_width=3),
        )
        cylinder_grid = VGroup()
        for y in [-0.5, -1.0, -1.5]:
            cylinder_grid.add(Ellipse(width=2.8, height=0.65, color=grid_color, stroke_width=2).shift(UP * y))
        for x in [-0.7, 0, 0.7]:
            cylinder_grid.add(Line([x, 0, 0], [x, -2.0, 0], color=grid_color, stroke_width=2))
        cylinder = VGroup(cylinder_top, cylinder_bottom, cylinder_sides, cylinder_grid)
        cylinder.move_to(RIGHT * 1.0 + UP * 1.35)
        cylinder_label = Text("cylinder", font_size=24, color=ink).next_to(cylinder, DOWN, buff=0.18)

        roll_arrow = DoubleArrow(
            sheet.get_right() + RIGHT * 0.15,
            cylinder.get_left() + LEFT * 0.15,
            color=flat_color,
            stroke_width=4,
            buff=0,
        )
        roll_label = Text("roll / unroll", font_size=21, color=flat_color)
        roll_label.next_to(roll_arrow, UP, buff=0.12)
        preserved = Text("distances and angles are preserved", font_size=20, color=flat_color)
        preserved.move_to(RIGHT * 4.65 + UP * 1.35)

        # A sphere cannot be developed into a plane without distortion or cuts.
        sphere = Circle(radius=1.0, color=ink, stroke_width=3)
        sphere.add(Ellipse(width=0.75, height=2.0, color=curved_color, stroke_width=2))
        sphere.add(Ellipse(width=1.45, height=2.0, color=curved_color, stroke_width=2))
        sphere.add(Ellipse(width=2.0, height=0.65, color=curved_color, stroke_width=2))
        sphere.add(Ellipse(width=2.0, height=1.35, color=curved_color, stroke_width=2))
        sphere.move_to(LEFT * 3.2 + DOWN * 2.25)
        sphere_label = Text("sphere", font_size=24, color=ink).next_to(sphere, DOWN, buff=0.12)

        flatten_arrow = Arrow(
            sphere.get_right() + RIGHT * 0.25,
            RIGHT * 0.65 + DOWN * 2.25,
            color=curved_color,
            stroke_width=4,
            buff=0,
        )
        flatten_label = Text("flatten", font_size=21, color=curved_color)
        flatten_label.next_to(flatten_arrow, UP, buff=0.1)

        gores = VGroup()
        for i in range(5):
            gore = Polygon(
                [-0.34, 0.9, 0],
                [0.34, 0.9, 0],
                [0.18, 0, 0],
                [0.34, -0.9, 0],
                [-0.34, -0.9, 0],
                [-0.18, 0, 0],
                color=curved_color,
                fill_color="#fef3c7",
                fill_opacity=1,
                stroke_width=3,
            )
            gores.add(gore)
        gores.arrange(RIGHT, buff=0.16).move_to(RIGHT * 2.2 + DOWN * 2.25)
        tear_marks = VGroup(*[
            Text("tear", font_size=15, color=curved_color).rotate(PI / 2)
            for _ in range(4)
        ])
        for mark, left_gore, right_gore in zip(tear_marks, gores[:-1], gores[1:]):
            mark.move_to((left_gore.get_right() + right_gore.get_left()) / 2)

        impossible = Text(
            "tears create gaps;\nstretching distorts",
            font_size=18,
            color=curved_color,
            line_spacing=0.85,
        )
        impossible.move_to(RIGHT * 5.2 + DOWN * 2.1)

        top_rule = Text("intrinsically flat", font_size=22, color=flat_color)
        top_rule.move_to(RIGHT * 4.65 + UP * 0.8)
        bottom_rule = Text("intrinsically curved", font_size=22, color=curved_color)
        bottom_rule.move_to(RIGHT * 5.2 + DOWN * 2.8)

        self.add(
            title,
            sheet,
            sheet_label,
            cylinder,
            cylinder_label,
            roll_arrow,
            roll_label,
            preserved,
            top_rule,
            sphere,
            sphere_label,
            flatten_arrow,
            flatten_label,
            gores,
            tear_marks,
            impossible,
            bottom_rule,
        )
