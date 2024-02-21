from turtle import *
import random 
from math import atan,sin,cos,pi,fabs
from time import *
def variables():
    size_of_block=50
    fill_color=['green','yellow']
    pen_color=['yellow','red','blue','black','orange','purple']
    start_end=['START','END']
    pre_lock=[1,2,3,100,99]
    ladder_gap=size_of_block/4
    ladder_count=5
    snake_count=5
    curve=size_of_block/4
    turtle_size=size_of_block/25
    p_position=['player_positions',1,1,1,1,1,1]
    return p_position,turtle_size,snake_count,curve,ladder_count,ladder_gap,pre_lock,size_of_block,fill_color,pen_color,start_end
def drawing_rows(size_of_block):
    starting_X=size_of_block*(-5)
    ending_X=size_of_block*5
    for rows in range(-5,6):
        Y=size_of_block*rows
        penup()
        setpos(starting_X,Y)
        pendown()
        setpos(ending_X,Y)
        
def drawing_columns(size_of_block):
    starting_Y=size_of_block*(-5)
    ending_Y=size_of_block*5
    for columns in range(-5,6):
        X=size_of_block*columns
        penup()
        setpos(X,starting_Y)
        pendown()
        setpos(X,ending_Y)

def getPositions():
    positions=[[0,0]]
    pass

def wrtiting_numbers_positions(size_of_block):
    positionsX=[[0]]
    positionsY=[[0]]
    starting_X=size_of_block*(-5)
    starting_Y=size_of_block*(-5)
    X,Y=starting_X+size_of_block/2,starting_Y+size_of_block/2
    for column in range(1,11):
        count=column
        for row in range(1,11):
            penup()
            setpos(X,Y)
            pendown()
            if row==1 and column==1:
                count=1
            if row==1:
                count=column
                positionsX[column-1][0]=X
                positionsY[column-1][0]=Y
            elif row%2==0:
                count=count+19-2*(column-1)
                positionsX[column-1].append(X)
                positionsY[column-1].append(Y)
            else:
                count=count+1+2*(column-1)
                positionsX[column-1].append(X)
                positionsY[column-1].append(Y)
            write(count) 
            Y=Y+size_of_block
        positionsX.append([0])
        positionsY.append([0])
        Y=starting_Y+size_of_block/2
        X=X+size_of_block
    return positionsX,positionsY

def color_start_and_end(X,Y,size_of_block,fill_color):
    penup()
    for i in range(0,2):
        drawX=X[i]-size_of_block/2
        drawY=Y[i]-size_of_block/2
        setpos(drawX,drawY)
        fillcolor(fill_color[i])
        begin_fill()
        pendown()
        for turns in range(1,5):
            fd(size_of_block)
            left(90)
        penup()
        end_fill()
        setheading(0)

def set_start_and_end(X,Y,pen_color,text,size_of_block):
    penup()
    for i in range(0,2):
        setpos(X[i]-size_of_block/4,Y[i])
        pencolor(pen_color[i])
        pendown()
        write(text[i])
        penup()
def reArrange_Positions_according_to_count(X):
    new=[0]
    count=0
    for row in range(0,10):
        for column in range(0,10):
            if (row+1)%2==1:
                if column==0 and row==0:
                    new[count]=X[column][row]
                else:
                    new.append(X[column][row])
            else:
                new.append(X[9-column][row])
            count+=1
    return new
def drawTruss(startX,startY,endX,endY,ladder_gap,tita_pi,pen_color):
    truss=Turtle()
    gap=25
    truss_len=25
    tita=tita_pi+90
    if 0>tita_pi:
        tita_pi=tita_pi+180
    currentX,currentY=startX,startY-ladder_gap
    truss.penup()
    truss.ht()
    truss.speed(0)
    truss.pencolor(pen_color[2])
    truss.setpos(currentX,currentY)
    l=((currentY-endY)**2+(currentX-endX)**2)
    run=0
    while l**0.5-gap>run:
        truss.penup()
        truss.setheading(tita_pi)
        truss.fd(gap)
        truss.setheading(tita)
        truss.pendown()
        truss.fd(truss_len)
        truss.penup()
        truss.back(truss_len)
        truss.setheading(tita_pi)
        currentX+=(gap*cos(tita_pi))
        currentY+=(gap*sin(tita_pi))
        run+=gap
        
def draw_ladders(pre_lock,start,end,startX,startY,endX,endY,ladder_gap,pen_color,is_ok):
    if is_ok:
        try:
            tita=atan((endY-startY)/(endX-startX))
        except:
            del pre_lock[-1]
            del pre_lock[-1]
            return 0,pre_lock
        tita_pi=180/pi*tita
        if round(tita_pi,0)!=180 and round(tita_pi,0)!=0:
            pencolor(pen_color[2])
            for i in [-ladder_gap,ladder_gap]:
                penup()
                setpos(startX,startY+i)
                pendown()
                setheading(tita_pi)
                setpos(endX,endY+i)
                penup()
            drawTruss(startX,startY,endX,endY,ladder_gap,tita_pi,pen_color)
            return 1,pre_lock
        else:
            del pre_lock[-1]
            del pre_lock[-1]
            return 0,pre_lock
    else:
        return 0,pre_lock
