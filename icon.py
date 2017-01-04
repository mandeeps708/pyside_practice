# Import required modules
import sys, time
from PySide.QtGui import *
from PySide.QtCore import *
from PySide.QtGui import QApplication, QWidget, QIcon
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

        appIcon = QIcon("icon.png")
        self.setWindowIcon(appIcon)
        print("Sample Window show in the GUI\n")
        self.setIconModes()
        self.show()

    def setIconModes(self):
        myIcon1 = QIcon('icon.png')
        myLabel1 = QLabel('sample', self)
        pixmap1 = myIcon1.pixmap(60, 60, QIcon.Active, QIcon.On)
        myLabel1.setPixmap(pixmap1)
        myLabel1.show()
        myIcon2 = QIcon('icon.png')
        myLabel2 = QLabel('sample', self)
        pixmap2 = myIcon2.pixmap(60, 60, QIcon.Disabled, QIcon.Off)
        myLabel2.setPixmap(pixmap2)
        myLabel2.move(70, 0)
        myLabel2.show()
        myIcon3 = QIcon('icon.png')
        myLabel3 = QLabel('sample', self)
        pixmap3 = myIcon3.pixmap(60, 60, QIcon.Selected, QIcon.On)
        myLabel3.setPixmap(pixmap3)
        myLabel3.move(140, 0)
        myLabel3.show()

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
