import pygame
import menu_class
class Defense:
    def __init__(self, window_width, window_height, location = (0, 0)):
        self._direction = [1, 0]
        self._total_wait_since_last_move = 0
    def is_time_to_move(self, time_since_last_tick, inter_move_wait_time):
        self._total_wait_since_last_move = self._total_wait_since_last_move + time_since_last_tick
        if self._total_wait_since_last_move <= inter_move_wait_time:
            return False
        else:
            return True
    
    def move(self, window_width, window_height):
        self._total_wait_since_last_move = 0
        self._defense_rect = self._defense_rect.move(self._direction)
    
    def draw(self, screen, gold_object):
        self._defense_image_template.set_alpha(255)
        screen.blit(self._defense_image_template, self._defense_rect)
    
    def shadow_draw(self, screen):
        self._defense_image_template.set_alpha(80)
        screen.blit(self._defense_image_template, self._defense_rect)
    
    def bar_create(self, window_width, window_height):
        return menu_class.Defense_Slot(window_width, window_height, self._defense_image_template, self._menubar_order, self._price, self._damage)
    
    def mouse_click(self, clicked_mouse_position, gold_object):
        return False
    
    def interaction(self, other_object):
        rett = False
        if other_object.rect_control(self._defense_rect):
            other_object.hp_control(self._damage)
            rett = True
        return rett
    
    def hp_control(self, damage):
        return False
    
    def rect_control(self, defense_rect):
        return False

class Defense1(Defense):
    _defense_image_template = pygame.image.load("./assets/defense1.png")
    _price = 10
    _damage = 10
    def __init__(self, window_width, window_height, location = (0, 0)):
        self._defense_image_template = pygame.transform.scale(Defense1._defense_image_template, (2 * window_width / 24, 3 * window_height / 16))
        self._defense_rect = self._defense_image_template.get_rect()
        self._damage = Defense1._damage
        self._price = Defense1._price
        self._menubar_order = 1
        Defense.__init__(self, window_width, window_height, location = (0, 0))
        self._defense_rect.left, self._defense_rect.top = location
class Defense2(Defense):
    _defense_image_template = pygame.image.load("./assets/defense2.png")
    _price = 20
    _damage = 30
    def __init__(self, window_width, window_height, location = (0, 0)):
        self._defense_image_template = pygame.transform.scale(Defense2._defense_image_template, (2 * window_width / 24, 3 * window_height / 16))
        self._defense_rect = self._defense_image_template.get_rect()
        self._damage = Defense2._damage
        self._price = Defense2._price
        self._menubar_order = 2
        Defense.__init__(self, window_width, window_height, location = (0, 0))
        self._defense_rect.left, self._defense_rect.top = location
class Defense3(Defense):
    _defense_image_template = pygame.image.load("./assets/defense3.png")
    _price = 30
    _damage = 50
    def __init__(self, window_width, window_height, location = (0, 0)):
        self._defense_image_template = pygame.transform.scale(Defense3._defense_image_template, (2 * window_width / 24, 3 * window_height / 16))
        self._defense_rect = self._defense_image_template.get_rect()
        self._damage = Defense3._damage
        self._price = Defense3._price
        self._menubar_order = 3
        Defense.__init__(self, window_width, window_height, location = (0, 0))
        self._defense_rect.left, self._defense_rect.top = location
class Defense4(Defense):
    _defense_image_template = pygame.image.load("./assets/defense4.png")
    _price = 40
    _damage = 70
    def __init__(self, window_width, window_height, location = (0, 0)):
        self._defense_image_template = pygame.transform.scale(Defense4._defense_image_template, (2 * window_width / 24, 3 * window_height / 16))
        self._defense_rect = self._defense_image_template.get_rect()
        self._damage = Defense4._damage
        self._price = Defense4._price
        self._menubar_order = 4
        Defense.__init__(self, window_width, window_height, location = (0, 0))
        self._defense_rect.left, self._defense_rect.top = location