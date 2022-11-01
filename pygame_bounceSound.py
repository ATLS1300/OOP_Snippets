'''
Example code - Sound, Collision

Demonstates how to play backgond music and have sound effects.
Also shows collision with rects and windows.
Requires tech.wav, boing.wav and oof.wav to be in the same folde as this script.

*** ATTENTION ***
When working with sounds or images, files must be in the same folder. Do not use paths (path/to/folder/file.wav), or they will
not un on any computer and you will lose points for errors.

You must also mak surer that you woking folder in VS code is the same folder that contains this script and your 
sound/image files. Click the folder icon on the lefthand menu and select the containing folder. A new VS Code
window will generate and you will have to reopen the file.

'''
import pygame
import pygame.mixer as mixer #alias for faster typing
pygame.init()


# FOR BACKGROUND MUSIC 
# Load music using file name (.mp3 or .wav are usable)
soundfile = "tech.wav" # change to your file name
mixer.music.load(soundfile)

# Play the song at startup
# mixer.music.play()

# Stop the song
#mixer.music.stop()


# FOR MULTIPLE SOUND FX or MULTIPLE SOUND TRACKS
oof = "oof.wav"
bounce = "boing.wav"

def playFX(x,y):
    if x<0:
     mixer.Channel(0).play(mixer.Sound(oof))
    else:
     mixer.Channel(1).play(mixer.Sound(bounce))
     
# USE IN SIMPLE ANIMATION
w = 600
h = 400
win = pygame.display.set_mode((w,h))

class Circ:
    def __init__(self, x,y,rad=20, color=(100,100,100),sound=bounce):
        self.rad = rad
        self.color = color
        self.speed = 5
        self.sound = sound
        self.box = pygame.draw.circle(win,color,(x,y),rad) # draw circle, save Rect
        
    def move(self):
        '''horizontal bubble with bounce embedded. Uses contains to see if shape is 
        contained within window.'''
        self.box = self.box.move(self.speed,0) # moves left-right only
        # print(test)
        if (not win.get_rect().contains(self.box)):
            # box is not completely in window (off-screen)
            self.speed *= -1 # reverse direction
        self.draw()
    
    def draw(self):
        pygame.draw.circle(win, self.color, self.box[:2],self.rad)

    def bounce(self, rect,sound=True):
        '''plays sound if collides with another rect'''
        if (self.box.colliderect(rect)):
            self.speed *= -1
            if sound:
                mixer.Channel(0).play(mixer.Sound(self.sound))

def main():
    clock = pygame.time.Clock()   
    running = True

    # make objeects
    circRed = Circ(w-50,h/2,color=(255,100,100)) # plays
    circRed.speed = -5 # go left

    circGray = Circ(50,h/2,sound=oof) # plays boing sound

    while running:
        win.fill((0,0,0))
        
        # animate circles
        circRed.move()
        circRed.bounce(circGray.box)
        circGray.move()
        circGray.bounce(circRed.box,sound=False)

            
        for event in pygame.event.get():
            # ========= Add events here ========= 
            
            if (event.type == pygame.QUIT):
                pygame.quit()
                
        pygame.display.update()
        clock.tick(30)

# RUN CODE
main()