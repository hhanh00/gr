from manim import *
import numpy as np
from diagram_text import Text


class GradientForm(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        ink = BLACK
        contour_color = "#2563eb"
        gradient_color = "#dc2626"
        tangent_color = "#d97706"
        covector_color = "#7c3aed"
        muted = "#64748b"

        title = Text("The differential and gradient of a scalar field", font_size=32, color=ink)
        title.to_edge(UP, buff=0.28)

        origin = LEFT * 3.2 + DOWN * 0.2
        axes = VGroup(
            Arrow(origin + LEFT * 2.4, origin + RIGHT * 2.5, buff=0, color=muted, stroke_width=3),
            Arrow(origin + DOWN * 2.1, origin + UP * 2.2, buff=0, color=muted, stroke_width=3),
        )
        x_label = MathTex("x", color=muted, font_size=30).next_to(axes[0].get_end(), RIGHT, buff=0.08)
        y_label = MathTex("y", color=muted, font_size=30).next_to(axes[1].get_end(), UP, buff=0.08)

        contours = VGroup()
        for radius, opacity in [(0.62, 0.45), (1.18, 0.7), (1.74, 1.0)]:
            contours.add(Circle(radius=radius, color=contour_color, stroke_width=3, stroke_opacity=opacity).move_to(origin))
        contour_label = MathTex("f=x^2+y^2", color=contour_color, font_size=34)
        contour_label.next_to(contours, DOWN, buff=0.23)
        level_label = Text("level curves: f = constant", font_size=21, color=contour_color)
        level_label.next_to(contour_label, DOWN, buff=0.08)

        angle = 38 * DEGREES
        p = origin + 1.18 * np.array([np.cos(angle), np.sin(angle), 0])
        radial = np.array([np.cos(angle), np.sin(angle), 0])
        tangent = np.array([-np.sin(angle), np.cos(angle), 0])
        p_dot = Dot(p, color=ink, radius=0.07)
        p_label = MathTex("p", color=ink, font_size=29).next_to(p_dot, UP + LEFT, buff=0.08)

        gradient_arrow = Arrow(
            p,
            p + radial * 1.35,
            buff=0,
            color=gradient_color,
            stroke_width=7,
            max_tip_length_to_length_ratio=0.14,
        )
        gradient_label = MathTex(r"\operatorname{grad}f", color=gradient_color, font_size=33)
        gradient_label.next_to(gradient_arrow, RIGHT, buff=0.12)

        tangent_arrow = Arrow(
            p - tangent * 0.62,
            p + tangent * 0.62,
            buff=0,
            color=tangent_color,
            stroke_width=6,
            max_tip_length_to_length_ratio=0.16,
        )
        tangent_label = MathTex(r"t", color=tangent_color, font_size=30)
        tangent_label.next_to(tangent_arrow.get_end(), UP, buff=0.06)

        # Parallel short marks visualize a covector as level-set information.
        covector_marks = VGroup()
        for offset in [-0.12, 0, 0.12]:
            center = p + radial * 0.24 + tangent * offset
            covector_marks.add(
                Line(
                    center - tangent * 0.12,
                    center + tangent * 0.12,
                    color=covector_color,
                    stroke_width=4,
                )
            )
        covector_label = MathTex("df", color=covector_color, font_size=32)
        covector_label.next_to(covector_marks, LEFT, buff=0.12)

        right_heading = Text("At p", font_size=28, color=ink)
        right_heading.move_to(RIGHT * 3.75 + UP * 1.55)
        df_rule = MathTex(r"df=2r\,dr", color=covector_color, font_size=38)
        df_rule.next_to(right_heading, DOWN, buff=0.25)
        df_explanation = Text(
            "df is a covector:\nits value is the rate of change\nalong an input vector.",
            font_size=22,
            color=muted,
            line_spacing=0.85,
        )
        df_explanation.next_to(df_rule, DOWN, buff=0.28)
        tangent_rule = MathTex(r"df(t)=0", color=tangent_color, font_size=36)
        tangent_rule.next_to(df_explanation, DOWN, buff=0.32)
        metric_rule = MathTex(r"g(\operatorname{grad}f,v)=df(v)", color=gradient_color, font_size=33)
        metric_rule.next_to(tangent_rule, DOWN, buff=0.42)
        metric_explanation = Text(
            "The Euclidean metric identifies\ndf with the outward gradient vector.",
            font_size=22,
            color=muted,
            line_spacing=0.85,
        )
        metric_explanation.next_to(metric_rule, DOWN, buff=0.20)

        self.add(
            title,
            axes,
            x_label,
            y_label,
            contours,
            contour_label,
            level_label,
            p_dot,
            p_label,
            tangent_arrow,
            tangent_label,
            covector_marks,
            covector_label,
            gradient_arrow,
            gradient_label,
            right_heading,
            df_rule,
            df_explanation,
            tangent_rule,
            metric_rule,
            metric_explanation,
        )