def validationLadders(start,end,pre_lock):
    check1=False
    check2=False
    final_check=False
    count=1
    l_list=len(pre_lock)
    if 4<(end-start)<15:
        check1=True
        for i in range(0,l_list):
            if pre_lock[i]==start or pre_lock[i]==end:
                break
            else:
                if count==l_list:
                    check2=True
                    pre_lock.append(start)
                    pre_lock.append(end)
            count+=1
        if check1 and check2:
            final_check=True
        return final_check,pre_lock
    else:
        return final_check,pre_lock
    
    
def count_ladders(ladder_count,X,Y,ladder_gap,pen_color,pre_lock):
    created=0
    ladder_start=['n']
    ladder_end=['n']
    while created<ladder_count:
        start,end=random.randint(1,100),random.randint(1,100)
        startX=X[start-1]
        endX=X[end-1]
        startY=Y[start-1]
        endY=Y[end-1]
        is_ok,pre_lock=validationLadders(start,end,pre_lock)
        ok,pre_lock=draw_ladders(pre_lock,start,end,startX,startY,endX,endY,ladder_gap,pen_color,is_ok)
        if ok==1 and created==0:
            ladder_start[0]=start
            ladder_end[0]=end
        elif ok==1:
            ladder_start.append(start)
            ladder_end.append(end)
        created=created+ok
    return ladder_start,ladder_end,pre_lock

def count_snakes(snake_count,X,Y,curve,pen_color,pre_lock):
    created=0
    snake_start=['n']
    snake_end=['n']
    while created<snake_count:
        start,end=random.randint(1,100),random.randint(1,100)
        startX=X[start-1]
        endX=X[end-1]
        startY=Y[start-1]
        endY=Y[end-1]
        is_ok,pre_lock=validationLadders(start,end,pre_lock)
        ok,pre_lock=draw_snakes(pre_lock,start,end,startX,startY,endX,endY,curve,pen_color,is_ok)
        if ok==1 and created==0:
            snake_start[0]=start
            snake_end[0]=end
        elif ok==1:
            snake_start.append(start)
            snake_end.append(end)
        created=created+ok
    return snake_start,snake_end,pre_lock

def draw_snakes(pre_lock,start,end,startX,startY,endX,endY,curve,pen_color,is_ok):
    if is_ok:
        try:
            tita=atan((endY-startY)/(endX-startX))
        except:
            del pre_lock[-1]
            del pre_lock[-1]
            return 0,pre_lock
        tita_pi=180/pi*tita
        if round(tita_pi,0)<180 and round(tita_pi,0)>0:
            tita_pi=tita_pi-90
            pencolor(pen_color[1])
            l=((startY-endY)**2+(startX-endX)**2)**0.5
            run=0
            penup()
            setpos(startX,startY)
            pendown()
            setheading(tita_pi)
            while l-2*curve>run:
                circle(curve,180)
                run+=(2*curve)
                if l-2*curve:
                    circle(-curve,180)
                    run+=(2*curve)
            dot(curve)
            return 1,pre_lock
        else:
            del pre_lock[-1]
            del pre_lock[-1]
            return 0,pre_lock
    else:
        return 0,pre_lock
def Menu():
    ok=True
    while ok:
        try:
            players=int(input('Enter the No. of players (Max=6): '))
            if 0<players<=6:
                ok=False
        except:
            print('Enter valid Number.')
    return players
def choose_players(players,pen_color):
    player_colors=['player colors']
    count=1
    copy_pen_color=['copy']
    for pen in pen_color:
        if pen==pen_color[0]:
            copy_pen_color[0]=pen
        else:
            copy_pen_color.append(pen)
    selected_colors=['selected']
    while players>0:
        is_out=False
        print('Remainning Colors : ')
        count_c=1
        for pen in copy_pen_color:
            if pen!=0:
                print(count_c,pen,sep='.')
            count_c+=1
        try:
            index=int(input('Enter the color of player '+str(count)+' : '))
            c=0
            for colo in selected_colors:
                if colo==index:
                    break
                else:
                    c+=1
                    if c==len(selected_colors):
                        is_out=True
            if 0<index<=len(pen_color) and is_out:
                color_index=index-1
                players-=1
                player_colors.append(color_index)
                copy_pen_color[color_index]=0
                selected_colors.append(index)
                count+=1
            else:
                print('This color already selected or Invalid Color')
        except Exception as e:
            print('Enter valid color',e)
    count_p=1
    print('\nPlayers\n')
    for pen in player_colors:
        if pen!='player colors':
            print('player '+str(count_p),pen_color[pen],sep=' -> ')
            count_p+=1 
    return player_colors
