"""

Use turtle graphics to draw a smily face in python
file: smiles.py
author: HH

"""

import turtle

def initialize():
    """
    Initialize the turtle so that it is facing North with the pen up
    """
    turtle.up()
    turtle.lt( 90 )

def drawH():
    """
    Draw a circle for the outline of the face
    """
    turtle.bk( 100 )
    turtle.rt( 90 )
    turtle.pd()
    turtle.circle( 100 )
    turtle.up()
    turtle.lt( 90 )
    turtle.fd( 100 )

def drawM():
    """
    Draw a smiling mouth
    """
    turtle.bk( 60 )
    turtle.lt( 65 )
    turtle.fd( 30 )
    turtle.lt( 180 )
    turtle.pd()
    turtle.fd( 30 )
    turtle.lt( 50 )
    turtle.fd( 30 )
    turtle.lt( 180 )
    turtle.up()
    turtle.fd( 30 )
    turtle.lt( 65 )
    turtle.fd( -60 )
    turtle.lt( 180 )

def drawN():
    """
    Draw a nose as an equilateral triangle
    """
    turtle.bk( 30 )
    turtle.lt( 90 )
    turtle.pd()
    turtle.fd( 15 )
    turtle.rt( 120 )
    turtle.fd( 30 )
    turtle.rt( 120 )
    turtle.fd( 30 )
    turtle.rt( 120 )
    turtle.fd( 15 )
    turtle.up()
    turtle.lt( 90 )
    turtle.bk( 30 )
    turtle.lt( 180 )

def drawE():
    """
    Draw both eyes as circles
    """
    turtle.lt( 90 )
    turtle.fd( 50 )
    turtle.rt( 180 )
    eye()
    turtle.fd( 100 )
    eye()
    turtle.rt( 180 )
    turtle.fd( 50 )
    turtle.lt( 90 )
    turtle.lt( 180 )

def eye():
    """
    Draw a single eye as a 15-point-radius circle
    Assume the turtle is facing right at the bottom of where the eye will be
    Leave the turtle in that same state.
    """
    turtle.pd()
    turtle.circle( 15 )
    turtle.up()

def smile():
    """
    Draw a smiley face
    """
    drawH()
    drawM()
    drawN()
    drawE()
    
def main():
    """
    The program creates a picture canvas and waits for the user to select a function
    """
    initialize()
    toggle = 0
    turtle.ht()
    active = True
    while active:
        print( "VALID COMMANDS INCLUDE:\n" )
        print( "smile - creates a smiley face" )
        print( "clear - closes current window and opens new one" )
        print( "part - creates a part of the smiley face" )
        print( "cursor - toggles cursor visibility ON/OFF" )
        print( "end - closes the window and ends program\n" )
        x = input( "PLEASE ENTER A VALID COMMAND: " )
        print( "\nCOMMAND = " + str( x ) + "\n" )
        if x == "end":
            turtle.bye()
            print( "GOODBYE" )
            active = False            
        elif x == "smile":
            smile()            
        elif x == "clear":
            turtle.bye()
            initialize()
        elif x == "part":
            print( "VALID PARTS INCLUDE:\n" )
            print( "head - creates the head of the smiley face")
            print( "mouth - creates the mouth of the smiley face")
            print( "nose - creates the nose of the smiley face")
            print( "eye - creates the eyes of the smiley face\n" )
            y = input( "PLEASE ENTER A VALID PART: " )
            print( "\nPART = " + y  + "\n")            
            if y == "head":
                if toggle == 0:
                    turtle.ht()
                else:
                    turtle.st()
                drawH()
            elif y == "mouth":
                if toggle == 0:
                    turtle.ht()
                else:
                    turtle.st()
                drawM()
            elif y == "nose":
                if toggle == 0:
                    turtle.ht()
                else:
                    turtle.st()
                drawN()
            elif y == "eye":
                if toggle == 0:
                    turtle.ht()
                else:
                    turtle.st()
                drawE()
            else:
                print( "\nPART NOT RECOGNIZED\n" )
        elif x == "cursor":    
            if toggle == 0:
                turtle.st()
                print( "VISIBILITY - ON\n" )
                toggle = 1
            else:
                turtle.ht()
                print( "VISIBILITY - OFF\n" )
                toggle = 0        
        else:
            print( "COMMAND NOT RECOGNIZED\n" )
            
main()

