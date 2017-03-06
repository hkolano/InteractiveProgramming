import pygame
import time

'''music files'''



class TileArtModel:
    """ Encodes the game state """
    def __init__(self, num_columns=16, tile_size=40, border_size=10):
        positions = [border_size]
        for i in range(num_columns):
            positions.append(positions[i] + tile_size + border_size)
        self.columns = []
        for x in positions:
            newcolumn = Column(color_dict['white'], x, y=10)
            self.columns.append(newcolumn)


class Column:
    '''definition of a column'''
    def __init__(self, color, x, y):
        self.tiles = []
        positions = (10, 60, 110, 160, 210, 260, 310)
        for y in positions:
            newtile = Tile(color, x, y)
            self.tiles.append(newtile)


class Tile:
    '''definition of a singular tile'''
    def __init__(self, color, x, y, width=40, height=40):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.color = color


class Instrument:
    '''defines attributes of an instrument'''
    def __init__(self): # , instr_name, notes_list):
        note_dict = dict()
        note_names = ['c', 'd', 'e', 'f', 'g', 'a', 'b', 'C']
        for i in range(0, 7):
            pygame.mixer.music.load(notes_list[i])
            note_dict[note_names[i]] = pygame.mixer.Sound(note)
        self.c = note_dict['c']
        self.d = note_dict


class Cursor:
    '''cursor object'''


class TileArtController:
    '''controls the cursor and the state of the tile'''


class TileArtWindowView:
    """ A view of brick breaker rendered in a Pygame window """
    def __init__(self, model, screen):
        self.model = model
        self.screen = screen

    def draw(self):
        self.screen.fill(pygame.Color(0, 0, 0))
        for column in self.model.columns:
            for tile in column.tiles:
                pygame.draw.rect(self.screen, pygame.Color(tile.color[0],
                                 tile.color[1], tile.color[2]),
                                 pygame.Rect(
                                 tile.x, tile.y, tile.width,
                                 tile.height))
        pygame.display.update()




if __name__ == '__main__':
    pygame.init()
    pygame.mixer.init()
    ins = Instrument
    color_dict = {'green': (0, 255, 0),
                  'blue': (0, 0, 255),
                  'red': (255, 0, 0),
                  'purple': (255, 0, 255),
                  'teal': (0, 255, 255),
                  'yellow': (255, 255, 0),
                  'white': (255, 255, 255)
                  }

    size = (810, 360)
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
