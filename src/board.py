from typing import Tuple

import networkx as nx

from constants import ROWS, COLS, WINDOW_SIZE, USERS_COLORS, BLACK
from draw import _Draw


class Board(_Draw):
    def __init__(
        self,
        rows: int = ROWS,
        cols: int = COLS,
        window_size: Tuple[int, int] = WINDOW_SIZE,
        background_color=BLACK,
        users_colors: Tuple = USERS_COLORS,
    ):
        super().__init__(rows, cols, window_size, background_color, users_colors)
        self._state = self._create_init_state()

    def _create_init_state(self) -> nx.Graph:
        state = nx.Graph()
        nodes = [(i, j) for i in range(self.rows) for j in range(self.cols)]
        state.add_nodes_from(nodes)
        return state

    def update(self, node1: Tuple[int, int], node2: Tuple[int, int], screen) -> None:
        self._state.add_edge(node1, node2)

    def is_there_path(self, node1: Tuple[int, int], node2: Tuple[int, int]) -> bool:

        if next(nx.all_simple_paths(self._state, node1, node2), None) is None:
            return False
        return True
