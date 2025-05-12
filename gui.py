###############################################
#           RhymeBot Application
#     Software to help break writer's block
#
#           TO-DO
#
##############################################


from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import main
import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class IntroWindow(QDialog):
    WIDTH = 500
    HEIGHT = 300
    def __init__(self):
        super(IntroWindow, self).__init__()
        self.setWindowTitle("LyricLink")
        self.setFixedSize(self.WIDTH, self.HEIGHT)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("lyriclink.ico")), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.setWindowIcon(icon)

        self.buttonBox = QDialogButtonBox()
        self.rhymesButton = QPushButton("Rhymes", self)
        self.rhymesButton.clicked.connect(self.goToRhymes)
        self.rhymesButton.setStyleSheet("background-color: #bfbfbf")
        self.synsButton = QPushButton("Synonyms/Antonyms", self)
        self.synsButton.clicked.connect(self.toSynonyms)
        self.synsButton.setStyleSheet("background-color: #bfbfbf")
        self.exitButton = QPushButton("Exit", self)
        self.exitButton.setStyleSheet("background-color: #bfbfbf")
        self.exitButton.clicked.connect(self.confirmExit)
        self.exitButton.setAutoDefault(False)
        self.buttonBox.addButton(self.rhymesButton, QDialogButtonBox.ActionRole)
        self.buttonBox.addButton(self.exitButton, QDialogButtonBox.ActionRole)
        self.buttonBox.addButton(self.synsButton, QDialogButtonBox.ActionRole)

        pixmap = QtGui.QPixmap(resource_path("lyriclink.png")).scaled(300,300)
        self.title_image = QLabel()
        self.title_image.setPixmap(pixmap)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.title_image)
        mainLayout.addWidget(self.buttonBox)
        mainLayout.setAlignment(self.buttonBox, Qt.AlignCenter)
        mainLayout.setAlignment(self.title_image, Qt.AlignCenter)

        self.setStyleSheet("background-color: #8c8c8c")

        self.setLayout(mainLayout)
    # To go to the section for rhymes
    def goToRhymes(self):
         self.w = RhymeWindow()
         self.w.show()
         self.hide()
    # To go to the section for synonyms/antonyms
    def toSynonyms(self):
         self.w = Synonyms()
         self.w.show()
         self.hide()
         
    def confirmExit(self):
        msg = QMessageBox()
        msg.setWindowTitle("Confirmation")
        msg.setText("Are you sure you want to exit?")
        msg.setIcon(QMessageBox.Question)
        no = msg.addButton(
        'No', QtWidgets.QMessageBox.AcceptRole)
        yes = msg.addButton(
        'Yes', QtWidgets.QMessageBox.RejectRole)
        msg.setDefaultButton(yes)
        msg.exec_()
        msg.deleteLater()

        if msg.clickedButton() is yes:
             print("made it")
             self.close()

class Synonyms(QDialog):
    WIDTH = 900
    HEIGHT = 700

    collected_syns = []
    collected_ants = []

    def __init__(self):
                super(Synonyms, self).__init__()
                self.setWindowTitle("LyricLink: Synonyms/Antonyms")
                self.setFixedSize(self.WIDTH, self.HEIGHT)

                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(resource_path("lyriclink.ico")), QtGui.QIcon.Selected, QtGui.QIcon.On)
                self.setWindowIcon(icon)

                # Scroll Area Setup
                self.scroll_area = QScrollArea()
                self.scroll_area.setWidgetResizable(True)
                # Content widget inside the scroll area
                self.scroll_widget = QWidget()
                self.scroll_layout = QVBoxLayout(self.scroll_widget)
                self.scroll_layout.setAlignment(Qt.AlignTop)
                self.scroll_layout.setSpacing(8)  # Reduced spacing

                self.scroll_area.setWidget(self.scroll_widget)

                self.buttonBox = QDialogButtonBox()
                self.backButton: QPushButton = QPushButton("Back")
                self.exitButton = QPushButton("Exit", self)
                self.exitButton.clicked.connect(self.confirmExit)
                self.exitButton.setAutoDefault(False)
                self.buttonBox.addButton(self.backButton, QDialogButtonBox.ActionRole)
                self.buttonBox.addButton(self.exitButton, QDialogButtonBox.ActionRole)

                self.backButton.clicked.connect(self.goToIntro)
                self.backButton.setAutoDefault(False)

                # Layout
                mainLayout = QVBoxLayout()
                mainLayout.addWidget(self.buttonBox)
                self.setLayout(mainLayout)
    def goToIntro(self):
         self.w = IntroWindow()
         self.w.show()
         self.hide()

    def confirmExit(self):
        msg = QMessageBox()
        msg.setWindowTitle("Confirmation")
        msg.setText("Are you sure you want to exit?")
        msg.setIcon(QMessageBox.Question)
        no = msg.addButton(
        'No', QtWidgets.QMessageBox.AcceptRole)
        yes = msg.addButton(
        'Yes', QtWidgets.QMessageBox.RejectRole)
        msg.setDefaultButton(yes)
        msg.exec_()
        msg.deleteLater()

        if msg.clickedButton() is yes:
             self.close()
    
     

