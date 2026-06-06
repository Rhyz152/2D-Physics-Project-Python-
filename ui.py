from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTimer, Qt

from world import worldShapes
from shapes import ball, square, rectangle
from physics import update_engine
from render import draw
from PyQt5.QtGui import QPainter
from time import sleep


class Canvas(QWidget):
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(Qt.white) # type: ignore
        painter.setBrush(Qt.NoBrush) # type: ignore

        draw(painter)

        painter.end()


class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(300, 200, 800, 600)
        self.setWindowTitle("2D Physics Engine")
        self.setWindowIcon(QIcon("icon.png"))

        self.gravity = 0.5

        self.ballButton = QPushButton("Ball")
        self.squareButton = QPushButton("Square")
        self.rectangleButton = QPushButton("Rectangle")

        self.init_ui()

        self.timer = QTimer()
        self.timer.timeout.connect(self.tick)
        self.timer.start(16)

    def init_ui(self):
        self.setStyleSheet("""
    QWidget {
        background-color: black;
    }

    QPushButton {
        color: white;
        background-color: #222;
    }

    QPushButton:hover {
        background-color: #444;
    }
        """)
        central = QWidget()
        self.setCentralWidget(central)

        layout = QVBoxLayout()
        central.setLayout(layout)

        button_row = QHBoxLayout()
        button_row.addWidget(self.ballButton)
        button_row.addWidget(self.squareButton)
        button_row.addWidget(self.rectangleButton)

        layout.addLayout(button_row)

        self.canvas = Canvas()
        layout.addWidget(self.canvas)

        self.ballButton.clicked.connect(self.spawn_ball)
        self.squareButton.clicked.connect(self.spawn_square)
        self.rectangleButton.clicked.connect(self.spawn_rectangle)

    def spawn_ball(self):
        worldShapes["balls"].append(ball(200, 100, 3, 0, 20))

    def spawn_square(self):
        worldShapes["squares"].append(square(200, 100, 3, 0, 50, 50))

    def spawn_rectangle(self):
        worldShapes["rectangles"].append(rectangle(200, 100, 3, 0, 100, 50))

    def tick(self):
        update_engine(self.gravity, self.width(), self.height())
        self.canvas.update()
        while len(worldShapes["balls"]) > 1000:
            worldShapes["balls"].pop(0)

        while len(worldShapes["rectangles"]) > 1000:
            worldShapes["rectangles"].pop(0)

        while len(worldShapes["squares"]) > 1000:
            worldShapes["squares"].pop(0)