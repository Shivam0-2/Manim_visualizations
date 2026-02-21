from manim import *

class BinarySearch(Scene):
    def construct(self):

        arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

        low_index = 0
        high_index = len(arr) - 1

        # ---------------------------
        # Create Array Boxes
        # ---------------------------

        boxes = VGroup()
        for num in arr:
            box = Square(side_length=1)
            box.set_stroke(width=2)
            box.set_fill(opacity=0)

            label = Text(str(num), font_size=28)
            box.add(label)
            boxes.add(box)

        boxes.arrange(RIGHT, buff=0.3)
        boxes.shift(UP * 0.5)

        self.play(Create(boxes))
        self.wait(1)

        # ---------------------------
        # Create Arrows + Labels Groups
        # ---------------------------

        # Low
        low_arrow = Arrow(UP, DOWN, color=BLUE)
        low_label = Text("Low", font_size=24, color=BLUE)
        low_group = VGroup(low_arrow, low_label)
        low_label.next_to(low_arrow, DOWN, buff=0.1)
        low_label.shift(DOWN * 0.5)  # slight offset

        # Mid
        mid_arrow = Arrow(UP, DOWN, color=YELLOW)
        mid_label = Text("Mid", font_size=24, color=YELLOW)
        mid_group = VGroup(mid_arrow, mid_label)
        mid_label.next_to(mid_arrow, DOWN, buff=0.1)

        # High
        high_arrow = Arrow(UP, DOWN, color=RED)
        high_label = Text("High", font_size=24, color=RED)
        high_group = VGroup(high_arrow, high_label)
        high_label.next_to(high_arrow, DOWN, buff=0.1)
        high_label.shift(DOWN * 0.9)  # larger offset

        # Initial positions (same arrow level)
        low_group.next_to(boxes[low_index], DOWN, buff=0.9)
        high_group.next_to(boxes[high_index], DOWN, buff=0.9)

        self.play(Create(low_group), Create(high_group))
        self.wait(1)

        # ---------------------------
        # Status Text
        # ---------------------------

        status_text = Text("", font_size=30).to_edge(UP)
        self.add(status_text)

        target = 7
        start_text = Text(f"Searching for {target}", font_size=30).to_edge(UP)
        self.play(Transform(status_text, start_text))
        self.wait(1)

        # ---------------------------
        # Binary Search Loop
        # ---------------------------

        mid_created = False

        while low_index <= high_index:

            mid_index = (low_index + high_index) // 2

            # Create or move mid group
            if not mid_created:
                mid_group.next_to(boxes[mid_index], DOWN, buff=0.9)
                self.play(Create(mid_group))
                mid_created = True
            else:
                self.play(mid_group.animate.next_to(boxes[mid_index], DOWN, buff=0.9))

            self.wait(0.5)

            # Highlight mid
            self.play(boxes[mid_index][0].animate.set_color(YELLOW))
            self.wait(0.5)

            # FOUND
            if target == arr[mid_index]:
                found_text = Text("Element Found!", font_size=30, color=GREEN).to_edge(UP)
                self.play(
                    boxes[mid_index][0].animate.set_color(GREEN),
                    Transform(status_text, found_text)
                )
                self.wait(2)
                break

            # TARGET GREATER
            elif target > arr[mid_index]:

                explanation = Text(
                    f"{target} > {arr[mid_index]} → Move Low Right",
                    font_size=28
                ).to_edge(UP)

                self.play(Transform(status_text, explanation))

                low_index = mid_index + 1
                self.play(low_group.animate.next_to(boxes[low_index], DOWN, buff=0.9))

            # TARGET SMALLER
            else:

                explanation = Text(
                    f"{target} < {arr[mid_index]} → Move High Left",
                    font_size=28
                ).to_edge(UP)

                self.play(Transform(status_text, explanation))

                high_index = mid_index - 1
                self.play(high_group.animate.next_to(boxes[high_index], DOWN, buff=0.9))

            # Reset mid color
            self.play(boxes[mid_index][0].animate.set_color(WHITE))
            self.wait(0.3)

        # Not Found
        if low_index > high_index:
            not_found = Text("Element Not Found", font_size=30, color=RED).to_edge(UP)
            self.play(Transform(status_text, not_found))
            self.wait(2)
