import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPalette
if __name__ == "__main__":
    app = QApplication([])
    app.setStyle("Fusion")

    qp = QPalette()
    qp.setColor(QPalette.ButtonText, Qt.red)
    qp.setColor(QPalette.Window, Qt.black)
    app.setPalette(qp)

    w = QWidget()
    grid = QGridLayout(w)

    for i in range(3):
        for j in range(3):
            grid.addWidget(QPushButton("button"),i,j)
    w.show()
    sys.exit(app.exec_())