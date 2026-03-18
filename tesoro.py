import pygame
import random

class Tesoro:
    def __init__(self, imagenes):
        self.__imagenes = imagenes
        self.__image = random.choice(self.__imagenes)
        self.__rect = self.__image.get_rect()
        self.reubicar()
        
    @property
    def rect(self):
        return self.__rect

    @property
    def image(self):
        return self.__image

    def reubicar(self):
        """Cambia la posición y la imagen del tesoro de forma aleatoria"""
        self.__rect.x = random.randint(50, 750)
        self.__rect.y = random.randint(50, 500)
        self.__image = random.choice(self.__imagenes)
        
    def dibujar(self, superficie):
        """Dibuja el tesoro en la superficie proporcionada"""
        superficie.blit(self.__image, self.__rect)
