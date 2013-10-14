#!/usr/bin/env python
"""
Player class
"""
import pygame


class Player(pygame.sprite.Sprite):
  def __init__(self,xCoordintat,yCoordinat,image,maxSpeed,screenWidth,screenHeight):
    self.rect   = pygame.Rect(xCoordintat,yCoordinat,image.get_width(),image.get_height())
    self.image  = image
    self.xVel   = 0
    self.yVel   = 0
    self.maxWidth   = screenWidth
    self.maxHeight  = screenHeight
    self.sprinting = False
    self.maxSpeed = maxSpeed
    self.slowing = False
    self.width = image.get_width()
    self.height = image.get_height()
    self.falling = True
    self.jumpCounter = 0
    self.jumping = False

  def update(self,*args):
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
    self.slowing = False
    if self.sprinting:
      self.xVel = -self.maxSpeed
    else:
      self.xVel = -(self.maxSpeed/2)

  def moveRight(self):
    self.slowing = False
    if self.sprinting:
      self.xVel = self.maxSpeed
    else:
      self.xVel = (self.maxSpeed/2)

  def sprint(self):
    self.sprinting = True

  def stopSprint(self):
    self.sprinting = False

  def stop(self):
    self.slowing = True

  def moveSingleAxis(self, xVel, yVel, objects):
    self.rect.left  += xVel
    self.rect.top   += yVel
    for object in objects:
      if self.rect.colliderect(object.rect) and (xVel or yVel):
        if self.rect.right > object.rect.left: #moving right hiting left side
          print "trzecia"
          self.rect.right = object.rect.left
          self.xVel = 0
        elif self.rect.left < object.rect.right: #moving left hiting right side
          print object.rect.right, self.rect.left
          self.rect.left = object.rect.right
          self.xVel = 0
        elif yVel > 0 and self.rect.bottom > object.rect.top : #moving down hitting top
          print "pierwsza"
          self.rect.bottom= object.rect.top
          self.falling = False
          self.jumping = False
          self.yVel = 0
        elif yVel < 0 and self.rect.top < object.rect.bottom: #moving up hitting bottom
          print "druga"
          self.yVel = 0
          self.rect.top = object.rect.bottom
      if self.rect.top < 0 or self.rect.bottom > self.maxHeight or self.rect.left < 0 or self.rect.left > self.maxWidth:
        self.rect.center = (self.maxWidth/2, self.maxHeight/2)

  def jump(self):
    if not self.jumping:
      self.jumping = True
      self.jumpCounter = 30
      self.yVel = -6
