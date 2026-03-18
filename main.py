import pygame
import sys
import random
from jugador import PersonajeTaifa
from enemigo import Raton, RatonJefe
from tesoro import Tesoro
from pocion import Pocion

pygame.init()
pygame.mixer.init()
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Taifa se va de compras")
reloj = pygame.time.Clock()

ORO = (255, 215, 0)

fondo_inicio = pygame.transform.scale(pygame.image.load("assets/taifi/inicio.png"), (ANCHO, ALTO))
escenario = pygame.transform.scale(pygame.image.load("assets/taifi/escenario.png"), (ANCHO, ALTO))

taifa_img = pygame.transform.scale(pygame.image.load("assets/taifi/taifa.png"), (60, 60))
taifa_desc = pygame.transform.scale(pygame.image.load("assets/taifi/taifiDescanso.png"), (60, 60))
taifa_hechicera_img = pygame.transform.scale(pygame.image.load("assets/taifi/hechicera.png"), (60, 60))

pocion_img = pygame.transform.scale(pygame.image.load("assets/taifi/pocion.png"), (35, 55)) 
item_resistencia = Pocion(pocion_img)

cesta_img = pygame.transform.scale(pygame.image.load("assets/taifi/cesta.png"), (80, 80))
cesta_rect = cesta_img.get_rect(topleft=(ANCHO - 120, ALTO - 120))

tesoros_imgs = [pygame.transform.scale(pygame.image.load(f"assets/taifi/{n}"), (40, 40)) 
                for n in ["aceituna.png", "esparrago.png", "gomillas.png", "lentejas.png", "yogur.png"]]
ratones_imgs = [pygame.transform.scale(pygame.image.load(f"assets/taifi/{n}"), (50, 50)) 
                for n in ["ratonBlanco.png", "ratonMarron.png", "ratonNegro.png"]]
raton_jefe_img = pygame.transform.scale(pygame.image.load("assets/taifi/ratonJefe.png"), (90, 90))

s_choque = pygame.mixer.Sound("assets/taifi/sonidos/choque.wav")
miau = pygame.mixer.Sound("assets/taifi/sonidos/miau.wav")

pygame.mixer.music.load("assets/taifi/sonidos/musica_inicio.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

fuente_especial = pygame.font.Font("assets/taifi/fuente/EnchantedLand.otf", 80)
fuente_pts = pygame.font.SysFont("Arial", 30, bold=True)
fuente_reglas = pygame.font.SysFont("Arial", 22)

MENU, REGLAS, JUEGO, RESULTADOS = 0, 1, 2, 3
estado_actual = MENU
puntuacion = 0
tiempo_inicio = 0
DURACION_MAXIMA = 90 

# --- INSTANCIAS ---
taifa_jugador = PersonajeTaifa(taifa_img, taifa_desc, taifa_hechicera_img, fuente_pts)
tesoro_obj = Tesoro(tesoros_imgs)
jefe = RatonJefe(raton_jefe_img)
lista_ratones = []

# --- EVENTOS DE TIEMPO ---
SPAWN_RATON = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_RATON, 1500)
MOVER_CESTA_EVENT = pygame.USEREVENT + 2
pygame.time.set_timer(MOVER_CESTA_EVENT, 10000)
APARECER_POCION = pygame.USEREVENT + 3
pygame.time.set_timer(APARECER_POCION, 15000)

