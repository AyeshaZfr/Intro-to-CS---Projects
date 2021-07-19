import os
import random
global game, y_lvl, colors_list, w, h, cell

cell = 20
w = 200
h = 400
   
#make a list of colors, order here is: red, blue, greeen, yellow, purple, white, black    
colors_list=[[255,51,52],[12, 150, 228], [30, 183, 66], [246, 187, 0], [76, 0, 153], [255, 255, 255], [0, 0, 0]]


def backdrop():
    background(210,210,210)
    j = 0
    for c in range(w//cell):
        stroke(180)
        line(j, 0, j, h) #verticle
        j+=cell
    
    i = 0       
    for r in range(h//cell):
        stroke(180)
        line(0, i, w, i)
        i+=cell
 
    
   
#list of all the y values of every column, used to see where a block should land, initiated at 380 
y_lvl={}
for col in range(w//cell):
    y_lvl[col] = h - cell

    
       
             
class Block:
    def __init__ (self):
        self.y = -cell                      #intialize y at -cell so it is before grid      
        self.clr = random.randint(0,6)           
        self.stop = False                    #boolean value telling us when to stop a block fro oving or when to stop the update func in this from iterating.
        x=random.choice(list(y_lvl.keys()))
        self.x =  x*cell                      #random.randint(0, w//cell -1)*cell #will generate random block with attributes of that block
        
    
    #movement of block in y and x dimentions 
    def move(self):
         #checks to see if index of x generated is in dictionary keys or not, if not it won't execute loop 
            if self.x//cell in list(y_lvl.keys()):
                
                # stop a block from moving further down if it reaches botton or lands on another block 
                if self.y == y_lvl[self.x//cell]: 
                    #booleen value changed to true will be used in game class to stop iteration
                    self.stop =  True
                     #update the dictionary value corresponding to the key of the column block lands in so other blocks land on top of it
                    y_lvl[self.x//cell] = y_lvl[self.x//cell] - cell
        
                #increase y value by dim if block can still move downwards
                elif self.y < y_lvl[self.x//cell] and self.y>=-cell: #increase y value by cell if block can still move downwards
                    self.y += cell
            
                #makes sure that block does not move in last line after landing 
                if self.stop == False: 
                    # initializes the press of any key and defines and defines movement horizontally
                     if keyPressed ==True: 
                        
                        #  conditions makes sure block doesn't go out of domain that a block won't move into another block on the left/right
                        if keyCode == LEFT:
                            if cell<=self.x and y_lvl[(self.x//cell) - 1] - self.y > 0:
                                self.x -= cell                                                         
                        
                        elif keyCode == RIGHT:
                            if self.x <= w - cell*2 and y_lvl[(self.x//cell)+1] - self.y > 0:                
                                self.x += cell
                        else:
                            self.x +=0
    #initialize at every display 
    def update(self):
        self.move()
 
    #  what to disiplay everytime, update i.e. how blocks move, square of x,y values and color.
    #color is chosen randomly from a list of color codes (coded in  list format)   
    def display(self):
        self.update()  
        fill(colors_list[self.clr][0], colors_list[self.clr][1], colors_list[self.clr][2])
        noStroke()
        square(self.x, self.y, cell)

    
# inherit game from list class to easily store all boxes ans this display them.
#initiate game class with length and width of box.

class Game(list):
    def __init__(self): 
        self.append(Block())
        
        #initialize speed of 0 and score of zero, both increment when necessary during game
        self.speed = 0
        self.score = 0
        #initialize game end at Flase
        self.game_end = False
          
    
    def update(self):
        #update dictionary remove the index of any column that is full. this ensures that no random block is further generated in this column

        for key in y_lvl:
            if y_lvl[key] == -cell:
                del y_lvl[key]
         #define end condition, that all roes and columns in grid are full
       
        if len(self) == h//cell*w//cell:
            self.game_end = True
        else:
            self.game_end = False

        if self[len(self)-1].stop == True and self.game_end == False: 
            self.rmv_block()
            self.score_board()
            return self.append(Block())

    # print score board in top right of screen
    def score_board(self):
        fill(0,255,255)
        textSize(15)
        text("Score:" + str(self.score), w - cell*3, h/10)
    
    #define syntax of how to remove blocks
    def rmv_block(self):
        
        #create empty list to store instances of blocks
        rmv = []
        
        #if there is a block which has the same column, same color and is within a certain distance in the same column from the block, append it to the list.
        for b in self:
            if  b.clr == self[len(self)-1].clr and b.x  == self[len(self)-1].x and  b.y - self[len(self)-1].y <= cell*3:
                rmv.append(b)
        
        # when list len ==4, remove these blocks, reset speed to 1, increase the height of the column as other blocka have a new ground now and increment score y 1
        if len(rmv) == 4:
            y_lvl[self[len(self)-1].x//cell] = y_lvl[self[len(self)-1].x//cell] + (cell*4)
            self.score +=1
            self.speed = 0
            for b in rmv:
                self.remove(b)
         #otherwise, if blocks arent removed, increment frameCount to increase speed of incoming blocks
        else:
            if frameCount % 0.25 == 0:
                self.speed = self.speed + 0.25

    #display the board                     
    def display(self):        
        if self.game_end == True:
            background(0)
            fill (0, 255,255)
            textSize(15)
            textAlign(CENTER)
            text("Game over\n" +  "Score:" + str(self.score), w/2, h/2 + cell)
            return 
   
        backdrop() 
        self.update()
        self.score_board() 
        
        
        for block in self:
            block.display()
              
game = Game()

def setup():
    size(w, h)
    backdrop()
    frameRate(1000000)
    
def draw():
#slow down the game by not displaying every frame
    if frameCount%(max(1, int(8 - game.speed)))==0 or frameCount==1: 
        background(210)

#this calls the display method of the game class 
        game.display()


def mouseClicked():
    global game, y_lvl, colors_list, w, h, cell
    if game.game_end == True:
        game = Game()
    
            
