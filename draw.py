import pygame
from typing import Tuple, Dict
from coordinates import CoordinatesHandler
from constants import ROWS, COLS, WINDOW_SIZE, USERS_COLORS, BLACK


class _Draw:
    def __init__(
        self,
        rows: int = ROWS,
        cols: int = COLS,
        window_size: Tuple[int, int] = WINDOW_SIZE,
        background_color=BLACK,
        users_colors: Tuple = USERS_COLORS,
    ):
        self.rows = rows
        self.cols = cols
        self.window_size = window_size
        self.background_color = background_color
        self.users_colors = users_colors
        self._coordinates_handler = CoordinatesHandler(rows, cols, window_size)
        self._rectangle_size = self._compute_rectangle_size()
        self._circle_radius = min(self._rectangle_size) // 4
        self._human_coordinates = self._coordinates_handler.compute_human_coordinates()
        self._forbidden_coordinates = (
            self._coordinates_handler.compute_forbidden_coordinates()
        )
        self._screen_coordinates = self._coordinates_handler.compute_screen_coordinates(
            self._rectangle_size
        )
        self._circle_coordinates = self._compute_circle_coordinates()
        self._colors = self._get_colors()

    def _get_colors(self) -> Dict[Tuple[int, int], Tuple[int, int]]:
        color_1, color_2 = self.users_colors
        return {
            (i, j): color_1 if i % 2 == 0 else color_2
            for (i, j) in self._human_coordinates
        }

    def _compute_rectangle_size(self) -> Tuple[int, int]:
        return self.window_size[0] // self.rows, self.window_size[1] // self.cols

    def _compute_circle_coordinates(self) -> Dict[Tuple[int, int], Tuple[int, int]]:

        return {
            coordinates: (
                self._screen_coordinates[coordinates][0] + self._rectangle_size[0] // 2,
                self._screen_coordinates[coordinates][1] + self._rectangle_size[1] // 2,
            )
            for coordinates in self._screen_coordinates
        }

    def draw(self):

        pygame.init()
        screen = pygame.display.set_mode(self.window_size)

        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            screen.fill(self.background_color)
            for coordinates in self._human_coordinates:
                if coordinates not in self._forbidden_coordinates:
                    pygame.draw.circle(
                        surface=screen,
                        color=self._colors[coordinates],
                        center=self._circle_coordinates[coordinates],
                        radius=self._circle_radius,
                    )
            pygame.display.flip()
