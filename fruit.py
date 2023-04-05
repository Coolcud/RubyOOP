class Fruit:
    def __init__(self, taste, color):
        self.taste = taste
        self.color = color

    def is_ripe(self):
        return self.color != "green"
    
    # TODO: Could add a ripeness dictionary??