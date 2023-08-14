import numpy as np
from manim import *

config["background_color"] = WHITE

class ConvergingCycleCorrect(Scene):
    # rendered at 1920 x 540
    def construct(self):
        config["frame_height"] = 4
        title = Tex(
            "Roommate matching: Phase 2",
            color=BLACK
        ).scale(0.8).to_edge(UP, buff=0.10)
        subtitle = Tex(
            "Example 1: Single cycle until convergence",
            color=BLACK
        ).scale(0.65).next_to(title, DOWN, buff=0.10)
        self.add(title)
        self.add(subtitle)

        A1 = Tex("1", color=BLACK, font_size=32)
        A2 = Tex("2", color=BLACK, font_size=32)
        A3 = Tex("3", color=BLACK, font_size=32)
        A4 = Tex("4", color=BLACK, font_size=32)


        col_labels = [
            Tex("\\textbf{1}", color=BLACK, font_size=32),
            Tex("\\textbf{2}", color=BLACK, font_size=32),
            Tex("\\textbf{3}", color=BLACK, font_size=32),
            Tex("\\textbf{4}", color=BLACK, font_size=32)
        ]

        # cross for no match
        cross = VGroup(
            Line(1.2*UP + 1.85*LEFT, 1.2*DOWN + 1.85*RIGHT, stroke_width=2),
            Line(1.2*UP + 1.85*RIGHT, 1.2*DOWN + 1.85*LEFT, stroke_width=2),
        ).scale(0.2)
        cross.set_color(RED)

        ###########
        # initial table
        ###########

        t1 = MobjectTable(
            [
                [A3.copy(), A4.copy(), A2.copy(), A1.copy()],
                [A4.copy(), A3.copy(), A1.copy(), A2.copy()]
            ],
            col_labels=[label.copy() for label in col_labels],
            line_config={"stroke_color": BLACK, "stroke_width": 2},
            include_outer_lines=True
        ).scale(0.65).to_edge(LEFT, buff=0.1).shift(0.75*DOWN)
        # coloring of cells
        for i in range(1,5):
            t1.add_highlighted_cell((1,i), color=GREEN)

        self.add(t1)

        # header 1
        header1 = Tex("Initial preferences in phase 2", color=BLACK, font_size=24).next_to(t1, UP, buff=0.15)
        self.add(header1)

        ###########
        # arrow and description
        ###########

        ar0 = Arrow(
            t1.get_right(),
            t1.get_right() + 2.2*RIGHT,
            color=BLACK,
            stroke_width=2,
            max_tip_length_to_length_ratio=0.1
        )
        self.add(ar0)

        desc0 = Tex("set up p-q table", color=BLACK, font_size=24).next_to(ar0, UP, buff=0.1)
        desc1 = Tex("to detect cycles", color=BLACK, font_size=24).next_to(ar0, DOWN, buff=0.1)
        self.add(desc0)
        self.add(desc1)

        ###########
        # p-q table
        ###########

        t2 = MobjectTable(
            [
                [A1.copy(), A4.copy()],
                [A2.copy(), A3.copy()],
                [A1.copy(), Tex("?", color=WHITE)]
            ],
            col_labels=[
                Tex("\\textbf{p}", color=BLACK, font_size=32),
                Tex("\\textbf{q}", color=BLACK, font_size=32)],
            line_config={"stroke_color": BLACK, "stroke_width": 2},
            include_outer_lines=False,
        ).scale(0.65).next_to(ar0, RIGHT, buff=0.25).shift(0.275*UP)

        # highlight the cells with re-appearing agent 1
        t2.add_highlighted_cell((2,1), color=YELLOW)
        t2.add_highlighted_cell((4,1), color=YELLOW)

        ar1 = Arrow(t2.get_cell((2,2)).get_center(), t2.get_cell((3,1)).get_center(), color=RED, stroke_width=1)
        ar2 = Arrow(t2.get_cell((3,2)).get_center(), t2.get_cell((4,1)).get_center(), color=RED, stroke_width=1)

        self.add(t2)
        self.add(ar1)
        self.add(ar2)

        ###########
        # arrow and description
        ###########

        ar3 = Arrow(
            t2.get_right(),
            t2.get_right() + 2.2*RIGHT,
            color=BLACK,
            stroke_width=2,
            max_tip_length_to_length_ratio=0.1
        ).shift(
            0.25*DOWN
        )
        self.add(ar3)

        desc2 = Tex("$q_i$ deletes $p_{i+1}$", color=BLACK, font_size=24).next_to(ar3, UP, buff=0.1)
        desc3 = Tex("(and vice versa)", color=BLACK, font_size=24).next_to(ar3, DOWN, buff=0.1)
        self.add(desc2)
        self.add(desc3)

        ###########
        # final table
        ###########

        t3 = t1.copy().next_to(ar3, RIGHT, buff=0.25)

        t3.add_highlighted_cell((3,1), color=MAROON_A)
        t3.add_highlighted_cell((2,4), color=MAROON_A)
        t3.add_highlighted_cell((3,2), color=YELLOW_A)
        t3.add_highlighted_cell((2,3), color=YELLOW_A)

        self.add(t3)

        # header for matching table
        header2 = Tex("Matching after phase 2", color=BLACK, font_size=24).next_to(t3, UP, buff=0.15)
        self.add(header2)

        # cross out deletions
        rejects = [(2,1), (2,2), (3,3), (3,4)]
        for reject in rejects:
            self.add(cross.copy().move_to(t3.get_cell(reject).get_center()))


