###############################################
#           RhymeBot Application
#     Software to help break writer's block
#
#           TO-DO
#     • Create the labels to display what the purpose of the software is
#     • Fix the issue with the program crashing after searching twice
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
            # Creates an array to hold created labels
            self.created_label = []

            self.new_label = QLabel()
            # Sets value for number of added labels
            self.finishedAddingLabels = False
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
            self.cancelButton: QPushButton = self.buttonBox.addButton(QDialogButtonBox.Cancel)
            # Add them to the button box
            self.buttonBox.addButton(self.searchButton, QDialogButtonBox.ActionRole)
            # Connect buttons to form
            self.searchButton.clicked.connect(self.getRhymes)     # When search button is clicked
            self.cancelButton.clicked.connect(self.reject)  # When cancel button is clicked
            # Whenever the search button is clicked, do getRhymes
            self.buttonBox.accepted.connect(self.getRhymes)
            # creating a vertical layout
            mainLayout = QVBoxLayout()

            # Adding form group box to the layout
            mainLayout.addWidget(self.frame)
            # Adding button box to the layout
            mainLayout.addWidget(self.buttonBox)
            # Setting lay out
            self.setLayout(mainLayout)
      # Function to handle adding labels
      def addLabels(self, target_x, target_y):
            quantity = len(self.collected_rhymes)
            started = False
            for i in range(quantity):
                  if started == True and self.collected_rhymes[i][0:10] == "1 syllable":
                        break
                  rhyme_text = self.collected_rhymes[i]

                  label = QtWidgets.QLabel(self.frame)

                  # Safely extract syllable count substring
                  syllable = rhyme_text[0:2].strip()
                  try:
                        syllable_int = int(syllable)
                        if syllable_int == 1:
                              label.setText(rhyme_text[0:11])
                        elif syllable_int < 10:
                              label.setText(rhyme_text[0:12])
                        else:
                              label.setText(rhyme_text[0:13])
                  except ValueError:
                        label.setText(rhyme_text)

                  label.setGeometry(0, (50 + (10 * i)), len(label.text()) + 100, 50)
                  label.show()
                  self.created_label.append(label)
                  if started == False:
                        started = True
      def getRhymes(self):
            def showError(self, text):
                  msg = QMessageBox()
                  msg.setWindowTitle("Error")
                  msg.setText(text)
                  msg.setIcon(QMessageBox.Question)
                  msg.setStandardButtons(QMessageBox.Ok)
                  msg.setDefaultButton(QMessageBox.Ok)
                  x = msg.exec_()

            try:
                  if len(self.user_input.text()) == 0:
                        showError(self, "Please input a word")
                  else:
                        print("Chosen Word: {0}".format(self.user_input.text()))
                        rhymes = main.main(self.user_input.text())
                        if len(rhymes) != 0:
                              # Clear any existing labels
                              for label in self.created_label:
                                    label.deleteLater()
                              self.created_label.clear()

                              self.collected_rhymes = rhymes
                              self.addLabels(0, 50)
                        else:
                              showError(self, "No rhymes found")
            except Exception as e:
                  showError(self, "Something weird happened... Try again")
            

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


if __name__ == '__main__':
      # Instantiate our application
      app = QApplication(sys.argv)
      # Instantiate our window
      win = Window()
      # Show the window
      win.show()
      # Start the app
      sys.exit(app.exec())



#  def addLabels(self, target_x, target_y):
#             quantity = len(self.collected_rhymes)
#             started = False
#             print(f"Start: {self.finishedAddingLabels}")
#             for syllableAmount in range(quantity):
#                   # If for some reason, it combines "almost" rhymes with "perfect" rhymes on page, stop the for loop
#                   if started == True and self.collected_rhymes[syllableAmount][0:10] == "1 syllable":
#                         break
#                   # If you've already searched and search again, remove labels
#                   if self.finishedAddingLabels == True:
#                         for label in self.created_label:
#                               # print(label.parent())
#                               label.deleteLater()
#                               # print(f"Destroyed label: {label}")
#                         print("Finished Deleting labels")
#                         break
#                   else:
#                         print("Creating Labels...")
#                         label = QtWidgets.QLabel(self.frame)
#                         # If it's a 1 syllable
#                         if int(self.collected_rhymes[syllableAmount][0:2].strip()) == 1:
#                               label.setText(self.collected_rhymes[syllableAmount][0:11])
#                         # If it's any syllable > 1 but < 10
#                         elif int(self.collected_rhymes[syllableAmount][0:2].strip()) != 1 and int(self.collected_rhymes[syllableAmount][0:2].strip()) < 10:
#                               label.setText(self.collected_rhymes[syllableAmount][0:12])
#                         # If it's any syllable amount > 10
#                         elif int(self.collected_rhymes[syllableAmount][0:2].strip()) != 1 and int(self.collected_rhymes[syllableAmount][0:2].strip()) > 10:
#                               label.setText(self.collected_rhymes[syllableAmount][0:13])
#                         label.setGeometry(0, (50 + (10 * syllableAmount)), (len(label.text()) + 100), 50)
#                         label.show()
#                         self.created_label.append(label)
#                         if started == False:
#                               started = True
#             # If you've cleared all the labels, call the function again to add the new labels
#             if self.finishedAddingLabels == True:
#                   print("Telling the program you wanna add new labels")
#                   self.finishedAddingLabels = False
#                   print("Calling addLabels again...")
#                   self.addLabels(0,50)
#             else:
#                   print("You're done adding labels")
#                   self.finishedAddingLabels = not self.finishedAddingLabels