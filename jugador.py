import pygame

class PersonajeTaifa:
    def __init__(self, img_normal, img_dormida, img_hechicera, fuente_pts):
        self.img_normal_der = img_normal
        self.img_hechicera_der = img_hechicera
        
        self.img_normal_izq = pygame.transform.flip(img_normal, True, False)
        self.img_hechicera_izq = pygame.transform.flip(img_hechicera, True, False)
        
        self.img_dormida = img_dormida
        
        self.image = self.img_normal_der
        self.rect = self.image.get_rect(center=(400, 300))
        self.fuente_pts = fuente_pts
              
        self.__velocidad = 6  
        self.__energia = 100.0 
        self.__dormida = False
        self.__tiene_tesoro = False 
        self.__es_hechicera = False
    
    @property
    def energia(self):
        return self.__energia

    @energia.setter
    def energia(self, valor):
        self.__energia = max(0, min(100, valor))

    @property
    def dormida(self):
        return self.__dormida

    @property
    def tiene_tesoro(self):
        return self.__tiene_tesoro

    @tiene_tesoro.setter
    def tiene_tesoro(self, valor):
        self.__tiene_tesoro = valor

    @property
    def es_hechicera(self):
        return self.__es_hechicera

    @es_hechicera.setter
    def es_hechicera(self, valor):
        self.__es_hechicera = valor


    def mover(self, teclas, miau):
        if self.__dormida:
            self.energia += 0.15 
            if self.energia >= 60:
                self.__dormida = False
                self.image = self.img_hechicera_der if self.__es_hechicera else self.img_normal_der
            return

        movido = False
        
        if teclas[pygame.K_a] and self.rect.left > 0: 
            self.rect.x -= self.__velocidad
            self.image = self.img_hechicera_izq if self.__es_hechicera else self.img_normal_izq
            movido = True

        if teclas[pygame.K_d] and self.rect.right < 800: 
            self.rect.x += self.__velocidad
            self.image = self.img_hechicera_der if self.__es_hechicera else self.img_normal_der
            movido = True

        if teclas[pygame.K_w] and self.rect.top > 0: 
            self.rect.y -= self.__velocidad
            movido = True
        if teclas[pygame.K_s] and self.rect.bottom < 600: 
            self.rect.y += self.__velocidad
            movido = True

        if movido:
            self.energia -= 0.15
            if self.energia <= 0:
                self.__dormida = True
                self.image = self.img_dormida
            
            if not pygame.mixer.get_busy():
                miau.set_volume(0.4)
                miau.play()

    def dibujar(self, superficie):
        superficie.blit(self.image, self.rect)
        if self.__dormida:
            txt = self.fuente_pts.render("Zzz...", True, (255, 255, 255))
            superficie.blit(txt, (self.rect.x, self.rect.y - 20))
