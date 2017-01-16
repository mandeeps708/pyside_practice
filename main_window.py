# Import required modules
import sys
import time
from PySide.QtGui import QMainWindow, QApplication, QStatusBar, QProgressBar, QLabel
from PySide.QtCore import QCoreApplication

# Our main window class
class MainWindow(QMainWindow):
    # constructor
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initGUI()

    def initGUI(self):
        self.setWindowTitle("This is Main Window")
        self.setGeometry(300, 250, 400, 300)
        self.show()

    def createProgressBar(self):
        self.progressBar = QProgressBar()
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(100)

    def createStatusBar(self):
        """Function to create status bar
        """
        self.createProgressBar()
        self.myStatusBar = QStatusBar()
        self.statusLabel = QLabel()
        # self.myStatusBar.showMessage('Ready', 2000)
        self.myStatusBar.addWidget(self.statusLabel, 1)
        self.myStatusBar.addWidget(self.progressBar, 2)
        self.setStatusBar(self.myStatusBar)

    def showProgress(self, progress):
        """ function to show progress
        """
        if progress == 100:
            self.statusLabel.setText('Ready')
            self.progressBar.setValue(100)
            return
        else:
            print("yeah!!")
            self.progressBar.setValue(progress)
            return

if __name__ == '__main__':
    try:
        myApp = QApplication(sys.argv)
        mainWindow = MainWindow()
        mainWindow.createStatusBar()
        mainWindow.show()
        mainWindow.showProgress(0)
        # mainWindow.showProgress(100)
        QCoreApplication.processEvents()
        time.sleep(1)
        print("ho")
        mainWindow.showProgress(50)
        time.sleep(3)
        mainWindow.showProgress(100)
        myApp.exec_()
        sys.exit(0)
    except NameError:
        print("NameError:", sys.exc_info()[1])
    except SystemExit:
        print("Closing Window...")
    except Exception:
        print(sys.exc_info()[1])
