import sys
import random
from functools import partial
from types import new_class
from numpy import number
from sudoku import Sudoku
from PySide2.QtWidgets import *
from main_window import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.menu_new.triggered.connect(self.new_game)
        self.ui.menu_Openfile.triggered.connect(self.open_file)
        self.line_edits = [[None for i in range(9)] for j in range(9)]

        for i in range(9):
            for j in range(9):
                new_cell = QLineEdit()
                self.ui.grid_layout.addWidget(new_cell,i,j)
                new_cell.textChanged.connect(partial(self.validation,i,j))
                self.line_edits[i][j] = new_cell

        self.new_game()        

    def new_game(self):
        puzzle = Sudoku(3,seed=random.randint(1, 1000)).difficulty(0.5)
        self.show_board(puzzle.board)

    def open_file(self):
        file_path = QFileDialog.getOpenFileName(self,"Open file...")[0]
        print(file_path)
        f = open(file_path,"r")
        big_text = f.read()
        rows = big_text.split("\n")
        puzzle_board = [[None for i in range(9)] for j in range(9)]
        for i in range(len(rows)):
            cells = rows[i].split(" ")
            for j in range(len(cells)):
                puzzle_board[i][j] = int(cells[j])

        self.show_board(puzzle_board)
    
    def show_board(self,puzzle_board):
        for i in range(9):
            for j in range(9):
                self.line_edits[i][j].setReadOnly(False)
                if puzzle_board[i][j] != None:
                    self.line_edits[i][j].setText(str(puzzle_board[i][j]))
                    self.line_edits[i][j].setStyleSheet('color: rgb(255, 0, 0);')
                    self.line_edits[i][j].setReadOnly(True)
                else:
                    self.line_edits[i][j].setText("")

    def validation(self,i,j,text):
        if text not in ["1","2","3","4","5","6","7","8","9"]:
            self.line_edits[i][j].setText(None)
        self.check()

    def check(self):
        for s in range(9):
            for j in range(9):
                for i in range(9):
                    number1 = self.line_edits[s][j].text()
                    number2 = self.line_edits[s][i].text()
                    if number1 == number2 and number1 != "" and number2 != "" and j != i:
                        print("sf")
                        break

                    number1 = self.line_edits[j][s].text()
                    number2 = self.line_edits[i][s].text()
                    if number1 == number2 and number1 != "" and number2 != "" and j != i:
                        print("sfg")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec_()