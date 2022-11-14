'''
Uses pygame Timer and font objects to make a countup (stopwatch) and countdown timer class.

To use, either copy methods and attributes to use as needed or import with:
import pgTimer

then use dot notation to instantiate an object:
myTimer = pgTimer.Timer()

then you can use the object using dot nottaion:
myTimer.countUp() # call inside while loop
myTimer.showTime(WIN) # pass in surface to write time on.

Don't forget to play and tweak! You may want to edit parameters if you'll use with different fonts. 
'''
import pygame
pygame.init()

class Timer:
  def __init__(self,countDir=True,time=60,text='0'):
      self.totalTime = time
      self.countDir = countDir # if False, then clock counts up
      self.setToZero(time) # resets clock based on self.countDown

      # text settings
      self.fontSize=30
      self.font = pygame.font.SysFont('Consolas',
                                      self.fontSize)
      self.text = text # string to print
    
  def countUp(self):
      '''calculates time passed and returns time in
      seconds (int).'''
      seconds=(pygame.time.get_ticks()-self.start_ticks)/1000
      self.currTime = int(seconds)
      return self.currTime
      
  def countDown(self):
      '''calculates time elapsed and subtracts from time limit (self.totalTime). Returns time in
      seconds (int).'''
      self.currTime = self.totalTime-self.countUp()
      return self.currTime
    
  def showTime(self, surface):
      '''Uses pygame font object to draw time on screen.
      Argument - Surface (pygame Surface) to add text to.'''
      self.text = str(self.currTime)
      surface.blit(self.font.render(self.text, True, 
                    (255, 255, 255)),
                   (self.fontSize*1.2, 
                    int(self.fontSize*1.2)))

  def setToZero(self,time=60): 
      '''Gets computer clock time at method call,
      and resets Timer values (self.currTime).'''
      self.start_ticks=pygame.time.get_ticks()
      
      if self.countDir:
          self.currTime = time
      else:
          self.currTime = 0
          
# ================ EXAMPLE USE ================
#instantiate object
# timer = Timer()

# inside a loop, call methods:
# to count down, only call: timer.countDown()
# or counting up (stop watch) only call: timer.countUp()
# DO NOT call both countDown and countUp in the same while loop!

# You can choose to show the text on screen by using:
# timer.showTime(WIN) # pass in the name of the surface to draw on

# You can have the timer counting down and not show your users for an added challenge!
