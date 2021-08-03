import pygame
import os
# (load image form images file) (use os.path.join to ensure that the path will not be error)
# (load images first, and reform it to the proper size)
UPGRADE_MENU_before = pygame.image.load(os.path.join("images", "upgrade_menu.png"))
UPGRADE_MENU=pygame.transform.scale(UPGRADE_MENU_before, (250, 250))

UPGRAGE_BUTTON_before = pygame.image.load(os.path.join("images", "upgrade.png"))
UPGRADE_BUTTON=pygame.transform.scale(UPGRAGE_BUTTON_before,(50,50))

SELL_BUTTON_before = pygame.image.load(os.path.join("images", "sell.png"))
SELL_BUTTON= pygame.transform.scale(SELL_BUTTON_before,(50,50))

class UpgradeMenu:
    def __init__(self, x, y):
        # (define the UPGRADE IMAGE) (Follow the x,y based on class TowerGroup)
        self.image = UPGRADE_MENU
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        # (Create a list about buttons) (define the buttons) (The position of buttons depend on Menu)
        self.__buttons = [Button(UPGRADE_BUTTON, "upgrade", x, y+90),Button(SELL_BUTTON, "sell", x, y-90)]
        self.upgrade_button=self.__buttons[0]
        self.sell_button=self.__buttons[1]

    def draw(self, win):
        """
        (Q1) draw menu itself and the buttons
        (This method is call in draw() method in class TowerGroup)
        :return: None
        """
        # (draw buttons and menu)
        win.blit(self.image, self.rect)
        win.blit(self.upgrade_button.image,self.upgrade_button.rect)
        win.blit(self.sell_button.image, self.sell_button.rect)

    def get_buttons(self):
        """
        (Q1) Return the button list.
        (This method is call in get_click() method in class TowerGroup)
        :return: list
        """
        return self.__buttons


class Button:
    def __init__(self, image, name, x, y):
        self.image = image
        self.name = name
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def clicked(self, x, y):
        """
        (Q2) Return Whether the button is clicked
        (This method is call in get_click() method in class TowerGroup)
        :param x: mouse x
        :param y: mouse y
        :return: bool
        """
        if self.rect.collidepoint(x, y):
            return True
        else:
            False

    def response(self):
        """
        (Q2) Return the button name.
        (This method is call in get_click() method in class TowerGroup)
        :return: str
        """
        return self.name