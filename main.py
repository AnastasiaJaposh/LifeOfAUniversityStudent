import pygame
from sys import exit
from pygame.math import Vector2 as Vec
import constants as c
import backgrounds as bg
import characters as chr
import tree

# extracts text into a list from a file by only a filename
def extract_txt(filename):
    l = []
    with open(f'story/{filename}.txt') as f:
        line = f.readline().strip()
        while line != '':
            l.append(line)
            line = f.readline().strip()
    return l

pygame.init()

screen = pygame.display.set_mode((c.SCREEN_SIZE, c.SCREEN_SIZE))
pygame.display.set_caption('Semester project')
clock = pygame.time.Clock()

# set up the initial surface
surface = pygame.image.load('sprites/Backgrounds/start.png')
surface = pygame.transform.scale(surface, (c.SCREEN_SIZE, c.SCREEN_SIZE))


sprite_sheet_image = pygame.image.load('sprites/Characters.png').convert_alpha()

story_unlock_txt = pygame.font.SysFont('arial', c.AVG_TXT).render('Press ENTER to navigate through the story', True, 'White')
interact_txt = pygame.font.SysFont('arial', c.AVG_TXT).render('Press E to interact', True, 'White')
text_rect = pygame.Rect(15, 425, 575, 175)

barrier_txt_w = pygame.Rect(0, 400, 600, 200)
barrier_wall = pygame.Rect(0,0,600, 120)

# set up the bedroom scenes
bedroom_surface = pygame.transform.scale(pygame.image.load('sprites/Backgrounds/Bedroom.png'), (c.SCREEN_SIZE, c.SCREEN_SIZE))

barrier_bed = pygame.Rect(0,0,120, 200)
barrier_sofa = pygame.Rect(520, 0, 600, 220)

alarm_interactable = bg.Interactable(Vec(500, 180), 'Would you like to: 1. go back to sleep, 2. get up?',2)
uni_brkfst_interactable = bg.Interactable(Vec(255, 150), 'What is your choice: 1 or 2?',2)

bedroom_scene_1 = bg.Scene(bedroom_surface, [barrier_txt_w, barrier_wall, barrier_bed, barrier_sofa], 
                           alarm_interactable, extract_txt('bedroom_story_1'), text_rect, Vec(145, 160), chr.Stats(0,0,0))
bedroom_scene_2 = bg.Scene(bedroom_surface, [barrier_txt_w, barrier_wall, barrier_bed, barrier_sofa], 
                           uni_brkfst_interactable, extract_txt('bedroom_story_2'), text_rect, Vec(150, 160), chr.Stats(0, 1, 0))

# set up the kitchen scene
kitchen_surface = pygame.transform.scale(pygame.image.load('sprites/Backgrounds/Kitchen.png'), (c.SCREEN_SIZE, c.SCREEN_SIZE))

barrier_kitchen_items = pygame.Rect(0,0,400,150)
barrier_kitchen_table = pygame.Rect(495, 0, 105, 190)

stove_interactable = bg.Interactable(Vec(275, 140), 'Would you like to 1. have breakfast, 2.skip it?', 2)
lib_home_kitchen_interactable = bg.Interactable(Vec(480, 180), '1. go to the library to study, 2.stay home and do nothing?', 2)

kitchen_scene_3 = bg.Scene(kitchen_surface, [barrier_txt_w, barrier_wall, barrier_kitchen_items, barrier_kitchen_table], 
                           stove_interactable, extract_txt('kitchen_story_3'), text_rect, Vec(300, 300), chr.Stats(1, 0.5, 0))
kitchen_scene_4 = bg.Scene(kitchen_surface, [barrier_txt_w, barrier_wall, barrier_kitchen_items, barrier_kitchen_table], 
                           lib_home_kitchen_interactable, extract_txt('kitchen_story_4'), text_rect, Vec(300, 300), chr.Stats(0, 1, 0))
# set up the university scene
university_surface = pygame.transform.scale(pygame.image.load('sprites/Backgrounds/University.png'), 
                                            (c.SCREEN_SIZE, c.SCREEN_SIZE))

barrier_left_seats_1 = pygame.Rect(60, 175, 156, 30)
barrier_left_seats_2 = pygame.Rect(60, 275, 156, 30)

