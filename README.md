# Fernando Herrera Lab 6

It is recommended that you read the entire lab before you start working.

What you will do:

Practice the use of loops.
Process the arrow keys.
Use lists and tuples.
Task1 :
Create a program that simulates an etch a sketch machine on the gfxhat. The use use the arrow keys of the keyboard to create the pixels.
Wrap around the falue of x and y, ie if x is > 127, it goes back to x=0. If y > 63, it goes back to 0. Same for x<0 back to 127, y<0 back to 63.
Use the function getch from the click module to capture a keystroke
The key s is use to start again a new drawing on the hat.
The key q is used to quit.
The character code for the arrow keys are the following:
'\x1b[A' UP arrow key
'\x1b[B' DOWN arrow key
'\x1b[C' RIGHT arrow key
'\x1b[D' LEFT arro key
Your program should also display the text Etch a Sketch somewhere on the screen. Use the function displayText provided.
from gfxhat import lcd,  fonts
from PIL import Image, ImageFont, ImageDraw

def clearScreen(lcd):
    lcd.clear()
    lcd.show()

def displayText(text,lcd,x,y):
    lcd.clear()
    width, height = lcd.dimensions()
    image = Image.new('P', (width, height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fonts.AmaticSCBold, 24)
    w, h = font.getsize(text)
    draw.text((x,y), text, 1, font)
    for x1 in range(x,x+w):
        for y1 in range(y,y+h):
            pixel = image.getpixel((x1, y1))
            lcd.set_pixel(x1, y1, pixel)
    lcd.show() 
Task2:
Write a function displayObject with the folowing signature:
displayObject(obj,x,y)
The function displays an object represented as a tuple or a list on the gfxhat at position x,y

Test your function on the following objects:
f1 =  [
[1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1],
[0,1,1,1,1,1,1,0],
[1,0,1,1,1,1,0,1],
[1,0,0,1,1,0,0,1],
[1,0,0,1,1,0,0,1],
[0,0,0,1,1,0,0,0],
[0,0,0,0,0,0,0,0]
]

pm = [[0,0,0,1,1,1,1,1,0,0,0],
[0,0,1,1,1,1,1,1,1,0,0],
[0,1,1,1,1,1,1,1,1,1,0],
[1,1,1,1,1,1,1,1,0,0,0],
[1,1,1,1,1,1,1,0,0,0,0],
[1,1,1,1,1,1,0,0,0,0,0],
[1,1,1,1,1,1,0,0,0,0,0],
[1,1,1,1,1,1,1,0,0,0,0],
[1,1,1,1,1,1,1,1,0,0,0],
[0,1,1,1,1,1,1,1,1,1,0],
[0,0,1,1,1,1,1,1,1,0,0],
[0,0,0,1,1,1,1,1,0,0,0]
]
Write a program that tests your displayObject function. The program prompts the user for the x,y coordinates, the object to display and displays it.
Feel free to create your own objects to display on the gfxhat. I used piskel to create the two objects.