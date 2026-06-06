import sys
import ctypes

from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon

from ui import mainWindow

app = QApplication(sys.argv)

app.setWindowIcon(QIcon("icon.ico"))

window = mainWindow()
window.show()

sys.exit(app.exec_())