import numpy as np
from manim import *

config["background_color"] = WHITE
config["frame_width"] = 12
config["frame_height"] = 10


# starting point: preferences of agents
class StartingPointVertical(Scene):
    def construct(self):
        np.random.seed(45)
        # figure header
        title = Tex("Roommate matching: preferences", color=BLACK).scale(0.85).to_edge(UP, buff=1.8)
        self.add(title)

        # Agents
        A1 = Tex("Agent 1", color=BLACK, font_size=32)
        A2 = Tex("Agent 2", color=BLACK, font_size=32)
        A3 = Tex("Agent 3", color=BLACK, font_size=32)
        A4 = Tex("Agent 4", color=BLACK, font_size=32)
        A5 = Tex("Agent 5", color=BLACK, font_size=32)

        No_one = Tex("", color=WHITE)

        # network header
        net_head = Tex("Example network", color=BLACK)
        net_head.next_to(title, DOWN, buff=0.2).scale(0.6)
        self.add(net_head)

        # network
        vertices: list = [1, 2, 3, 4, 5]
        edges: list[tuple] = [ (1, 2), (1, 3), (2, 3), (2, 5), (3, 4), (3, 5), (4, 5)]
        vertex_config: dict = {"color": BLACK, "fill_color": RED, "fill_opacity": 1}
        G = Graph(
            vertices,
            edges,
            labels=True,
            label_fill_color=BLACK,
            vertex_config=vertex_config,
            edge_config={"color": BLACK, "stroke_width": 2}
        )
        G.scale(0.5)
        self.add(G.next_to(net_head, DOWN, buff=0.15))

        # table header
        tab_head = Tex("Preferences", color=BLACK)#.to_edge(LEFT, buff=3.5)
        tab_head.next_to(G, DOWN, buff=0.25).scale(0.6)
        self.add(tab_head)

        # tables
        col_labels=[A1.copy(), A2.copy(), A3.copy(), A4.copy(), A5.copy()]
        col_labels = [col_label.scale(1.15) for col_label in col_labels]
        prefs = MobjectTable(
            [
                [A2.copy(), A1.copy(), A4.copy(), A5.copy(), A3.copy()],
                [A3.copy(), A5.copy(), A5.copy(), A3.copy(), A4.copy()],
                [No_one.copy(), A3.copy(), A1.copy(), No_one.copy(), A2.copy()],
                [No_one.copy(), No_one.copy(), A2.copy(), No_one.copy(), No_one.copy()]
            ],
            col_labels=col_labels,
            line_config={"stroke_color": BLACK, "stroke_width": 2},
            include_outer_lines=True,
        ).scale(0.6)
        for i in range(1, 6):
            prefs.add_highlighted_cell((1, i), color=GREEN)

        self.add(prefs.next_to(tab_head, DOWN, buff=0.15))


class StartingPointHorizontal(Scene):
    # rendered with ratio 1920 x 1080
    def construct(self):
        config["frame_height"] = 8
        np.random.seed(123)
        # figure header
        title = Tex("Roommate matching: preferences", color=BLACK).scale(0.75).to_edge(UP, buff=1.2)
        self.add(title)

        # Agents
        A1 = Tex("1", color=BLACK, font_size=32)
        A2 = Tex("2", color=BLACK, font_size=32)
        A3 = Tex("3", color=BLACK, font_size=32)
        A4 = Tex("4", color=BLACK, font_size=32)
        A5 = Tex("5", color=BLACK, font_size=32)

        col_labels = [
            Tex("\\textbf{1}", color=BLACK, font_size=32),
            Tex("\\textbf{2}", color=BLACK, font_size=32),
            Tex("\\textbf{3}", color=BLACK, font_size=32),
            Tex("\\textbf{4}", color=BLACK, font_size=32),
            Tex("\\textbf{5}", color=BLACK, font_size=32),
        ]

        No_one = Tex("", color=WHITE)

        # network header
        net_head = Tex("Example network", color=BLACK).scale(0.6)
        net_head.move_to(np.array([-3.5, 1.75, 0]))
        self.add(net_head)

        # network
        vertices: list = [1, 2, 3, 4, 5]
        edges: list[tuple] = [ (1, 2), (1, 3), (2, 3), (2, 5), (3, 4), (3, 5), (4, 5)]
        vertex_config: dict = {"color": BLACK, "fill_color": RED, "fill_opacity": 1}
        G = Graph(
            vertices,
            edges,
            labels=True,
            label_fill_color=BLACK,
            layout_scale=3,
            vertex_config=vertex_config,
            edge_config={"color": BLACK, "stroke_width": 2}
        )
        G.scale(0.65)
        self.add(G.next_to(net_head, DOWN, buff=0.4))

        # table header
        tab_head = Tex("Agents' preferences", color=BLACK).move_to(np.array([2.5, 1.75, 0])).scale(0.6)
        self.add(tab_head)

        # tables
        col_labels = [col_label.scale(1.15) for col_label in col_labels]
        prefs = MobjectTable(
            [
                [A2.copy(), A1.copy(), A4.copy(), A5.copy(), A3.copy()],
                [A3.copy(), A5.copy(), A5.copy(), A3.copy(), A4.copy()],
                [No_one.copy(), A3.copy(), A1.copy(), No_one.copy(), A2.copy()],
                [No_one.copy(), No_one.copy(), A2.copy(), No_one.copy(), No_one.copy()]
            ],
            col_labels=col_labels,
            line_config={"stroke_color": BLACK, "stroke_width": 2},
            include_outer_lines=True,
        ).scale(0.75)
        for i in range(1, 6):
            prefs.add_highlighted_cell((1, i), color=GREEN)

        self.add(prefs.next_to(tab_head, DOWN, buff=0.15))



