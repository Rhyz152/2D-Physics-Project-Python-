from world import *
from PyQt5.QtCore import Qt

def draw(painter):

    for b in worldShapes["balls"]:
        painter.drawEllipse(
            int(b.x - b.r),
            int(b.y - b.r),
            int(b.r * 2),
            int(b.r * 2)
        )

    for s in worldShapes["squares"]:
        painter.drawRect(
            int(s.x),
            int(s.y),
            int(s.width),
            int(s.height)
        )

    for r in worldShapes["rectangles"]:
        painter.drawRect(
            int(r.x),
            int(r.y),
            int(r.width),
            int(r.height)
        )