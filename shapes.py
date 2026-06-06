#All shape classes
class shape():
    def __init__(self, x, y, vx, vy) -> None:
        #Positions
        self.x = x
        self.y = y
        #Velocity
        self.vx = vx
        self.vy = vy
    
class ball(shape):
    def __init__(self, x, y, vx, vy, r):
        super().__init__(x, y, vx, vy)
        #Radius
        self.r = r

class square(shape):
    def __init__(self, x, y, vx, vy, width, height):
        super().__init__(x, y, vx, vy)
        #Width & Height
        self.width = width
        self.height = height
    
class rectangle(shape):
    def __init__(self, x, y, vx, vy, width, height):
        super().__init__(x, y, vx, vy)
        #Width & Height
        self.width = width
        self.height = height