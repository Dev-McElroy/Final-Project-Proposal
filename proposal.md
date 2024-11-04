# Advanced Color Selector

## [Link to Repository]([url](https://github.com/Dev-McElroy/Final-Project-Proposal.git))

## General Description

The Advanced color selector I am creating for my final project will be reminiscent  of the color selector you would find in any digital drawing software such as photoshop of illustrator. However these tools have a few limitation that I would like to resolve.
### Features

The features will include both replicas of the features found in colors selectors as well as my own adjustments:


Basic Features:

- The ability to enter a RGB code to produce a color in the viewport
- The ability to change the color in the viewport
- Save colors in a data set to be used for later
  - You should also be able to switch quickly between them without having to reenter their name or RGB code
- Remove colors from your saved selection


Features I want to add:

- The ability to look up a color by name rather than RGB code
- Name colors to personal specifications so they can retrieved easily from you saved colors
- Color comparison:
  - Be able to compare multiple colors within the same viewport
  - The user should be able to select the number of colors they want to compare and then select which colors go where in the viewport
  - This removes the need to switch back and forth within a color selector
- Adjusting comparisons:
  - After making your selections you should be able to swap color's positions to get an idea of which colors look better next to each other - Be able to switch between using RGB, HSL, and CMYK Color codes:
  - Additionally if you have named a color it's equivalent in another color code should maintain the name
 

## Potential Challenges
### Too Much Information
- The nature of colors is that there is nearly an infinite amount. Restricting myself to color codes limits the number of colors however there are still a near uncountable amount. So rather than producing a near endless string of if and else if statements to name colors, perhaps I could research a pre-exiting library that contains that information.

### The Viewport
- Although pygame is clearly a very robust tool I would be lying if I said I was fully comfortable with it. In order to make a viewport that can adapt to the number of colors the user wants to display I would need to do significant research of pygames capabilities.


## Possible Outcomes
###Ideal Outcome
After completing this project I would hope too create a color selector that is both easy to navigate and functional. My number one goal would be too allow the color comparison system to be quick to operate and easy to learn for any average person.

###Minimal Viable Outcome
Assuming the task becomes to difficult I would at the very least like to have a project that can:
- Display a color based on at least one color code
- Change which color is being displayed easily
- Save a specific color for later use.

In this state the project would not exactly be unique to other color pickers however it would be functional and simple to use.

## Major Milestones

1.) Establishing basic color selection
  - Entering Color codes
  - Displaying 1 color to the viewport
  - Being able to change the color that is being displayed

2.) Utilization of Color naming
  - The ability to save colors
  - Look up colors based on the name
  - Customize names of colors specifically those in you saved list

3.) Addition of color comparison
  - Be able to ask user for how many colors they want to compare
  - Allow user to select specific colors
  - Move the selected colors around, remove colors, or add more colors.
