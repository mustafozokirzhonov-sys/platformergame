class World:
    def __init__(self,levels,level_index, surfs):
        self.grass = []
        self.lava = []
        self.coin =  []
        self.blob = []
        self.dirt = []
        self.door = []

        self.levels = levels
        self.surfs = surfs
        self.load_levels(level_index)

    def load_levels(self,level_index):
        self.grass = []
        self.lava = []
        self.coin =  []
        self.blob = []
        self.dirt = []
        self.door = []

        for index, item in enumerate(self.levels[level_index]):
            for letter_index, letter in enumerate(item):
                if letter == "0":
                    x = letter_index * 25 
                    y = index * 25 
                    rect = self.surfs["lava"].get_rect(topleft=(x,y))
                    self.lava.append(rect)

                if letter == "1":
                    x = letter_index * 25
                    y = index * 25
                    rect = self.surfs["coin"].get_rect(topleft=(x+9,y+3))
                    self.coin.append(rect)

                if letter == "#":
                    x = letter_index * 25
                    y = index * 25
                    rect = self.surfs["grass"].get_rect(topleft=(x,y))
                    self.grass.append(rect)

                if letter == "9":
                    x = letter_index * 25
                    y = index * 25
                    rect = self.surfs["blob"].get_rect(topleft=(x,y+4))
                    self.blob.append(rect)

                if letter == "5":
                    x = letter_index * 25
                    y = index * 25
                    rect = self.surfs["dirt"].get_rect(topleft=(x,y))
                    self.dirt.append(rect)

                if letter == "7":
                    x = letter_index * 25
                    y = index * 25
                    rect = self.surfs["door"].get_rect(topleft=(x,y-4))
                    self.door.append(rect)
    def draw (self, screen):
        for item in self.grass:                      
            screen.blit(self.surfs["grass"],item)

        for item in self.blob:
            screen.blit(self.surfs["blob"],item)

        for item in self.lava:
            screen.blit(self.surfs["lava"],item)

        for item in self.coin:
            screen.blit(self.surfs["coin"],item)

        for item in self.dirt:
            screen.blit(self.surfs["dirt"],item)

        for item in self.door:
            screen.blit(self.surfs["door"],item)