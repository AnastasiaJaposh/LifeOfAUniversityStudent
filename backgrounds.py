from pygame.math import Vector2 as Vec
import pygame

# in this module I'm storing everything that is related static display, the backgrounds, even the interactable objects and buttons

class Interactable():
    def __init__(self, pos, text, n):
        self.pos = pos # position of the interactable object
        self.text = pygame.font.SysFont('arial', 25).render(text, True, 'White') # transforms the string into pygame object
        self.rect = pygame.Rect(pos.x, pos.y, 50, 50)
        self.n = n # the number of choices, needed in case third child is also an option
        self.interacted = False
        
    def in_vicinity(self, rect):
        """
        Checks if an object is near self 
        
        :param rect: The rect of the object
        """
        if self.rect.colliderect(rect):
            return True
        return False

class Scene():
    def __init__(self, surface, barriers, interactables, text, text_rect, start_plr_pos, stats):
        self.surface = surface # the background surface
        self.barriers = barriers # list of all the barriers, for example: the wall, table, etc.
        self.interactables = interactables # an object which you can interact with
        self.text_position = -1 # the index of the list self.text it is currently displaying
        self.text_finished = False # if displaying the text is finished
        self.printing = False # if its currently printing
        self.text = text # list of the lines with has to be displayed
        self.text_rect = text_rect # all the texts have the same rect, since they are displayed in one window
        self.start_plr_pos = start_plr_pos # The start position of the player when the scene is initiated
        self.stats = stats # how each scene changes the stats of the player

    def print_text(self, screen): # prints the story
        """
        Displays the next line of the story onto the screen, in the dedicated text window
        
        :param screen: The screen the text will be displayed on
        """
        if not self.text_finished:
            if self.text_position >= len(self.text):
                self.text_finished = True
                self.printing = False
                return
            txt = pygame.font.SysFont('arial', 25).render(self.text[self.text_position], True, 'White')
            screen.blit(txt, self.text_rect)
        
    def print_interactable_txt(self, screen): # prints the question where you can choose
        """
        Displays the interactable text onto the screen, in the dedicated text window

        :param screen: The screen the text will be displayed on.
        """
        screen.blit(self.interactables.text, self.text_rect)



class Button(): # button object for the choosing the characters
    def __init__(self,id,  x, y, img):
        self.img = img
        self.id = id
        self.rect = self.img.get_rect(center=(x,y))
        self.clicked = False

    def draw(self, screen):
        """
        Draw the button on the screen.
        
        :param screen: The screen the button will be drawn on
        """
        screen.blit(self.img, self.rect)


                
