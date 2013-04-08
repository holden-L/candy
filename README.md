Candy Game
==========

A simple 2D game written in Python 2.X, with the Pygame module.
I wrote it as a first project using OOP and multiple files, as well as to familiarize myself with Pygame.
None of the artwork or sounds are my own.

Prerequisites
------------

* Python
* Pygame

To Run
------

1. Download all files.
2. Navigate to the directory with main.py.
3. Run "python main.py".

To Do
-----

* Make candies automatically move after a period of time.
* Create a gameover, based on how many candies have been missed.
* Keep track of the score in window, rather than printing it to a terminal after the game finishes.

Game Play
--------

Player is controlled either with arrow keys or with WASD. Sounds can be muted with 'm' key.
Score is displayed in the top left; lives in the top right.
Every candy missed takes away a live (gameover when zero lives).
Every candy caught grants a point.
