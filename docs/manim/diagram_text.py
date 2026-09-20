from manim import Tex, VGroup, DOWN


def Text(content, font_size=24, color=None, line_spacing=1.0, **_):
    """Render prose through LaTeX so it matches MathTex in static diagrams."""
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
        "−": "-",
        "–": "--",
        "—": "---",
        "’": "'",
        "“": "``",
        "”": "''",
    }

    def escape(line):
        return "".join(replacements.get(character, character) for character in line)

    lines = [
        Tex(r"\text{" + escape(line) + "}", font_size=font_size, color=color)
        for line in content.split("\n")
    ]
    if len(lines) == 1:
        return lines[0]
    group = VGroup(*lines)
    for previous, line in zip(lines, lines[1:]):
        line.next_to(previous, DOWN, buff=0.12 * line_spacing)
    return group
