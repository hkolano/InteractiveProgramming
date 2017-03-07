import pygame
import time


class TileArtModel:
    """ Encodes the game state """
    def __init__(self, num_columns=16, tile_size=40, border_size=10):
        self.cursor = Cursor((150, 100, 200), 30, 30)
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
        positions = (10, 60, 110, 160, 210, 260, 310, 360)
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
    def __init__(self, notes_list):
        note_dict = dict()
        note_names = ['c', 'd', 'e', 'f', 'g', 'a', 'b', 'C']
        self.channel1 = pygame.mixer.Channel(1)
        self.channel2 = pygame.mixer.Channel(2)
        for i in range(0, 8):
            pygame.mixer.music.load(notes_list[i])
            note_dict[note_names[i]] = pygame.mixer.Sound(notes_list[i])
        self.c = note_dict['c']
        self.d = note_dict['d']
        self.e = note_dict['e']
        self.f = note_dict['f']
        self.g = note_dict['g']
        self.a = note_dict['a']
        self.b = note_dict['b']
        self.C = note_dict['C']


class Cursor:
    """ Encodes the state of the cursor in the game """
    def __init__(self, color, x, y, radius=10, width=0, column=0, row=0):
        self.color = color
        self.x = x
        self.y = y
        self.pos = [self.x,self.y]
        self.radius = radius
        self.width = width
        self.whichcolumn = column
        self.whichrow = row


class TileArtController:
    '''controls the cursor and the state of the tile'''
    def __init__(self, model):
        self.model = model

    def handle_keydown_event(self, event):
        column_of_tile = self.model.cursor.whichcolumn
        row_of_tile = self.model.cursor.whichrow
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.model.cursor.pos[0] += -50
                self.model.cursor.whichcolumn += -1
            elif event.key == pygame.K_RIGHT:
                self.model.cursor.pos[0] += +50
                self.model.cursor.whichcolumn += 1
            elif event.key == pygame.K_UP:
                self.model.cursor.pos[1] += -50
                self.model.cursor.whichrow += -1
            elif event.key == pygame.K_DOWN:
                self.model.cursor.pos[1] += +50
                self.model.cursor.whichrow += 1
            elif event.key == pygame.K_r:
                self.model.columns[column_of_tile].tiles[row_of_tile].color = color_dict['red']
            elif event.key == pygame.K_w:
                self.model.columns[column_of_tile].tiles[row_of_tile].color = color_dict['white']
            elif event.key == pygame.K_g:
                self.model.columns[column_of_tile].tiles[row_of_tile].color = color_dict['gray']
            elif event.key == pygame.K_y:
                self.model.columns[column_of_tile].tiles[row_of_tile].color = color_dict['yellow']
            elif event.key == pygame.K_p:
                self.model.columns[column_of_tile].tiles[row_of_tile].color = color_dict['purple']
            elif event.key == pygame.K_b:
                self.model.columns[column_of_tile].tiles[row_of_tile].color = color_dict['blue']
            elif event.key == pygame.K_e:
                self.model.columns[column_of_tile].tiles[row_of_tile].color = color_dict['green']
            elif event.key == pygame.K_t:
                self.model.columns[column_of_tile].tiles[row_of_tile].color = color_dict['teal']


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
        pygame.draw.circle(self.screen, pygame.Color(
                         self.model.cursor.color[0],
                         self.model.cursor.color[1],
                         self.model.cursor.color[2]),
                         self.model.cursor.pos, self.model.cursor.radius,
                         self.model.cursor.width)
        pygame.display.update()
    def read_column(self):
        for column in self.model.columns:newtile = Tile(color, x, y)
                positions.append(positions[i] + tile_size + border_size)
            for i in range(8):
                if columns[i].color = 'red'
                newtile = Tile(color, x, y)
                positions.append(positions[i] + tile_size + border_size)


if __name__ == '__main__':
    pygame.init()
    pygame.mixer.init()
    guitar = Instrument(['c6gui.wav', 'd6guit.wav', 'e6guit.wav',
                         'f6guit.wav', 'g6guit.wav', 'a6guit.wav',
                         'b6guit.wav', 'c7guit.wav'])
    guitar.channel1.play(guitar.e)
    guitar.channel2.play(guitar.b)
    time.sleep(.75)
    guitar.channel1.play(guitar.g)
    guitar.channel2.play(guitar.c)
    time.sleep(.75)
    guitar.channel1.play(guitar.e)
    guitar.channel2.play(guitar.b)
    time.sleep(.75)
    color_dict = {'green': (0, 255, 0),
                  'blue': (0, 0, 255),
                  'red': (255, 0, 0),
                  'purple': (255, 0, 255),
                  'teal': (0, 255, 255),
                  'yellow': (255, 255, 0),
                  'white': (255, 255, 255),
                  'gray': (100, 100, 100)
                  }

    size = (810, 410)
    screen = pygame.display.set_mode(size)

    model = TileArtModel()
    view = TileArtWindowView(model, screen)
    controller = TileArtController(model)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                controller.handle_keydown_event(event)
        view.draw()
        time.sleep(.001)

    pygame.quit()
