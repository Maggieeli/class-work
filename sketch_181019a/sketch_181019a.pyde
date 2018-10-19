def setup():
    size(1154,1080)
    
x = 0   

def draw():
    global x
    
    if x >= 1150:
        x = 0
    background(138,43,226)
    x += 5
    fill(255)
    ellipse(x+50,540-75,100,100)
