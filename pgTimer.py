'''
AUTHOR: Suibi, Dr. Z
11/9/2022

12/13/2022 - Updated to make get_Time(). No longer called with display to help stop clocks.
Added font parameter to Timer init to allow ease of changing fonts.

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
  def __init__(self,countDir=True,time=60,text='0',font='Consolas'):
      self.totalTime = time
      self.countDir = countDir # if False, then clock counts up
      self.reset(time) # resets clock based on self.countDown

      # text settings
      self.fontSize=30
      self.font = pygame.font.SysFont(font,
                                      self.fontSize)
      self.text = text # string to print
      self.manual = False # for overRiding clock time.
    
  def getTime(self):
      '''Gets the current time. For se in countdown and countup.'''
      return=(pygame.time.get_ticks()-self.start_ticks)/1000

  def countUp(self):
      '''calculates time passed and returns time in
      seconds (int).'''
      self.currTime = int(getTime())
      return self.currTime
      
  def countDown(self):
      '''calculates time elapsed and subtracts from time limit (self.totalTime). Returns time in
      seconds (int).'''
      self.currTime = self.totalTime-self.countUp()
      return self.currTime
    
  def setCurrTime(self,time):
      self.currTime = time
  
  def showTime(self, surface):
      '''Uses pygame font object to draw time on screen.
      Argument - Surface (pygame Surface) to add text to.'''
      self.text = str(self.currTime)
      surface.blit(self.font.render(self.text, True, 
                    (255, 255, 255)),
                   (self.fontSize*1.2, 
                    int(self.fontSize*1.2)))

  def reset(self,time=60): 
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
# timer.showTime(win) # pass in the name of the surface to draw on

# You can now override the time by calling setTime:
# timer.setTime(0) # time set to zero
# timer.showTime(win) # zero time displayd

# You can now reset the clock (or pause it)
# timer.reset(60) # resets the countDown timer to 60 s
# timer.showTime() # reseet time displayed

# You can have the timer counting down and not show your users for an added challenge!
