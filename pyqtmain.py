from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtGui import QPixmap
import sys

class MainWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.button_show()

    def button_show(self):
        button = QPushButton("CLICK ME!", self)
        button.resize(2000, 60)
        button.clicked.connect(self.on_click)

    def on_click(self):
        print("USER CLICKED ME!")

class ImageWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.show_image()

    def show_image(self):
        image = QPixmap("car.jpg")
        print(image)
        label = QLabel(self)
        label.setPixmap(image)


def main():

    application = QApplication(sys.argv)
    widget = ImageWidget()
    widget.resize(250, 250)
    widget.setWindowTitle("This is the sample PYQT5 App")
    widget.show()
    sys.exit(application.exec_())


if __name__ == '__main__':
    main()