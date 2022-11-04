'''Methods to draw and hide images upon collision.
    what class should have this method? 
       - score keepers (paddles, counters, etc)
       - any object that disappears on collision(method set up for this)
       
    you do NOT want two classes to have this method (bubble AND paddle/bucket/basket)
       
  Attributes & variables you will need:
      self.draw (bool) - defined in the same class that hass these methods.
          when draw == True - imagse will be add to the screen & collide with rects. otherwise, the won't!
      self.face (pygame Surface) - the image or shape needed on screen.
      win (global, pygame Surface) - the window you're drawing on'''

def show(self):
    if (self.draw):
        # only draw when self.draw is "on" (True)
        win.blit(self.face,(self.x,self.y))


def collide(self,rect):
    '''Controls what happens when coliding with another drawn object.
    Arguments
      rect (Rect object) - another pygame shape or Rect object that may be collided		
      example argument: Button.box'''
        # use self.draw to toggle drawing on and off. should be set to True to start
        if (self.draw): 
            # Only collide if drawing is on
            if self.box.colliderect(rect):
                # Change to be your outcome after collision
                self.draw = False # turn off drawing
    

#======== CALLING THESE METHODS =====

# yourObj.show() # call inside while loop (each iteration), outside of event for loop
# yourObj.collide() # call inside while loop (each iteration). put inside event for loop if key or mouse event is linked to collision

# mouse clicking in bubble should use self.box.collidepoint() instead
