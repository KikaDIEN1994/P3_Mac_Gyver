class Item:
    """In this class we going to define each objet to pick"""

    def __init__(self, x, y, image):
    #init picture of items
        self.x = x
        self.y = y
        self.is_drop = False
        self.image = image

    def get_position(self):
    # get position items
        return (self.x, self.y)

    def is_item_drop(self):
        return self.is_drop

    def drop_item(self):
        self.is_drop = True