barrier_right_seats_1 = pygame.Rect(385, 175, 150, 30)
barrier_right_seats_2 = pygame.Rect(385, 275, 150, 30)


lib_home_uni_interactable = bg.Interactable(Vec(210,200), '1. go to the library to study, 2.stay home and do nothing?', 2)
sleep_not_uni_interactable = bg.Interactable(Vec(210,200), '1. sleep in class, 2. stay awake?', 2)

uni_scene_5 = bg.Scene(university_surface, [barrier_txt_w, barrier_wall, barrier_left_seats_1, barrier_left_seats_2,
                         barrier_right_seats_1, barrier_right_seats_2], lib_home_uni_interactable, extract_txt('uni_story_5'),
                         text_rect, Vec(300, 350), chr.Stats(1, 1, 0))
uni_scene_6 = bg.Scene(university_surface, [barrier_txt_w, barrier_wall, barrier_left_seats_1, barrier_left_seats_2, 
                                            barrier_right_seats_1, barrier_right_seats_2], sleep_not_uni_interactable, 
                                            extract_txt('uni_story_6'), text_rect, Vec(300, 350), chr.Stats(0, 0, 0))
uni_scene_7 = bg.Scene(university_surface, [barrier_txt_w, barrier_wall, barrier_left_seats_1, barrier_left_seats_2, 
                                            barrier_right_seats_1, barrier_right_seats_2], lib_home_uni_interactable, 
                                            extract_txt('uni_story_7'), text_rect, Vec(300, 350), chr.Stats(0,1, 0))
uni_scene_7_2 = uni_scene_7 = bg.Scene(university_surface, [barrier_txt_w, barrier_wall, barrier_left_seats_1, 
                                            barrier_left_seats_2, barrier_right_seats_1, barrier_right_seats_2], 
                                            lib_home_uni_interactable, extract_txt('uni_story_7'), text_rect, Vec(300, 350), chr.Stats(1, 0, 0))

# set up the library scene
library_surface = pygame.transform.scale(pygame.image.load('sprites/Backgrounds/Library.png'), (c.SCREEN_SIZE, c.SCREEN_SIZE))

barrier_lib_tables = pygame.Rect(0, 0, 233, 250)
barrier_lib_bookshelf = pygame.Rect(300, 290, 300, 310)

call_interactable = bg.Interactable(Vec(150,245), '1. I have the gift ready, 2. I forgot about the birthday', 2)
bar_lib_home_interactable = bg.Interactable(Vec(150, 245), 'What is your choice: 1, 2 or 3?', 3)

lib_scene_8 = bg.Scene(library_surface, [barrier_txt_w, barrier_wall, barrier_lib_bookshelf, barrier_lib_tables], 
                       call_interactable, extract_txt('lib_story_8'), text_rect, Vec(200, 350), chr.Stats(1, 0, 0))
lib_scene_10 = bg.Scene(library_surface, [barrier_txt_w, barrier_wall, barrier_lib_bookshelf, barrier_lib_tables], 
                        bar_lib_home_interactable, extract_txt('lib_home_story_10_11'), text_rect, Vec(120, 300), chr.Stats(0, 0, 2))
lib_scene_10_2 = bg.Scene(library_surface, [barrier_txt_w, barrier_wall, barrier_lib_bookshelf, barrier_lib_tables],
                         bar_lib_home_interactable, extract_txt('lib_home_story_10_11'), text_rect, Vec(120, 300), chr.Stats(0, 0, 0))

bedroom_scene_9 = bg.Scene(bedroom_surface, [barrier_txt_w, barrier_wall, barrier_bed, barrier_sofa], call_interactable, 
                           extract_txt('bedroom_story_9'), text_rect, Vec(150, 160), chr.Stats(0, 0.3, 0))
bedroom_scene_11 = bg.Scene(bedroom_surface, [barrier_txt_w, barrier_wall, barrier_bed, barrier_sofa], bar_lib_home_interactable, 
                            extract_txt('lib_home_story_10_11'), text_rect, Vec(150, 160), chr.Stats(0, 0, 2))
bedroom_scene_11_2 = bg.Scene(bedroom_surface, [barrier_txt_w, barrier_wall, barrier_bed, barrier_sofa], bar_lib_home_interactable, 
                              extract_txt('lib_home_story_10_11'), text_rect, Vec(150, 160), chr.Stats(0,0,0))

