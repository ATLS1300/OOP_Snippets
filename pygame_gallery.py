#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 12:10:26 2021

@author: sazamore

This script will display your art by running your code, and then will allow
the user to step through the images using the left and right arrow keys.


Save this file in the same folder/repository as your individual scripts (.py).


When you run this code, a second window will pop up and show your art. To close that
window, simply hit the red X in the upper left corner. YOU MUST CLOSE THE
WINDOW BEFORE DISPLAYING THE NEXT PIECE. Ignore any white text errors that may
show up when running the code. It's all back-end gibberish that means very little.

Hit the red x on the GREEN MENU SCREEN to stop running the gallery.

YOU MUST END YOUR SCRIPT NAME WITH A NUMBER. (Ex. gallery1.py, gallery2.py)
"""
import pygame
import turtle, glob, os
pygame.init()

class GalleryManager():
    def __init__(self):

        # get files
        self.fileList = [] # empty list for files
        for name in glob.glob("*.py"):
            if name[-4].isdigit():
                self.fileList.append(name) # get all files that end in numbers
        self.numFiles = len(self.fileList)
        
        # print(f"There are {self.numFiles} images in this gallery"))
        # print("Use left and right arrows to step through them!")
        self.galIDX = 0 #gallery view index
        self.file = self.fileList[self.galIDX]
    
        self.buildMenu()
    
    def incDown(self):
        print("Drawing piece number {}".format(self.galIDX))
        print("This piece is titled '{}'".format(self.file[:-4]))
        # stop previous script
        command = "pkill " + self.file
        os.system(command)
        self.galIDX -=1
        if self.galIDX < 0:
            self.galIDX = len(self.fileList)-1
        self.displayArt()
        print(self.galIDX)
    
    def key(self,event):
        key= pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.incDown()
            print("left")
        if key[pygame.K_RIGHT]:
            self.incUp()
            print("right")
       
    def displayArt(self):
        """runs the script based on list index"""
        self.file = self.fileList[self.galIDX]
        command = "python " + self.file
        os.system(command)

    def incUp(self):
        print("Drawing piece number {}".format(self.galIDX))
        print("This piece is titled '{}'".format(self.file[:-4]))

        # stop previous script
        command = "pkill " + self.file
        os.system(command)
        
        self.galIDX +=1
        if self.galIDX >= len(self.fileList):
            self.galIDX = 0
            
        self.displayArt()
        print(self.galIDX)
            
    def buildMenu(self):
        # set up screen size, position & title
        w = 700
        h = 200
        self.menu = pygame.display.set_mode((w,h))
        pygame.display.set_caption("Generative Gallery Control Menu")

        running = True
        
        while running:
            self.menu.fill(pygame.Color("olivedrab"))
            
            # write instructions
            text = ["Use L and R arrows to enjoy each piece",
                    f"({self.numFiles} total)",
                    "Use arrows, don't close pop ups!"]
            font = pygame.font.SysFont("Arial",30, True)
            for i in range(3):
                render = font.render(text[i],True,(255,255,255))
                self.menu.blit(render,(w/10,h/6+i*50))
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                self.key(event)


if __name__=="__main__":
    gal = GalleryManager()


# turtList = [] #empty list
# colors = ["red","green"] # "red" is colors[0], "green" is colors[1]
# numTriangle = 2

# for i in range(numTriangle): # range creates values 0, 1
#     turt = turtle.Turtle("triangle")
#     # customize turtle
#     turt.shapesize(2)
#     turt.color(colors[i])
#     # add turtle to turtList
#     turtList.append(turt)
    
# turtList[1].forward(50)