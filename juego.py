# Importación de librerías e inicialización
import pygame  # Biblioteca para crear videojuegos
pygame.init()  # Inicializa Pygame

import time  # Para manejar pausas en el juego

# Configuración de la ventana del videojuego
alto = 600
ancho = 800
pantalla = pygame.display.set_mode((ancho, alto))

# Encabezado de la ventana
pygame.display.set_icon(pygame.image.load("Logo.png"))  # Ícono de la ventana
pygame.display.set_caption("F1: DRIVE TO SURVIVE")  # Título de la ventana

# Cargar el auto y ajustar su tamaño
ferrari = pygame.image.load("Ferrari.png")
ferrari = pygame.transform.scale(ferrari, (56, 155))
anchoferrari = 56  # Ancho del auto

# Cargar y escalar imágenes del fondo
borde1 = pygame.image.load("Borde Izquierdo.png")
borde1 = pygame.transform.scale(borde1, (175, 600))  # Borde izquierdo más ancho

borde2 = pygame.image.load("Borde Derecho.png")
borde2 = pygame.transform.scale(borde2, (175, 600))  # Borde derecho más ancho

pista = pygame.image.load("Pista.png")
pista = pygame.transform.scale(pista, (450, 600))  # Pista más angosta

# Preparar mensaje de choque
fuente = pygame.font.SysFont(None, 50)  # Fuente para el texto
msjChocar = fuente.render("¡CHOCASTE!", True, (255, 255, 255))  # Texto blanco

# Reloj para controlar los FPS (fotogramas por segundo)
reloj = pygame.time.Clock()

# Dibuja el auto en la pantalla en las coordenadas x, y
def auto(x, y):
    pantalla.blit(ferrari, (x, y))

# Dibuja el fondo: pista y bordes
def fondo():
    pantalla.blit(borde1, (0, 0))        # Borde izquierdo
    pantalla.blit(pista, (175, 0))       # Pista centrada
    pantalla.blit(borde2, (625, 0))      # Borde derecho

# Bucle principal del juego
def juego():
    coordenadaX = 0  # Movimiento horizontal
    x = 400  # Posición inicial del auto en X
    y = 450  # Posición inicial del auto en Y

    jugando = True  # Variable para controlar el estado del juego

    while jugando:
        for event in pygame.event.get():  # Manejo de eventos del usuario
            if event.type == pygame.QUIT:  # Salir al cerrar la ventana
                jugando = False

            # Detectar teclas presionadas
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    coordenadaX = -5
                if event.key == pygame.K_RIGHT:
                    coordenadaX = 5

            # Detectar teclas soltadas
            if event.type == pygame.KEYUP:
                if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    coordenadaX = 0

        x += coordenadaX  # Actualizar posición del auto

        pantalla.fill((0, 28, 51))  # Fondo base
        fondo()  # Dibuja bordes y pista
        auto(x, y)  # Dibuja el auto

        # Si el auto se sale de los límites de la pista, muestra mensaje de choque
        if x > 660 - anchoferrari or x < 150:
            texto_x = ancho // 2 - msjChocar.get_width() // 2
            texto_y = 285

            # Dibuja bandera roja detrás del texto
            pygame.draw.rect(
                pantalla,
                (139, 0, 0),  # Rojo oscuro (bandera roja)
                (texto_x - 10, texto_y - 10, msjChocar.get_width() + 20, msjChocar.get_height() + 20)
            )  # Rectángulo rojo con padding alrededor del texto

            pantalla.blit(msjChocar, (texto_x, texto_y))  # Dibuja el mensaje centrado
            pygame.display.update()

            time.sleep(3)  # Espera 3 segundos antes de reiniciar el juego
            # Reiniciar las posiciones
            x = 400  # Restablece la posición del auto en X
            y = 450  # Restablece la posición del auto en Y
            coordenadaX = 0  # Reinicia la velocidad horizontal

        pygame.display.update()  # Actualiza la pantalla
        reloj.tick(120)  # Limita a 120 FPS

    pygame.quit()  # Finaliza Pygame

# Inicia el juego
juego()
