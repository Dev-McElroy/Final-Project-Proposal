import pygame
import csv

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
    i = 0
    while(quit == False):
        R = int(input(f"please enter the 'R' value in the RGB code of your color: "))
        G = int(input(f"please enter the 'G' value in the RGB code of your color: "))
        B = int(input(f"please enter the 'B' value in the RGB code of your color: "))
        colorName = input("Please enter the name of your color: ")
        with open("colorNames.csv", "a") as add_item:
            csv_writer = csv.writer(add_item)
            csv_writer.writerow([colorName, R, G, B])
        if((input("If you have no other colors to enter type 'q' to quit, or enter anything else to continue entering colors")).lower() == 'q'):
            quit = True



if __name__ == "__main__":
    main()