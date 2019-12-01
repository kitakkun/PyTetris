# Tetris
 Simple Tetris like game powered by Python.

## Installation
First of all, you need python3-installed pc.
If you haven't install python yet, please visit https://www.python.org.
After installing python, install numpy, and pygame.
If you have homebrew environment,
just run `pip install numpy` and `pip install pygame` on your terminal.
**On macOS, there's a bug in the newest version of pygame(1.9.6),
so please install 2.0.0.dev(or higher).**
To select a version of packages, just add "==version" to the end of code.
For example, `pip install pygame==2.0.0.dev`.

## How to run the code
After downloaded the files, open Terminal(macOS, Linux) or Command Prompt, then move into **src** directory by using `cd` command, and type `python tetris.py`.

## Feature
Press **space bar** to **rotate Block**.
Press **left-arrow key** to **move Block to the left**.
Press **right-arrow key** to **move Block to the right**.
Press **down-arrow key** to **make the speed of Block's falling faster**(If you also press shift key simultaneously, Block will fall to the bottom in a moment).
