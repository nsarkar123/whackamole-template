import pygame
import random

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        mole_pos = (0,0)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    mole_x, mole_y = mole_pos
                    print(f"Mouse clicked at: ({mouse_x}, {mouse_y})")
                    print(f"Mole is at: ({mole_x}, {mole_y})")
                    if (mole_x <= mouse_x < mole_x + 32) and (mole_y <= mouse_y < mole_y + 32):
                        mole_pos = (random.randint(0, 19) * 32, random.randint(0, 15) * 32)
            screen.fill("light blue")
            xVal = 0
            for x in range(0, 640, 32):
                pygame.draw.line(screen, "black", (x, 0), (x, 512))
            for y in range(0, 512, 32):
                pygame.draw.line(screen, "black", (0, y), (640, y))
            screen.blit(mole_image, mole_image.get_rect(topleft=mole_pos))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
