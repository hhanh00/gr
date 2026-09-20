from manim import *
from diagram_text import Text


class ContravariantRescaling(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        ink = BLACK
        axis_color = "#64748b"
        vector_color = "#2563eb"
        basis_color = "#7c3aed"
        guide_color = "#cbd5e1"

        title = Text("Same vector, rescaled coordinate", font_size=32, color=ink)
        title.to_edge(UP, buff=0.3)

        axis_left = -4.6
        axis_right = 4.6
        top_y = 1.25
        bottom_y = -1.35
        unit_x = 1.9
        unit_x_prime = unit_x / 2
        origin_x = -3.8

        def coordinate_axis(y, spacing, values, label):
            axis = Line([axis_left, y, 0], [axis_right, y, 0], color=axis_color, stroke_width=3)
            ticks = VGroup()
            labels = VGroup()
            for value in values:
                position = origin_x + value * spacing
                ticks.add(Line([position, y - 0.10, 0], [position, y + 0.10, 0], color=axis_color, stroke_width=3))
                number = MathTex(str(value), color=ink, font_size=25)
                number.next_to([position, y, 0], DOWN, buff=0.15)
                labels.add(number)
            axis_label = MathTex(label, color=ink, font_size=32)
            axis_label.next_to(axis.get_right(), RIGHT, buff=0.18)
            return VGroup(axis, ticks, labels, axis_label)

        top_axis = coordinate_axis(top_y, unit_x, range(5), "x")
        bottom_axis = coordinate_axis(bottom_y, unit_x_prime, range(9), "x'=2x")

        vector_start = [origin_x, 0, 0]
        vector_end_x = origin_x + 2 * unit_x

        top_vector = Arrow(
            [origin_x, top_y + 0.58, 0],
            [vector_end_x, top_y + 0.58, 0],
            buff=0,
            color=vector_color,
            stroke_width=7,
            max_tip_length_to_length_ratio=0.10,
        )
        top_vector_label = MathTex(r"V=2\,\partial_x", color=vector_color, font_size=34)
        top_vector_label.next_to(top_vector, UP, buff=0.10)

        top_basis = Arrow(
            [origin_x, top_y - 0.58, 0],
            [origin_x + unit_x, top_y - 0.58, 0],
            buff=0,
            color=basis_color,
            stroke_width=6,
            max_tip_length_to_length_ratio=0.18,
        )
        top_basis_label = MathTex(r"\partial_x", color=basis_color, font_size=30)
        top_basis_label.next_to(top_basis, DOWN, buff=0.08)

        bottom_vector = Arrow(
            [origin_x, bottom_y + 0.58, 0],
            [vector_end_x, bottom_y + 0.58, 0],
            buff=0,
            color=vector_color,
            stroke_width=7,
            max_tip_length_to_length_ratio=0.10,
        )
        bottom_vector_label = MathTex(r"V=4\,\partial_{x'}", color=vector_color, font_size=34)
        bottom_vector_label.next_to(bottom_vector, UP, buff=0.10)

        bottom_basis = Arrow(
            [origin_x, bottom_y - 0.58, 0],
            [origin_x + unit_x_prime, bottom_y - 0.58, 0],
            buff=0,
            color=basis_color,
            stroke_width=6,
            max_tip_length_to_length_ratio=0.30,
        )
        bottom_basis_label = MathTex(r"\partial_{x'}", color=basis_color, font_size=30)
        bottom_basis_label.next_to(bottom_basis, DOWN, buff=0.08)

        guides = VGroup(
            DashedLine(
                [origin_x, top_y + 0.85, 0],
                [origin_x, bottom_y - 0.82, 0],
                color=guide_color,
                stroke_width=2,
            ),
            DashedLine(
                [vector_end_x, top_y + 0.85, 0],
                [vector_end_x, bottom_y - 0.82, 0],
                color=guide_color,
                stroke_width=2,
            ),
        )

        note = Text(
            "same geometric arrow",
            font_size=21,
            color=axis_color,
        )
        note.move_to([vector_end_x + 2.3, 0.05, 0])
        same_length = DoubleArrow(
            [vector_end_x + 1.25, top_y + 0.58, 0],
            [vector_end_x + 1.25, bottom_y + 0.58, 0],
            buff=0,
            color=axis_color,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.12,
        )

        relation = MathTex(
            r"\partial_{x'}=\tfrac12\partial_x,\qquad V^{x'}=2V^x",
            color=ink,
            font_size=34,
        )
        relation.to_edge(DOWN, buff=0.26)

        self.add(
            title,
            guides,
            top_axis,
            bottom_axis,
            top_vector,
            top_vector_label,
            top_basis,
            top_basis_label,
            bottom_vector,
            bottom_vector_label,
            bottom_basis,
            bottom_basis_label,
            same_length,
            note,
            relation,
        )
