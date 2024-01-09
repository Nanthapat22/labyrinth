import os
import time
import random

class Pos:
    def __init__(self, y, x) -> None:
        self.y = y
        self.x = x

class Maze:
    def __init__(self) -> None:
        self.maze = [
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", " ", " ", " ", "X", " ", "X"],
            ["X", " ", "X", " ", "X", " ", " "],
            ["X", " ", "X", " ", "X", " ", "X"],
            ["X", " ", "X", " ", " ", " ", "X"],
            ["X", " ", "X", "X", "X", "X", "X"],
        ]
        self.player = Pos(5, 1)
        self.end = Pos(2, 6)
        self.maze[self.player.y][self.player.x] = "P"
        self.maze[self.end.y][self.end.x] = "E"

    def is_in_bound(self, y, x):
        return 0 <= y < len(self.maze) and 0 <= x < len(self.maze[0])

    def print_maze(self):
        os.system("cls" if os.name == "nt" else "clear")
        print("\n\n\n")
        for row in self.maze:
            for col in row:
                print(col, " ", end="")
            print("")
        print("\n\n\n")

    def print_end(self):
        os.system("cls" if os.name == "nt" else "clear")
        print("\n\n\n")
        print(">>>>> Congratulations!!! <<<<<")
        print("\n\n\n")

    def move_up(self):
        next_move = Pos(self.player.y - 1, self.player.x)
        if self.is_in_bound(next_move.y, next_move.x) and self.maze[next_move.y][next_move.x] != "X":
            self.maze[self.player.y][self.player.x] = " "
            self.maze[next_move.y][next_move.x] = "P"
            self.player = next_move
            time.sleep(0.25)
            return True
        return False

    def move_down(self):
        next_move = Pos(self.player.y + 1, self.player.x)
        if self.is_in_bound(next_move.y, next_move.x) and self.maze[next_move.y][next_move.x] != "X":
            self.maze[self.player.y][self.player.x] = " "
            self.maze[next_move.y][next_move.x] = "P"
            self.player = next_move
            time.sleep(0.25)
            return True
        return False

    def move_left(self):
        next_move = Pos(self.player.y, self.player.x - 1)
        if self.is_in_bound(next_move.y, next_move.x) and self.maze[next_move.y][next_move.x] != "X":
            self.maze[self.player.y][self.player.x] = " "
            self.maze[next_move.y][next_move.x] = "P"
            self.player = next_move
            time.sleep(0.25)
            return True
        return False

    def move_right(self):
        next_move = Pos(self.player.y, self.player.x + 1)
        if self.is_in_bound(next_move.y, next_move.x) and self.maze[next_move.y][next_move.x] != "X":
            self.maze[self.player.y][self.player.x] = " "
            self.maze[next_move.y][next_move.x] = "P"
            self.player = next_move
            time.sleep(0.25)
            return True
        return False

    def explore_path_randomly(self):
        while self.player.y != self.end.y or self.player.x != self.end.x:
            random_direction = random.choice(["up", "down", "left", "right"])

            if random_direction == "up":
                self.move_up()
            elif random_direction == "down":
                self.move_down()
            elif random_direction == "left":
                self.move_left()
            elif random_direction == "right":
                self.move_right()

            self.print_maze()

if __name__ == '__main__':
    m = Maze()
    m.print_maze()
    m.explore_path_randomly()
    m.print_end()
