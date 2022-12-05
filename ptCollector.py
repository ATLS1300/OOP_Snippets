'''
Code collects cursor points along clicks and drags

Use the class to get points from your screen.

The example in "if name" statment below will run when you run this code.
You can also import this tool with:

import ptCollcetor
c = ptCollector.Collector()

To use as a libary, make sure ptCollctor.py is in the same 
folder & select that folder in VS Code (File> Open Folder).

'''
import pygame

class Collector:
    def __init__(self):
        self.drag = False
        self.pts = []
        
    def getPts(self, event):
        '''
        Takes pygame event as argumeent. 
        A click returns a single point as a tuple (x,y)
        A click and drag returns a list of tuples [(x1,y1),...(xn,yn)]
        '''
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not self.drag:
                # drag is False
                self.pts = [] # reset points with new click-and-drag         
            x,y = event.pos
            self.pts.append((x,y))
            self.drag = True
            
        elif event.type == pygame.MOUSEBUTTONUP:
            # release button, stop collecting points
            self.drag = False
            return self.pts
        
        elif self.drag and event.type == pygame.MOUSEMOTION:
            # collect points after click
            x,y = event.pos
            self.pts.append((x,y))
        
if __name__ == "__main__":
    c = Collector()
    pts = [] # empty container
    win = pygame.display.set_mode((400,400))

    while True:
        
        for event in pygame.event.get():
            pts = c.getPts(event)
            
            if event.type == pygame.QUIT:
                pygame.quit()
        
        # draw mouse positions
        if pts: # points is not empty    
            # breakpoint()  
            if len(pts)>1:
                # therre was drragging, many point paiss collected
                pygame.draw.lines(win,(255,255,255),False,pts,5)
                pts = [] # clear points after drawing (mouse release)
            elif len(pts)==1:
                pts = pts[0] # use tuple, not list
                print(pts)
                # there was only a click, one point pair collected
                pygame.draw.circle(win,(255,255,255),pts,4)
                pts = []
        
        pygame.display.update()
            