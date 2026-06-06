#Modules
from world import *

#Apply physics to all
def update_all(gravity):
    for b in worldShapes["balls"]:
        b.vy += gravity
        b.x += b.vx
        b.y += b.vy

    for s in worldShapes["squares"]:
        s.vy += gravity
        s.x += s.vx
        s.y += s.vy

    for r in worldShapes["rectangles"]:
        r.vy += gravity
        r.x += r.vx
        r.y += r.vy

#Collisions for all shapes
def collideBalls(width, height):
    for b in worldShapes["balls"]:
            if b.x - b.r < 0 or b.x + b.r > width:
                b.vx *= -1
                b.x = max(b.r, min(width - b.r, b.x))
            
            if b.y - b.r < 0 or b.y + b.r > height:
                b.vy *= -1
                b.y = max(b.r, min(height - b.r, b.y))
                
def collideSquares(width, height):
    for s in worldShapes["squares"]:
            if s.x < 0 or s.x + s.width > width:
                s.vx *= -1
                s.x = max(s.width, min(width - s.width, s.x))
            
            if s.y < 0 or s.y + s.height > height:
                s.vy *= -1
                s.y = max(s.height, min(height - s.height, s.y))

def collideRectangles(width, height):
    for r in worldShapes["rectangles"]:

        if r.x < 0 or r.x + r.width > width:
            r.vx *= -1
            r.x = max(0, min(width - r.width, r.x))

        if r.y < 0 or r.y + r.height > height:
            r.vy *= -1
            r.y = max(0, min(height - r.height, r.y))

#Apply collision physics to each shape
def update_engine(gravity, width, height):
    update_all(gravity)
    collideBalls(width, height)
    collideSquares(width, height)
    collideRectangles(width, height)