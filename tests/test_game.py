import os
import sys

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, BASE_DIR)
from snake.game import SnakeGame  # noqa: E402


def test_snake_moves_right():
    """Проверяем, что змейка двигается вправо."""
    game = SnakeGame(width=5, height=5)
    initial_head = game.snake[0]
    game.step()
    assert game.snake[0] == (initial_head[0], initial_head[1] + 1)


def test_generate_food_not_on_snake():
    """Еда не появляется на змейке."""
    game = SnakeGame(width=5, height=5)
    assert game.food not in game.snake