# phase 1 of Irving's (1985) roommate matching algorithm
class Phase1(Scene):
    # rendered with ratio 1920 x 945
    def construct(self):
        config["frame_height"] = 6
        # title
        title = Tex("Roommate matching: Phase I", color=BLACK).scale(0.8).to_edge(UP, buff=0.2)
        self.add(title)
        subtitle: str = "Agents propose to their top choice"
        self.add(Tex(subtitle, color=BLACK).scale(0.65).next_to(title, DOWN, buff=0.1))

        # preference table
        # Agents
        A1 = Tex("1", color=BLACK, font_size=32)
        A2 = Tex("2", color=BLACK, font_size=32)
        A3 = Tex("3", color=BLACK, font_size=32)
        A4 = Tex("4", color=BLACK, font_size=32)
        A5 = Tex("5", color=BLACK, font_size=32)

        col_labels = [
            Tex("\\textbf{1}", color=BLACK, font_size=32),
            Tex("\\textbf{2}", color=BLACK, font_size=32),
            Tex("\\textbf{3}", color=BLACK, font_size=32),
            Tex("\\textbf{4}", color=BLACK, font_size=32),
            Tex("\\textbf{5}", color=BLACK, font_size=32),
        ]

        No_one = Tex("", color=WHITE)

        cross = VGroup(
            Line(1.2*UP + 1.85*LEFT, 1.2*DOWN + 1.85*RIGHT, stroke_width=2),
            Line(1.2*UP + 1.85*RIGHT, 1.2*DOWN + 1.85*LEFT, stroke_width=2),
        ).scale(0.18)
        cross.set_color(RED)

        ############
        # table 1
        ############

        # tables
        prefs1 = MobjectTable(
            [
                [A2.copy(), A1.copy(), A4.copy(), A5.copy(), A3.copy()],
                [A3.copy(), A5.copy(), A5.copy(), A3.copy(), A4.copy()],
                [No_one.copy(), A3.copy(), A1.copy(), No_one.copy(), A2.copy()],
                [No_one.copy(), No_one.copy(), A2.copy(), No_one.copy(), No_one.copy()]
            ],
            col_labels=col_labels,
            line_config={"stroke_color": BLACK, "stroke_width": 2},
            include_outer_lines=True
        ).scale(0.585).move_to(np.array([-3.825, 0, 0]))

        for i in range(1, 6):
            prefs1.add_highlighted_cell((1, i), color=GREEN)

        self.add(prefs1)

        ar = Arrow(prefs1.get_right() + 0.0*RIGHT, prefs1.get_right() + 3.5*RIGHT, color=BLACK, stroke_width=2)
        self.add(ar)
        process_text = Tex("Accept best proposal", color=BLACK).scale(0.5)
        self.add(process_text.next_to(ar, UP, buff=0.1))
        proc_text2 = Tex("Reject those below", color=BLACK).scale(0.5)
        self.add(proc_text2.next_to(ar, DOWN, buff=0.1))

        t2 = prefs1.copy()
        t2.add_highlighted_cell((2, 1), color=YELLOW)
        t2.add_highlighted_cell((2, 2), color=YELLOW)
        t2.add_highlighted_cell((3, 3), color=YELLOW)
        t2.add_highlighted_cell((3, 4), color=YELLOW)
        t2.add_highlighted_cell((3, 5), color=YELLOW)

        self.add(t2.next_to(ar, RIGHT, buff=0.15))

        t3 = MobjectTable(
            [[Tex("Best offer", color=BLACK)],
            [rej:=Tex("Rejected", color=BLACK)]],
            #col_labels=[Tex("\\textbf{Legend}", color=BLACK)],
            line_config={"stroke_color": BLACK, "stroke_width": 2},
            include_outer_lines=True,
        )
        t3.add_highlighted_cell((1, 1), color=YELLOW)
        #t3.add_highlighted_cell((1, 1), color=GREEN)

        self.add(t3.scale(0.4).move_to(np.array([0, -1.75, 0])))

        rejects = [
            (3,1),
            (3,2),
            (4,2),
            (4,3),
            (4,5),
            (5,3)
        ]

        for reject in rejects:
            self.add(cross.copy().move_to(t2.get_cell(reject)))

        self.add(cross.copy().scale(0.9).move_to(t3.get_cell((2,1))))


