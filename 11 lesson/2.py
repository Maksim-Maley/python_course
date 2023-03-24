import sys
from PyQt5.QtWidgets import *
if __name__ == "__main__":
    app = QApplication([])
    w = QWidget()
    w.setWindowTitle("QboxLayout")
    btn1 = QPushButton("Bird")
    btn2 = QPushButton("Animal")
    btn3 = QPushButton("Fish")

    hbox = QVBoxLayout(w)

    hbox.addWidget(btn1)
    hbox.addWidget(btn2)
    hbox.addWidget(btn3)

    w.show()
    sys.exit(app.exec_())