from manim import *


class ConnectionIndices3D(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        ink = "#0f172a"
        blue = "#2563eb"
        purple = "#7c3aed"
        green = "#059669"
        slate = "#94a3b8"

        title = Text("Connection indices on a sphere", font_size=32, color=ink)
        title.to_edge(UP, buff=0.28)

        sphere = Circle(radius=2.05, color=slate, stroke_width=3)
        sphere.set_fill("#dbeafe", opacity=0.7)
        sphere.move_to([-1.7, 0.15, 0])

        # Longitude and latitude curves make the 2D drawing read as a sphere.
        grid = VGroup()
        for width in [0.65, 1.25, 1.75]:
            grid.add(Ellipse(width=width, height=4.0, color=slate, stroke_width=1.2, stroke_opacity=0.45).move_to(sphere.get_center()))
        for height in [0.65, 1.25, 1.75]:
            grid.add(Ellipse(width=4.1, height=height, color=slate, stroke_width=1.2, stroke_opacity=0.45).move_to(sphere.get_center()))

        event = np.array([-0.65, 1.05, 0])
        tangent_plane = DashedLine(event + np.array([-0.72, -0.22, 0]), event + np.array([1.25, 0.52, 0]), color=slate, stroke_width=3, dash_length=0.12)
        tangent_plane_2 = DashedLine(event + np.array([-0.55, 0.48, 0]), event + np.array([0.88, -0.65, 0]), color=slate, stroke_width=3, dash_length=0.12)
        point = Dot(event, radius=0.08, color=ink)

        x_arrow = Arrow(event, event + np.array([0.85, 0.30, 0]), color=blue, buff=0, stroke_width=7)
        y_arrow = Arrow(event, event + np.array([-0.28, 0.88, 0]), color=purple, buff=0, stroke_width=7)
        z_arrow = Arrow(event, event + np.array([0.75, -0.45, 0]), color=green, buff=0, stroke_width=7)
        x_label = MathTex(r"\partial_x", color=blue, font_size=30).next_to(x_arrow.get_end(), RIGHT, buff=0.08)
        y_label = MathTex(r"\partial_y", color=purple, font_size=30).next_to(y_arrow.get_end(), LEFT, buff=0.08)
        z_label = MathTex(r"\partial_z", color=green, font_size=30).next_to(z_arrow.get_end(), DOWN, buff=0.08)

        equation = MathTex(r"\nabla_{\partial_x}\partial_y=\Gamma^z{}_{xy}\,\partial_z", font_size=38, color=ink)
        equation.move_to([4.15, 1.8, 0])
        equation[0][0:10].set_color(blue)
        equation[0][10:17].set_color(green)
        labels = VGroup(
            Text("μ = x: direction of differentiation", font_size=22, color=blue),
            Text("ν = y: basis vector being differentiated", font_size=22, color=purple),
            Text("ρ = z: output direction", font_size=22, color=green),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.17).move_to([3.95, 0.5, 0])

        note = Text("All three arrows are local tangent directions at one point on the sphere.", font_size=21, color=ink).to_edge(DOWN, buff=0.25)
        self.add(title, sphere, grid, tangent_plane, tangent_plane_2, point, x_arrow, y_arrow, z_arrow, x_label, y_label, z_label, equation, labels, note)