# set up the bar scene
bar_surface = pygame.transform.scale(pygame.image.load('sprites/Backgrounds/Bar.png'), (c.SCREEN_SIZE, c.SCREEN_SIZE))
barrier_tables_left = pygame.Rect(0, 0, 255, 267)
barrier_tables_right = pygame.Rect(320, 0, 280, 267)
bar_table = pygame.Rect(0, 0, 600, 150)
end_interactable = bg.Interactable(Vec(300, 300), 'end the game? 1-2 : yes', 2)

bar_scene_12 = bg.Scene(bar_surface, [barrier_txt_w, barrier_wall, barrier_tables_left, bar_table, barrier_tables_right], end_interactable, 
                        extract_txt('bar_story_12'), text_rect, Vec(300,360), chr.Stats(0, 0.4, 1))
lib_scene_13 = bg.Scene(library_surface, [barrier_txt_w, barrier_wall, barrier_lib_bookshelf, barrier_lib_tables], end_interactable, 
                        extract_txt('lib_story_13'), text_rect, Vec(300, 350), chr.Stats(1, 0, 0))
bedroom_scene_14 = bg.Scene(bedroom_surface, [barrier_txt_w, barrier_wall, barrier_bed, barrier_sofa], end_interactable, 
                            extract_txt('bedroom_story_14'), text_rect, Vec(150, 160), chr.Stats(0, 1, 0))

# set up the nodes and their children
node_14 = tree.Node(14, bedroom_scene_14)
node_13 = tree.Node(13, lib_scene_13)
node_12 = tree.Node(12, bar_scene_12)

node_11 = tree.Node(11, bedroom_scene_11, node_12, node_13, node_14)
node_10 = tree.Node(10, lib_scene_10, node_12, node_13, node_14)

node_9 = tree.Node(9, bedroom_scene_9, node_11, node_11)
node_8 = tree.Node(8, lib_scene_8, node_10, node_10)

node_7 = tree.Node(7, uni_scene_7, node_8, node_9)
node_6 = tree.Node(6, uni_scene_6, node_7, node_7)
node_5 = tree.Node(5, uni_scene_5, node_8, node_9)
node_4 = tree.Node(4, kitchen_scene_4, node_8, node_9)

node_2 = tree.Node(2, bedroom_scene_2, node_4, node_5)
node_3 = tree.Node(3, kitchen_scene_3, node_5, node_6)

node_1 = tree.Node(1, bedroom_scene_1, node_2, node_3)

tr = tree.Tree(node_1)

