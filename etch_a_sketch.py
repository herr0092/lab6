
import click
import herr0092_library as f


f.clearConsole()
f.clearScreen()
f.displayText('Etch a Sketch', 20, 15 )


print('''======================
    Instructions

 s = start/clear
 q = quit

======================''')

# Init variables
command = ''

x = 0
y = 0


while( command != 'q' ):
    command = click.getchar()
    f.randomBgColor()
    
    if ( command == '\x1b[A' ):
        y = y - 1
        if( y < 0 ):
            y = 63
        
        f.setPixel(x,y,1)
        

    elif ( command == '\x1b[B'):
        y = y + 1
        if( y > 63 ):
            y = 0
        
        f.setPixel(x,y,1)

    elif ( command == '\x1b[C'):
        x = x + 1
        if( x > 127 ):
            x = 0
        
        f.setPixel(x,y,1)

    elif ( command == '\x1b[D'):
        x = x - 1
        if( x < 0 ):
            x = 127
        
        f.setPixel(x,y,1)

    elif ( command == 's'):
        f.clearScreen()
    
    elif ( command == 'q' ):
        print('Have a nice day!')
        f.clearScreen()
        f.clearBacklight()