class Phase1ChooseAgain(Scene):
    # rendered with ratio 1920 x 810
    def construct(self):
        config['frame_height'] = 6
        title = Tex("Roommate Matching: Phase I", color=BLACK).scale(0.8).to_edge(UP, buff=0.6)
        subtitle = Tex("Agent 1 chooses again", color=BLACK).scale(0.65).next_to(title, DOWN, buff=0.15)

        self.add(title)
        self.add(subtitle)
        # Agent labels
        A1 = Tex("1", color=BLACK, font_size=32)
        A2 = Tex("2", color=BLACK, font_size=32)
        A3 = Tex("3", color=BLACK, font_size=32)
        A4 = Tex("4", color=BLACK, font_size=32)

        # column labels for table
        col_labels = [
            Tex("\\textbf{1}", color=BLACK, font_size=32),
            Tex("\\textbf{2}", color=BLACK, font_size=32),
            Tex("\\textbf{3}", color=BLACK, font_size=32),
            Tex("\\textbf{4}", color=BLACK, font_size=32),
        ]

        No_one = Tex("", color=WHITE)

        cross = VGroup(
            Line(1.2*UP + 1.85*LEFT, 1.2*DOWN + 1.85*RIGHT, stroke_width=2),
            Line(1.2*UP + 1.85*RIGHT, 1.2*DOWN + 1.85*LEFT, stroke_width=2),
        ).scale(0.2)
        cross.set_color(RED)

        ###########
        # first step
        ###########


        # table 1 header
        tab_head = Tex(
            "a) 1 proposes to 2, 2 accepts\\\\ 2 deletes lower-ranked 4",
            color=BLACK
            ).scale(0.5).move_to(np.array([-4.05, 0.75, 0]))

        # preference table 1
        table1 = MobjectTable(
            [
                [A2.copy(), A3.copy(), A2.copy(), A1.copy()],
                [A4.copy(), A1.copy(), A1.copy(), A2.copy()],
                [A3.copy(), A4.copy(), A4.copy(), A3.copy()],
            ],
            line_config={"stroke_color": BLACK, "stroke_width": 2},
            include_outer_lines=True,
            col_labels=[label.copy() for label in col_labels],
        ).scale(0.6).next_to(tab_head, DOWN, buff=0.15)
        for i in range(1, 5):
            table1.add_highlighted_cell((1, i), color=GREEN)
        #table1.add_highlighted_cell((2, 1), color=YELLOW)
        table1.add_highlighted_cell((3, 2), color=YELLOW)

        self.add(tab_head)
        self.add(table1)

        self.add(cross.copy().move_to(table1.get_cell((4,2))))
        self.add(cross.copy().move_to(table1.get_cell((3,4))))

        ###########
        # second step
        ###########

        # table 2 header
        tab_head2 = Tex(
            "b) 2 and 3 propose to each other\\\\ (stable match)",
            color=BLACK
        ).scale(0.5).move_to(np.array([0, 0.75, 0]))

        # preference table 2
        table2 = MobjectTable(
            [
                [A2.copy(), A3.copy(), A2.copy(), A1.copy()],
                [A4.copy(), A1.copy(), A1.copy(), No_one.copy()],
                [A3.copy(), No_one.copy(), A4.copy(), A3.copy()],
            ],
            line_config={"stroke_color": BLACK, "stroke_width": 2},
            include_outer_lines=True,
            col_labels=[label.copy() for label in col_labels],
        ).scale(0.6).next_to(tab_head2, DOWN, buff=0.15)

        # coloring of tables
        for i in range(1, 5):
            table2.add_highlighted_cell((1, i), color=GREEN)
        yellows = [
            (2, 2),
            (2, 3)
        ]
        for yellow in yellows:
            table2.add_highlighted_cell(yellow, color=YELLOW)

        self.add(table2)
        self.add(tab_head2)

        # rejections
        rejects = [
            (3, 3),
            (4, 3),
            (4, 4),
            (2, 1),
            (4, 1),
            (3, 2)
        ]

        for reject in rejects:
            self.add(cross.copy().move_to(table2.get_cell(reject)))


        ###########
        # third step
        ###########

        # table 3 header
        tab_head3 = Tex(
            "c) 1 lost initial match,\\\\ proposes to next-highest (4)",
            color=BLACK
        ).scale(0.5).move_to(np.array([4.05, 0.75, 0]))

        # preference table 3
        table3 = MobjectTable(
            [
                [No_one.copy(), A3.copy(), A2.copy(), A1.copy()],
                [A4.copy(), No_one.copy(), No_one.copy(), No_one.copy()],
            ],
            line_config={"stroke_color": BLACK, "stroke_width": 2},
            include_outer_lines=True,
            col_labels=[label.copy() for label in col_labels],
        ).scale(0.6).next_to(tab_head3, DOWN, buff=0.15)
        # coloring of tables
        for i in range(1, 5):
            table3.add_highlighted_cell((1, i), color=GREEN)

        yellows = [
            #(2, 2),
            #(2, 3),
            (3, 1),
            (2, 4)
        ]
        for yellow in yellows:
            table3.add_highlighted_cell(yellow, color=YELLOW)

        maroons = [(2,2), (2,3)]
        for maroon in maroons:
            table3.add_highlighted_cell(maroon, color=MAROON_A)



        self.add(table3)
        self.add(tab_head3)

        ###########
        # annotation 3
        ###########

        annot = Tex(
            "$\\rightarrow$ Only stable matches \\\\ Phase II not necessary",
            color=BLACK
        ).scale(0.5).next_to(table3, DOWN, buff=0.25)
        self.add(annot)


