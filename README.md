# Space-Invaders

<p align="center"><img src="images/game.jpg"></p>

## Installing tools

In this we will be basically using Python 3 and turtle shell.
having thought everyone is having python 3... just type the following command in the terminal to install Tkinter & Turtle.
```bash
sudo apt-get install python3-tk
```
this is for linux users as am using in terminal in ubuntu.

## Getting started
We will be using turtle to create all the characters and also for the borders for the game design.

```bash
import turtle
import os
```
start creating the windoww for the game to pop up and the borders for it.
and for the game to stay there and not to dissapear use:
```bash
delay = input("press enter to terminate...")
```
so as th game pop's up..it will only terminaate if pressed Enter in the terminal

wn.register_shape is used to assign the images to the characters in game:
```bash
wn.register_shape("invader.gif")
```
remember that to access these images into the python code, they have to be in the same folder as the code is saved.
## the input images should be in GIF format.
i specifically resized the background image to (600x600) pixels.

  
