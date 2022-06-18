import pygame
class Soldier:
    _soldier_image_template = pygame.image.load("./assets/guard3.png")
    
    def __init__(self, window_width, window_height, number):
        self._soldier_image_template = pygame.transform.scale(Soldier._soldier_image_template, (2 * window_width / 24, 3 * window_height / 16))
        self._soldier_rect = self._soldier_image_template.get_rect()
        self._soldier_rect.right = 8 * window_width / 24
        self._soldier_rect.top = (number * 3 + 3) * window_height / 16 

    def is_time_to_move(self, time_since_last_tick, inter_move_wait_time):
        return False

    def draw(self, screen, gold_object):
        screen.blit(self._soldier_image_template, self._soldier_rect)

    def mouse_click(self, clicked_mouse_position, gold_object):
        return False
    
    def interaction(self, other_object):
        return False
    
    def hp_control(self, damage):
        return False

    def rect_control(self, defense_rect):
        return False
    
    def selected_object_insertion(self, window_width, window_height, selected_object, gold_object):
        return selected_object.object_insertion(window_width, window_height, self._soldier_rect.topright, gold_object)
    
    def selected_object_shadow_draw(self, screen, window_width, window_height, selected_object):
        selected_object.shadow_draw(screen, window_width, window_height, self._soldier_rect.topright) 