# this one not necessary
class Phase1point5(Scene):
    def construct(self):
        title = Tex("Roommate matching: Phase 1.5", color=BLACK).scale(1.5).to_edge(UP, buff=0.2)
        self.add(title)

        # Agents
        A1 = Tex("Agent 1", color=BLACK, font_size=32)
        A2 = Tex("Agent 2", color=BLACK, font_size=32)
        A3 = Tex("Agent 3", color=BLACK, font_size=32)
        A4 = Tex("Agent 4", color=BLACK, font_size=32)
        A5 = Tex("Agent 5", color=BLACK, font_size=32)

        No_one = Tex("No-one", color=WHITE)

        t1 = MobjectTable(
            [
                [A2.copy(), A1.copy()],
                [No_one.copy(), No_one.copy()]
            ],
            col_labels=[A1.copy().scale(1.5), A2.copy().scale(1.5)],
            line_config={"stroke_color": BLACK, "stroke_width": 2},
            include_outer_lines=True
        )
        t1.add_highlighted_cell((1, 1), color=GREEN)
        t1.add_highlighted_cell((1, 2), color=GREEN)
        t1.add_highlighted_cell((2, 1), color=YELLOW)
        t1.add_highlighted_cell((2, 2), color=YELLOW)
        self.add(t1.scale(0.75).to_edge(LEFT, buff=2))
        stab_text = Tex("Stable matching", color=BLACK).scale(0.75)
        self.add(stab_text.next_to(t1, DOWN, buff=0.25))

        t2 = MobjectTable(
            [
                [A4.copy(), A5.copy(), A3.copy()],
                [A5.copy(), A3.copy(), A4.copy()],
            ],
            col_labels=[A3.copy().scale(1.5), A4.copy().scale(1.5), A5.copy().scale(1.5)],
            line_config={"stroke_color": BLACK, "stroke_width": 2},
            include_outer_lines=True
        )
        tops = [(1,1), (1,2), (1,3)]
        for top in tops:
            t2.add_highlighted_cell(top, color=GREEN)
        offers = [(3,1), (3,2), (3,3)]
        for offer in offers:
            t2.add_highlighted_cell(offer, color=YELLOW)

        self.add(t2.scale(0.75).next_to(t1, RIGHT, buff=1))
        stab_text2 = Tex("Continue in Phase II", color=BLACK).scale(0.75)
        self.add(stab_text2.next_to(t2, DOWN, buff=0.25))