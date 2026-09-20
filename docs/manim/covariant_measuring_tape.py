from manim import *

from diagram_text import Text


class CovariantMeasuringTape(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        ink = BLACK
        mark_color = "#2563eb"
        vector_color = "#dc2626"
        covector_color = "#7c3aed"
        muted = "#64748b"

        title = Text("The same measurement with a rescaled tape", font_size=32, color=ink)
        title.to_edge(UP, buff=0.28)

        left = -5.7
        right = 1.0
        width = right - left
        box_height = 1.75
        top_y = 1.35
        bottom_y = -1.45

        def tape_box(y, marks):
            box = Rectangle(width=width, height=box_height, color=ink, stroke_width=3)
            box.move_to([(left + right) / 2, y, 0])
            lines = VGroup(*[
                Line([x, y - box_height / 2, 0], [x, y + box_height / 2, 0], color=mark_color, stroke_width=4)
                for x in marks
            ])
            return VGroup(box, lines)

        top_marks = [-4.7, -3.1, -1.5, 0.1]
        bottom_marks = [-4.7, -3.9, -3.1, -2.3, -1.5, -0.7, 0.1]
        top_tape = tape_box(top_y, top_marks)
        bottom_tape = tape_box(bottom_y, bottom_marks)

        top_heading = MathTex(r"x", color=ink, font_size=34)
        top_heading.next_to(top_tape, UP, buff=0.18)
        top_form = MathTex(r"\omega=dx", color=covector_color, font_size=34)
        top_form.next_to(top_heading, RIGHT, buff=0.24)

        bottom_heading = MathTex(r"x'=2x", color=ink, font_size=34)
        bottom_heading.next_to(bottom_tape, DOWN, buff=0.18)
        bottom_form = MathTex(r"\omega=\tfrac12 dx'", color=covector_color, font_size=34)
        bottom_form.next_to(bottom_heading, RIGHT, buff=0.24)

        start_x = -4.7
        end_x = -1.5
        top_vector = Arrow(
            [start_x, top_y, 0],
            [end_x, top_y, 0],
            buff=0,
            color=vector_color,
            stroke_width=7,
        )
        bottom_vector = Arrow(
            [start_x, bottom_y, 0],
            [end_x, bottom_y, 0],
            buff=0,
            color=vector_color,
            stroke_width=7,
        )
        top_vector_label = MathTex(r"V^x=2", color=vector_color, font_size=31)
        top_vector_label.next_to(top_vector, DOWN, buff=0.12)
        bottom_vector_label = MathTex(r"V^{x'}=4", color=vector_color, font_size=31)
        bottom_vector_label.next_to(bottom_vector, UP, buff=0.12)

        guides = VGroup(
            DashedLine([start_x, top_y - 1.1, 0], [start_x, bottom_y + 1.1, 0], color="#cbd5e1", stroke_width=2),
            DashedLine([end_x, top_y - 1.1, 0], [end_x, bottom_y + 1.1, 0], color="#cbd5e1", stroke_width=2),
        )

        result_heading = Text("The physical measurement is unchanged", font_size=26, color=ink)
        result_heading.move_to([4.55, 1.55, 0])
        top_result = MathTex(r"\omega_xV^x=1\times2=2", color=ink, font_size=35)
        top_result.move_to([4.55, 0.75, 0])
        bottom_result = MathTex(r"\omega_{x'}V^{x'}=\tfrac12\times4=2", color=ink, font_size=35)
        bottom_result.move_to([4.55, -0.05, 0])
        explanation = MathTex(
            r"\begin{gathered}"
            r"\text{Finer coordinate marks make the vector component larger}\\"
            r"\text{and the covector component smaller.}"
            r"\end{gathered}",
            font_size=18,
            color=muted,
        )
        explanation.move_to([4.55, -1.35, 0])
        invariant = MathTex(r"\omega_{x'}V^{x'}=\omega_xV^x", color=vector_color, font_size=36)
        invariant.move_to([4.55, -2.45, 0])

        self.add(
            title,
            guides,
            top_tape,
            bottom_tape,
            top_heading,
            top_form,
            bottom_heading,
            bottom_form,
            top_vector,
            bottom_vector,
            top_vector_label,
            bottom_vector_label,
            result_heading,
            top_result,
            bottom_result,
            explanation,
            invariant,
        )
