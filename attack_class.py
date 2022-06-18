import pygame
import random
import castle_class
class Attack:
    _red = 220, 20, 60
    _green = 34, 139, 34
    
    def __init__(self, window_width, window_height):
        self._initial_size = window_width, window_height
        self._attack_rect.left = window_width
        self._attack_rect.top = random.randint(1,4) * 3 * window_height / 16
        self._direction = [-1, 0]
        self._total_wait_since_last_move = 0
        self._font = pygame.font.SysFont("Phosphate", 16)
        self._red_hp_rect = pygame.Rect((self._attack_rect.left, self._attack_rect.bottom), (self._attack_image_template.get_width(), self._attack_image_template.get_height() / 12))
        self._green_hp_rect = pygame.Rect((self._attack_rect.left, self._attack_rect.bottom), (self._attack_image_template.get_width(), self._attack_image_template.get_height() / 12))
        self._hp_rendered = self._font.render(f"HP: {int(self._hp)}", True, (255,255,255))
        self._hp_rendered_rect = self._hp_rendered.get_rect(center = (self._red_hp_rect.centerx,self._red_hp_rect.centery))
        
    def is_time_to_move(self, time_since_last_tick, inter_move_wait_time):
        self._total_wait_since_last_move = self._total_wait_since_last_move + time_since_last_tick
        if self._total_wait_since_last_move <= inter_move_wait_time:
            return False
        else:
            return True
    
    def move(self, window_width, window_height):
        self._total_wait_since_last_move = 0
        self._attack_rect = self._attack_rect.move(self._direction)
        self._red_hp_rect = self._red_hp_rect.move(self._direction)
        self._green_hp_rect = self._green_hp_rect.move(self._direction)
        self._hp_rendered_rect = self._hp_rendered_rect.move(self._direction)

    def draw(self, screen, gold_object): 
        screen.blit(self._attack_image_template, self._attack_rect)
        pygame.draw.rect(screen, Attack._red, self._red_hp_rect)
        pygame.draw.rect(screen, Attack._green, self._green_hp_rect)
        screen.blit(self._hp_rendered, self._hp_rendered_rect)
            
    def mouse_click(self, clicked_mouse_position, gold_object):
        return False
    
    def is_dead(self):
        if self._hp <= 0:
            return True

    def interaction(self, other_object):
        if self.is_dead():
            return True
        else:
            if isinstance(other_object, castle_class.Castle):
                if other_object.rect_control(self._attack_rect):
                    return other_object.hp_control(self._damage) # this return depends only on castle and attack object interact or not 
            else:
                return False # this return depends only on castle and attack object interact or not 

    def rect_control(self, defense_rect):
        return self._attack_rect.colliderect(defense_rect)

    def hp_control(self, damage):
        self._hp -= damage
        self._hp_rendered = self._font.render(f"HP: {int(self._hp)}", True, (255,255,255))
        self._hp_rendered_rect = self._hp_rendered.get_rect(center = (self._red_hp_rect.centerx,self._red_hp_rect.centery))
        self._green_hp_rect.update((self._attack_rect.left, self._attack_rect.bottom), ((self._hp / self._initial_hp)*self._attack_image_template.get_width(), self._attack_image_template.get_height() / 12))
        self._damage -= damage # The damage of an attack object decrease as damage value of the defense item when attack object interacts with defense object
        return False

class Attack1(Attack):
    _attack_image_template = pygame.image.load("./assets/attack1.png")
    _hp = 20
    _damage = 20
    def __init__(self, window_width, window_height):        
        self._attack_image_template = pygame.transform.scale(Attack1._attack_image_template, (2 * window_width / 24, 3 * window_height / 16))
        self._attack_rect = self._attack_image_template.get_rect()
        self._hp = Attack1._hp
        self._initial_hp = Attack1._hp
        self._damage = Attack1._damage
        Attack.__init__(self, window_width, window_height)
class Attack2(Attack):
    _attack_image_template = pygame.image.load("./assets/attack2.png")
    _hp = 60
    _damage = 60
    def __init__(self, window_width, window_height):
        self._attack_image_template = pygame.transform.scale(Attack2._attack_image_template, (2 * window_width / 24, 3 * window_height / 16))
        self._attack_rect = self._attack_image_template.get_rect()
        self._hp = Attack2._hp
        self._initial_hp = Attack2._hp
        self._damage = Attack2._damage
        Attack.__init__(self, window_width, window_height)
class Attack3(Attack):
    _attack_image_template = pygame.image.load("./assets/attack3.png")
    _hp = 100
    _damage = 100
    def __init__(self, window_width, window_height):
        self._attack_image_template = pygame.transform.scale(Attack3._attack_image_template, (2 * window_width / 24, 3 * window_height / 16))
        self._attack_rect = self._attack_image_template.get_rect()
        self._hp = Attack3._hp
        self._initial_hp = Attack3._hp
        self._damage = Attack3._damage
        Attack.__init__(self, window_width, window_height)
class Attack4(Attack):
    _attack_image_template = pygame.image.load("./assets/attack4.png")
    _hp = 140
    _damage = 140
    def __init__(self, window_width, window_height):
        self._attack_image_template = pygame.transform.scale(Attack4._attack_image_template, (2 * window_width / 24, 3 * window_height / 16))
        self._attack_rect = self._attack_image_template.get_rect()
        self._hp = Attack4._hp
        self._initial_hp = Attack4._hp
        self._damage = Attack4._damage
        Attack.__init__(self, window_width, window_height)