def setup():
    size(1200,1000)
#x,y,z for clouds and sun
#a,b for sheep
#c for dog    
x = 0   
y = 0 
z = 0
a = 0
b = 0
c = 0
def draw():
    global x
    global y
    global z
    global a
    global b
    global c
    noStroke()
    
    if x >= 1200:
        x = 0
    if y >= 1000:
        y = 0
    if z >= 1200:
        z = 0
    if a >= 1200:
        a = 0
    if b >= 1200:
        b = 0
    if c >= 1200:
        c = 0
    background(100,206,250)
    
    if x >= 300:
        background(37, 159, 237)
    if x >= 600:
        background(18, 119, 221)
    if x >= 900:
        background(0, 71, 171)
    if x >= 1150:
        background(29, 34, 90)
    
    x += 1.9
    y += 0.8
    z += 2.3
    a += 2
    b += 2.5
    c += 1.1
    #sun
    fill(255,255,0)
    ellipse(x,y,100,100)
    

    
    fill(255)
    #cloud 1
    ellipse(x+50,540-275,100,100)
    ellipse(x+20,540-225,100,100)
    ellipse(x+70,540-245,100,100)
    ellipse(x+70,540-285,100,100)
    #cloud 2
    ellipse(z+20,540-455,100,100)
    ellipse(z-20,540-425,100,100)
    ellipse(z+45,540-450,100,100)
    ellipse(z-45,540-475,100,100)
    
    #sheep 1
    fill(255,225,177)
    #legs
    rect(a+15,700,30,100)
    rect(a-45,700,30,100)
    #head
    ellipse(a+70,685,55,55)
    fill(255)
    ellipse(a+60,660,25,25)
    ellipse(a+75,660,25,25)
    ellipse(a+90,660,25,25)
    #eyes
    fill(0)
    ellipse(a+85,685,3,3)
    ellipse(a+70,685,3,3)
    #body
    fill(255)
    ellipse(a+20,680,70,70)
    ellipse(a-20,680,70,70)
    ellipse(a+25,720,70,70)
    ellipse(a-25,720,70,70)
    
    #sheep 2
    fill(255,225,177)
    #legs
    rect(b+15,700,30,100)
    rect(b-45,700,30,100)
    #head
    ellipse(b+70,685,55,55)
    fill(0)
    ellipse(b+60,660,25,25)
    ellipse(b+75,660,25,25)
    ellipse(b+90,660,25,25)
    #eyes
    fill(0)
    ellipse(b+85,685,3,3)
    ellipse(b+70,685,3,3)
    #body
    fill(0)
    ellipse(b+20,680,70,70)
    ellipse(b-20,680,70,70)
    ellipse(b+25,720,70,70)
    ellipse(b-25,720,70,70)

    #pig
    fill(255,192,203)
    #body
    ellipse(c+10,740,100,60)
    #head
    ellipse(c+65,730,50,50)
    #ear
    triangle(c+70,710,c+75,695,c+80,710)
    triangle(c+50,710,c+55,695,c+60,710)
    #eyes
    fill(0)
    ellipse(c+75,720,3,3)
    ellipse(c+60,720,3,3)
    #mouth
    triangle(c+62,730,c+67,740,c+72,730)
    #legs
    fill(255,192,203)
    rect(c+30,750,10,45)
    rect(c-30,750,10,45)
    #tail
    triangle(c-50,750,c-25,740,c-20,750)
    
    #barn
    fill(178,34,34)
    rect(950,600,350,400)
    #roof
    fill(160,82,45)
    triangle(900,600,1150,400,1350,600)


    
    
    fill(44,177,55)
    rect(0,790,1200,400)
