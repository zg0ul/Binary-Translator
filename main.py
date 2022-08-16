import sys
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication


class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("MainGUI.ui", self)
        self.BinaryToTextButton.clicked.connect(self.gotobinarytotext)
        self.TextToBinaryButton.clicked.connect(self.gototexttobinary)

    def gotobinarytotext(self): #goes to the Binary to text window
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gototexttobinary(self): #goes to the Text to binary window
        widget.setCurrentIndex(widget.currentIndex()+2)



class BinaryToText(QDialog):
    def __init__(self):
        super(BinaryToText, self).__init__()
        loadUi('BinaryToTextGUI.ui', self)
        self.TranslateButton.clicked.connect(self.Translate_Binary_to_Human)
        self.BackButton.clicked.connect(self.backbutton)

    def backbutton(self):
        widget.setCurrentIndex(widget.currentIndex()-1)
        self.OutputBox.setPlainText("")
        self.textEdit.setPlainText("")

    def Translate_Binary_to_Human(self):
        self.OutputBox.setStyleSheet("border-radius: \'10px\';\n"
                                     "background-color: rgb(54, 54, 54);\n"
                                     "color: \'lime\'")

        self.OutputBox.setPlainText("")
        binary = self.textEdit.toPlainText()
        Binary_lst = list(map(str, binary.split())) # to split each binary code for a letter in a seperate string inside a list.

        digit_place = 1 # starts at 1 so every digit after it is multiplied by 2 {1, 2, 4, 8, 16, 32, 64, 128}
        letter_count = 0 # Used to store the number representing a letter.
        final_text = ''

        for i in range(len(Binary_lst)): # How many strings in the list (one string represents a letter).

            for j in range(len(Binary_lst[i])): # for how manny zeros and ones in a single string.
            
                if len(Binary_lst[i]) % 8 == 0: # cheks if there are 8 zeros and ones inside a string.
            
                    if Binary_lst[i][::-1][j] == '1': #starts at the end of the string and checks if the number is 1 
                        letter_count += digit_place
                        digit_place *= 2

                    elif Binary_lst[i][::-1][j] == '0': #starts at the end of the string and checks if the number is 1 
                        digit_place *= 2

                    else:
                        self.OutputBox.setStyleSheet("border-radius: \'10px\';\n"
                                     "background-color: rgb(54, 54, 54);\n"
                                     "color: \'red\'")
                        final_text = "Error: Make sure you only type 0 or 1 in the binary code."
                        break


                else:
                    self.OutputBox.setStyleSheet("border-radius: \'10px\';\n"
                                     "background-color: rgb(54, 54, 54);\n"
                                     "color: \'red\'")
                    final_text = "Error: please make sure that the binary code is at least 8 digits or its multiples."
                    break

            final_text += chr(letter_count)
            letter_count = 0
            digit_place = 1

        
        self.OutputBox.setPlainText(final_text)



class TextToBinary(QDialog):
    def __init__(self):
        super(TextToBinary, self).__init__()
        loadUi('TextToBinaryGUI.ui', self)
        self.TranslateButton2.clicked.connect(self.Translate_Human_to_Binary)
        self.BackButton2.clicked.connect(self.goback)

    def goback(self):
        widget.setCurrentIndex(widget.currentIndex()-2)
        self.OutputBox2.setPlainText("")
        self.TextBox2.setPlainText("")

    def Translate_Human_to_Binary(self):
        string = self.TextBox2.toPlainText()

        letter_code = 0
        temp_bi = ''
        final_translated = ''

        for i in range(len(string)):
            letter_code = ord(string[i]) #ord returns the ascii code of a string for example A -> 65

            if letter_code >= 128:
                temp_bi += '1'
                letter_code -= 128
            else:
                temp_bi += '0'
            if letter_code >= 64:
                temp_bi += '1'
                letter_code -= 64
            else:
                temp_bi += '0'
            if letter_code >= 32:
                temp_bi += '1'
                letter_code -= 32
            else:
                temp_bi += '0'
            if letter_code >= 16:
                temp_bi += '1'
                letter_code -= 16
            else:
                temp_bi += '0'
            if letter_code >= 8:
                temp_bi += '1'
                letter_code -= 8
            else:
                temp_bi += '0'
            if letter_code >= 4:
                temp_bi += '1'
                letter_code -= 4
            else:
                temp_bi += '0'
            if letter_code >= 2:
                temp_bi += '1'
                letter_code -= 2
            else:
                temp_bi += '0'
            if letter_code >= 1:
                temp_bi += '1'
                letter_code -= 1
            else:
                temp_bi += '0'

            final_translated += temp_bi
            final_translated += ' '
            letter_code = 0
            temp_bi = ''

        self.OutputBox2.setPlainText(final_translated)
        

    




app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
mainwindow = MainWindow()
binarttotext = BinaryToText()
texttobinary = TextToBinary()
widget.addWidget(mainwindow)
widget.addWidget(binarttotext)
widget.addWidget(texttobinary)
widget.setFixedHeight(600)
widget.setFixedWidth(500)
widget.setWindowTitle(" Binary Translator ")
widget.setWindowIcon(QIcon('binary-code.png'))
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting")