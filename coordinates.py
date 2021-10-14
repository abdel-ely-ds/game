from typing import Tuple, Dict, List


class CoordinatesHandler:
    def __init__(
        self,
        rows: int,
        cols: int,
        window_size: Tuple[int, int],
    ):
        self.rows = rows
        self.cols = cols
        self.window_size = window_size

    def compute_human_coordinates(self) -> List[Tuple[int, int]]:
        return [(i, j) for i in range(self.rows) for j in range(self.cols)]

    def compute_screen_coordinates(
        self, rectangle_size: Tuple[int, int]
    ) -> Dict[Tuple[int, int], Tuple[int, int]]:
        return {
            (i, j): (i * rectangle_size[0], j * rectangle_size[1])
            for (i, j) in self.compute_human_coordinates()
        }

    def compute_forbidden_coordinates(self) -> List[Tuple[int, int]]:
        human_coordinates = self.compute_human_coordinates()
        forbidden_coordinates = []
        for (i, j) in human_coordinates:
            if abs(i - j) % 2 == 0:
                forbidden_coordinates.append((i, j))

        return forbidden_coordinates