class RhymeWindow(QDialog):
    WIDTH = 1000
    HEIGHT = 1000

    collected_rhymes = []
    
    def __init__(self):
        super(RhymeWindow, self).__init__()
        self.created_label = []
        self.setWindowTitle("LyricLink: Rhymes")
        self.setFixedSize(self.WIDTH, self.HEIGHT)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("lyriclink.ico")), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.setWindowIcon(icon)

        # Scroll Area Setup
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        # Content widget inside the scroll area
        self.scroll_widget = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_widget)
        self.scroll_layout.setAlignment(Qt.AlignTop)
        self.scroll_layout.setSpacing(8)  # Reduced spacing

        self.scroll_area.setWidget(self.scroll_widget)

        # Input setup
        self.user_input = QLineEdit()
        self.user_input.setMinimumWidth(10)
        self.user_input.setMaximumWidth(50)

        self.createForm()

        # Buttons
        self.buttonBox = QDialogButtonBox()
        self.searchButton: QPushButton = QPushButton("Search")
        self.backButton: QPushButton = QPushButton("Back")
        self.exitButton = QPushButton("Exit", self)
        self.exitButton.clicked.connect(self.confirmExit)
        self.exitButton.setAutoDefault(False)
        self.buttonBox.addButton(self.searchButton, QDialogButtonBox.ActionRole)
        self.buttonBox.addButton(self.backButton, QDialogButtonBox.ActionRole)
        self.buttonBox.addButton(self.exitButton, QDialogButtonBox.ActionRole)

        self.searchButton.clicked.connect(self.getRhymes)
        self.backButton.clicked.connect(self.goToIntro)
        self.backButton.setAutoDefault(False)
        self.buttonBox.accepted.connect(self.getRhymes)
        self.searchButton.setDefault(True)

        # Layout
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.frame)
        mainLayout.addWidget(self.scroll_area)
        mainLayout.addWidget(self.buttonBox)
        self.setLayout(mainLayout)

    def goToIntro(self):
         self.w = IntroWindow()
         self.w.show()
         self.hide()

    def addLabels(self):
      quantity = len(self.collected_rhymes)
      previous_syllable_count = None

      current_group = []
      current_count = None

      def add_group_to_layout(syllable_count, group):
            if not group:
                  return
            header = QLabel(f"{syllable_count} syllable{'s' if syllable_count != 1 else ''}")
            header.setStyleSheet("font-weight: bold; font-size: 14px; margin-bottom: 0px;")  # Reduced margin
            self.scroll_layout.addWidget(header)
            self.created_label.append(header)

            for item in group:
                  # Remove the syllable count from the rhyme label
                  parts = item.split()
                  word_only = ' '.join(parts[2:]) if len(parts) > 1 else item

                  label = QLabel(word_only)
                  label.setWordWrap(True)

                  self.scroll_layout.addWidget(label)
                  self.created_label.append(label)


      for i in range(quantity):
            rhyme_text = self.collected_rhymes[i]

            try:
                  current_syllable_count = int(rhyme_text.split()[0])
            except (ValueError, IndexError):
                  continue

            if previous_syllable_count is not None and current_syllable_count < previous_syllable_count:
                  #print(f"Stopping: {current_syllable_count} < {previous_syllable_count}")
                  break

            # Fix missing space after colon
            if ":" in rhyme_text and not rhyme_text[rhyme_text.index(":") + 1] == " ":
                  rhyme_text = rhyme_text.replace(":", ": ")

            if current_count is None:
                  current_count = current_syllable_count

            if current_syllable_count != current_count:
                  add_group_to_layout(current_count, current_group)
                  current_group = []
                  current_count = current_syllable_count

            current_group.append(rhyme_text)
            previous_syllable_count = current_syllable_count

      add_group_to_layout(current_count, current_group)

      # Ensure the layout has minimal spacing
      self.scroll_layout.setSpacing(4)  # Reduced overall spacing between widgets

    def getRhymes(self):
        def showError(text):
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText(text)
            msg.setIcon(QMessageBox.Question)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.exec_()

        try:
            if len(self.user_input.text()) == 0:
                showError("Please input a word")
            else:
                # print("Chosen Word: {0}".format(self.user_input.text()))
                rhymes = main.scrapeRhymes(self.user_input.text())
                if len(rhymes) != 0:
                    for label in self.created_label:
                        label.deleteLater()
                    self.created_label.clear()
                    for i in reversed(range(self.scroll_layout.count())):
                        item = self.scroll_layout.itemAt(i)
                        if item.widget():
                            item.widget().deleteLater()
                        elif item.spacerItem():
                            self.scroll_layout.removeItem(item)

                    self.collected_rhymes = rhymes
                    self.addLabels()
                else:
                    showError("No rhymes found")
        except Exception as e:
            showError("Something weird happened... Try again")

    def createForm(self):
        layout = QGridLayout()

        # Purpose label
        purpose_label = QLabel("LyricLink helps you find rhymes to overcome writer's block.")
        purpose_label.setAlignment(Qt.AlignCenter)
        purpose_label.setStyleSheet("font-size: 16px; font-weight: bold; margin-bottom: 10px;")
        layout.addWidget(purpose_label, 0, 2, Qt.AlignCenter)
        layout.addWidget(QLabel("Enter your word below"), 1, 2, Qt.AlignCenter)
        layout.addWidget(self.user_input, 2, 2, Qt.AlignCenter)

        # layout.addRow(QLabel("Enter your word here: "), self.user_input)
        

        self.frame = QFrame()
        self.frame.setLayout(layout)

    def confirmExit(self):
        msg = QMessageBox()
        msg.setWindowTitle("Confirmation")
        msg.setText("Are you sure you want to exit?")
        msg.setIcon(QMessageBox.Question)
        no = msg.addButton(
        'No', QtWidgets.QMessageBox.AcceptRole)
        yes = msg.addButton(
        'Yes', QtWidgets.QMessageBox.RejectRole)
        msg.setDefaultButton(yes)
        msg.exec_()
        msg.deleteLater()

        if msg.clickedButton() is yes:
             self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # win = RhymeWindow()
    win = IntroWindow()
    win.show()
    sys.exit(app.exec())