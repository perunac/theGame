#!/usr/bin/env python
"""
Player class
@autor: Pawel Wisniewski
"""
import pygame,pdb


class Player(pygame.sprite.Sprite):
  def __init__(self,xCoordintat,yCoordinat,image,maxSpeed,screenWidth,screenHeight):
    """
    Constructor sets all variables to starting state
    """
    self.rect   = pygame.Rect(xCoordintat,yCoordinat,image.get_width(),image.get_height())
    self.image  = image
    self.xVel   = 0
    self.yVel   = 0
    self.maxWidth   = screenWidth
    self.maxHeight  = screenHeight
    self.sprinting  = False
    self.maxSpeed   = maxSpeed
    self.slowing    = False
    self.width      = image.get_width()
    self.height     = image.get_height()
    self.falling    = True
    self.jumpCounter= 0
    self.jumping    = False
    self.onGround   = False

  def update(self,*args):
    """
    Deals with jumps and stuff
    """
    if not self.jumping and not self.onGround:
      self.falling = True
    if self.jumpCounter > 1:
      self.yVel += 0.2
      self.jumpCounter -= 1
    elif self.jumpCounter == 1:
      self.falling = True
      self.jumpCounter -= 1
    if self.falling:
      if self.yVel < 6:
        self.yVel += 0.1
    if self.slowing:
      if self.xVel > 0:
        self.xVel -= 0.1
      if self.xVel < 0:
        self.xVel += 0.1
    self.moveSingleAxis(self.xVel,0,*args)
    self.moveSingleAxis(0,self.yVel,*args)

  def moveLeft(self):
    """
    Moves player left
    """
    self.slowing = False
    self.onGround = False
    if self.sprinting:
      self.xVel = -self.maxSpeed
    else:
      self.xVel = -(self.maxSpeed/2)

  def moveRight(self):
    """
    Moves player right
    """
    self.slowing = False
    self.onGround = False
    if self.sprinting:
      self.xVel = self.maxSpeed
    else:
      self.xVel = (self.maxSpeed/2)

  def sprint(self):
    """
    Makes player sprint
    """
    self.sprinting = True

  def stopSprint(self):
    """
    Stops player sprinting
    """
    self.sprinting = False

  def stop(self):
    """
    Stops player
    """
    self.slowing = True

  def moveSingleAxis(self, xVel, yVel, objects):
    """
    This method checks for collisons and acually moves a player
    """
    self.rect.left  += xVel
    self.rect.top   += yVel
    for object in objects:
      if self.rect.colliderect(object.rect) and (xVel or yVel):
        if yVel > 0 and self.rect.bottom > object.rect.top : #moving down hitting top
          print "pierwsza"
          print self.rect,object.rect
          self.rect.bottom= object.rect.top
          self.falling = False
          self.jumping = False
          self.yVel = 0
          self.onGround = True
        elif yVel < 0 and self.rect.top < object.rect.bottom: #moving up hitting bottom
          print "druga"
          print self.rect,object.rect
          self.yVel = 0
          self.rect.top = object.rect.bottom
        elif self.rect.right > object.rect.left and self.rect.right < object.rect.right: #moving right hiting left side
          print "trzecia"
          print self.rect,object.rect
          self.rect.right = object.rect.left
          self.xVel = 0
        elif self.rect.left < object.rect.right: #moving left hiting right side
          print "czwarta"
          print self.rect,object.rect
          self.rect.left = object.rect.right
          self.xVel = 0

  def jump(self):
    """
    Makes player jump
    """
    if not self.jumping:
      self.onGround = False
      self.jumping = True
      self.jumpCounter = 30
      self.yVel = -6
      self.falling = False
