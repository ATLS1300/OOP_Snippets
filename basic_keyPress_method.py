
'''Basic key press interaction method
For moving the drawn object around. Does not have screen edge boundraies. 
Pair with pygaame draw call (circle, rect, ellipse) or surface blit() call


Your class will need position attributes:
self.x 
self.y

To move an image, self.x and self.y should be used to draw images or place Surface:
    pygame.draw.circle(surface,color,   (self.x, self.y),    radius)

'''

def keyPress(self, event, step= 5, up=pygame.K_UP, down=pygame.K_DOWN, left=pygame.K_LEFT, right=pygame.K_RIGHT):
    '''Checks for key press from pygame event.
    Argument:
        event - (pygame event), from pygame.event.get() (usually in loop)
        step - (int) the amount of movement with each key stroke, in pixels
        up - (pygame key) moves up, default is up arrow
        down - (pygame key) moves down, default is down arrow
        left - (pygame key) moves left, default is left arrow
        right - (pygame key) moves right, default is right arrow
    
    Call inside event for loop.
    '''
    if event.type == pygame.KEYDOWN:
        if event.key == up:
            self.y -= step
        elif event.key == down:
            self.y += step
        elif event.key == left:
            self.x -= step
        elif event.key == right:
            self.x += step                
# ========== CALLING THIS METHOD ==============

# yourObject.keyPress(event) # call inside of event for loop, inside while loop
