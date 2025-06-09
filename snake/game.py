import random
from dataclasses import dataclass
from typing import List, Tuple

Direction = Tuple[int, int]


@dataclass
class SnakeGame:
    """Простая логика игры «Змейка»."""

    width: int = 20
    height: int = 20
    snake: List[Tuple[int, int]] | None = None
    direction: Direction = (0, 1)  # движемся вправо
    food: Tuple[int, int] | None = None
    over: bool = False

    def __post_init__(self) -> None:
        if self.snake is None:
            self.snake = [(self.height // 2, self.width // 2)]
        self.generate_food()

    def change_direction(self, new_direction: Direction) -> None:
        """Меняет направление движения, если оно не противоположно текущему."""
        opposite = (-self.direction[0], -self.direction[1])
        if new_direction != opposite:
            self.direction = new_direction

    def step(self) -> None:
        """Продвинуть игру на один шаг."""
        if self.over:
            return

        head_y, head_x = self.snake[0]
        dy, dx = self.direction
        new_head = (head_y + dy, head_x + dx)

        # проверяем столкновение со стеной
        if (
            new_head[0] < 0
            or new_head[0] >= self.height
            or new_head[1] < 0
            or new_head[1] >= self.width
        ):
            self.over = True
            return

        # проверяем столкновение с самим собой
        if new_head in self.snake:
            self.over = True
            return

        # перемещаем змейку
        self.snake.insert(0, new_head)
        if new_head == self.food:
            self.generate_food()
        else:
            self.snake.pop()

    def generate_food(self) -> None:
        """Размещает еду в случайном свободном месте."""
        available = [
            (y, x)
            for y in range(self.height)
            for x in range(self.width)
            if (y, x) not in self.snake
        ]
        if available:
            self.food = random.choice(available)
        else:
            self.food = None
