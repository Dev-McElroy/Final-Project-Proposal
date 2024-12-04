# ANGM 2305 Final-Project

## Link to Repository

Repository: <https://github.com/Dev-McElroy/Final-Project-Proposal.git>

## Demo

Demo Video: <https://vimeo.com/1036167685?share=copy>

# Explaination of The Project

## Major Functions

- Allows the user to create colors using RBG codes
- Allows the user to store colors using custom names and ustilize the names later 
- Allows the user to display their stored colors using their created names
- Allows the user to compare two different colors which they have generated
- The user is able to easily exit out of and re-enter pygame display through teh use of loops to continue using color display and comparison functions

## Explaination of process

### Step 1:

- Upon runnning the program the user will be prompted to begin entering RGB values.
    - The prompts will go in order of R, then G, then B.
- The user will then be asked to name the color they have just created.
- This cycle will loop until the user enters 'q' to quit this first step.

### Step 2:

- After quitting the color creation stage the user will be provided with a list of teh colors they created along with the colors RGB data.
- The user can then select a color to use
    - Upon answering the prompt, the pygame window will open with an 800 by 600 display with the given color painted onto it.
    - THe window can then be closed and the user will be asked to enter a new color or to quit the color display mode.

### Step 3:

- After quitting teh color display mode, the user will be prompted to select two colors
    - After selecting two colors the pygame display will open and display both colors simulaneously. One on the left, the other on the right
    - This window similarily to teh last can be closed which will prompt the user to select two more colors or quit the program.