class Phase2Example2(Scene):
    # rendered at 1920 x 1080
    def construct(self):
        title = Tex(
            "Roommate matching: Phase 2",
            color=BLACK
        ).scale(0.8).to_edge(UP, buff=0.10)
        subtitle = Tex(
            "Example 2: Two cycles until convergence",
            color=BLACK
        ).scale(0.65).next_to(title, DOWN, buff=0.10)
        self.add(title)
        self.add(subtitle)

        A1 = Tex("1", color=BLACK, font_size=32)
        A2 = Tex("2", color=BLACK, font_size=32)
        A3 = Tex("3", color=BLACK, font_size=32)
        A4 = Tex("4", color=BLACK, font_size=32)


        col_labels = [
            Tex("\\textbf{1}", color=BLACK, font_size=32),
            Tex("\\textbf{2}", color=BLACK, font_size=32),
            Tex("\\textbf{3}", color=BLACK, font_size=32),
            Tex("\\textbf{4}", color=BLACK, font_size=32)
        ]

        No_one = Tex("?", color=WHITE, font_size=32)

        # cross for no match
        cross = VGroup(
            Line(1.2*UP + 1.85*LEFT, 1.2*DOWN + 1.85*RIGHT, stroke_width=2),
            Line(1.2*UP + 1.85*RIGHT, 1.2*DOWN + 1.85*LEFT, stroke_width=2),
        ).scale(0.2)
        cross.set_color(RED)

        ###########
        # initial table
        ###########

        t1 = MobjectTable(
            [
                [A3.copy(), A4.copy(), A2.copy(), A1.copy()],
                [A4.copy(), A3.copy(), A4.copy(), A3.copy()],
                [No_one.copy(), No_one.copy(), A1.copy(), A2.copy()]
            ],
            col_labels=[label.copy() for label in col_labels],
            include_outer_lines=True,
            line_config={"stroke_color": BLACK, "stroke_width": 2}
        ).scale(0.65).to_edge(LEFT, buff=0.35).shift(1*UP)
        # color the cells
        for i in range(1,5):
            t1.add_highlighted_cell((1,i), color=GREEN)

        self.add(t1)

        # header for initial table
        header1 = Tex("a) Initial Preferences", color=BLACK, font_size=24).next_to(t1, UP, buff=0.15)
        self.add(header1)

        ###########
        # first pq table
        ###########

        pq1 = MobjectTable(
            [
                [A1.copy(), A4.copy()],
                [A2.copy(), A3.copy()],
                [A1.copy(), No_one.copy()]
            ],
            col_labels = [
                Tex("\\textbf{p}", color=BLACK, font_size=32),
                Tex("\\textbf{q}", color=BLACK, font_size=32)
            ],
            include_outer_lines=False,
            line_config={"stroke_color": BLACK, "stroke_width": 2}
        ).scale(0.65).next_to(t1, RIGHT, buff=0.35)

        # color the cells
        pq1.add_highlighted_cell((2,1), color=YELLOW)
        pq1.add_highlighted_cell((4,1), color=YELLOW)

        ar1 = Arrow(
            pq1.get_cell((2,2)).get_center(),
            pq1.get_cell((3,1)).get_center(),
            color=RED, stroke_width=1)
        ar2 = Arrow(
            pq1.get_cell((3,2)).get_center(),
            pq1.get_cell((4,1)).get_center(),
            color=RED, stroke_width=1)

        self.add(pq1)
        self.add(ar1)
        self.add(ar2)

        ###########
        # second table
        ###########

        # arrow between pq1 and t2
        arw = Arrow(
            pq1.get_right() + 0.15*RIGHT,
            pq1.get_right() + 1.5*RIGHT,
            color=BLACK, stroke_width=2,
            max_tip_length_to_length_ratio=0.175
        )
        self.add(arw)

        t2 = MobjectTable(
            [
                [A3.copy(), A4.copy(), A2.copy(), A1.copy()],
                [A4.copy(), A3.copy(), A4.copy(), A3.copy()],
                [No_one.copy(), No_one.copy(), A1.copy(), A2.copy()]
            ],
            col_labels=[label.copy() for label in col_labels],
            include_outer_lines=True,
            line_config={"stroke_color": BLACK, "stroke_width": 2}
        ).scale(0.65).next_to(arw, RIGHT, buff=0.25)
        #color the cells
        for i in range(1,5):
            t2.add_highlighted_cell((1,i), color=GREEN)

        self.add(t2)

        # cross out rejects from first cycle
        rejects = [
            (2,1),
            (2,2),
            (4,3),
            (4,4)
        ]
        for reject in rejects:
            self.add(cross.copy().move_to(t2.get_cell(reject)))

        # header for second table
        header2 = Tex("b) First cycle deletions", color=BLACK, font_size=24).next_to(t2, UP, buff=0.15)
        self.add(header2)

        ###########
        # second pq table
        ###########

        pq2 = MobjectTable(
            [
                [A3.copy(), A4.copy()],
                [A3.copy(), No_one.copy()],
            ],
            col_labels = [
                Tex("\\textbf{p}", color=BLACK, font_size=32),
                Tex("\\textbf{q}", color=BLACK, font_size=32)
            ],
            include_outer_lines=False,
            line_config={"stroke_color": BLACK, "stroke_width": 2}
        ).scale(0.6).next_to(t2, RIGHT, buff=0.35).shift(0.35*UP)

        # color cells
        pq2.add_highlighted_cell((2,1), color=YELLOW)
        pq2.add_highlighted_cell((3,1), color=YELLOW)

        self.add(pq2)

        ar3 = Arrow(
            pq2.get_cell((2,2)).get_center(),
            pq2.get_cell((3,1)).get_center(),
            color=RED, stroke_width=1
        )
        self.add(ar3)

        ###########
        # third table
        ###########

        t3 = MobjectTable(
            [
                [No_one.copy(), No_one.copy(), A2.copy(), A1.copy()],
                [A4.copy(), A3.copy(), A4.copy(), A3.copy()]
            ],
            col_labels=[label.copy() for label in col_labels],
            include_outer_lines=True,
            line_config={"stroke_color": BLACK, "stroke_width": 2}
        ).scale(0.65).next_to(t1, DOWN, buff=1.15).shift(1.25*RIGHT)
        #color the cells
        for i in range(1,5):
            t3.add_highlighted_cell((1,i), color=GREEN)

        self.add(t3)

        # arrow to t3
        arw = Arrow(
            t3.get_left() + 1.5*LEFT,
            t3.get_left() + 0.15*LEFT,
            color=BLACK, stroke_width=2,
            max_tip_length_to_length_ratio=0.175
        )
        self.add(arw)

        # header for third table
        header3 = Tex("c) Second cycle deletions", color=BLACK, font_size=24).next_to(t3, UP, buff=0.15)
        self.add(header3)

        # cross out rejects from second cycle
        rejects = [
            (3,3),
            (3,4)
        ]
        for reject in rejects:
            self.add(cross.copy().move_to(t3.get_cell(reject)))

        ###
        # arrow to final table

        ar4 = Arrow(
            t3.get_right() + 0.15*RIGHT,
            t3.get_right() + 1.5*RIGHT,
            color=BLACK, stroke_width=2,
            max_tip_length_to_length_ratio=0.175
        )
        self.add(ar4)

        ###########
        # final table
        ###########

        t4 = MobjectTable(
            [
                [No_one.copy(), No_one.copy(), A2.copy(), A1.copy()],
                [A4.copy(), A3.copy(), No_one.copy(), No_one.copy()]
            ],
            col_labels=[label.copy() for label in col_labels],
            include_outer_lines=True,
            line_config={"stroke_color": BLACK, "stroke_width": 2}
        ).scale(0.65).next_to(ar4, RIGHT, buff=0.5)
        # color the cells
        for i in range(1,5):
            t4.add_highlighted_cell((1,i), color=GREEN)

        # color the matches
        t4.add_highlighted_cell((3,1), color=YELLOW_A)
        t4.add_highlighted_cell((3,2), color=MAROON_A)
        t4.add_highlighted_cell((2,3), color=MAROON_A)
        t4.add_highlighted_cell((2,4), color=YELLOW_A)

        self.add(t4)

        # header for final table
        header4 = Tex("d) Stable matches", color=BLACK, font_size=24).next_to(t4, UP, buff=0.15)
        self.add(header4)


