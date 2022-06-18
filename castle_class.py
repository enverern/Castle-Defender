import pygame
class Castle:
    _castle_image_template = pygame.image.load("./assets/castle8.png")
    _total_wait_since_last_hp_gain = 0
    
    def __init__(self, window_width, window_height):
        self._castle_image_template = pygame.transform.scale(Castle._castle_image_template, (6 * window_width / 24, 12 * window_height / 16))
        self._castle_rect = self._castle_image_template.get_rect()
        self._castle_rect.left = 0
        self._castle_rect.top = 3 * window_height / 16
        self._hp = 500
        self._last_hp = 500
        self._font = pygame.font.SysFont("Phosphate", 20)
        self._hp_value = self._font.render(f"Castle HP: {int(self._hp)}", True, (0,0,0))
        self._hp_value_rect = self._hp_value.get_rect(bottomleft = (self._castle_rect.left + window_width / 48, self._castle_rect.top))
        
    def is_time_to_move(self, time_since_last_tick, inter_move_wait_time):
        return True
    
    def is_time_to_gain_hp(self, time_since_last_tick, hp_wait_time):
        Castle._total_wait_since_last_hp_gain = Castle._total_wait_since_last_hp_gain + time_since_last_tick
        if self._last_hp != self._hp:
            self._last_hp = self._hp
            Castle._total_wait_since_last_hp_gain = 0
            return False
        elif Castle._total_wait_since_last_hp_gain <= hp_wait_time:
            return False
        else:
            return True

    def gain_hp(self):
        Castle._total_wait_since_last_hp_gain = 100
        self._hp += 10  

    
    def move(self, window_width, window_height):
        self._hp_value = self._font.render(f"Castle HP: {int(self._hp)}", True, (0,0,0))
        self._hp_value_rect = self._hp_value.get_rect(bottomleft = (self._castle_rect.left + window_width / 48, self._castle_rect.top))

    def draw(self, screen, gold_object):
        screen.blit(self._castle_image_template, self._castle_rect)
        screen.blit(self._hp_value, self._hp_value_rect)
    
    def mouse_click(self, clicked_mouse_position, gold_object):
        return False
    
    def interaction(self, other_object):
        if self._hp <= 0:
            return True
        else:
            return False

    def hp_control(self, damage):
        self._hp -= damage
        return True

    def rect_control(self, attack_rect):
        return self._castle_rect.colliderect(attack_rect)