# Authors: Alexandra Bacula, Ethan Villalovoz
# Oregon State University CHARISMA Lab
# Program: geometryGUI
# Description: Allows an easy to see interface when going through the geometryScript3.0


# Imports
import tkinter
from tkinter import * # General import when creating a GUI

from tkinter.ttk import * # Add a combobox widget

from tkinter import scrolledtext # Add a ScrolledText widget (Tkinter textarea)

from tkinter import messagebox # Used for message box

from tkinter.ttk import Progressbar # To create a progress bar, you can use the progressbar class like this:
from tkinter import ttk

from tkinter import filedialog #Add a filedialog (file & directory chooser)
from os import path

from tkinter import Menu # Add a Menu bar

import PySimpleGUI as sg

from tkinter.messagebox import showinfo

def main():

    #Establishes a new window for the GUI
    window = Tk()
    # Names the top page user is currently in
    window.title("Geometry Visualisation")
    # Creates a size of the window
    window.geometry('2000x500')

    # Adds a label to the screen
    lbl = Label(window, text="What shape would you like to select?", font=("Arial Bold", 20))
    lbl.grid(column=0, row=0)

    lbl1 = Label(window, text="Click the shape:", font=("Arial Bold", 20))
    lbl1.grid(column=0, row=1)

    ### Functions for the buttons of each shape
    def clickedSquare():
        # Reference X Goal
        x_goal = Label(window, text="What is the X coordinate you would want the reference goal to be?")
        x_goal.grid(column=1, row=2)

        # Reference Y Goal
        y_goal = Label(window, text="What is the Y coordinate you would want the reference goal to be?")
        y_goal.grid(column=1, row=3)

        # Length of the Square
        length = Label(window, text="What is the side length of the square you would like?")
        length.grid(column=1, row=4)

        # Number of robots in Configuration
        numRobots = Label(window, text="How many robots would you want for the shape? (Must be at least 4 and no greater than 10)")
        numRobots.grid(column=1, row=5)

        # Orientation of Shape
        orientation = Label(window, text="How would you like the orientation of the shape? (Up - 0 degrees, Down - 180 Degrees, Custom - X Degrees)")
        orientation.grid(column=1, row=6)

        # Example
        example = Label(window, text="Respond as the format: X,Y,Length/Radius,# of robots,Orientation")
        example.grid(column=1, row=7)
        example2 = Label(window, text="Example: 3,3,5,2,90")
        example2.grid(column=1, row=8)

        # User Input
        # Inserts a input text box
        txt = Entry(window, width=10)
        txt.grid(column=1, row=9)

    def clickedTriangle():
        # Reference X Goal
        x_goal = Label(window, text="What is the X coordinate you would want the reference goal to be?")
        x_goal.grid(column=2, row=2)

        # Reference Y Goal
        y_goal = Label(window, text="What is the Y coordinate you would want the reference goal to be?")
        y_goal.grid(column=2, row=3)

        # Length of the Triangle
        length = Label(window, text="What is the side length of the triangle you would like?")
        length.grid(column=2, row=4)

        # Number of robots in Configuration
        numRobots = Label(window,
                          text="How many robots would you want for the shape? (Must be at least 3 and no greater than 10)")
        numRobots.grid(column=2, row=5)

        # Orientation of Shape
        orientation = Label(window,
                            text="How would you like the orientation of the shape? (Down - 0 degrees, Up - 180 Degrees, Custom - X Degrees)")
        orientation.grid(column=2, row=6)

        # Example
        example = Label(window, text="Respond as the format: X,Y,Length/Radius,# of robots,Orientation")
        example.grid(column=2, row=7)
        example2 = Label(window, text="Example: 3,3,5,2,90")
        example2.grid(column=2, row=8)

        # User Input
        # Inserts a input text box
        txt = Entry(window, width=10)
        txt.grid(column=2, row=9)

    def clickedSemiCircle():
        # Reference X Goal
        x_goal = Label(window, text="What is the X coordinate you would want the reference goal to be?")
        x_goal.grid(column=3, row=2)

        # Reference Y Goal
        y_goal = Label(window, text="What is the Y coordinate you would want the reference goal to be?")
        y_goal.grid(column=3, row=3)

        # Radius of the Semi-Circle
        radius = Label(window, text="What is the radius of the semi-circle you would like?")
        radius.grid(column=3, row=4)

        # Number of robots in Configuration
        numRobots = Label(window,
                          text="How many robots would you want for the shape? (Must be at least 3 and no greater than 10)")
        numRobots.grid(column=3, row=5)

        # Orientation of Shape
        orientation = Label(window,
                            text="How would you like the orientation of the shape? (Up - 0 degrees, Down - 180 Degrees, Custom - X Degrees)")
        orientation.grid(column=3, row=6)

        # Example
        example = Label(window, text="Respond as the format: X,Y,Length/Radius,# of robots,Orientation")
        example.grid(column=3, row=7)
        example2 = Label(window, text="Example: 3,3,5,2,90")
        example2.grid(column=3, row=8)

        # User Input
        # Inserts a input text box
        txt = Entry(window, width=10)
        txt.grid(column=3, row=9)

    def clickedClump():
        # Reference X Goal
        x_goal = Label(window, text="What is the X coordinate you would want the reference goal to be?")
        x_goal.grid(column=4, row=2)

        # Reference Y Goal
        y_goal = Label(window, text="What is the Y coordinate you would want the reference goal to be?")
        y_goal.grid(column=4, row=3)

        # Length of the Clump
        length = Label(window, text="What is the side length of the clump you would like?")
        length.grid(column=4, row=4)

        # Number of robots in Configuration
        numRobots = Label(window,
                          text="How many robots would you want for the shape? (Must be at least 3 and no greater than 10)")
        numRobots.grid(column=4, row=5)

        # Orientation of Shape
        orientation = Label(window,
                            text="How would you like the orientation of the shape? (Up - 0 degrees, Down - 180 Degrees, Custom - X Degrees)")
        orientation.grid(column=4, row=6)

        # Example
        example = Label(window, text="Respond as the format: X,Y,Length/Radius,# of robots,Orientation")
        example.grid(column=4, row=7)
        example2 = Label(window, text="Example: 3,3,5,2,90")
        example2.grid(column=4, row=8)

        # User Input
        # Inserts a input text box
        txt = Entry(window, width=10)
        txt.grid(column=4, row=9)

    def clickedCircle():
        # Reference X Goal
        x_goal = Label(window, text="What is the X coordinate you would want the reference goal to be?")
        x_goal.grid(column=5, row=2)

        # Reference Y Goal
        y_goal = Label(window, text="What is the Y coordinate you would want the reference goal to be?")
        y_goal.grid(column=5, row=3)

        # Radius of the Circle
        radius = Label(window, text="What is the radius of the circle you would like?")
        radius.grid(column=5, row=4)

        # Number of robots in Configuration
        numRobots = Label(window,
                          text="How many robots would you want for the shape? (Must be at least 3 and no greater than 10)")
        numRobots.grid(column=5, row=5)

        # Orientation of Shape
        orientation = Label(window,
                            text="How would you like the orientation of the shape? (Up - 0 degrees, Down - 180 Degrees, Custom - X Degrees)")
        orientation.grid(column=5, row=6)

        # Example
        example = Label(window, text="Respond as the format: X,Y,Length/Radius,# of robots,Orientation")
        example.grid(column=5, row=7)
        example2 = Label(window, text="Example: 3,3,5,2,90")
        example2.grid(column=5, row=8)

        # User Input
        # Inserts a input text box
        txt = Entry(window, width=10)
        txt.grid(column=5, row=9)

    def clickedLine():
        # Reference X Goal
        x_goal = Label(window, text="What is the X coordinate you would want the reference goal to be?")
        x_goal.grid(column=6, row=2)

        # Reference Y Goal
        y_goal = Label(window, text="What is the Y coordinate you would want the reference goal to be?")
        y_goal.grid(column=6, row=3)

        # Length of the Line
        length = Label(window, text="What is the side length of the line you would like?")
        length.grid(column=6, row=4)

        # Number of robots in Configuration
        numRobots = Label(window,
                          text="How many robots would you want for the shape? (Must be at least 2 and no greater than 10)")
        numRobots.grid(column=6, row=5)

        # Orientation of Shape
        orientation = Label(window,
                            text="How would you like the orientation of the shape? (Up - 0 degrees, Horizontal - 90 Degrees, Custom - X Degrees)")
        orientation.grid(column=6, row=6)

        # Example
        example = Label(window, text="Respond as the format: X,Y,Length/Radius,# of robots,Orientation")
        example.grid(column=6, row=7)
        example2 = Label(window, text="Example: 3,3,5,2,90")
        example2.grid(column=6, row=8)

        # User Input
        # Inserts a input text box
        txt = Entry(window, width=10)
        txt.grid(column=6, row=9)

    ### Creates a button

    # Square Selection
    btnSquare = Button(window, text="Square", command=clickedSquare)
    btnSquare.grid(column=1, row=1)

    # Triangle Selection
    btnTriangle = Button(window, text="Triangle", command=clickedTriangle)
    btnTriangle.grid(column=2, row=1)

    # Semi-Circle Selection
    btnSemiCircle = Button(window, text="Semi-Cirlce", command=clickedSemiCircle)
    btnSemiCircle.grid(column=3, row=1)

    # Clump Selection
    btnClump = Button(window, text="Clump", command=clickedClump)
    btnClump.grid(column=4, row=1)

    # Circle Selection
    btnCircle = Button(window, text="Circle", command=clickedCircle)
    btnCircle.grid(column=5, row=1)

    # Line Selection
    btnLine = Button(window, text="Line", command=clickedLine)
    btnLine.grid(column=6, row=1)

    # function calls the endless loop of the window, so the window will wait for any user interaction till we close it.
    window.mainloop()
    # ^^^^^ Must have this at the end ALWAYS


if __name__ == "__main__":
    main()