# This handles the walking, interacting, barriers and displaying the text in the specific scene
def Scene_playthrough(plr, scene):
    """
    Handles walking, interacting with interactable objects, colliding with the barriers and displaying the text in the specific scene. 
    
    :param plr: Player object of the game
    :param scene: The scene which everything is drawn on.
    """    
    can_walk = True # player can only walk if this is set to True, I set it to false if player has collided with a barrier

    #I've defined 2 time objects 
    time = pygame.time.get_ticks() # this is for walking
    time_txt = pygame.time.get_ticks() # this is for navigating through the text

    # changes player settings based on the scene
    plr.change_scene(scene.start_plr_pos, scene.stats)

    last_clicked_arrow = pygame.time.get_ticks()
    while True:
        # set up the screen
        screen.blit(scene.surface, (0,0))
        plr.draw(screen)

        # check the events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        
        # first the collisions are detected, since 
        # the player is set back before they even get a chance to change directions
        
        # if the player is colliding with any of the barriers,
        # they will be set back a little bit and they would change the state to idle
        # the collision becomes True
        for x in scene.barriers:
            if x.colliderect(plr.rect):
                plr.collision = True
                plr.idle()
                plr.pos.x -= plr.direc.x*plr.vel
                plr.pos.y -= plr.direc.y*plr.vel
                break
            plr.collision = False


        keys = pygame.key.get_pressed()

        # if the arrow keys are pressed, it sets the can_walk to True, else the player is in idle state
        # if the player encountered a barrier and is still going the same direction, can_walk becomes False
        if keys[pygame.K_RIGHT] or keys[pygame.K_LEFT] or keys[pygame.K_UP] or keys[pygame.K_DOWN]:
            current_click_arrow = pygame.time.get_ticks()
            time_passed = False
            if current_click_arrow - last_clicked_arrow >= 1000:
                time_passed = True
            if keys[pygame.K_RIGHT] and time_passed:
                    can_walk = True
                    if  plr.collision and plr.direc == Vec(1,0):
                        can_walk = False
                    plr.direc = Vec(1, 0)
            if keys[pygame.K_LEFT] and time_passed:
                    can_walk = True
                    if plr.collision and plr.direc == Vec(-1,0):
                        can_walk = False
                    plr.direc = Vec(-1, 0)
            if keys[pygame.K_UP] and time_passed:
                    can_walk = True
                    if  plr.collision and plr.direc == Vec(0, -1):
                        can_walk = False
                    plr.direc = Vec(0, -1)
            if keys[pygame.K_DOWN] and time_passed:
                    can_walk = True
                    if  plr.collision and plr.direc == Vec(0, 1):
                        can_walk = False
                    plr.direc = Vec(0, 1)
            
            if can_walk:
                time = plr.walk(time)
            else:
                plr.idle()
        else:
            plr.idle()
        
        # if story isn't being displayed yet, tells the player to press Enter
        if not scene.text_finished and not scene.printing:
            screen.blit(story_unlock_txt, text_rect)

        # go through the story if enter is pressed
        # first we check if the time between presses is big enough, if it is the line will be increased by 1
        # then we set the variable scene.printing to True, so even if enter isn't currently pressed the text will still show
        if keys[pygame.K_RETURN]:
            current_time = pygame.time.get_ticks()
            if current_time - time_txt > 1000:
                scene.text_position +=1
                scene.printing = True
                time_txt = current_time
        # if scene.printing is True, print the text
        if scene.printing:
            scene.print_text(screen)

        # we can only interact with the interactable object if the story has been read and if we're close to the object
        if scene.interactables.in_vicinity(plr.rect) and scene.text_finished:
            if not scene.interactables.interacted:
                screen.blit(interact_txt, text_rect) # blits the text 'Press E to interact', if it hasn't been interacted yet
            if keys[pygame.K_e]: # if they pressed E then it has already been interacted with
                scene.interactables.interacted = True

        # if they already interacted with the object, the choice will be displayed
        if scene.interactables.interacted:
            scene.print_interactable_txt(screen)
            # once the player chooses 1, 2 or 3(in some case) this function will return the choice
            # and we will advance in the tree
            if keys[pygame.K_1]:
                return 1
            elif keys[pygame.K_2]:
                return 2 
            # the number of choices must be 3 for the 'K_3' to be a valid input
            elif keys[pygame.K_3] and scene.interactables.n == 3: 
                return 3
        
        pygame.display.update()
        clock.tick(c.FPS)

