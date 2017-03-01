import pygame
import time


class TileArtModel:
    """ Encodes the game state """
    def __init__(self):
        self.tiles = []
        positions = (10, 50, 100)
        for x in positions:
            newtile = Tile((0, 255, 0), x, 120)
            print(x)
            self.tiles.append(newtile)
        

class Tile:
    '''definition of a singular tile'''
    def __init__(self, color, x, y, width=20, height=20):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.color = color

# class Column:
#     '''definition of a column'''
#     def __init__(self):
#         self.
#
#
# class Grid:
#
#
# class View:
#
#
# class Cursor:


class TileArtController:
    '''controls the cursor and the state of the tile'''


class TileArtWindowView:
    """ A view of brick breaker rendered in a Pygame window """
    def __init__(self, model, screen):
        self.model = model
        self.screen = screen

    def draw(self):
        self.screen.fill(pygame.Color(0, 0, 0))
        for tile in self.model.tiles:
            pygame.draw.rect(self.screen, pygame.Color(tile.color[0],
                             tile.color[1], tile.color[2]),
                             pygame.Rect(
                             tile.x, tile.y, tile.width,
                             tile.height))
        # pygame.draw.rect(self.screen, pygame.Color(
                        #  self.model.paddle.color[0],
                        #  self.model.paddle.color[1],
                        #  self.model.paddle.color[2]), pygame.Rect(
                        #  self.model.paddle.x, self.model.paddle.y,
                        #  self.model.paddle.width, self.model.paddle.height))
        pygame.display.update()




if __name__ == '__main__':
    pygame.init()

    size = (640, 480)
    screen = pygame.display.set_mode(size)

    model = TileArtModel()
    view = TileArtWindowView(model, screen)
    controller = TileArtController()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # if event.type == pygame.MOUSEMOTION:
            #     controller.handle_mouse_event(event)
        view.draw()
        time.sleep(.001)

    pygame.quit()
