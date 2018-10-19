def setup():
    size(1154,1080)
    
x = 0   
y = 0 
def draw():
    global x
    global y
    noStroke()
    
    if x >= 1150:
        x = 0
    if y >= 900:
        y = 0
    background(135,206,250)
    x += 2
    y += 1


    fill(255,255,0)
    ellipse(x,y,100,100)
    fill(255)
    ellipse(x+50,540-75,100,100)
    ellipse(x+20,540-25,100,100)
    ellipse(x+70,540-45,100,100)
    ellipse(x+70,540-85,100,100)

    ellipse(x+20,540-355,100,100)
    ellipse(x-20,540-325,100,100)
    ellipse(x+45,540-350,100,100)
    ellipse(x-45,540-375,100,100)

    fill(0,0,255)
    rect(0,600,1154,400)
