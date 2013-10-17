#!/usr/bin/env python
"""
Different types of blocks
@author: Pawel Wisniewski
"""
import pygame


class Wall(pygame.sprite.Sprite):
  def __init__(self, xCoordintat, yCoordinat, image):
    self.image = image
    self.width = image.get_width()
    self.height = image.get_height()
    self.rect   = pygame.Rect(xCoordintat, yCoordinat, self.width, self.height)

  def update(self):
    pass
class Ladder(pygame.sprite.Sprite):
  def __init__(self, xCoordintat, yCoordinat, image):
    self.image = image
    self.width = image.get_width()
    self.height = image.get_height()
    self.rect   = pygame.Rect(xCoordintat, yCoordinat, self.width, self.height)

  def update(self):
    pass
