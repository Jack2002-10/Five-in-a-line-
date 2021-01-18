import turtle
from tkinter.messagebox import showinfo

turtle.title("五子棋")
turtle.setup(width=1000, height=700)
pen = turtle.Pen()
turtle.bgcolor("#E8B565")
pen.speed(10)


def drawing():
    '''
    draing the keyboard
    :return:
    '''
    turtle.tracer(False)
    for i in vertex:#draw horizontal lines
        pen.up()
        pen.setposition(-280,i)
        pen.down()
        pen.forward(560)
    pen.left(90)
    for i in vertex:#vertical
        pen.penup()
        pen.setposition(i,-280)
        pen.down()
        pen.forward(560)
    turtle.update()

def drawpoints(x,y):
    '''
    draw the rated specific points
    :param x: x-coordinate
    :param y:y-coordinate
    :return:
    '''
    pen.up()
    pen.goto(x,y)
    pen.pencolor('black')
    pen.dot(6)

def showuser():
    '''

    :return: draw the user coin.
    '''
    pen.setposition(367, 236)
    pen.pendown()
    pen.fillcolor("black")
    pen.begin_fill()
    pen.circle(-50)
    pen.end_fill()
    pen.penup()


    # Draw the write coin
    pen.setposition(-367.0 ,-236.0)
    pen.pendown()
    pen.fillcolor("white")
    pen.begin_fill()
    pen.circle(50)
    pen.end_fill()
    pen.penup()

def drawCoin(x, y, color):
    """
    落子
    :param x:
    :param y:
    :param color: 颜色
    :return:
    """

    pen.showturtle()
    pen.penup()
    pen.pencolor(color)
    pen.fillcolor(color)
    pen.setposition(x, y)
    pen.dot(30)

def swapplayer():
    '''
    black coin player TRUE
    white coin player FALSE
    exchange palyer
    :return:
    '''
    global player
    pen.color('red')
    if player == 'black':
        pen.goto(-423.0 ,-150.0)
        player = 'white'
    else:
        pen.goto(417.0, 158.0)
        player = 'black'
    turtle.update()

def checkFull():
    global player
    coincannotput= True
    for i in range(15):
        for j in range(15):
            if board[i][j] == '*':
                coincannotput = False
    if coincannotput == True:
        player = 'draw'
        winneroutput()



def playChess(x,y):
    if x < -280 or x > 280:
        return
    if y > 280 or y < -280:
        return
    x2 = exactCoordinate(x)
    y2 = exactCoordinate(y)

    recordcoin(x2,y2) # draw coin and check Game and swap player



def exactCoordinate(coordinate):
    '''
    return the exact coordinate on the intersection of lines
    :param coordinate: x or y
    :return: the exact coordinate
    '''
    for i in vertex:
        if i >= coordinate:
            if i - coordinate < 20:
                return i
            else:
                return i - 40

def coordinateConverter(x):
    return x//40 + 7

def winneroutput():
    global player
    showinfo('Winner Output','The winner is %s'%player)
    pen.reset()
    init()

def showrange(x):
    if x-4 < 0:
        begin=0
    else:
        begin = x-4
    if x+4 > 0:
        end = 11
    else:
        end = x +1 #后面会用到range（）
    return begin,end

def showdiagonaluprange(x,y):
    diagonalleast = min([x, y])
    if (x<4 and y>10) or (x>10 and y<4):
        return 0,0,0
    elif diagonalleast < 4:
        diagonalstartx=x-diagonalleast
        diagonalstarty=y-diagonalleast
    else:
        diagonalstartx=x-4
        diagonalstarty=y-4
    diagonalmax= max ([x,y])
    if diagonalmax >10:
        numberofloop=15- diagonalmax
    else:
        numberofloop=5
    return diagonalstartx,diagonalstarty,numberofloop




def checkGame(x,y):
    '''
    check whether or not this user wins
    :param x: relative coordinate
    :param y: relative
    :return:
    '''
    checkFull()

    found = False #found means which user wins
    beginx,endx=showrange(x)
    beginy,endy=showrange(y)
    for i in range(beginx,endx):
        if board[i][y]==player and board[i+1][y]==player and board[i+2][y]==player and board[i+3][y]==player and board[i+4][y]==player:
            winneroutput()
            found=True
    if found == False:
        for i in range(beginy,endy):
            if board[x][i]==player and board[x][i+1]==player and board[x][i+2]==player and board[x][i+3]==player and board[x][i+4]==player:
                winneroutput()
                found = True



    if found ==False:
        beginx,beginy,numberofloop=showdiagonaluprange(x,y) #check diagonal upwards
        for i in range(numberofloop):
            if board[beginx][beginy] == player and  board[beginx+1][beginy+1] == player and  board[beginx+2][
                beginy+2] == player and  board[beginx+3][beginy+3] == player and  board[beginx+4][beginy+4] == player:
                winneroutput()
                found = True
            beginx += 1
            beginy += 1

    if found == False:
        beginx,beginroughy,numberofloop=showdiagonaluprange(x,14-y) #check diagonal downwards
        beginy = 14 - beginroughy
        for i in range(numberofloop):
            if board[beginx][beginy] == player and board[beginx + 1][beginy - 1] == player and board[beginx + 2][
                beginy - 2] == player and board[beginx + 3][beginy - 3] == player and board[beginx + 4][
                beginy - 4] == player:
                winneroutput()
                found = True
            beginx += 1
            beginy -= 1
    if found ==False:
        swapplayer()











def recordcoin(x,y):
    '''
    This used to change the board
    :param x: absolute position
    :param y: absolute position
    :return:
    check horizontal and vertical
    '''
    global board
    x1 = coordinateConverter(x)#x1,y1 are relative coordinates
    y1 = coordinateConverter(y)
    if board[x1][y1] == '*':
        drawCoin(x, y, player)
        board[x1][y1] = player
        checkGame(x1,y1)





def init():
    global vertex,board,player
    pen.shape("circle")
    vertex=[]
    begainning= -280
    for i in range(15):
        vertex.append(begainning)
        begainning += 40


    drawing()
    drawpoints(0,0)
    drawpoints(-160,160)
    drawpoints(160,160)
    drawpoints(160,-160)
    drawpoints(-160,-160)

    showuser()

    player= 'black'
    pen.fillcolor('red')
    pen.setposition(417,153)
    pen.down()
    turtle.update()

    board=[['*' for i in range(15)] for j in range(15)]


#*********Main program starts here.**********
init()
turtle.onscreenclick(playChess, btn=1)  # Left mouse bottom.
 # Right one



turtle.done()