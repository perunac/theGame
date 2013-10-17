#!/usr/bin/env python
"""
Game class
@author: Pawel Wisniewski
"""


import pygame,sys,player,misc,walls
from pygame.locals import *


class Game(object):
  def __init__(self):
    """
    Game object constructor
    """
    #define constants
    self.SCREENWIDTH  = 800
    self.SCREENHEIGHT = 640
    self.PLAYER_START_X = 400
    self.PLAYER_START_Y = 590
    self.PLAYER_MAX_SPEED = 4
    self.FPS = 60
    self.MAP_FILE_PATH = './map.map'
    self.BLOCK_IMAGE_PATH = './blok.png'
    self.LADDER_IMAGE_PATH = './drabinka.png'


    #start pygame and get pygame surfaces




  def run(self):
    """
    This is main game function, well for now
    """
    pygame.init()
    self.SCREEN = pygame.display.set_mode((self.SCREENWIDTH,self.SCREENHEIGHT),pygame.DOUBLEBUF)
    self.PLAYER_IMAGE = pygame.image.load("./ludek.png")
    self.WALL_IMAGE = pygame.image.load(self.BLOCK_IMAGE_PATH)
    self.LADDER_IMAGE = pygame.image.load(self.LADDER_IMAGE_PATH)
    blocks = self.getMap(self.MAP_FILE_PATH, self.WALL_IMAGE, self.LADDER_IMAGE)


    self.PLAYER = player.Player(self.PLAYER_START_X, self.PLAYER_START_Y, self.PLAYER_IMAGE, self.PLAYER_MAX_SPEED, self.SCREENWIDTH, self.SCREENHEIGHT)
    CLOCK = pygame.time.Clock()

    running = True
    while running:
      self.SCREEN.fill(misc.Colors.WHITE)

      #events handling
      for event in pygame.event.get():
        if event.type == QUIT:
          running = False
        if event.type == KEYUP:
          if event.key == K_LEFT or event.key == K_RIGHT or event.key == K_UP or event.key == K_DOWN:
            self.PLAYER.stop()
          elif event.key == K_LSHIFT:
            self.PLAYER.stopSprint()
      keys = pygame.key.get_pressed()
      if keys[K_LEFT]:
        self.PLAYER.moveLeft()
      if keys[K_RIGHT]:
        self.PLAYER.moveRight()
      if keys[K_LSHIFT]:
        self.PLAYER.sprint()
      if keys[K_SPACE]:
        self.PLAYER.jump()
      if keys[K_UP]:
        self.PLAYER.moveUp()
      if keys[K_DOWN]:
        self.PLAYER.moveDown()


      #updating objects
      self.PLAYER.update(blocks);
      #bliting
      self.SCREEN.blit(self.PLAYER.image, self.PLAYER.rect)
      for block in blocks:
        self.SCREEN.blit(block.image, block.rect)

      pygame.display.flip()
      CLOCK.tick(self.FPS)

    pygame.quit()
    sys.exit()


  def getMap(self, mapFile, blockImage, ladderImage):
    """
    This returns blocks on the map
    """
    with open(mapFile) as f:
      rawMap = f.readlines()
    blocks = []
    x = y = 0
    for line in rawMap:
      for block in line:
        if block == "B":
          blocks.append(walls.Wall(x, y, blockImage))
        if block == "D":
          blocks.append(walls.Ladder(x, y, ladderImage))
        x += blockImage.get_width()
      x = 0
      y += blockImage.get_height()
    return blocks
