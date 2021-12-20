class Location:
    x_location: int
    y_location: int

    def __init__(self, x: int = 0, y: int = 0):
        self.x_location = x
        self.y_location = y

    def __repr__(self):
        return f'| X: {self.x_location}; Y: {self.y_location} |'
