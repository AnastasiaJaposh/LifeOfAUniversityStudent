import pygame
import constants as const
import backgrounds as bg
import tree
from pygame.math import Vector2 as Vec


# each list consists of 3 frames and the middle one is for idle
class Skin(): # handles different walk/idle animations for different skins
    def __init__(self, id, forward, backwards, left, right):
        self.id = id 
        self.forward = forward # list of frames, which is needed for moving forward 
        self.backwards = backwards # list of frames, which is needed for moving backwards
        self.left = left # list of frames, which is needed for moving left
        self.right = right # list of frames, which is needed for moving right


class Stats(): # stores stats
    def __init__(self, knowledge = 0, health = 0, friendship = 0):
        self.knowledge = knowledge
        self.rested = health
        self.friendship = friendship


class Player():
    def __init__(self, skin, pos, frame, anim, direc):
        self.skin = skin
        self.pos = pos 
        self.frame = frame # current frame
        self.anim = anim # list of frames which is looped over during animation
        self.rect = self.anim[frame].get_rect(center=(pos.x, pos.y))
        self.direc = direc # Vector2
        self.stats = Stats(0,0,0)
        self.walking = False
        self.collision = False
        self.vel = const.VELOCITY
    
    # when the scene changes, we need to change the players position(and rect) and their stats
    def change_scene(self, pos, stats):
        """
        Handles the change of player parameters in case the scene is changed.
        
        :param pos: The new position of the player.
        :param stats: How many points will each of the player stats be increased by.
        """
        self.pos = pos
        self.rect = self.anim[self.frame].get_rect(center=(pos.x, pos.y))
        self.stats.knowledge += stats.knowledge
        self.stats.rested += stats.rested
        self.stats.friendship += stats.friendship

    def draw(self, screen):
        """
        Draws the player on the screen
        
        :param screen: The screen the player is drawn on.
        """
        # since the player will have a new position we need to reset the rect too
        self.rect = self.anim[self.frame].get_rect(center=(self.pos.x, self.pos.y))
        screen.blit(self.anim[self.frame], self.rect)

    def idle(self):
        """
        Handles the idle state of the player.
        
        """
        self.walking = False
        self.frame = 1 # in the animations the middle one is the idle
    
    def walk(self, start_time):
        """
        Handles the walk of the player. Changes the animation and the frames based on their direction.
        
        :param start_time: The time at the start of the walk
        """
        # change the animation based on the direction
        if self.direc == Vec(0, 1):
            self.anim = self.skin.backwards
        elif self.direc == Vec(1, 0):
            self.anim = self.skin.right
        elif self.direc == Vec(0, -1):
            self.anim = self.skin.forward
        elif self.direc == Vec(-1, 0):
            self.anim = self.skin.left

        # if the animation happened, returns current time,
        # if it didn't returns previous time
        current_time = pygame.time.get_ticks()
        if current_time - start_time >= 150:
            # changes position based on the direction and velocity
            self.pos.x += self.vel*self.direc.x
            self.pos.y += self.vel*self.direc.y

            # restart the animation
            if len(self.anim) > self.frame + 1:
                self.frame +=1
            else:
                self.frame = 0
            return current_time
        return start_time




