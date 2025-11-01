from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, QTimer, QCoreApplication
from PyQt5.QtWidgets import QMainWindow, QApplication
from frontend import Ui_MainWindow


class Timer(QMainWindow):
    def __init__(self, max):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.maxmin = max
        self.s = 0
        self.min = 0
        self.angle1 = 0.999
        self.angle2 = 1.000

        self.ui.start.clicked.connect(self.start)
        self.ui.pause.clicked.connect(self.pause)
        self.ui.reset.clicked.connect(self.reset)

    def start(self):
        self.timer = QTimer()
        self.timer.start(1000)
        self.timer.timeout.connect(self.secinc)

    def pause(self):
        self.timer.stop()

    def reset(self):
        self.s = 0
        self.min = 0
        self.ui.label.setText(QCoreApplication.translate("Ui_MainWindow", "00:00"))
        self.angle1 = 0.999
        self.angle2 = 1.000
        self.ui.progress.setStyleSheet("QFrame{\n"
                                       "    border-radius: 150px;\n"
                                       "    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:" + str(self.angle1) + " rgba(255, 0, 127, 0), stop:" + str(self.angle2) + " rgba(85, 170, 255, 255));\n"
                                        "}")

    def secinc(self):
        if self.min == self.maxmin:
            self.pause()
        else:
            self.angle1 -= (10 / 900)
            self.angle2 -= (10 / 900)
            if self.min < self.maxmin/3:
                self.ui.progress.setStyleSheet("QFrame{\n"
                                               "    border-radius: 150px;\n"
                                               "    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:" + str(self.angle1) + " rgba(255, 0, 127, 0), stop:" + str(self.angle2) + " rgba(85, 170, 255, 255));\n"
                                                                                       "}")
            elif self.min < (self.maxmin/3)*2:
                self.ui.progress.setStyleSheet("QFrame{\n"
                                               "    border-radius: 150px;\n"
                                               "    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:" + str(self.angle1) + " rgba(255, 0, 127, 0), stop:" + str(self.angle2) + " rgba(0, 255, 150, 255));\n"
                                                                                       "}")
            elif self.min > (self.maxmin/3)*2:
                self.ui.progress.setStyleSheet("QFrame{\n"
                                               "    border-radius: 150px;\n"
                                               "    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:" + str(self.angle1) + " rgba(255, 0, 127, 0), stop:" + str(self.angle2) + " rgba(255, 0, 0, 255));\n"
                                                                                       "}")

            self.s += 10
            if self.s == 60:
                self.s = 0
                self.min += 1
            if self.s < 10:
                if self.min < 10:
                    self.ui.label.setText(QCoreApplication.translate("Ui_MainWindow", "0" + str(self.min) + ":0" + str(self.s)))
                else:
                    self.ui.label.setText(QCoreApplication.translate("Ui_MainWindow", str(self.min) + ":0" + str(self.s)))
            else:
                if self.min < 10:
                    self.ui.label.setText(
                        QCoreApplication.translate("Ui_MainWindow", "0" + str(self.min) + ":" + str(self.s)))
                else:
                    self.ui.label.setText(QCoreApplication.translate("Ui_MainWindow", str(self.min) + ":" + str(self.s)))


if __name__ == "__main__":
    import sys
    m = int(input('Enter Time in minutes '))
    app = QtWidgets.QApplication(sys.argv)
    Timer = Timer(m)
    Timer.show()
    sys.exit(app.exec_())
