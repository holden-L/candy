#!/usr/bin/env python
import Game

# Some constants to be imported into other files
WIDTH, HEIGHT = 700, 600
SPEED = 5
UP = DOWN = LEFT = RIGHT = False


def main():
    game = Game.Game()
    game.mainloop()
    return

if __name__ == "__main__":
    main()
