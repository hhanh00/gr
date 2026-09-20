from manim import *

from diagram_text import Text


class OneFormMeasuringTape(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        ink = BLACK
        mark_color = "#2563eb"
        parallel_color = "#d97706"
        crossing_color = "#dc2626"
        muted = "#64748b"

        title = Text("A one-form as a measuring tape", font_size=32, color=ink)
        title.to_edge(UP, buff=0.28)

        left = -5.6
        right = 1.1
        bottom = -2.55
        top = 2.25
        surface = Rectangle(width=right - left, height=top - bottom, color=ink, stroke_width=3)
        surface.move_to([(left + right) / 2, (top + bottom) / 2, 0])

        # The level lines x = constant visualize the one-form dx.
        marks = VGroup()
        for x in [-4.8, -3.7, -2.6, -1.5, -0.4, 0.7]:
            marks.add(Line([x, bottom, 0], [x, top, 0], color=mark_color, stroke_width=4))
        form_label = MathTex(r"dx", color=mark_color, font_size=38)
        form_label.next_to(marks, UP, buff=0.18)
        mark_label = Text("equally spaced marks: x = constant", font_size=21, color=mark_color)
        mark_label.next_to(form_label, RIGHT, buff=0.22)

        parallel_start = [-3.7, -1.75, 0]
        parallel_end = [-3.7, 0.65, 0]
        parallel_vector = Arrow(
            parallel_start,
            parallel_end,
            buff=0,
            color=parallel_color,
            stroke_width=7,
        )
        parallel_label = MathTex(r"V_\parallel", color=parallel_color, font_size=32)
        parallel_label.next_to(parallel_vector.get_end(), RIGHT, buff=0.14)
        parallel_result = MathTex(r"dx(V_\parallel)=0", color=parallel_color, font_size=33)
        parallel_result.move_to([-3.75, -2.02, 0])

        crossing_start = [-4.8, -0.65, 0]
        crossing_end = [-1.5, -0.65, 0]
        crossing_vector = Arrow(
            crossing_start,
            crossing_end,
            buff=0,
            color=crossing_color,
            stroke_width=7,
        )
        crossing_label = MathTex(r"V_\perp", color=crossing_color, font_size=32)
        crossing_label.move_to([-2.10, -0.22, 0])
        crossing_result = MathTex(r"dx(V_\perp)=3", color=crossing_color, font_size=33)
        crossing_result.move_to([-2.05, -1.38, 0])

        arrow = Arrow([1.65, -0.15, 0], [2.55, -0.15, 0], buff=0, color=muted, stroke_width=4)
        explanation_heading = Text("What dx measures", font_size=27, color=ink)
        explanation_heading.move_to([4.45, 1.55, 0])
        explanation = MathTex(
            r"\begin{gathered}"
            r"\text{Counts marked intervals}\\"
            r"\text{crossed by a vector.}\\[0.45em]"
            r"\text{Measures one component,}\\"
            r"\text{not a full length.}"
            r"\end{gathered}",
            font_size=23,
            color=muted,
        )
        explanation.move_to([4.45, -0.15, 0])
        note = Text("A metric is needed for lengths and angles.", font_size=20, color=ink)
        note.move_to([4.45, -2.35, 0])

        self.add(
            title,
            surface,
            marks,
            form_label,
            mark_label,
            parallel_vector,
            parallel_label,
            parallel_result,
            crossing_vector,
            crossing_label,
            crossing_result,
            arrow,
            explanation_heading,
            explanation,
            note,
        )
