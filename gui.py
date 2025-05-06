from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QInputDialog
from PyQt5.QtCore import Qt
import main
import pyautogui
import sys

from qtpy import QT5

app = QApplication(sys.argv)
win = QMainWindow()
chosen_word = ""

def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())



def prompt():
      text, ok = QInputDialog.getText(None, "RhymeBot", "Please enter your word here")
      global chosen_word
      chosen_word = text
      

def window():
    WIDTH = 1000
    HEIGHT = 1000
    win.setFixedSize(WIDTH,HEIGHT)
    win.setWindowTitle("RhymeBot")
    center(win)
    main_screen_labels(win)
    print("Chosen Word: ", chosen_word)
    main.main(chosen_word)
    win.show()
    sys.exit(app.exec_())

def main_screen_labels(window):
      title = QtWidgets.QLabel(window)
      title.setGeometry(0,0,240,500)
      title.setStyleSheet("QLabel{font-size: 13pt;}")
      title.setText("Rhyme Bot")
      title.setAlignment(Qt.AlignCenter)
      title.move(( 1000 - title.width() ) // 2, -150)

      desc = QtWidgets.QLabel(window)
      desc.setGeometry(0,0,200,200)
      desc.setStyleSheet("QLabel{font-size: 8pt;}")
      desc.setText("Software to help break writer's block")
      desc.setAlignment(Qt.AlignCenter)
      desc.move(( 1000 - desc.width() ) // 2, 20)

prompt()
window()