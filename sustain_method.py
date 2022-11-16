'''
Method to wait a determined number of frames.
Good for:
limiting collisions over time, 
creating periods of invisibility, or 
periods of harder/easier gameplay (changed speed/time).

You will need an atttibute defined as:
    self.count = 0
which you can toggle with the output of this method, or chane the return lines in this method.

See the pygame example Repo for a working example.
'''

def sustain(self, numFrames):
    '''Creates True outcome for a determined number of frames.
    Argument:
    numFrames (int) - number of animation frames to keep the condition.
    This will change based on your fps. (2 s at 30fps is 60 frames, 2s at 60fps is 120 frames.)
    Returns boolean: True means the sustained period is on.'''
    
    self.count += 1
    
    if (self.count<numFrames):
        return True
    else:
        self.count = 0 #reset counter
        return False
    
    
#======== CALLING THIS METHOD =====

# Use in methods that get called each frame.
# def collide(self,rect):
# if (self.box.colliderect(rect)) and self.sustain(10):
#     self.draw = False # turn off drawing
