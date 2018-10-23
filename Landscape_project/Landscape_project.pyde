def setup():
    size(1154,1000)
    
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
  
    
    light = color(135,206,250)
    dark = color(0,0,128)
    lerpColor(light,dark,)
    background = lerpColor
    
    x += 2
    y += 1.5

    fill(255,255,0)
    ellipse(x,y,100,100)
    
    fill(255)
    ellipse(x+50,540-275,100,100)
    ellipse(x+20,540-225,100,100)
    ellipse(x+70,540-245,100,100)
    ellipse(x+70,540-285,100,100)

    ellipse(x+20,540-455,100,100)
    ellipse(x-20,540-425,100,100)
    ellipse(x+45,540-450,100,100)
    ellipse(x-45,540-475,100,100)
    
    #sheep 1
    fill(255,225,177)
    #legs
    rect(x+15,700,30,100)
    rect(x-45,700,30,100)
    #head
    ellipse(x+70,685,55,55)
    
    #body
    fill(255)
    ellipse(x+20,680,70,70)
    ellipse(x-20,680,70,70)
    ellipse(x+25,720,70,70)
    ellipse(x-25,720,70,70)

    
    
    fill(44,177,55)
    rect(0,790,1154,400)