def create_turtles(player_colors,X,Y,turtle_size,pen_color):
    turtles=['players']
    for player in player_colors:
        if player!='player colors':
            demo_turtle=Turtle()
            demo_turtle.fillcolor(pen_color[player])
            demo_turtle.penup()
            demo_turtle.turtlesize(turtle_size)
            demo_turtle.setpos(X,Y)
            demo_turtle.speed(1)
            turtles.append(demo_turtle)
    return turtles
def dice():
    is_one=False
    sleep(3)
    num=random.randint(1,6)
    if num==1:
        is_one=True
    return num,is_one
def snake_down_ladder_up(code,p_positions,player,turtle,destination,snake_ladder_end,snake_ladder_start,X,Y):
    is_on_snake_ladder=False
    count=0
    for head in snake_ladder_end:
        if head==destination:
            is_on_snake_ladder=True
            break
        count+=1
    if is_on_snake_ladder:
        startX,startY=X[snake_ladder_start[count]-1],Y[snake_ladder_start[count]-1]
        turtle.setpos(startX,startY)
        p_positions[player]=snake_ladder_start[count]
        if code=='up':
            print('player',player,' GO UP !!!')
        else:
            print('player',player,' GO DOWN ###')
    
    
def demo_player(p_positions,player,turtle,destination,current_position,X,Y,snake_end,ladder_start,snake_start,ladder_end):
    desX=X[destination-1]
    desY=Y[destination-1]
    cX=X[current_position-1]
    cY=Y[current_position-1]
    while cX!=desX or cY!=desY:
        turtle.setpos(cX,cY)
        current_position+=1
        cX=X[current_position-1]
        cY=Y[current_position-1]
    turtle.setpos(cX,cY)
    p_positions[player]=destination
    snake_down_ladder_up('down',p_positions,player,turtle,destination,snake_end,snake_start,X,Y)
    snake_down_ladder_up('up',p_positions,player,turtle,destination,ladder_start,ladder_end,X,Y)
    if p_positions[player]==100:
        print('\n\nWinner is player',player,'  !!!!!!!\n\nEnd!!!')
        return True
    else:
        return False

def player_changing(player,p_positions,turtles,snake_end,ladder_start,snake_start,ladder_end,X,Y):
    is_one=True
    is_over=False
    while is_one:
        print('player '+str(player)+' : ',end='')
        num,is_one=dice()
        print(num,end='\n')
        current_position=p_positions[player]
        destination=p_positions[player]+num
        turtle=turtles[player]
        if destination<=100:
            is_over=demo_player(p_positions,player,turtle,destination,current_position,X,Y,snake_end,ladder_start,snake_start,ladder_end)
        else:
            print('Try Again Later. You can\'t go forward')
    return is_over
def main_code():
    speed(0)
    ht()
    print('Loading...')
    print('creating background...')
    p_positions,turtle_size,snake_count,curve,ladder_count,ladder_gap,pre_lock,size_of_block,fill_color,pen_color,start_end=variables()
    drawing_rows(size_of_block)
    drawing_columns(size_of_block)
    positionsX,positionsY=wrtiting_numbers_positions(size_of_block)
    X=[positionsX[0][0],positionsX[0][-1]]
    Y=[positionsY[0][0],positionsY[0][-1]]
    color_start_and_end(X,Y,size_of_block,fill_color)
    set_start_and_end(X,Y,pen_color,start_end,size_of_block)
    X=reArrange_Positions_according_to_count(positionsX)
    Y=reArrange_Positions_according_to_count(positionsY)
    print('Done!!!\ncreating ladders...')
    ladder_start,ladder_end,pre_lock=count_ladders(ladder_count,X,Y,ladder_gap,pen_color,pre_lock)
    print('Done!!!\ncreating snakes..')
    snake_start,snake_end,pre_lock=count_snakes(snake_count,X,Y,curve,pen_color,pre_lock)
    print('Done!!!\n\nWelcome!!!\n\nMenu')
    print(ladder_start,ladder_end,snake_start,snake_end)
    players=Menu()
    player_colors=choose_players(players,pen_color)
    startX,startY=X[0],Y[0]
    turtles=create_turtles(player_colors,startX,startY,turtle_size,pen_color)
    player_counter=1
    is_over=False
    while not is_over: 
        is_over=player_changing(player_counter,p_positions,turtles,snake_end,ladder_start,snake_start,ladder_end,X,Y)
        player_counter+=1
        if player_counter>players:
            player_counter=1
    
main_code()

