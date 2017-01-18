from PySide.QtCore import *
from PySide.QtGui import *
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
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.myStatusBar = QStatusBar()
        self.setStatusBar(self.myStatusBar)
        self.myStatusBar.showMessage('Ready', 10000)
        self.CreateActions()
        self.CreateMenus()
        self.fileMenu.addAction(self.newAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAction)
        self.editMenu.addAction(self.copyAction)
        self.fileMenu.addSeparator()
        self.editMenu.addAction(self.pasteAction)
        self.helpMenu.addAction(self.aboutAction)

    def newFile(self):
        self.textEdit.setText('')

    def exitFile(self):
        self.close()

    def aboutHelp(self):
        QMessageBox.about(self, "About Simple Text Editor",
                          "This example demosntrates the use of Menu bar")

    def CreateActions(self):
        """Function to create actions for menus
        """
        self.newAction = QAction(QIcon('icon.png'), '&New',
                                 self, shortcut=QKeySequence.New,
                                 statusTip="Create a New File",
                                 triggered=self.newFile)
        self.exitAction = QAction(QIcon('icon.png'), '&Exit',
                                  self, shortcut="Ctrl+Q",
                                  statusTip="Exit the Application",
                                  triggered=self.exitFile)
        self.copyAction = QAction(QIcon('icon.png'), '&Copy',
                                  self, shortcut="Ctrl+C",
                                  statusTip="Copy",
                                  triggered=self.textEdit.copy)
        self.pasteAction = QAction(QIcon('icon.png'), '&Paste',
                                   self, shortcut="Ctrl+V",
                                   statusTip="Paste",
                                   triggered=self.textEdit.paste)
        self.aboutAction = QAction(QIcon('icon.png'), '&About',
                                   self, statusTip="Displays info about editor",
                                   triggered=self.aboutHelp)

    # Actual menu bar item creation
    def CreateMenus(self):
        """ Function to create actual menu bar
        """
        self.fileMenu = self.menuBar().addMenu("&File")
        self.editMenu = self.menuBar().addMenu("&Edit")
        self.helpMenu = self.menuBar().addMenu("&Help")


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
