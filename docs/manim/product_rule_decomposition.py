import numpy as np
from manim import *
from diagram_text import Text


class ProductRuleDecomposition(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        ink = "#0f172a"
        slate = "#64748b"
        purple = "#7c3aed"
        green = "#059669"
        blue = "#2563eb"

        def prose(content, x, y, size=24, color=ink):
            return Text(content, font_size=size, color=color).move_to([x, y, 0])

        def math(content, x, y, color=ink, size=30):
            return MathTex(content, font_size=size, color=color).move_to([x, y, 0])

        def arrow(start, end, color):
            return Arrow(
                start, end, buff=0, color=color, stroke_width=6,
                max_tip_length_to_length_ratio=0.16,
            )

        self.add(
            prose("Why the product rule has two terms", 0, 3.35, 34),
            prose("Differentiate along X; compare all contributions at the same point.",
                  0, 2.8, 23, slate),
        )

        centers = [-4.5, 0, 4.5]
        headings = ["1. Change the scalar", "2. Change the vector", "3. Add the contributions"]
        terms = [r"X[f]\,V", r"f\,\nabla_XV", r"\nabla_X(fV)"]
        colors = [purple, green, blue]
        for x, heading, term, color in zip(centers, headings, terms, colors):
            card = RoundedRectangle(
                width=4.12, height=4.35, corner_radius=0.16,
                stroke_color="#e2e8f0", stroke_width=1.5,
                fill_color="#f8fafc", fill_opacity=1,
            ).move_to([x, 0.15, 0])
            self.add(card, prose(heading, x, 1.92, 25),
                     math(term, x, 1.35, color))

        # These arrows are derivative vectors at one point, not finite
        # endpoint differences. Choose a Euclidean example with unit V
        # turning, so the vector-change contribution is perpendicular to V.
        a = np.array([1.65, 0, 0])
        b = np.array([0, 1.45, 0])
        origins = [np.array([x - 0.85, -0.85, 0]) for x in centers]

        # A faint reference indicates V's direction without pretending that
        # the direction X of differentiation is a component of the result.
        for origin in origins[:2]:
            reference = DashedLine(
                origin, origin + 2.35 * RIGHT,
                color=slate, stroke_width=2, dash_length=0.09,
            )
            self.add(reference, math("V", origin[0] + 2.35, -1.17, slate, 25))

        self.add(
            arrow(origins[0], origins[0] + a, purple),
            Dot(origins[0], color=ink, radius=0.035),
            prose("Scaling contributes along V.", centers[0], -1.65, 22, slate),
            arrow(origins[1], origins[1] + b, green),
            Dot(origins[1], color=ink, radius=0.035),
            prose("Here, V turns at fixed length.", centers[1], -1.65, 22, slate),
        )

        origin = origins[2]
        self.add(
            DashedLine(origin, origin + b, color=green,
                       stroke_width=2, dash_length=0.09, stroke_opacity=0.35),
            DashedLine(origin + b, origin + a + b, color=purple,
                       stroke_width=2, dash_length=0.09, stroke_opacity=0.35),
            arrow(origin, origin + a, purple),
            arrow(origin + a, origin + a + b, green),
            arrow(origin, origin + a + b, blue),
            Dot(origin, color=ink, radius=0.035),
            prose("Place the two terms tip to tail.", centers[2], -1.65, 22, slate),
        )

        formula = MathTex(
            r"\nabla_X(fV)", "=", r"X[f]\,V", "+", r"f\,\nabla_XV",
            font_size=37, color=ink,
        ).move_to([0, -2.65, 0])
        formula[0].set_color(blue)
        formula[2].set_color(purple)
        formula[4].set_color(green)
        self.add(
            formula,
            prose("The arrows show rates of change, not finite displacements.",
                  0, -3.23, 22, slate),
            prose("In general, the vector term can change both length and direction.",
                  0, -3.62, 22, slate),
        )
