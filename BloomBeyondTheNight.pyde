# BloomBeyondTheNight


# Create an empty list for the stars and flowers
stars = []
flowers = []

# Track the position and activity of meteors
meteorX = 0
meteorY = 0
meteorActive = False

# Set up the CANVAS and 150 stars
def setup():
    size(1000, 700)

# A random 150 fixed stars
    for i in range(150):
        x = random(width)
        y = random(420)
        s = random(1, 4)

        brightness = random(150, 225)
        speed = random(0.2, 0.6)

        stars.append([x, y, s, brightness, speed])
        
def draw():
    global meteorX
    global meteorY
    global meteorActive

    # SKY CHANGES WITH FLOWERS
# Count flowers to control the transition from night to day
    flowerCount = len(flowers)
    
# Convert the flower count into a daylight value between 0 and 1
    daylight = map(flowerCount, 30, 50, 0, 1)
    daylight = constrain(daylight, 0, 1)
    
# The color of the sky
    skyR = 10 + 125 * daylight
    skyG = 15 + 191 * daylight
    skyB = 40 + 195 * daylight

    background(skyR, skyG, skyB)


    # STARS
    noStroke()
# Read the position, size and brightness of each star
    for star in stars:
        x = star[0]
        y = star[1]
        s = star[2]
        brightness = star[3]

        fill(brightness)
        ellipse(x, y, s, s)
        
# Updata the brightness to create a twinkling effect
        star[3] = star[3] + star[4]

# Reverse the brightness change when it reaches the upper limit
        if star[3] > 225:
            star[3] = 225
            star[4] = -star[4]

# Reverse the brightness change when it reaches thr lower limit
        if star[3] < 120:
            star[3] = 120
            star[4] = -star[4]


    # SHOOTING STAR
# Only draw and move the meteor when it is active
    if meteorActive:
        stroke(255)
        strokeWeight(4)

        line(meteorX, meteorY, meteorX - 60, meteorY - 35)

        noStroke()
        fill(255)

        ellipse(meteorX, meteorY, 10, 10)

# Move the meteor towards the lower right of the screen
        meteorX = meteorX + 8
        meteorY = meteorY + 5

# Generate a flower when the meteor reaches the ground
        if meteorY > 500:
            flowerX = constrain(meteorX, 30, width - 30)

# Generate a random RGB colour for the new flower
            r = random(180, 255)
            g = random(100, 220)
            b = random(150, 255)

# Store the flower's position and colour in the flower list
            flowers.append([flowerX, 500, r, g, b])

# Stop the meteor after creating the flower
            meteorActive = False


    # GRASS GRADIENT
    noStroke()

# Blend the sky colour into the grass using horizonta lines
    for y in range(420, 500):
        value = map(y, 420, 500, 0, 1)

        r = skyR + (45 - skyR) * value
        g = skyG + (85 - skyG) * value
        b = skyB + (60 - skyB) * value

        fill(r, g, b)
        rect(0, y, width, 1)


    # MAIN GRASS
    fill(45, 85, 60)
    rect(0, 500, width, 200)


    # HOUSE

# House body
    noStroke()
    fill(187, 152, 158)
    rect(80, 430, 180, 140)

# Roof
    fill(82, 25, 19)
    triangle(60, 430, 280, 430, 170, 340)

# Door
    fill(105, 82, 157)
    rect(150, 500, 40, 70)

# Window
    fill(205, 173, 79)
    rect(105, 465, 35, 35)
    rect(200, 465, 35, 35)
  
    # TEXT
# Display the project title on the grass
    fill(27, 72, 58)
    textSize(36)
    text("BLOOM BEYOND the NIGHT", 520, 620)

    # STONE PATH
# Draw stones using different positions, size and colours
    noStroke()

    fill(150, 150, 150)
    ellipse(250, 590, 24, 18)
    ellipse(285, 610, 20, 15)

    fill(170, 170, 170)
    ellipse(320, 630, 26, 18)
    ellipse(355, 650, 22, 16)

    fill(130, 130, 130)
    ellipse(390, 670, 24, 17)


    # FLOWERS
# Draw all flowers stored in the flowers list
    for flower in flowers:
        x = flower[0]
        y = flower[1]

# Read the RGB colour values of each flower
        r = flower[2]
        g = flower[3]
        b = flower[4]

# Stem
        stroke(40, 110, 60)
        strokeWeight(3)
        line(x, y, x, y - 30)

# Petals
        noStroke()
        fill(r, g, b)

# Draw five petals around the flower centre
        ellipse(x, y - 40, 14, 18)
        ellipse(x - 9, y - 33, 14, 18)
        ellipse(x + 9, y - 33, 14, 18)
        ellipse(x - 6, y - 22, 14, 18)
        ellipse(x + 6, y - 22, 14, 18)

# Flower center
        fill(225, 210, 80)
        ellipse(x, y - 30, 10, 10)


    # PRESS SPACE
# Detect the space bar to create a new shooting star
def keyPressed():
    global meteorX
    global meteorY
    global meteorActive

    if key == ' ':
# Set a random starting position in the sky
        meteorX = random(50, 500)
        meteorY = random(50, 250)

# Activate the shooting star animation
        meteorActive = True
        
       
