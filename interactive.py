import pygame
import time
'''
interactive.py
Sam Eppinger and Hannah Kolano
March 2017

Created as an interactive game experience for SoftDes Spr17. Draw in the grid
with colors green (g), blue (b), purple (p), yellow (y), or white (w) to play
different instruments. hit (m) to play your art.
'''

class TileArtModel:
    """ Encodes the game state.
    self.columns: list of column objects
    self.cursor: a cursor object
    initiates channels to play sound on"""
    def __init__(self, num_columns=16, tile_size=40, border_size=10):
        self.cursor = Cursor((150, 100, 200), 30, 30)
        positions = [border_size]
        for i in range(num_columns):
            positions.append(positions[i] + tile_size + border_size)
        self.columns = []
        for x in positions:
            newcolumn = Column(color_dict['white'], x, y=10)
            self.columns.append(newcolumn)
        self.channel1 = pygame.mixer.Channel(1)
        self.channel2 = pygame.mixer.Channel(2)
        self.channel3 = pygame.mixer.Channel(3)
        self.channel4 = pygame.mixer.Channel(4)
        self.channel5 = pygame.mixer.Channel(5)
        self.channel6 = pygame.mixer.Channel(6)
        self.channel7 = pygame.mixer.Channel(7)
        self.channel0 = pygame.mixer.Channel(0)
        self.Channels = [self.channel1, self.channel2, self.channel3,
                         self.channel4, self.channel5, self.channel6,
                         self.channel7, self.channel0]


    def read_column(self):
        '''Goes across the board and plays the notes designated by each tile
        '''
        for column in self.columns:
            time.sleep(.7)
            for channel in self.Channels:
                channel.fadeout(400)
            for i in range(8):
                channel = self.Channels[i]
                if column.tiles[i].color == color_dict['green']:
                    channel.play(guitar.note_dict[guitar.note_names[7-i]])
                if column.tiles[i].color == color_dict['blue']:
                    channel.play(trumpet.note_dict[trumpet.note_names[7-i]])
                if column.tiles[i].color == color_dict['purple']:
                    channel.play(cello.note_dict[cello.note_names[7-i]])
                if column.tiles[i].color == color_dict['yellow']:
                    channel.play(sax.note_dict[sax.note_names[7-i]])

class Column:
    '''definition of a column
    self.tiles: a list of tile objects from top to bottom'''
    def __init__(self, color, x, y):
        self.tiles = []
        positions = (10, 60, 110, 160, 210, 260, 310, 360)
        for y in positions:
            newtile = Tile(color, x, y)
            self.tiles.append(newtile)


class Tile:
    '''definition of a singular tile
    has a height, width, x position, y position, and color'''
    def __init__(self, color, x, y, width=40, height=40):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.color = color


class Instrument:
    '''defines an Instrument
    self.note_dict: maps note names to their corresponding sounds
    self.note_names: a list of note note_names
    self.a, etc: maps to a sound file. can play with ex guitar.e.play()'''
    def __init__(self, notes_list):
        self.note_dict = dict()
        self.note_names = ['c', 'd', 'e', 'f', 'g', 'a', 'b', 'C']
        for i in range(0, 8):
            pygame.mixer.music.load(notes_list[i])
            self.note_dict[self.note_names[i]] = pygame.mixer.Sound(notes_list[i])
        self.c = self.note_dict['c']
        self.d = self.note_dict['d']
        self.e = self.note_dict['e']
        self.f = self.note_dict['f']
        self.g = self.note_dict['g']
        self.a = self.note_dict['a']
        self.b = self.note_dict['b']
        self.C = self.note_dict['C']


class Cursor:
    """ Encodes the state of the cursor in the game
    has a color, x position, y position, radius, width
    self.whichcolumn keeps track of the column it's in
    self.whichrow keeps track of the row it's in"""
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
    '''takes all possible inputs and changes objects appropriately'''
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
            elif event.key == pygame.K_w:
                self.model.columns[column_of_tile].tiles[row_of_tile].color = color_dict['white']
            elif event.key == pygame.K_g:
                self.model.columns[column_of_tile].tiles[row_of_tile].color = color_dict['green']
            elif event.key == pygame.K_y:
                self.model.columns[column_of_tile].tiles[row_of_tile].color = color_dict['yellow']
            elif event.key == pygame.K_p:
                self.model.columns[column_of_tile].tiles[row_of_tile].color = color_dict['purple']
            elif event.key == pygame.K_b:
                self.model.columns[column_of_tile].tiles[row_of_tile].color = color_dict['blue']
            elif event.key ==pygame.K_m:
                self.model.read_column()


class TileArtWindowView:
    """ the view, in a pygame window """
    def __init__(self, model, screen):
        self.model = model
        self.screen = screen

    def draw(self):
        '''draws the tiles and the cursor'''
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


if __name__ == '__main__':
    pygame.init()
    pygame.mixer.init()
    guitar = Instrument(['c6gui.wav', 'd6guit.wav', 'e6guit.wav',
                         'f6guit.wav', 'g6guit.wav', 'a6guit.wav',
                         'b6guit.wav', 'c7guit.wav'])
    trumpet = Instrument(['c4trum.wav', 'd4trum.wav', 'e4trum.wav',
                          'f4trum.wav', 'g4trum.wav', 'a4trum.wav',
                          'b4trum.wav', 'c5trum.wav'])
    cello = Instrument(['c2cello.wav', 'd2cello.wav', 'e2cello.wav',
                        'f2cello.wav', 'g2cello.wav', 'a2cello.wav',
                        'b2cello.wav', 'c3cello.wav'])
    sax = Instrument(['c3sax.wav', 'd3sax.wav', 'e3sax.wav', 'f3sax.wav',
                      'g3sax.wav', 'a3sax.wav', 'b3sax.wav', 'c4sax.wav'])
    color_dict = {'green': (0, 255, 0),
                  'blue': (0, 0, 255),
                  'purple': (255, 0, 255),
                  'yellow': (255, 255, 0),
                  'white': (255, 255, 255),
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
