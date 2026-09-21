from manim import *
from diagram_text import Text


class ConnectionIndices(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        ink = "#0f172a"
        slate = "#64748b"
        blue = "#2563eb"
        purple = "#7c3aed"
        green = "#059669"

        title = Text("What the three connection indices mean", font_size=32, color=ink)
        title.to_edge(UP, buff=0.3)

        equation = MathTex(
            r"\nabla_{\partial_\mu}\partial_\nu",
            "=",
            r"\Gamma^\rho{}_{\mu\nu}",
            r"\partial_\rho",
            font_size=42,
        ).move_to([0, 2.25, 0])
        equation[0].set_color(blue)
        equation[2].set_color(purple)
        equation[3].set_color(green)

        def card(x, heading, body, color):
            box = RoundedRectangle(
                width=3.45, height=2.5, corner_radius=0.15,
                stroke_color=color, stroke_width=2,
                fill_color="#f8fafc", fill_opacity=1,
            ).move_to([x, -0.25, 0])
            h = MathTex(heading, font_size=34, color=color).move_to([x, 0.45, 0])
            b = Text(body, font_size=22, color=slate).move_to([x, -0.35, 0])
            return VGroup(box, h, b)

        left = card(-4.2, r"\mu", "direction\nof differentiation", blue)
        middle = card(0, r"\nu", "basis vector\nbeing differentiated", purple)
        right = card(4.2, r"\rho", "component of\nthe output vector", green)

        leaders = VGroup(
            DashedLine([-4.2, 1.62, 0], [-1.6, 2.02, 0], color=blue, stroke_width=3),
            DashedLine([0, 1.02, 0], [0, 1.72, 0], color=purple, stroke_width=3),
            DashedLine([4.2, 1.02, 0], [1.42, 2.02, 0], color=green, stroke_width=3),
        )

        note = Text(
            "The index positions show how each slot is used.\n"
            "Christoffel symbols still are not tensors: their coordinate change\n"
            "contains extra second-derivative terms.",
            font_size=22, color=slate,
        ).move_to([0, -2.35, 0])

        self.add(title, equation, leaders, left, middle, right, note)
