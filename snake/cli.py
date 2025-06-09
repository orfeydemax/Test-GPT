import curses
from typing import Dict

from .game import SnakeGame

DIRECTIONS: Dict[int, tuple[int, int]] = {
    curses.KEY_UP: (-1, 0),
    curses.KEY_DOWN: (1, 0),
    curses.KEY_LEFT: (0, -1),
    curses.KEY_RIGHT: (0, 1),
}


def main(stdscr: curses.window) -> None:
    """Основная функция игры в терминале."""
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.timeout(100)

    game = SnakeGame()
    while not game.over:
        key = stdscr.getch()
        if key in DIRECTIONS:
            game.change_direction(DIRECTIONS[key])

        game.step()

        stdscr.clear()
        # Рисуем границы
        for y in range(game.height + 2):
            stdscr.addstr(y, 0, "#")
            stdscr.addstr(y, game.width + 1, "#")
        for x in range(game.width + 2):
            stdscr.addstr(0, x, "#")
            stdscr.addstr(game.height + 1, x, "#")

        # Рисуем еду
        if game.food:
            fy, fx = game.food
            stdscr.addstr(fy + 1, fx + 1, "*")

        # Рисуем змейку
        for y, x in game.snake:
            stdscr.addstr(y + 1, x + 1, "O")

        stdscr.refresh()

    stdscr.nodelay(False)
    stdscr.addstr(game.height // 2, game.width // 2 - 4, "Game Over!")
    stdscr.getch()


if __name__ == "__main__":
    curses.wrapper(main)
