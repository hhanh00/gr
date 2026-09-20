from manim import *
import numpy as np


class TidalConvergence(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        ink = BLACK
        path_color = "#2563eb"
        ref_color = "#9ca3af"

        radius = 1.3
        sphere = Circle(radius=radius, color=ink, stroke_width=3)
        mass_label = MathTex("M", color=ink, font_size=36).move_to(sphere.get_center())

        starts = [np.array([-1.1, 3.0, 0]), np.array([1.1, 3.0, 0])]

        actual_paths = VGroup()
        actual_dots = VGroup()
        for start in starts:
            direction = start / np.linalg.norm(start)
            surface_point = direction * radius
            actual_paths.add(Line(start, surface_point, color=path_color, stroke_width=6))
            actual_dots.add(Dot(surface_point, color=path_color, radius=0.06))

        reference_paths = VGroup()
        for start in starts:
            end = np.array([start[0], starts[0][1] - 2.0 * radius, 0])
            reference_paths.add(DashedLine(start, end, color=ref_color, stroke_width=3))

        start_dots = VGroup(*[Dot(s, color=path_color, radius=0.06) for s in starts])

        diagram = VGroup(sphere, mass_label, reference_paths, actual_paths, actual_dots, start_dots)
        diagram.move_to(ORIGIN).shift(DOWN * 0.3)

        ref_label = Text("uniform field", font_size=24, color=ref_color)
        ref_label.next_to(reference_paths[1], RIGHT, buff=0.3).shift(UP * 0.6)

        actual_label = Text("spherical field", font_size=24, color=path_color)
        actual_label.next_to(actual_paths[1], RIGHT, buff=0.3).shift(DOWN * 0.4)

        title = Text("Tidal convergence", font_size=32, color=ink)
        title.next_to(diagram, UP, buff=0.6)

        self.add(diagram, ref_label, actual_label, title)
