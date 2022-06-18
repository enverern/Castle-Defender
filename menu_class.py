import pygame
import defense_class
class Menu:
    _menubar_image_template = pygame.image.load("./assets/menubar.png")

    def __init__(self, window_width, window_height):
        self._menu_width = 16 * window_width / 24
        self._menu_height = 2.4 * window_height / 16
        self._menubar_image_template = pygame.transform.scale(Menu._menubar_image_template, (self._menu_width, self._menu_height))
        self._menubar_rect = self._menubar_image_template.get_rect()
        self._menubar_rect.left = 4 * window_width / 24
        self._menubar_rect.top = 0
        self._gold = 0
        self._font = pygame.font.SysFont("Phosphate", 16)
        self._font2 = pygame.font.SysFont("Phosphate", 40)
        self._progress = 0
        self._progress_amount = self._font.render(f"Score: {int(self._progress)}", True, (0,0,0)) # rendered version of amount of time that can be blitted 
        self._progress_amount_rect = self._progress_amount.get_rect(topleft = ((4 * window_width / 24) + (13.9 * self._menu_width / 16), 32))
        self._winning_condition = 40

    def is_time_to_move(self, time_since_last_tick, inter_move_wait_time):
        self._progress += (time_since_last_tick / 5000)
        return True

    def move(self, window_width, window_height):
        self._progress_amount = self._font.render(f"Score: {int(self._progress)}", True, (0,0,0)) # menu is an instance includes progress amount
        self._progress_amount_rect = self._progress_amount.get_rect(topleft = ((4 * window_width / 24) + (13.9 * self._menu_width / 16), 32))

    def draw(self, screen, gold_object):
        screen.blit(self._menubar_image_template, self._menubar_rect)
        screen.blit(self._progress_amount, self._progress_amount_rect)
    
    def win_draw(self, screen, window_width, window_height, win_template):
        screen.blit(win_template,(0,0))
        self._progress_amount = self._font2.render(f"Your Score is: {int(self._progress)}", True, (255,255,255))
        screen.blit(self._progress_amount, (15 * window_width / 36, window_height * 2/3))
    
    def lose_draw(self, screen, window_width, window_height, lose_template):
        screen.blit(lose_template,(0,0))
        self._progress_amount = self._font2.render(f"Your Score is: {int(self._progress)}", True, (255,255,255))
        screen.blit(self._progress_amount, (15 * window_width / 36, window_height * 2/3))

    def winning_control(self):
        return self._winning_condition < self._progress 
    
    def mouse_click(self, clicked_mouse_position, gold_object):
        return False
    
    def interaction(self, other_object):
        return False

    def hp_control(self, damage):
        return False

    def rect_control(self, defense_rect):
        return False
class Gold(Menu):
    def __init__(self, window_width, window_height):
        Menu.__init__(self, window_width, window_height)
        self._gold_amount = None    # rendered version of amount of gold that can be blitted 
        self._gold_amount_rect = None

    def is_time_to_move(self, time_since_last_tick, inter_move_wait_time):
        self._gold += (time_since_last_tick / 150)
        return True
    
    def move(self, window_width, window_height):
        self._gold_amount = self._font.render(f"Gold: {int(self._gold)}", True, (0,0,0))
        self._gold_amount_rect = self._gold_amount.get_rect(topleft = ((4 * window_width / 24) + (11.25 * self._menu_width / 16), 32))
    
    def draw(self, screen, gold_object):
        screen.blit(self._gold_amount, self._gold_amount_rect)
    
    def price_control(self, price):
        if price <= self._gold:
            return True
        else:
            return False
    def spend(self, price):
        self._gold -= price

class Defense_Slot(Menu):
    def __init__(self, window_width, window_height, defense_template, order, price, damage):
        Menu.__init__(self, window_width, window_height)
        self._defense_bar_template = pygame.transform.scale(defense_template, (self._menu_width / 10, self._menu_height / 1.3))
        self._defense_bar_rect = self._defense_bar_template.get_rect()
        self._order = order
        self._defense_bar_rect.left = (1.87 * window_width / 24) + self._order *  (self._menu_width / 6)
        self._defense_bar_rect.top = self._menu_height * 0.109
        self._price_value = price
        self._price_template = self._font.render(f"price: {self._price_value}", True, (0,0,0))
        self._price_rect = self._price_template.get_rect(topleft = ((1.84 * window_width / 24) + self._order *  (self._menu_width / 6), 34 + self._menu_height / 1.7))
        self._damage_value = damage
        self._damage_template = self._font.render(f"damage: {self._damage_value}", True, (0,0,0))
        self._damage_rect = self._price_template.get_rect(topleft = ((1.84 * window_width / 24) + self._order *  (self._menu_width / 6), 48 + self._menu_height / 1.7))

    def is_time_to_move(self, time_since_last_tick, inter_move_wait_time):
        return False

    def move(self, window_width, window_height):
        pass

    def draw(self, screen, gold_object):
        if gold_object.price_control(self._price_value):
            self._defense_bar_template.set_alpha(255)
            screen.blit(self._defense_bar_template, self._defense_bar_rect)
        else:
            self._defense_bar_template.set_alpha(80)
            screen.blit(self._defense_bar_template, self._defense_bar_rect)
        screen.blit(self._price_template, self._price_rect)
        screen.blit(self._damage_template,self._damage_rect)

    def mouse_click(self, clicked_mouse_position, gold_object):
        if gold_object.price_control(self._price_value):
            return self._defense_bar_rect.collidepoint(clicked_mouse_position)
        else:
            return False
    
    def object_insertion(self, window_width, window_height, soldier_topright, gold_object):
        gold_object.spend(self._price_value)
        if self._order == 1:
            return defense_class.Defense1(window_width, window_height, soldier_topright)
        elif self._order == 2:
            return defense_class.Defense2(window_width, window_height, soldier_topright)
        elif self._order == 3:
            return defense_class.Defense3(window_width, window_height, soldier_topright)
        else:
            return defense_class.Defense4(window_width, window_height, soldier_topright)
    
    def shadow_draw(self, screen, window_width, window_height, soldier_topright):
        if self._order == 1:
            defense_class.Defense1(window_width, window_height, soldier_topright).shadow_draw(screen)
        elif self._order == 2:
            defense_class.Defense2(window_width, window_height, soldier_topright).shadow_draw(screen)
        elif self._order == 3:
            defense_class.Defense3(window_width, window_height, soldier_topright).shadow_draw(screen)
        else:
            defense_class.Defense4(window_width, window_height, soldier_topright).shadow_draw(screen)
