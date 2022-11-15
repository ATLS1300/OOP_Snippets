"""
OOP Bounce Snippet
@author: Zamore

For use with objects.
A method for bounce interactions, using angle of incidence for naturalistic bounces.
Uses pygame vector to determine direction & movement.

HOW TO USE THIS CODE:
    
    1. Your class will reequire the following attributes:
        self.velocity = [x_vel,y_vel] (a velocity list with x and y speeds) 
    2. Copy the method & paste into your class
    3. Instantiate your object & call the method outside of a loop to ensure it works
    4. Adjust call, arguments to meet scripting needs
    5. Call inside loop

"""

def bounce(self,dim=2):
        '''calculates reflection of a bounced shape (pygame.Rect, turtle.Turtle), 
        if it is past a boundary.
        Arguments:
            dim (int) - dimension of bounce. 0 is horizontal bounce, 1 is vertical, 2 is corner (both, default)
        Example:
        
        Use this method with conditional:
            if (x < w) or (x <v 0):
                yourObj.bounce(0) # horizontal bounce
        '''

        if (dim==0):
            self.velocity[0] *= -1
        elif (dim==1):
            self.velocity[1] *= -1
        elif (dim==2):
            self.velocity[0] *= -1
            self.velocity[1] *= -1