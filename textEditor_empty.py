from __future__ import print_function
from PySide.QtGui import *
from PySide.QtCore import *
import sys


class TextEditor(QMainWindow):
    """Text editor"""
    def __init__(self):
        super(TextEditor, self).__init__()
        self.initGUI()

    def initGUI(self):
        self.setWindowTitle("TextEditor")
        self.setGeometry(300, 300, 300, 300)
        self.setupComponents()
        self.show()

    def setupComponents(self):
        """Setting the central widget
        """
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

if __name__ == '__main__':
    try:
        myApp = QApplication(sys.argv)
        editor = TextEditor()
        # editor.show()
        QCoreApplication.processEvents()
        myApp.exec_()
        sys.exit(0)
    except NameError:
        print("NameError: ", sys.exc_info()[1])
    except SystemExit:
        print("Closing window...")
    except Exception:
        print(sys.exc_info()[1])
