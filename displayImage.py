import pygame

pygame.init()

display_width = 800
display_height = 600

#Defining colors (in rgb)

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)

gameDisplay = pygame.display.set_mode((display_width,display_height))

#pygame.display.set_mode sets the game window size.
#Arguments are passed in as a tuple

pygame.display.set_caption("The Game Name")

#pygame.display.set_caption sets the game display name
#The name appears on the game display window

clock = pygame.time.Clock()

#pygame.time.Clock() defines the game clock
#Times things in the game

carImg = pygame.image.load("rcar.png")

def car(x,y):
    
    gameDisplay.blit(carImg, (x,y))
    
x = (display_width * 0.45)

y = (display_height * 0.8)



crashed = False

while not crashed:
    
    for event in pygame.event.get():
        
        #pygame.event.get() Checks for events(grabs events)
        #Mouse position, key strokes etc
        #Gets events per frame per second
        
        if event.type == pygame.QUIT:
            
            #pygame.QUIT identifies if player want to quit.
            #Quiting is by pressing the 'x' button on window
            
            crashed = True
            
    gameDisplay.fill(white)
    
    #Fills background white
    
    car(x,y)
    
    #Draws car at points x, y
    
    
    pygame.display.update()
    
    #Generally, all calculations happen in the background and after they are done they are displayed in a new frame
    #pygame.display.update() checks for all the events that have happened in the loop and updates the display frame
    
    clock.tick(60)
    
pygame.quit()

quit()