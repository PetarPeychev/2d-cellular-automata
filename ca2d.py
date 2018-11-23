class CA:
    def __init__(self, birth_rule, death_rule, neighbourhood, array = None, size_x = None, size_y = None):

        # Set CA array and array size depending on optional inputs
        if not array and size_x and size_y:
            self._size_x = size_x
            self._size_y = size_y
            self.array = [[0 for x in range(self._size_x)] for y in range(self._size_y)]
        elif array and not size_x and not size_y:
            self.array = array
            self._size_x = len(self.array[0])
            self._size_y = len(self.array)
        else:
            raise TypeError('invalid CA array or size arguments')

        # Set CA birth and death rules
        self.birth_rule = birth_rule
        self.death_rule = death_rule

        # Set CA neighbourhood type
        if neighbourhood == 'moore':
            self.neighbourhood = 'moore'
        elif neighbourhood == 'neumann':
            self.neighbourhood = 'neumann'
        else:
            raise TypeError('invalid CA neighbourhood')

    def step(self):
        pass
