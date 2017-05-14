from PySide import QtGui
from PySide import QtCore
from PySide import QtUiTools

class MyWidget(QtGui.QMainWindow):
    def __init__(self):
        apply(QtGui.QMainWindow.__init__, (self,))

        loader = QtUiTools.QUiLoader()
        file = QtCore.QFile("tablu.ui")
        file.open(QtCore.QFile.ReadOnly)
        self.myWidget = loader.load(file, self)
        file.close()

        self.setCentralWidget(self.myWidget)
        # QtCore.QObject.connect(self.myWidget.calculateButton, QtCore.SIGNAL("clicked()"), self.accept)
        self.accept()

    def accept(self):
        data1 = ['a1', 'a2', 'a3', 'a4']
        data2 = ['b1', 'b2', 'b3', 'b4']
        # for i in range(len(data1)):
        """
        # Using QTableWidget
        self.myWidget.tablu.insertRow(i)
        item = QtGui.QTableWidgetItem(data1[i])
        self.myWidget.tablu.setItem(i, 0, item)
        # item2 = QtGui.QTableWidgetItem(data2[i])
        # self.myWidget.tablu.setItem(i, 1, item2)
        """
        # Using QListWidget
        for i in range(len(data1)):
            self.myWidget.tablu.addItem(data1[i])
        """
        v1 = int(self.myWidget.val1.text())
        v2 = int(self.myWidget.val2.text())
        v1 = 1
        v2 = 4
        print("Sum of "+str(v1)+" and "+str(v2)+": "+str(v1+v2))
        """

if __name__ == '__main__':
    import sys
    import os
    print("Running in " + os.getcwd() + " .\n")

    app = QtGui.QApplication(sys.argv)

    win = MyWidget()
    win.show()

    app.connect(app, QtCore.SIGNAL("lastWindowClosed()"), app, QtCore.SLOT("quit()"))
    app.exec_()
