import pygame
from pygame.locals import *
import time
import random

SIZE= 40
Background_colour=(110,110,5)


class Noodles:
    def __init__(self,parent_screen):
        self.image = pygame.image.load("resources/noodles.png").convert()
        self.parent_screen = parent_screen
        self.x= SIZE * 3
        self.y= SIZE * 3
        
    def draw(self):
        #self.parent_screen.fill((230, 177, 138))
        self.parent_screen.blit(self.image,(self.x, self.y))
        pygame.display.flip()
        
        
    def move(self):
        self.x = random.randint(0,24)*SIZE
        self.y = random.randint(0,19)*SIZE


class Snake:
    
    def __init__(self,parent_screen,length):
        
        self.parent_screen= parent_screen
        self.block= pygame.image.load("resources/peng.jpg").convert() #buildng block 
        self.length = length
        self.x= [SIZE]*length #defined dimentions
        self.y= [SIZE]*length
        self.diirection= "right"
        
    
    def snake_length(self):
        self.length +=1
        self.x.append(-1) #adding a new element into the array
        self.y.append(-1)
        
        
         
    def move_left(self):
        self.diirection = "left"
        
    def move_right(self):
        self.diirection = "right"
        
    def move_up(self):
        self.diirection = "up"
        
    def move_down(self):
        self.diirection = "down"
        

        
    def walk(self):
        
        for i in range(self.length -1 , 0, -1 ):
            self.x[i] = self.x[i -1 ]
            self.y[i] = self.y[i -1 ]
            
            
            
        
        if self.diirection == "left":
            self.x[0] -= SIZE
        if self.diirection == "right":
            self.x[0] += SIZE
        if self.diirection == "up":
            self.y[0] -= SIZE
        if self.diirection == "down":
            self.y[0] += SIZE
            
        self.draw()
        
        
    def draw(self):
        #self.parent_screen.fill((Background_colour))
        for i in range(self.length):
            
            self.parent_screen.blit(self.block,(self.x[i], self.y[i]))
        pygame.display.flip()
        
        
        
        
        
class Snake_game: #making class 
    
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("(:__Pengu Snake Game___:)")
        pygame.mixer.init()
        self.background_music()
        
        self.game_surface = pygame.display.set_mode((1000, 1000)) #Have initialized the game window
        #self.game_surface.fill((230, 177, 138)) #Background color 
        self.snake= Snake(self.game_surface,1) #made the snake in the game 
        self.snake.draw() #DRWAWING THE SNAKE 
        self.noodles = Noodles(self.game_surface)
        self.noodles.draw()
        
        
        
    def collision(self,x1,y1,x2,y2): # to increase the snake size .
        if x1 >= x2 and x1 < x2 + SIZE :
            if y1 >= y2 and y1 < y2 + SIZE :
                return True
            
        return False 
            
    def background_music(self):
        pygame.mixer.music.load("resources/bg.mp3")  #music has used for contnuous play
        pygame.mixer.music.play()   
    
       
    def game_sound(self,sound_effect):
        sound_effect=pygame.mixer.Sound(f"resources/{sound_effect}.mp3")
        pygame.mixer.Sound.play(sound_effect)
        
    def background_game(self):
        bg=pygame.image.load("resources/mainbg.jpg")
        self.game_surface.blit(bg,(0,0))
        
    
    
    
    def play(self):
        self.background_game()
        self.snake.walk()
        self.noodles.draw()
        self.score_show()
        pygame.display.flip()
        
        
        #collision_logic (snake with apple)
        if self.collision(self.snake.x[0] , self.snake.y[0] , self.noodles.x, self.noodles.y):
            self.game_sound("bruh-sound-effect")
            self.snake.snake_length()
            self.noodles.move()
            
            
        #collision logic with snake it self 
        for i in range(3,self.snake.length):
            
            if self.collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                self.game_sound("uwu-sound-effect")
                raise "Game Over"
        
            
            
            
    def score_show(self):
       font=pygame.font.SysFont('comc sans',30)
       score=font.render(f"Score: {self.snake.length}" , True , (0,0,0))
       self.game_surface.blit(score, (800,10))
       
       
        
        

    def game_over(self):  # when snake bits itself, the game over logic will work
        self.background_game()
        font=pygame.font.SysFont('Roboto',40)
        new_line1= font.render(f"Pengiun's Tummy is full: Total noodles bowl eaten is {self.snake.length}" , True , (0,0,0))
        self.game_surface.blit(new_line1,(200,300))
        new_line2=font.render("To eat again press Enter.", True , (0,0,0))
        self.game_surface.blit(new_line2,(200,350))
        
        pygame.display.flip()
        
        pygame.mixer.music.pause()
        
    def reset(self):
        self.snake= Snake(self.game_surface,1) #made the snake in the game 
        self.noodles = Noodles(self.game_surface)
       
        
    
    
    
    
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
    def run(self):
        running = True
        pause= False
        while running:    #To quit the window
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    
                    if event.key == K_ESCAPE:
                        running = False
                        
                    if event.key== K_RETURN:
                        pygame.mixer.music.unpause()
                        pause= False
                        
                    if not pause:
                        
                                          
                        
                        if event.key == K_LEFT:
                            
                            self.snake.move_left()
                            
                        if event.key == K_RIGHT:
                            
                            self.snake.move_right()
                        
                        if event.key == K_UP:
                        
                            self.snake.move_up()
                            
                        if event.key == K_DOWN: 
                            
                            self.snake.move_down()#for movement (movement logic)
                    
                        
                elif event.type == QUIT :
                    running = False
                    
            try:
                if not pause :
                    
                    self.play()
            except Exception as e:
                self.game_over()
                pause=True #to pause the game after 
                self.reset()
                
            time.sleep(.2)
                
                    
         
        
    
        
    
'''def draw_block(): #function to move the block (will be called later)
    game_surface.fill((230, 177, 138))
    game_surface.blit(block, ( block_x , block_y ) )
    pygame.display.flip()'''
    
    

if __name__ == "__main__":
    game= Snake_game()
    game.run()
    
    
'''    pygame.display.flip()
    
    run = True
    
    while run:    #To quit the window
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
                    
                if event.key == K_UP:
                    block_y -= 10
                    draw_block() #it is drawing the blovk each time I am pressing the key 
                    
                if event.key == K_DOWN: #for movement (movement logic)
                    block_y += 10
                    draw_block()
                    
                if event.key == K_LEFT:
                    block_x -= 10
                    draw_block()
                    
                if event.key == K_RIGHT:
                    block_x += 10
                    draw_block()
                    
            elif event.type == QUIT :
                run = False'''
                
    
    