import pygame
import random
import castle_class
import attack_class
import defense_class
import menu_class
import soldier_class

class Game:
    _window_width, _window_height = 1024, 768
    _window_size = (_window_width, _window_height)
    _screen = pygame.display.set_mode(_window_size)
    _background = pygame.image.load("./assets/background.png")
    _win_background = pygame.image.load("./assets/win.png")
    _defeat_background = pygame.image.load("./assets/defeat.png")
    _lane_ground = pygame.image.load("./assets/lanes.png")
    _pause_background = pygame.image.load("./assets/pause.png")

    def __init__(self):
        self._inter_move_wait_time = 1
        self._inter_create_wait_time = 20000
        self._total_wait_since_last_create = 20000
        self._create_accelerator = 0
        self._hp_wait_time = 10000
        self._clock = pygame.time.Clock()
        self._background = pygame.transform.scale(Game._background,(Game._window_width, Game._window_height))
        self._win_background = pygame.transform.scale(Game._win_background,(Game._window_width, Game._window_height))
        self._defeat_background = pygame.transform.scale(Game._defeat_background,(Game._window_width, Game._window_height))
        self._lane_ground = pygame.transform.scale(Game._lane_ground,(16 * Game._window_width / 24, 12 * Game._window_height / 16))
        self._pause_background = pygame.transform.scale(Game._pause_background,(Game._window_width, Game._window_height))
        self._clicked_pos = None
        self._current_pos = None
        self._objects = []
        self._castle = castle_class.Castle(Game._window_width, Game._window_height)
        self._objects.append(self._castle)
        for i in range(4):
            self._objects.append(soldier_class.Soldier(Game._window_width, Game._window_height, i))
        self._defenses = [defense_class.Defense1,defense_class.Defense2,defense_class.Defense3,defense_class.Defense4]
        self._menu = menu_class.Menu(Game._window_width, Game._window_height)
        self._objects.append(self._menu)
        self._gold_object = menu_class.Gold(Game._window_width, Game._window_height)
        self._objects.append(self._gold_object)
        for defense in self._defenses:
            self._objects.append(defense(Game._window_width, Game._window_height, location = (0,0)).bar_create(Game._window_width, Game._window_height))
        self._dragging = False
        self._selected_object = None
        self._lanes = {self._objects[1]: (3 * Game._window_height / 16, 6 * Game._window_height / 16), self._objects[2]: (6 * Game._window_height / 16, 9 * Game._window_height / 16), self._objects[3]: (9 * Game._window_height / 16, 12 * Game._window_height / 16), self._objects[4]: (12 * Game._window_height / 16, 15 * Game._window_height / 16)}
        self._game_status = False # True -> defeat
        self._winning_status = False # True -> win
        self._pause = True
        self._optimizer = False
        self._delete_objects_index = []

    def background_color_adjust(self, brightness):
        self._background.set_alpha(brightness)
    def win_status_change(self):
        self._winning_status = True

    def winning_control(self):
        if self._menu.winning_control():
            self.win_status_change()

    def dragging(self, object):
        self._clicked_pos = pygame.mouse.get_pos()
        for object in self._objects:
            if object.mouse_click(self._clicked_pos, self._gold_object):
                self._selected_object = object
                self._dragging = True
    
    def dropping(self):
        self._clicked_pos = pygame.mouse.get_pos()
        for (soldier, lane) in self._lanes.items():
            if self._clicked_pos[1] >= lane[0] and self._clicked_pos[1] <= lane[1]: # defense_slot is unselected whether user click anywehere above the upper bound of the first lane or below the lower bound of the fourth lane
                self.defense_insertion_to_objectlist(soldier)

    def defense_insertion_to_objectlist(self,soldier):
        self._objects.append(soldier.selected_object_insertion(Game._window_width, Game._window_height, self._selected_object, self._gold_object))        
        self._clicked_pos = (-1, -1)
        self._dragging = False
    
    def is_time_to_create(self):
        self._total_wait_since_last_create = self._total_wait_since_last_create + self._clock.get_time()
        if self._total_wait_since_last_create <= self._inter_create_wait_time:
            return False
        else:
            self._total_wait_since_last_create = 0
            return True
    
    def create(self):
        random_number = random.randint(1,4)
        if random_number == 1:
            return attack_class.Attack1(Game._window_width, Game._window_height)
        elif random_number == 2:
            return attack_class.Attack2(Game._window_width, Game._window_height)
        elif random_number == 3:
            return attack_class.Attack3(Game._window_width, Game._window_height)
        else:
            return attack_class.Attack4(Game._window_width, Game._window_height)

    def unselecting(self):
        self._clicked_pos = (-1, -1)
        self._dragging = False

    def pausing(self):
        self._pause = True
    
    def unpausing(self):
        self._pause = False

    def castle_status(self):
        return self._game_status

    def castle_is_gone(self):
        self._game_status = True

    def insertion_to_remove_object_list(self, index):
        self._delete_objects_index.append(index)

    def remove_objects(self):
        for index in self._delete_objects_index:
            self._objects.pop(index)
        self.delete_list_refresh()
    
    def delete_list_refresh(self):
        self._delete_objects_index = []

    def create_accelerator_up(self):
        if self._create_accelerator < 100:
            self._create_accelerator += 1
        else:
            self._create_accelerator = 0

    def inter_create_wait_time(self):
        if self._create_accelerator == 100 and self._inter_create_wait_time > 5000:
            self._inter_create_wait_time = self._inter_create_wait_time - 1000
        else:
            self._inter_create_wait_time == self._inter_create_wait_time

    def attack_insertion_to_objectlist(self):
        self._objects.append(self.create())
    
    def win_status(self):
        return self._winning_status

    def while_lose_event(self):
        while self.castle_status():
            self._menu.lose_draw(Game._screen, Game._window_width, Game._window_height, self._defeat_background)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    self.quit()
            continue

    def while_winning_event(self):
        while self.win_status():
            self._menu.win_draw(Game._screen, Game._window_width, Game._window_height, self._win_background)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    self.quit()
            continue
        
    def while_pause_event(self):        
        while self._pause:
            Game._screen.blit(self._pause_background,(0,0))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    self.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.unpausing()
            self._clock.tick(60) # gold is given according to the time interval between last tick and now so using time.tick prevent the game from keep giving gold during in pause time
            continue

    def quit(self):
        pygame.quit()
    
    def optimize(self):
        self._optimizer = True
    
    def optimize_reset(self):
        self._optimizer = False
    
    def optimizer_check(self):
        return self._optimizer

    def TimeTick(self):
        self.optimize_reset()
        if self._castle.is_time_to_gain_hp(self._clock.get_time(), self._hp_wait_time):
            self._castle.gain_hp()
        if self.is_time_to_create():
            self.attack_insertion_to_objectlist()
            self.optimize()          
        for object in self._objects:
            if object.is_time_to_move(self._clock.get_time(), self._inter_move_wait_time):
                self.optimize()   
                object.move(Game._window_width, Game._window_height)
        if self.optimizer_check():
            Game._screen.blit(self._background,(0,0))
            Game._screen.blit(self._lane_ground,(8 * Game._window_width / 24, 3 * Game._window_height / 16))
            for index, object in enumerate(self._objects):
                for i in range(len(self._objects)):
                    if i == index:
                        continue   
                    other_object = self._objects[i]
                    if object.interaction(other_object):
                        if isinstance(object, castle_class.Castle):
                            self.castle_is_gone()
                        self.insertion_to_remove_object_list(index)
                        break
            self.remove_objects()
            for object in self._objects:
                object.draw(Game._screen, self._gold_object)
        if self._dragging:
            self._current_pos = pygame.mouse.get_pos()
            for (soldier, lane) in self._lanes.items():
                        if self._current_pos[1] >= lane[0] and self._current_pos[1] <= lane[1]: # defense_slot is unselected if user click anywehere above the upper bound of the first lane
                            soldier.selected_object_shadow_draw(Game._screen, Game._window_width, Game._window_height, self._selected_object) 
        self.winning_control()
        self.create_accelerator_up()
        self.inter_create_wait_time()
        pygame.display.flip()              

    def play(self):
        self.background_color_adjust(150)
        while 1:
            self.while_lose_event()
            self.while_winning_event()
            self.while_pause_event()
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    self.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.pausing()
                if event.type == pygame.MOUSEBUTTONDOWN and self._dragging == False:
                        if event.button == 1: 
                            self.dragging(object)
                            break
                if event.type == pygame.MOUSEBUTTONDOWN and self._dragging == True:
                    if event.button == 1: 
                        self.dropping()                        
                        self.unselecting()
            self.TimeTick()
            self._clock.tick(60)
