'''Basic click interaction method

Your class will need:
    self.draw (bool) - an attribute to act like a switch to turn drawing on and off. Should be on (True) at start.
    
FOR ANY CLICK INTERACTION, you MUST pair it with a corresponding key.
For clicking to "erase" or "pop" bubbles (modified Button class), consider using arrow keys to step through all of the 
bubbles and enter to pop them. This will require your bubble objects to be in a list, and the key function to be outside
of the class. We will over this in class on Tues, but be on the lookout for a tutorial.
'''

def checkClick(self, event):
    '''Checks for click interaction inside Rect in class (self.box)
    
    Call inside event for loop
    '''
    if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            # check for left mouse button
            if self.box.collidepoint(x, y):
                # check if click is inside & hide circle
                self.draw = False
                # self.size = -2 # stop drawing circle
                
# ========== CALLING THIS METHOD ==============

# yourObject.click(event) # call inside of event for loop, inside while loop
