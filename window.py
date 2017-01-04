# Import required modules
import sys, time
from PySide.QtGui import *
from PySide.QtCore import *
# Our main window class


class SampleWindow(QWidget):
    # Constructor function
    def __init__(self):
        super(SampleWindow, self).__init__()
        self.initGUI()

    def initGUI(self):
        self.setWindowTitle("Sample Window")
        self.setGeometry(600, 600, 700, 150)
        self.setMinimumHeight(100)
        self.setMinimumWidth(250)
        self.setMaximumHeight(200)
        self.setMaximumWidth(800)
        self.show()
        print("Sample Window show in the GUI\n")
if __name__ == '__main__':
    # Exception Handling
    try:
        myApp = QApplication(sys.argv)
        myWindow = SampleWindow()
        QCoreApplication.processEvents()
        time.sleep(3)
        myWindow.resize(300, 300)
        myWindow.setWindowTitle("Sample Window Resized")
        myWindow.repaint()
        myApp.exec_()
        sys.exit(0)
    except NameError:
        print("Name Error:", sys.exc_info()[1])
    except SystemExit:
        print("Closing Window...")
    except Exception:
        print (sys.exc_info()[1])