ejecutando = True
while ejecutando:
    reloj.tick(60) 
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
    
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
            if estado_actual == MENU: 
                estado_actual = REGLAS
            elif estado_actual == REGLAS:
                estado_actual = JUEGO
                tiempo_inicio = pygame.time.get_ticks()
                pygame.mixer.music.load("assets/taifi/sonidos/musica_juego.mp3")
                pygame.mixer.music.play(-1)
            elif estado_actual == RESULTADOS:
                puntuacion = 0
                taifa_jugador = PersonajeTaifa(taifa_img, taifa_desc, taifa_hechicera_img, fuente_pts)
                lista_ratones.clear()
                estado_actual = MENU

        if estado_actual == JUEGO:
            if evento.type == SPAWN_RATON and not taifa_jugador.es_hechicera:
                lista_ratones.append(Raton(ratones_imgs))
            if evento.type == MOVER_CESTA_EVENT:
                cesta_rect.x = random.randint(50, ANCHO - 150)
                cesta_rect.y = random.randint(50, ALTO - 150)
            if evento.type == APARECER_POCION:
                item_resistencia.reubicar()

    if estado_actual == MENU:
        pantalla.blit(fondo_inicio, (0, 0))
        txt_start = fuente_pts.render("PULSA ESPACIO PARA CONTINUAR", True, ORO)
        pantalla.blit(txt_start, txt_start.get_rect(center=(ANCHO//2, 220)))

    elif estado_actual == REGLAS:
        pantalla.fill((30, 30, 30))
        reglas_titulo = fuente_especial.render("Instrucciones", True, ORO)
        pantalla.blit(reglas_titulo, reglas_titulo.get_rect(center=(ANCHO//2, 80)))
        
        texto_reglas = [
            "- Usa W, A, S, D para mover a Taifa.",
            "- Recoge los tesoros y llévalos a la cesta.",
            "- Los ratones te quitan el tesoro si te tocan.",
            "- Coge las pociones para recuperar energía.",
            "- A los 10 puntos, ¡Hechicera y aparece el Jefe!",
            "PULSA ESPACIO PARA EMPEZAR"
        ]
        for i, linea in enumerate(texto_reglas):
            color = (255, 255, 255) if i < len(texto_reglas)-1 else (34, 177, 76)
            txt = fuente_reglas.render(linea, True, color)
            pantalla.blit(txt, (100, 180 + (i * 40)))

    elif estado_actual == JUEGO:
        pantalla.blit(escenario, (0, 0))
        pantalla.blit(cesta_img, cesta_rect)
        
        segundos_pasados = (pygame.time.get_ticks() - tiempo_inicio) // 1000
        tiempo_restante = max(0, DURACION_MAXIMA - segundos_pasados)
        if tiempo_restante <= 0: estado_actual = RESULTADOS

        if puntuacion >= 10 and not taifa_jugador.es_hechicera:
            taifa_jugador.es_hechicera = True
            lista_ratones.clear()

        taifa_jugador.mover(pygame.key.get_pressed(), miau)
        taifa_jugador.dibujar(pantalla)

        if not taifa_jugador.tiene_tesoro:
            tesoro_obj.dibujar(pantalla)
            if taifa_jugador.rect.colliderect(tesoro_obj.rect) and not taifa_jugador.dormida:
                taifa_jugador.tiene_tesoro = True
        else:
            tesoro_obj.rect.center = taifa_jugador.rect.center
            tesoro_obj.dibujar(pantalla)
            if taifa_jugador.rect.colliderect(cesta_rect):
                puntuacion += 1
                taifa_jugador.tiene_tesoro = False
                tesoro_obj.reubicar()

        item_resistencia.actualizar()
        if item_resistencia.activa:
            item_resistencia.dibujar(pantalla)
            if taifa_jugador.rect.colliderect(item_resistencia.rect):
                taifa_jugador.energia = 100
                item_resistencia.activa = False

        if not taifa_jugador.es_hechicera:
            for r in lista_ratones[:]:
                r.mover()
                r.dibujar(pantalla)
                if taifa_jugador.rect.colliderect(r.rect):
                    s_choque.play()
                    taifa_jugador.tiene_tesoro = False
                    tesoro_obj.reubicar()
                    lista_ratones.remove(r)
        else:
            jefe.mover(taifa_jugador.rect) 
            jefe.dibujar(pantalla)
            if taifa_jugador.rect.colliderect(jefe.rect):
                s_choque.play()
                puntuacion = max(0, puntuacion - 3)
                taifa_jugador.tiene_tesoro = False
                tesoro_obj.reubicar()
                jefe.rect.x = -100

        pygame.draw.rect(pantalla, (169, 40, 40), (20, 20, 200, 20))
        pygame.draw.rect(pantalla, (34, 177, 76), (20, 20, taifa_jugador.energia * 2, 20))
        txt_puntos = fuente_pts.render(f"Tesoros: {puntuacion}", True, ORO)
        pantalla.blit(txt_puntos, (ANCHO - 180, 20))
        txt_timer = fuente_pts.render(f"Tiempo: {tiempo_restante}s", True, (255, 255, 255))
        pantalla.blit(txt_timer, (ANCHO // 2 - 50, 20))

    elif estado_actual == RESULTADOS:
        pantalla.fill((0, 0, 0))
        msg = fuente_especial.render("¡TIEMPO AGOTADO!", True, ORO)
        pantalla.blit(msg, msg.get_rect(center=(ANCHO//2, 150)))

        txt_puntos = fuente_pts.render(f"Puntuación Final: {puntuacion}", True, (255, 255, 255))
        pantalla.blit(txt_puntos, txt_puntos.get_rect(center=(ANCHO//2, 280)))

        if puntuacion == 0:
            txt_final = fuente_pts.render("¡Los ratones te quitaron todos tus tesoros!", True, (255, 100, 100))
        else:
            txt_final = fuente_pts.render("¡Conseguiste llevarte tesoros a casa!", True, (100, 255, 100))

        pantalla.blit(txt_final, txt_final.get_rect(center=(ANCHO//2, 380)))
        
        retry = fuente_pts.render("Pulsa ESPACIO para volver al menú", True, (200, 200, 200))
        pantalla.blit(retry, retry.get_rect(center=(ANCHO//2, 500)))

    pygame.display.flip()

pygame.quit()
sys.exit()
