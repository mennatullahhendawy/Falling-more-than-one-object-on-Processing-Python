# Falling more than one objective on Processing Python
 
Falling More than One Object Game
This repository contains the updated version of the Falling Objects Catching Game, which includes multiple falling objects, implemented using loops and arrays, as part of the Game Development 1 course at the University of California, Santa Cruz.

Acknowledgments
Acknowledgments: This project was developed as an assignment for the Game Development 1 course (GAME 235) at the University of California, Santa Cruz. The code was developed with the help of Mohamed Samy and Mohamed-Ali-77. Additionally, we used ChatGPT to assist in structuring and refining parts of the project.

Overview
The Revamped Falling Object Game extends the previous version by adding multiple falling objects, programmed using loops and arrays. The game also introduces a more complex scoring system with hysteresis (delayed score display) and bonus points for faster objects.

Game Features:
•	Arrays and loops are used to programmatically move multiple falling objects.
•	The player controls the paddle via mouse input.
•	Collision detection is managed through loops and arrays for multiple objects.
•	Falling objects respawn at random locations when caught or missed.
•	A more advanced scoring system awards more points for catching faster objects.
•	Hysteresis is applied to the score display, gradually updating the visual score.

Installation
1.	Download and install Processing.
2.	Enable Python Mode:
o	Open Processing.
o	Go to the Mode drop-down menu at the top right.
o	Select Python mode from the list.
3.	Clone or download this repository to your local machine.
4.	Open the falling_object_game_v2.pde file in Processing.

Usage
1.	Launch Processing.
2.	Open the falling_object_game_v2.pde file from this repository.
3.	Click the Run button in Processing to start the game.
4.	Use your mouse to control the paddle and catch the falling objects.

Code Functionality
•	Multiple Falling Objects: The game now includes several falling objects, with their positions and speeds stored in arrays.
•	Hysteresis in Score Display: The visual score display is delayed and gradually updates to reflect the actual score.
•	Bonus Points for Faster Objects: Objects falling faster than a set threshold earn the player bonus points when caught.

Example Code Snippet
```python
Copy code
ballRadius = 20  # Radius of the ball
ballFallSpeed = 5  # Initial speed of the balls

paddlePosX = 0  # Start position of paddle (position x) 
paddlePosY = 450  # Start position of paddle (position y) 
paddleWidth = 50  # Width of the paddle
paddleHeight = 25  # Height of the paddle

score = 0  # Score
fail = 0  # Failure count
displayScore = 0  # Display score (delayed/hysteresis score)
scoreIncrementSpeed = 2  # Speed at which the score display catches up to the actual score

# List to store positions and speed of multiple balls
ballPosX = []
ballPosY = []
ballSpeed = []

numBalls = 5  # Number of balls

def setup():
    size(640, 480)  # Background size
    background(255, 120, 120)  # Background color
    noStroke()  # Background without a stroke
    textSize(32)  # Text size for "fail" and "score"
    rectMode(CENTER)  # Set mouse location mode
    
    global ballPosX, ballPosY, ballSpeed  # Real-time variables

    # Initialize positions and speeds for each ball
    for i in range(numBalls):
        ballPosX.append(random(0, width))  # Random initial X position for each ball
        ballPosY.append(-ballRadius)  # Initial Y position for each ball
        ballSpeed.append(random(1, ballFallSpeed))  # Speed of each ball assigned randomly

def draw():
    global paddlePosX, score, fail, displayScore

    paddlePosX = mouseX  # Paddle moves with mouse in X direction
    
    background(255, 120, 120)  # Reset background to avoid drawing trails
    
    # Update and draw each ball
    for i in range(numBalls):
        ballPosY[i] += ballSpeed[i]  # Ball repeated movement

        # Check for collision with paddle
        if ballPosX[i] > paddlePosX - paddleWidth / 2 and ballPosX[i] < paddlePosX + paddleWidth / 2:
            if ballPosY[i] >= paddlePosY - paddleHeight / 2 and ballPosY[i] <= paddlePosY + paddleHeight / 2:
                if ballSpeed[i] > 3:  # Increase score with bonus for faster objects
                    score += 4
                score += 1  # Regular score increment
                ballPosX[i] = random(0, width)  # Reset X position for new ball
                ballPosY[i] = -ballRadius  # Reset Y position for new ball
                ballSpeed[i] += 1  # Increase ball fall speed after catch

        # Ball falls off screen (failure case)
        if ballPosY[i] > height:
            fail += 1  # Increment failure count
            ballPosX[i] = random(0, width)  # Reset X position for new ball
            ballPosY[i] = -ballRadius  # Reset Y position for new ball
            
        # Draw each ball
        fill(120, 120, 255)
        circle(ballPosX[i], ballPosY[i], ballRadius * 2)
    
    # Gradual update of displayed score (hysteresis effect)
    if displayScore < score:
        displayScore += 0.1
        if displayScore > score:
            displayScore = score

    # Draw paddle
    fill(220, 220, 220)
    rect(paddlePosX, paddlePosY, paddleWidth, paddleHeight)

    # Display score and failure count
    fill(35, 35, 35)
    text("Score: " + str(int(displayScore)), 10, 30)
    text("Fail: " + str(fail), 450, 30)

