# image-processing-project

In this project we are going to find out the co-efficient of restitution of a ball using image processing techniques.
## Step-1
At first we need video of ball bouncing on the floor with good seperation of color from background in a well lit place. 
Make sure that the ball doesn't move side wise while jumping as much as possible. Do this on a flat horizontal surface. 

## Step-2
Retrieve frames from video recorded. 

## Step-3
Mask out the ball from the background by allowing a window of values for each channel of colors using etme.py file. 
When perfectly done, there can only be white pixels representing ball in that frame. 
Do the same for every frame. 

## Step-4
Calculate the height of the ball in each frame by searching for non-zer0 values in mask from top/bottom. 
Here, the height doesn't mean the actual height in meters, it is the height in pixels. 
Save the value of height as height.csv .

## Step-5
Plot the height vs frame graph and make sure the plot is smooth and okay. 
Now get the values of local maximums from the values by just iterating through the values of height.csv. 
By calculating square-root of ratios of consecutive heights gives us the "e" - coefficient of restitution. 
