import pygame
import csv

def main():
    print("Hello, welcome to the Dev McElroy Color picker!")
    print("lets get started")
    quit = False
    i = 0
    while(quit == False):
        R = int(input(f"please enter the 'R' value in the RGB code of your color: "))
        G = int(input(f"please enter the 'G' value in the RGB code of your color: "))
        B = int(input(f"please enter the 'B' value in the RGB code of your color: "))
        colorName = (input("Please enter the name of your color: ")).upper()
        with open("colorNames.csv", "a") as add_item:
            csv_writer = csv.writer(add_item)
            csv_writer.writerow([colorName, R, G, B])
        if((input("If you have no other colors to enter type 'q' to quit, or enter anything else to continue entering colors: ")).lower() == 'q'):
            quit = True
    select_colors("colorNames.csv")

def select_colors(file):
    with open("colorNames.csv")  as file:
        color_list = csv.reader(file)
        print("Here is the list of colors you created since first opening the color picker: ")
        for row in color_list:
            print(f"{row[0]} - {row[1]}, {row[2]}, {row[3]}")
    quit = False
    while (quit == False):
        selectedColor = input("Please enter the name of the color you wish to display: ").upper()
        with open("colorNames.csv") as file:
            color_list = csv.reader(file)
            for row in color_list:
                if row[0] == selectedColor:
                    print(f"Displaying color: {row[0]} with RGB values: {row[1]}, {row[2]}, {row[3]}")
                    colorDisplay(int(row[1]), int(row[2]), int(row[3]))
                    break
            else:
                print("Color not found.")
        
        if input("Type 'q' to quit and begin comparing colors or anything else to select a new color to display: ").lower() == 'q':
            quit = True

# Split ----------

    with open("colorNames.csv")  as file:
        color_list = csv.reader(file)
        print("Here is the list of colors you created since first opening the color picker: ")
        for row in color_list:
            print(f"{row[0]} - {row[1]}, {row[2]}, {row[3]}")
    quit = False
    while (quit == False):
        compared_colors = []
        for _ in range(2):
            selectedColor = input("Please enter a name of a color you wish to compare: ").upper()
            with open("colorNames.csv") as file:
                color_list = csv.reader(file)
                for row in color_list:
                    if row[0] == selectedColor:
                        print(f"Selected color: {row[0]} with RGB values: {row[1]}, {row[2]}, {row[3]}")
                        compared_colors.append((int(row[1]), int(row[2]), int(row[3])))
                        break
                else:
                    print(f"{selectedColor} not found in color list.")
        
        if len(compared_colors) == 2:
            colorComparison(compared_colors[0], compared_colors[1])
        
        if input("Type 'q' to quit or anything else to continue: ").lower() == 'q':
            quit = True
    
    


def colorDisplay(R, G, B):
    pygame.init()
    resolution = (800, 600)
    screen = pygame.display.set_mode(resolution)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # TODO: Some game logic
        screen.fill((R, G, B))
        pygame.display.flip()
    pygame.quit()

def colorComparison(colorOne, colorTwo):
    pygame.init()
    resolution = (800, 600)
    screen = pygame.display.set_mode(resolution)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # Fill the left half with colorOne
        pygame.draw.rect(screen, colorOne, (0, 0, resolution[0] // 2, resolution[1]))
        # Fill the right half with colorTwo
        pygame.draw.rect(screen, colorTwo, (resolution[0] // 2, 0, resolution[0] // 2, resolution[1]))
        pygame.display.flip()
    pygame.quit() 



if __name__ == "__main__":
    main()