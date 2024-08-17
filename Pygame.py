import pygame
import sys

# Inicialización de Pygame
pygame.init()

# Dimensiones de la pantalla
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("EcoCódigos: Clasifica y Recicla")

# Colores
WHITE = (255, 255, 255)

# Objetos de juego (representados como rectángulos)
items = {
    "paper": pygame.Rect(50, 500, 50, 50),
    "bottle": pygame.Rect(150, 500, 50, 50),
    "bag": pygame.Rect(250, 500, 50, 50),
}

# Contenedores
bins = {
    "paper": pygame.Rect(50, 100, 100, 100),
    "plastic": pygame.Rect(250, 100, 100, 100),
    "glass": pygame.Rect(450, 100, 100, 100),
}

score = 0
font = pygame.font.Font(None, 36)

# Bucle principal del juego
running = True
selected_item = None
while running:
    screen.fill(WHITE)
    
    # Mostrar contenedores
    pygame.draw.rect(screen, (200, 200, 255), bins["paper"])
    pygame.draw.rect(screen, (255, 200, 200), bins["plastic"])
    pygame.draw.rect(screen, (200, 255, 200), bins["glass"])
    
    # Mostrar elementos
    for item in items.values():
        pygame.draw.rect(screen, (0, 0, 0), item)
    
    # Mostrar puntuación
    score_text = font.render(f"Puntuación: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    
    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for key, rect in items.items():
                if rect.collidepoint(event.pos):
                    selected_item = key
        elif event.type == pygame.MOUSEBUTTONUP:
            if selected_item:
                for bin_key, bin_rect in bins.items():
                    if items[selected_item].colliderect(bin_rect):
                        if selected_item == bin_key:
                            score += 10
                            items[selected_item].topleft = (50, 500)
                selected_item = None
        elif event.type == pygame.MOUSEMOTION:
            if selected_item:
                items[selected_item].move_ip(event.rel)
    
    pygame.display.flip()

pygame.quit()
sys.exit()
