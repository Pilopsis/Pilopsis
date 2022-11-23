from tkinter import *
import random
#constants are like settings and one cannot change
GAME_WIDTH=700
GAME_HEIGHT=700
SPEED=150
SPACE_SIZE=50 #the number of boxes
BODY_PARTS=4
SNAKE_COLOR="pink"
FOOD_COLOR="red"
BACKGROUND_COLOR="black"


class Snake:
    def __init__(self):
      self.bodySize=BODY_PARTS
      self.coordinates=[]
      self.squares=[]

      for i in range (0,BODY_PARTS):
        self.coordinates.append([0,0])

      for x,y in self.coordinates:
        square=canvas.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=SNAKE_COLOR,tag="snake")
        self.squares.append(square)
class Food:
    def __init__(self):

        #places food randomly
        x=random.randint(0,(GAME_WIDTH/SPACE_SIZE)-1)* SPACE_SIZE
        y=random.randint(0,(GAME_WIDTH/SPACE_SIZE)-1)* SPACE_SIZE

        self.coordinates=[x,y]

        canvas.create_oval(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=FOOD_COLOR,tag="food") 

def next_turn(snake,food):
    x,y=snake.coordinates[0]
    if direction=="up":
        y-=SPACE_SIZE
    elif direction=="down":
        y+=SPACE_SIZE
    elif direction=="left":
        x-=SPACE_SIZE
    elif direction=="right":
        x+=SPACE_SIZE
    snake.coordinates.insert(0,(x,y))#update the coordinates of the snake

    square=canvas.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=SNAKE_COLOR)#new artmosphere

    snake.squares.insert(0,square)#new sgure created
 
    if x==food.coordinates[0]and y==food.coordinates[1]:
      global score

      score+=1

      label.config(text="Score:{}".format(score))

      canvas.delete("food")

      food=Food()

    else: 

     del snake.coordinates[-1]#remove the loop

     canvas.delete(snake.squares[-1])

     del snake.squares[-1]
    
    if collisions(snake):
         game_over()

    else:
      window.after(SPEED,next_turn,snake,food)

def change_direction(NewDirection):
    global direction

    if NewDirection=='left':
        if direction!= 'right':
         direction=NewDirection
    elif NewDirection=='right':
        if direction!= 'left':
         direction=NewDirection
    elif NewDirection=='up':
        if direction!= 'down':
         direction=NewDirection
    elif NewDirection=='down':
        if direction!= 'up':
         direction=NewDirection

def collisions(snake):
    x,y=snake.coordinates[0]

    if x<0 or x>=GAME_WIDTH:
        
        return True
    elif y<0 or y>=GAME_HEIGHT:   
        return True 
    
    for bodyPart in snake.coordinates[1:]:
        if x==bodyPart[0] and y==bodyPart[1]:
            return True
    return False        
    
def game_over():

    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2,canvas.winfo_height()/2,
     font=('consals',70),text="GAME OVER",fill="maroon",tag="gameover")
    

window=Tk()
window.title("Snake gamez")
window.resizable(False,False)

score=0
direction='down'
label=Label(window, text="Score:{}".format(score), font=('consolas,40'))
label.pack()

canvas=Canvas(window, bg=BACKGROUND_COLOR,height=GAME_HEIGHT,width=GAME_WIDTH)
canvas.pack()

window.update()
window_width=window.winfo_width()
window_height=window.winfo_height()
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()

x=int((screen_width/2)-(window_width/2))
y=int((screen_height/2)-(window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind('<Left>',lambda event: change_direction('left'))
window.bind('<Right>',lambda event: change_direction('right'))
window.bind('<Up>',lambda event: change_direction('up'))
window.bind('<Down>',lambda event: change_direction('down'))

snake=Snake()
food=Food()

next_turn(snake,food)


window.mainloop()