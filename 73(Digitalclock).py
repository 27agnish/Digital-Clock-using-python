import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTime, QTimer, Qt
from PyQt5.QtGui import QFont, QFontDatabase
class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.timer=QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(600,400,300,100)
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("font-size: 150px;"
                                      "color: #39fc03;")
        self.setStyleSheet("background-color: black;")
        #custom font
        font_id = QFontDatabase.addApplicationFont("path or relative path of DS-DIGIT.TTF")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family, 150)
        self.time_label.setFont(my_font)

        self.timer.timeout.connect(self.update_clock)
        self.timer.start(1) #refresh in 1 ms

        self.update_clock()
    def update_clock(self): 
        current_time = QTime.currentTime().toString("hh:mm:ss:AP")
        self.time_label.setText(current_time)

def main():
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()            
