import pygame

#Mode 1, Color saving
    #Introduce ability to input color values (3 Hex Codes)
        #ask if the user would like to save that value
        #request a name for the color
#Mode 2, Color Display
    #ask the user what color they would like to display, this can be entered as a name, or hex code.
    #Display the color to the monitor for a set amount of time
    #Quit teh display and let the user request anotehr color, or let them quit

def main():
    print("Hello, welcome to the Dev McElroy Color picker!")
    print("lets get started")
    quit = False
    while(quit == False):
        R = input(f"please enter the 'R' value in the RGB code of your color: ")
        G = input(f"please enter the 'G' value in the RGB code of your color: ")
        B = input(f"please enter the 'B' value in the RGB code of your color: ")
        colorName = input("Please enter the name of your color")

if __name__ == "__main__":
    main()