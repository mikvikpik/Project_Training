import pygame

class Ship():

    def __init__(self, screen):
        """Initialize the ship and set its starting postion."""
        self.screen = screen

        # Load the ship image and get its rest.
        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Movement flag
        self.moving_right = False

    def eupdate(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_righ:
            self.rect.centerx += 1
            
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
