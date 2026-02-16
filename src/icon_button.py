from PyQt6.QtWidgets import QPushButton, QLabel
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt


class IconButton(QPushButton):
    def __init__(self, image_name, parent=None):
        super().__init__(parent)

        self.label = QLabel(self)
        pixmap = QPixmap("img/{}.png".format(image_name))
        pixmap_scaled = pixmap.scaled(30, 30, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.label.setPixmap(pixmap_scaled)
        self.label.move(278, 0)