# This handles the last window, which displays stats
def sum_up(plr):
    """
    Handles the last window, which displays the final stats of the player.
    
    :param plr: Player object
    """
    # set up the texts for the last sum up window
    SUM_UP_TXT =  pygame.font.SysFont('arial', c.LARGE_TXT, bold=True).render(f'Stats: ', True, 'White')
    SUM_UP_RECT = SUM_UP_TXT.get_rect(center = (300, 50))

    KNOWLEDGE_TXT = pygame.font.SysFont('arial', c.STATS_TXT, bold=True).render(f'Knowledge: {(plr.stats.knowledge*10 / c.MAX_KNOWLEDGE) :.1f}/10', True, 'White')

    KNOWLEGE_RECT = KNOWLEDGE_TXT.get_rect(topleft = (20, 120))

    RESTED_TXT = pygame.font.SysFont('arial', c.STATS_TXT, bold=True).render(f'Rest: {(plr.stats.rested*10 / c.MAX_RESTED) :.1f}/10', True, 'White')

    RESTED_RECT = RESTED_TXT.get_rect(topleft = (20, 170))

    FRIENDSHIP_TXT = pygame.font.SysFont('arial', c.STATS_TXT, bold=True).render(f'Friendship: {(plr.stats.friendship*10 / c.MAX_FRIENDSHIP) :.1f}/10', True, 'White')
    FRIENDSHIP_RECT = FRIENDSHIP_TXT.get_rect(topleft = (20, 220))

    while True:
        screen.fill(c.BLACK)
        screen.blit(SUM_UP_TXT, SUM_UP_RECT)
        screen.blit(KNOWLEDGE_TXT, KNOWLEGE_RECT)
        screen.blit(RESTED_TXT, RESTED_RECT)
        screen.blit(FRIENDSHIP_TXT, FRIENDSHIP_RECT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.update()
        clock.tick(c.FPS)

# this handles the ending window, which is just an image
def ending(plr):
    """
    Handles the window which determines the endings. Endings are simply images.
    
    :param plr: Player object
    """
    n = 0
    if plr.stats.friendship >= c.MAX_FRIENDSHIP*0.5:
        if plr.stats.knowledge >= c.MAX_KNOWLEDGE*0.5:
            n = 3
        else:
            n = 1
    else:
        if plr.stats.knowledge >= c.MAX_KNOWLEDGE*0.5:
            n = 4
        else:
            n = 2
    ending_surface = pygame.image.load(f'sprites/Backgrounds/ending_{n}.png')
    ending_surface = pygame.transform.scale(ending_surface, (c.SCREEN_SIZE, c.SCREEN_SIZE))
    while True:
        screen.blit(ending_surface, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            # if you press ENTER, the stats window will appear 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                sum_up(plr)

        pygame.display.update()
        clock.tick(c.FPS)

# This is a recursive function which navigates through the tree
def navigate_tree(plr, root):
    """
    A recursive function which navigates through the tree of nodes.
    
    :param plr: Player object
    :param root: The root of the tree
    """
    # I know that root will never be none, since the recursion is
    # stopped if all of its children are none, but I still added this check
    if root is None:
        ending(plr)
        return
    
    choice = Scene_playthrough(plr, root.scene)

    # if the nodes children are none, we display the sum_up screen
    if root.first_child == None and root.sec_child == None and root.thr_child == None:
        ending(plr)
    
    # navigate through the nodes children by the choices
    if choice == 1:
        navigate_tree(plr, root.first_child)
    elif choice == 2:
        navigate_tree(plr, root.sec_child)
    elif choice == 3: # not all nodes have the 3rd child, but in the Scene_playthrough I added a check for that already
        navigate_tree(plr, root.thr_child)
    else: # I know that this will never be reached, but I added a check just in case
        ending(plr)
        return

# This is the second window, which handles choosing the characters
def choose_character():
    """
    Handles choosing the characters and then calls the navigate_tree function
    """
    last_clicked = pygame.time.get_ticks()
    # this extracts a specific character frame from the character sprite sheet by giving them the x and y positions 
    def get_image(frame_x, frame_y):
        image = pygame.Surface((c.CHARACTER_FRAME_WIDTH, c.CHARACTER_FRAME_HEIGHT)).convert_alpha() # create a blank surface
        # take from the sprite sheet and blit it onto the blink surface
        image.blit(sprite_sheet_image, (0,0), (frame_x*c.CHARACTER_FRAME_WIDTH,
        (frame_y*(c.DISTANCE_ON_SPRITE_SHEET+c.CHARACTER_FRAME_HEIGHT)) 
        + c.DISTANCE_ON_SPRITE_SHEET, (frame_x+1)*c.CHARACTER_FRAME_WIDTH, 
        (frame_y + 1)*(c.DISTANCE_ON_SPRITE_SHEET+c.CHARACTER_FRAME_HEIGHT)))
        
        # make the black background transparent
        image.set_colorkey(c.BLACK)
        
        return image

    # create the buttons
    Button_chr0 = bg.Button(0, 175, 200, get_image(1, 0))
    Button_chr1 = bg.Button(1, 425, 200, get_image(4, 0))
    Button_chr2 = bg.Button(2, 175, 425, get_image(7, 0))
    Button_chr3 = bg.Button(3, 425, 425, get_image(10, 0))
    id = -1 # id is -1 for now

    # create the texts and their rects
    CHOOSE_CHAR_TXT = pygame.font.SysFont('arial', c.LARGE_TXT, bold = True).render('Choose your character', True, 'White')
    CHOOSE_CHAR_RECT = CHOOSE_CHAR_TXT.get_rect(center=(300, 100))
        
    CONTINUE_TXT = pygame.font.SysFont('arial', c.SMALL_TXT).render('Press ENTER to continue', True, 'White')
    CONTINUE_RECT = CONTINUE_TXT.get_rect(center = (300, 500))

    while True:
        # update the screen
        screen.fill(c.BLACK)
        # get the mouse position to see if a specific button is clicked
        mouse_pos = pygame.mouse.get_pos()

        screen.blit(CHOOSE_CHAR_TXT, CHOOSE_CHAR_RECT)

        Button_chr0.draw(screen)
        Button_chr1.draw(screen)
        Button_chr2.draw(screen)
        Button_chr3.draw(screen)

        # check events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            # if the mouse was clicked on any of the buttons
            if event.type == pygame.MOUSEBUTTONDOWN and (Button_chr0.rect.collidepoint(mouse_pos) or 
                                                         Button_chr1.rect.collidepoint(mouse_pos) or 
                                                         Button_chr2.rect.collidepoint(mouse_pos) or 
                                                         Button_chr3.rect.collidepoint(mouse_pos)):
                current_click = pygame.time.get_ticks() # we store current time

                # if the button was clicked we set its transparency to 50%
                # we set the id to the button id
                if current_click - last_clicked >= 100:
                    last_clicked = current_click
                    if Button_chr0.rect.collidepoint(mouse_pos):
                        Button_chr0.img.set_alpha(128)
                        Button_chr1.img.set_alpha(255)
                        Button_chr2.img.set_alpha(255)
                        Button_chr3.img.set_alpha(255)
                        id = Button_chr0.id
                    elif Button_chr1.rect.collidepoint(mouse_pos):
                        Button_chr0.img.set_alpha(255)
                        Button_chr1.img.set_alpha(128)
                        Button_chr2.img.set_alpha(255)
                        Button_chr3.img.set_alpha(255)
                        id = Button_chr1.id
                    elif Button_chr2.rect.collidepoint(mouse_pos):
                        Button_chr0.img.set_alpha(255)
                        Button_chr1.img.set_alpha(255)
                        Button_chr2.img.set_alpha(128)
                        Button_chr3.img.set_alpha(255)
                        id = Button_chr2.id
                    elif Button_chr3.rect.collidepoint(mouse_pos):
                        Button_chr0.img.set_alpha(255)
                        Button_chr1.img.set_alpha(255)
                        Button_chr2.img.set_alpha(255)
                        Button_chr3.img.set_alpha(128)
                        id = Button_chr3.id
 
            # if the character has already been chosen and the player presses ENTER,
            # it sets up the player animation frames and starts to navigate through the tree
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and id >= 0:
                bkw = [get_image(id*3, 0), get_image(id*3 + 1,0), get_image(id*3 + 2,0)]
                frw = [get_image(id*3, 3), get_image(id*3 + 1,3), get_image(id*3 + 2,3)]
                lf = [get_image(id*3, 1), get_image(id*3 + 1,1), get_image(id*3 + 2,1)]
                rgt = [get_image(id*3, 2), get_image(id*3 + 1,2), get_image(id*3 + 2,2)]
                skin = chr.Skin(id, frw, bkw, lf, rgt)
                screen.fill(c.BLACK)
                navigate_tree(chr.Player(skin, bedroom_scene_1.start_plr_pos, 1, lf, Vec(0,-1)), node_1)

        # if any of the buttons were clicked, 'Press ENTER to continue' text will be displayed
        if id >= 0:
            screen.blit(CONTINUE_TXT, CONTINUE_RECT)

        pygame.display.update()
        clock.tick(c.FPS)

# This handles the start window
def start():
    """
    Handles the start window and then calls the choose_character
    """
    # create the texts and their rects
    START_TEXT_1 = pygame.font.SysFont('arial', c.LARGE_TXT, bold=True).render('Life of a University student', True, 'White')
    START_TEXT_2 = pygame.font.SysFont('arial', c.AVG_TXT).render('click to start', True, 'White')
    
    START_TEXT_1_RECT = START_TEXT_1.get_rect(center=(300, 200))
    START_TEXT_2_RECT = START_TEXT_2.get_rect(center=(300, 280))

    while True:
        # blit everything on the screen
        screen.blit(surface, (0,0))
        screen.blit(START_TEXT_1, START_TEXT_1_RECT)
        screen.blit(START_TEXT_2, START_TEXT_2_RECT)
        
        # check events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                choose_character()

        pygame.display.update()
        clock.tick(c.FPS)

start()



