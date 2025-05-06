###############################################
#           RhymeBot Application
#     Software to help break writer's block
#
#           TO-DO
#     • Create the labels to display what the purpose of the software is
#     • Create function that determines how many labels to add based on length of collected_rhymes, adds the labels to self.frame.
#       Beyond the first label, change the wording to reflect pluraity: "1 syllable" vs "2 syllables"
#
##############################################


from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import main
import sys

class Window(QDialog):
      WIDTH = 1000
      HEIGHT = 1000

      collected_rhymes = []
      def __init__(self):
            super(Window, self).__init__()
            # Creates the initial state
            self.new_label = None
            # Set Window Title
            self.setWindowTitle("RhymeBot")
            # Set size
            self.setFixedSize(self.WIDTH,self.HEIGHT)
            # Creates the window icon
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("assets/rhymebot_logo.ico"), QtGui.QIcon.Selected, QtGui.QIcon.On)
            # Sets the window icon
            self.setWindowIcon(icon)
            # Create a group box to house all of the components
            self.frame = QFrame()
            # Create an area for the user input
            self.user_input = QLineEdit()
            self.user_input.textChanged.connect(self.handleTextChange)
            self.user_input.setMinimumWidth(10)
            self.user_input.setMaximumWidth(50)
            # Function that builds the form
            self.createForm()
            # Create the box to hold the buttons
            self.buttonBox = QDialogButtonBox()

            #DEBUG BUTTON
            self.debugButton: QPushButton = QPushButton("Debug")
            self.buttonBox.addButton(self.debugButton, QDialogButtonBox.ActionRole)
            self.debugButton.clicked.connect(self.debug)

            # Create the buttons
            self.searchButton: QPushButton = QPushButton("Search")
            self.clearButton: QPushButton = QPushButton("Clear")
            self.cancelButton: QPushButton = self.buttonBox.addButton(QDialogButtonBox.Cancel)
            # Add them to the button box
            self.buttonBox.addButton(self.searchButton, QDialogButtonBox.ActionRole)
            self.buttonBox.addButton(self.clearButton, QDialogButtonBox.ActionRole)
            # Connect buttons to form
            self.searchButton.clicked.connect(self.getRhymes)     # When search button is clicked
            self.cancelButton.clicked.connect(self.reject)  # When cancel button is clicked
            self.clearButton.clicked.connect(self.clearText)
            # Whenever the search button is clicked, do getRhymes
            self.buttonBox.accepted.connect(self.getRhymes)
            # creating a vertical layout
            mainLayout = QVBoxLayout()

            # adding form group box to the layout
            mainLayout.addWidget(self.frame)
            # adding button box to the layout
            mainLayout.addWidget(self.buttonBox)
            # setting lay out
            self.setLayout(mainLayout)
      def addLabel(self, target_x, target_y):
            if not self.new_label:
                  self.new_label = QtWidgets.QLabel(self.frame)
                  self.new_label.setText("New Label created")
                  self.new_label.setGeometry(target_x,target_y, len(self.new_label.text()) * 3, 50)
                  self.new_label.show()
            else:
                  self.new_label.clear()
                  self.new_label.setText("Updated label")
                  self.new_label.setGeometry(target_x,target_y, 70, 50)
      def getRhymes(self):
            if len(self.user_input.text()) == 0:
                  print("Error: No word chosen. Please input a word")
                  return
            # Print the chosen word
            else:
                  print("Chosen Word: {0}".format(self.user_input.text()))
                  # Sets the rhymes returned by the webscrape to the colleted_rhymes array
                  if len(main.main(self.user_input.text())) != 0:
                        self.collected_rhymes = main.main(self.user_input.text())
                  else:
                        print("Error: No rhymes found")

            self.addLabel(0, 50)
      def clearText(self):
            # Clears the user_input field
            self.user_input.clear()
            self.user_input.text = " "
      def createForm(self):
            # Create form layout
            layout = QFormLayout()
            #Adds row for user input
            layout.addRow(QLabel("Enter your word here: "), self.user_input)
            # Setting the layout
            self.frame.setLayout(layout)
      def handleTextChange(self):
            user_input = self.user_input
      def debug(self):
            print("User Input: ", self.user_input.text())

# def window():
#     win.setFixedSize(WIDTH,HEIGHT)
#     win.setWindowTitle("RhymeBot")
#     center(win)
#     main_screen_labels(win)
#     print("Chosen Word: ", chosen_word)
#     main.main(chosen_word)
#     win.show()
#     sys.exit(app.exec_())

# def main_screen_labels(window):
#       title = QtWidgets.QLabel(window)
#       title.setGeometry(0,0,240,500)
#       title.setStyleSheet("QLabel{font-size: 13pt;}")
#       title.setText("Rhyme Bot")
#       title.setAlignment(Qt.AlignCenter)
#       title.move(( 1000 - title.width() ) // 2, -150)

#       desc = QtWidgets.QLabel(window)
#       desc.setGeometry(0,0,200,200)
#       desc.setStyleSheet("QLabel{font-size: 8pt;}")
#       desc.setText("Software to help break writer's block")
#       desc.setAlignment(Qt.AlignCenter)
#       desc.move(( 1000 - desc.width() ) // 2, 20)

      
#       window.addRow(QtWidgets.QLabel("Choose Word: "), user_input)



if __name__ == '__main__':
      # Instantiate our application
      app = QApplication(sys.argv)
      # Instantiate our window
      win = Window()
      # Show the window
      win.show()
      # Start the app
      sys.exit(app.exec())