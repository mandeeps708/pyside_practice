# Import required modules
import sys, time
from PySide.QtGui import *
from PySide.QtCore import *
import ipdb
import os
# Our main window class


class personal(QWidget):
    """My class ;-)
    """
    def __init__(self):
        super(personal, self).__init__()
        self.initGUI()
        self.mandeep()
        self.launch_button()

    def initGUI(self):
        # self.setWindowTitle("Personal")
        # self.setGeometry(0, 0, 400, 200)
        self.show()

    def mandeep(self):
        """wow my function.
        """
        my_icon = QIcon("icon.png")
        myLabel = QLabel('sample', self)
        pixmap1 = my_icon.pixmap(60, 60, QIcon.Active, QIcon.On)
        myLabel.setPixmap(pixmap1)
        myLabel.show()

    def launch(self):
        """launch the rockets!
        """
        os.system("chromium-browser google.com")
        os.system("xbacklight -set 10")

    def launch_button(self):
        my_button = QPushButton('Launch', self)
        my_button.move(50, 100)
        my_button.show()
        my_button.clicked.connect(self.launch)

if __name__ == '__main__':
    try:
        myApp = QApplication(sys.argv)
        mywindow = personal()
        QCoreApplication.processEvents()
        myApp.exec_()
        sys.exit(0)

    except NameError:
        print("Name Error:", sys.exc_info()[1])
    except SystemExit:
        print("Closing Window...")
    except Exception:
        print(sys.exc_info()[1])
