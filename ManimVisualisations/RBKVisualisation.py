from manim import *
import numpy as np

scaler = 1
config["background_color"] = WHITE
config["frame_width"] = 12
config["frame_height"] = 6

# Visualisation of the radial-based kernel ranking method
class RBKVis(Scene):
    # rendered with ratio 1920 x 945
    def construct(self):
        title: str = Tex("Classification ranking", color=BLACK).scale(0.75).to_edge(UP, buff=0.15)
        subtitle: str = "Schematic representation of the radial-based kernel ranking"
        self.add(title)
        self.add(Tex(subtitle, color=BLACK).scale(0.6).next_to(title, DOWN, buff=0.1))

        # the example graph on the LHS of the figure
        vertices: list = [0, 1, 2, 3, 4, 5, 6]
        # node 1 is connected to all of them
        edges: list[tuple] = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6)]
        # configs of nodes
        center_config: dict = {"fill_color": RED, "fill_opacity": 1, "radius": 0.25* scaler}
        neighbors_config = {"fill_color": BLUE, "fill_opacity": 1, "radius": 0.25*scaler}
        vertex_config:dict[int, dict] = {
            0: center_config,
            1: neighbors_config,
            2: neighbors_config,
            3: neighbors_config,
            4: neighbors_config,
            5: neighbors_config,
            6: neighbors_config
        }
        # edge configs
        edge_config: dict = {"stroke_color": BLACK, "stroke_width": 1*scaler}
        # neighbours' labels
        labels = [Tex(str(i), color=BLACK).scale(0.5*scaler) for i in range(1, 7)]

        # center node position
        center_pos = np.array([-3.75, -0.15, 0])
        # neighbours' positions on a circle around the center node radius 2
        neigh_pos =[center_pos + np.array([2*scaler*np.cos(2*np.pi/6*i), 2*scaler*np.sin(2*np.pi/6*i), 0]) for i in range(6)]
        #label' positions
        label_pos = [center_pos + np.array([1.5*scaler*np.cos(2*np.pi/6*i), 1.5*scaler*np.sin(2*np.pi/6*i), 0]) for i in range(6)]

        # layout
        lt = dict(zip(vertices, [center_pos] + neigh_pos))

        # create graph
        G = Graph(
            vertices,
            edges,
            layout=lt,
            vertex_config=vertex_config,
            edge_config=edge_config
        ).scale(0.75*scaler)

        self.add(G)

        # adjust labels' positions and add to figure
        for label, pos in zip(labels, label_pos):
            label.move_to(pos)
            self.add(label)

        def vec_pos(node_pos):
            return (node_pos - center_pos)*0.95 + center_pos
        # add feature values to the neighbouring nodes
        feature_vecs = [
            MathTex("(0.1, -0.5)", color=BLACK).scale(0.5*scaler).move_to(vec_pos(neigh_pos[0])+np.array([-0.4, 0.35*scaler, 0])),
            MathTex("(0.2, 0.5)", color=BLACK).scale(0.5*scaler).move_to(vec_pos(neigh_pos[2])),
            MathTex("(0.9, 0.5)", color=BLACK).scale(0.5*scaler).move_to(vec_pos(neigh_pos[1])),
            MathTex("(0.8, -0.2)", color=BLACK).scale(0.5*scaler).move_to(vec_pos(neigh_pos[3])+np.array([0.4, 0.35*scaler, 0])),
            MathTex("(0.3, -0.5)", color=BLACK).scale(0.5*scaler).move_to(vec_pos(neigh_pos[4])),
            MathTex("(0.7, 0.2)", color=BLACK).scale(0.5*scaler).move_to(vec_pos(neigh_pos[5]))
        ]
        for vec in feature_vecs:
            self.add(vec)

        # brace that connects neighbours and network to RBK
        brc = Brace(
            G,
            direction=np.array([1, 0, 0]),
            buff=0.5,
            color=BLACK,
            sharpness=0.75
        )
        self.add(brc)

        # RBK equation
        RBK_eq = Tex(
            "$\\pi_{ij}(t) = \\exp\\left(-\\frac{1}{2}\\lVert \\mathbf{z}_{ij}(t)-\\mathbf{z}'\\rVert^2\\right)$",
            color=BLACK
        ).scale(0.5*scaler).next_to(brc, RIGHT, buff=0.1)
        self.add(RBK_eq)

        RBK_tex = Tex("\\textbf{RBK:}", color=BLACK).scale(0.5*scaler).next_to(RBK_eq, UP, buff=0.1)
        self.add(RBK_tex)

        ia = Dot(color=GREEN_A, radius=0.35*scaler).next_to(RBK_tex, DOWN, buff=1)
        ia.set_z_index(-1)
        ideal = Tex("Ideal\\\\agent", color=BLACK).scale(0.5*scaler).move_to(ia.get_center())
        ideal_features = Tex("$\\mathbf{z}' = (1, 1)$", color=BLACK).scale(0.5*scaler).next_to(ideal, DOWN, buff=0.2)

        self.add(ideal)
        self.add(ia)
        self.add(ideal_features)

        # arrow pointing to ranking
        arrow = Tex("$\\Rightarrow$", color=BLACK, stroke_width=1*scaler).next_to(RBK_eq, RIGHT, buff=0.2)
        self.add(arrow)

        def RBK(vec: tuple):
            return np.exp(-0.5 * np.linalg.norm(np.array(vec) - np.array([1, 1]))**2)
        # add the ranking as a table, using the equation of RBK
        # rank high to low
        rbk_res: dict = {
            RBK(eval(feature_vecs[i].tex_strings[0])): i+1 for i in range(6)
        }
        rbk_vals: list = list(rbk_res.keys())
        rbk_vals.sort(reverse=True)
        rank_tab = MobjectTable(
            [
                [
                    Tex(rbk_res[rbk_val], color=BLACK),
                    Tex(np.round(rbk_val, 2), color=BLACK)
                    ]
                for rbk_val in rbk_vals
            ],
            col_labels=[
                Tex("Neighbor", color=BLACK),
                Tex("RBK", color=BLACK)
            ],
            include_outer_lines=True,
            line_config={"stroke_color": BLACK, "stroke_width": 2*scaler},
        ).next_to(arrow, RIGHT, buff=0)
        rank_tab_pos = rank_tab.get_center()
        rank_tab.move_to(rank_tab_pos + np.array([-1.2, -0.5*scaler, 0]))
        self.add(rank_tab.scale(0.5*scaler))

        # table header
        header = Tex("\\textbf{Ranking}", color=BLACK).scale(0.5*scaler).next_to(rank_tab, UP, buff=0.1*scaler)
        self.add(header)





