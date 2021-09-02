class Item:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.is_drop = False
        self.image = image

    def get_position(self):
        return (self.x, self.y)
        
        """
            fonction qui efface item quand homer_position = coordonnée items
        """
    def is_item_drop(self):
        #print("ok")
        return self.is_drop
        
    def drop_item(self):
        self.is_drop = True
        print("item")