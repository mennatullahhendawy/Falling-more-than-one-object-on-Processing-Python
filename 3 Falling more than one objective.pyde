# this code is developed based on the code submitted in the previous assignment #2 

#ballPosX = 0 #start position of ball (position x) not available anymore because we have more than one ball
#ballPosY = 0 #start position of ball (position Y)  not available anymore because we have more than one ball

# Initial variables

ballRadius = 20  # Radius of the ball
ballFallSpeed = 5  # Initial speed of the balls

paddlePosX = 0  #start position of paddle (position x) 
paddlePosY = 450  ##start position of paddle (position y) 
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
    size(640, 480)  #background size
    background(255, 120, 120)  #background color
    noStroke()  #background without a stroke
    textSize(32) # text size for "fail" and "start
    rectMode(CENTER)  #mouse location
    
    global ballPosX, ballPosY, ballSpeed #real-time variables
    #ballPosX = width/2 #start position of the ball in the middle of the screen / background (not needed anymore because more than one ball)
    #ballPosY = -ballRadius #falling of the ball (not needed anymore because more than one ball)

    # Initialize positions and speeds for each ball
    for i in range(numBalls): # loop for initial state
        ballPosX.append(random(0, width))  # Random initial X position for each ball
        ballPosY.append(-ballRadius)  # Initial Y position for each ball
        ballSpeed.append(random(1,ballFallSpeed)) # Speed of each ball assigned randombly
    
def draw():
    global paddlePosX, score, fail,displayScore #variables that wil change real-time
    
    paddlePosX = mouseX  #paddle moving with the mouse in X direction
    
    background(255, 120, 120)  # background adding again to make sure the ball and paddle colour donot cover the screen color
    
    #  for loop to drawi each ball in real time
    for i in range(numBalls):
        ballPosY[i] = ballPosY[i] + ballSpeed[i]  # ball repeated movement

        # condition of collision for all balls (success case)
        if ballPosX[i] > paddlePosX - paddleWidth / 2 and ballPosX[i] < paddlePosX + paddleWidth / 2: #collision if statement when the ball is inbetween in relation to paddle X and Y position
            if ballPosY[i] >= paddlePosY - paddleHeight / 2 and ballPosY[i] <= paddlePosY + paddleHeight / 2: #check if ball touches paddle
                if ballSpeed[i]> 3: # Increase score with bonus if the ball is very fast
                    score += 4
                score += 1  # Increase score
                ballPosX[i] = random(0, width)  #initialize of x position for each ball
                ballPosY[i] = -ballRadius  #initialize of y position for each ball
                ballSpeed[i] += 1  # Increase ball fall speed

        # Ball missed the paddle (failure case)
        if ballPosY[i] > height:
            fail += 1  # Increase fail count
            ballPosX[i] = random(0, width)  # initialize of x position for each ball
            ballPosY[i] = -ballRadius  #initialize of y position for each ball
            
        # Draw each ball
        fill(120, 120, 255)
        circle(ballPosX[i], ballPosY[i], ballRadius * 2)
        
    # Implement hysteresis effect for score display (gradual update)

 
    if displayScore < score:
        displayScore += 0.1
        if displayScore > score:
            displayScore = score

    # Draw paddle
    fill(220, 220, 220)
    rect(paddlePosX, paddlePosY, paddleWidth, paddleHeight)

    # Draw score and fail text with hysteresis effect
    fill(35, 35, 35)
    text("Score: " + str(int(displayScore)), 10, 30)
    text("Fail: " + str(fail), 450, 30)
