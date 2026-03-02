from manim import *

class BFS(Scene):
    def construct(self):

        positions = {
            "A": LEFT * 4 + UP*1,
            "B": LEFT * 2 + UP*2,
            "C": RIGHT * 2 + DOWN*1,
            "D": RIGHT * 1 + UP*2,
            "E": RIGHT*1,
            "F": RIGHT * 3 + DOWN*1,
        }

        nodes = {}
        nodes_group = VGroup()

        for label, pos in positions.items():
            node = Circle(radius=0.5)
            text = Text(label, font_size=28)
            group = VGroup(node, text)
            group.move_to(pos)
            node.add(text)
            node.move_to(pos)

            nodes[label] = group
            nodes_group.add(group)
        
        self.play(Create(nodes_group))
        self.wait(1)

        edges_list = [("A", "B"), ("A", "C"), ("B", "D"), ("B", "E"), ("C", "F"),("E", "F")]
        edges = VGroup()

        for start, end in edges_list:
            arrow = arrow = Arrow(
                nodes[start].get_center(),
                nodes[end].get_center(),
                buff=0.6, stroke_width=3)
            edges.add(arrow)
        self.play(Create(edges))
        self.wait(2)