class Phase2Example3(Scene):
    def construct(self):
        config['frame_height'] = 6
        title = Tex(
            "Roommate matching: Phase 2",
            color=BLACK
        ).scale(0.8).to_edge(UP, buff=1.15)
        subtitle = Tex(
            "Example 3: Cycle with a tail",
            color=BLACK
        ).scale(0.65).next_to(title, DOWN, buff=0.10)
        self.add(title)
        self.add(subtitle)

        A1 = Tex("1", color=BLACK, font_size=32)
        A2 = Tex("2", color=BLACK, font_size=32)
        A3 = Tex("3", color=BLACK, font_size=32)
        A4 = Tex("4", color=BLACK, font_size=32)

        No_one = Tex("?", color=WHITE, font_size=32)

        col_labels = [
            Tex("\\textbf{1}", color=BLACK, font_size=32),
            Tex("\\textbf{2}", color=BLACK, font_size=32),
            Tex("\\textbf{3}", color=BLACK, font_size=32),
            Tex("\\textbf{4}", color=BLACK, font_size=32)
        ]

        # cross for no match
        cross = VGroup(
            Line(1.2*UP + 1.85*LEFT, 1.2*DOWN + 1.85*RIGHT, stroke_width=2),
            Line(1.2*UP + 1.85*RIGHT, 1.2*DOWN + 1.85*LEFT, stroke_width=2),
        ).scale(0.2)
        cross.set_color(RED)

        ###########
        # first table
        ###########

        t1 = MobjectTable(
            [
                [A3.copy(), A3.copy(), A2.copy(), A1.copy()],
                [A4.copy(), A4.copy(), A1.copy(), A2.copy()]
            ],
            col_labels=[label.copy() for label in col_labels],
            include_outer_lines=True,
            line_config={"stroke_color": BLACK, "stroke_width": 2}
        ).scale(0.65).to_edge(LEFT, buff=1).shift(0.75*DOWN)
        # color the cells
        for i in range(1,5):
            t1.add_highlighted_cell((1,i), color=GREEN)

        self.add(t1)

        # header for first table
        header1 = Tex("a) Preferences at start of phase 2", color=BLACK, font_size=24).next_to(t1, UP, buff=0.15)
        self.add(header1)

        ###########
        # pq table
        ###########
        pq = MobjectTable(
            [
                [A1.copy(), A4.copy()],
                [A2.copy(), A4.copy()],
                [A2.copy(), No_one.copy()]
            ],
            col_labels=[
                Tex("\\textbf{p}", color=BLACK, font_size=32),
                Tex("\\textbf{q}", color=BLACK, font_size=32)
            ],
            include_outer_lines=False,
            line_config={"stroke_color": BLACK, "stroke_width": 2}
        ).scale(0.65).next_to(t1, RIGHT, buff=0.5).shift(0.3*UP)

        # color cycle cells
        pq.add_highlighted_cell((3,1), color=YELLOW)
        pq.add_highlighted_cell((4,1), color=YELLOW)
        # color tail cells in second row
        pq.add_highlighted_cell((2,2), color=MAROON_A)
        pq.add_highlighted_cell((2,1), color=MAROON_A)

        self.add(pq)

        # deletion arrows in pq table
        ar1 = Arrow(
            pq.get_cell((3,2)).get_center(),
            pq.get_cell((4,1)).get_center(),
            color=RED, stroke_width=1
        )
        self.add(ar1)

        # indicator for tail
        ar4 = Arrow(
            pq.get_cell((2,2)).get_right() + 0.6*RIGHT,
            pq.get_cell((2,2)).get_right() + 0.15*RIGHT,
            color=BLACK, stroke_width=2
        )
        self.add(ar4)
        tail = Tex("Tail", color=BLACK, font_size=24).next_to(ar4, RIGHT, buff=0.15)
        self.add(tail)

        ###########
        # second table
        ###########

        t2 = t1.copy().next_to(t1, RIGHT, buff=4.5)
        self.add(t2)

        rejects = [
            (3,2), (3,4)
        ]
        for reject in rejects:
            self.add(cross.copy().move_to(t2.get_cell(reject)))

        # header for second table
        header2 = Tex("b) Deletions", color=BLACK, font_size=24).next_to(t2, UP, buff=0.15)
        self.add(header2)