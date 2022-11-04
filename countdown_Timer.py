'''This class manages a countdown timer.
Does not display to screen (yet).

You can borrow this entire class and use it in your code FOR FREE.

DO NOT BORROW CODE YOU DO NOT UNDERSTAND
'''

class Timer:
    def __init__(self,limit=60):
        self.limit = limit
        self.clock = pygame.time.Clock()
        self.start=pygame.time.get_ticks() # get starter tick at Timer instantiation
        
        self.timeLeft = self.countDown()
        
    def countDown(self):
        '''Note: Will cound down based on time passed, not frame rate, or call frequency.
        Retuurns whole value time in seconds (int)'''
        currTime=(self.start + pygame.time.get_ticks())/1000 #calculate how many seconds
        return int(self.limit - currTime) # returns whole second numbers
    
    def countUp(self):
        '''Note: Will cound up based on time passed, not frame rate, or call frequency.
        Retuurns whole value time in seconds (int). THIS METHOD HAS NOT BEEN TESTED'''
        timePassed=(self.start + pygame.time.get_ticks())/1000 #calculate how many seconds
        return int(timePassed) # returns whole second numbers
      
# USING TIMER OBJECTS
# See https://github.com/ATLS1300/pygame-example/blob/main/pygame_clickGame.py for example use in game

# Instantiate outside of while loop:
#   timer = Timer() # note parameters

# Call countDown() method inside while loop:
#   timeLeft = timer.countDown()

# Use timeLeft to control gameplay with while loop:
#   if (timeLeft > 0): 
#   OR
#   while running and (timeLeft > 0):
