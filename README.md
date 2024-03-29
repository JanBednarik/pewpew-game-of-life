# PewPew Game of Life

[Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) for [PewPew](https://hackaday.io/project/159733-pewpew-standalone) CircuitPython device.

Great for [EuroPython 2019](https://ep2019.europython.eu/events/pewpew-workshops/) badges (game consoles).

In action video: https://youtu.be/ConQsd1Bu-o

## Usage

Connect PewPew to your computer, it will appear as USB flash drive.
Copy `main.py` to PewPew.

Pressing button `up`, `down`, `left` or `right` will load preset board with nice oscillating life examples.
Buttons `x` and `o` will reset life to random state.

There is no true random generator inside board's processor.
So after turning it on it may alway generate the same life.
If you press any button, you will reset the game and then it will start with random life.

If life on the board dies or gets stuck in still life, the game will automatically reset.
But when it get's into oscillating state, you have to reset it by pressing any button.
