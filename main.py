from pdb import line_prefix
import sys
import random
from functools import partial
from sudoku import Sudoku
from PySide2.QtWidgets import *
from main_window import Ui_window

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_window()
        self.ui.setupUi(self)
        self.ui.menu_new.triggered.connect(self.new_game)
        self.ui.menu_Openfile.triggered.connect(self.open_file)
        self.ui.menuAbout.triggered.connect(self.About)
        self.ui.menuexit_2.triggered.connect(self.Exit)
        self.ui.menuHelp.triggered.connect(self.Help)
        self.ui.menuSolve.triggered.connect(self.Solve)
        self.line_edits = [[None for i in range(9)] for j in range(9)]
        self.btn_dark_mode = QPushButton()
        self.btn_dark_mode.setText("Dark mode")
        self.btn_dark_mode.setMaximumHeight(50)
        self.btn_dark_mode.setMaximumWidth(80)
        self.btn_dark_mode.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.ui.menu.addWidget(self.btn_dark_mode)
        self.btn_dark_mode.clicked.connect(self.Dark_mode)
        self.d_l = 1
        self.new_board()
        self.new_game()   
        self.Dark_mode()     

    def Exit(self):
        msg_box = QMessageBox()
        msg_box.setText("Do you want to exit the game?")
        msg_box.exec_()
        exit(0)

    def Help(self):
        msg_box = QMessageBox()
        msg_box.setText("To win this game... \n You have to fill the empty houses with numbers 1 to 9 so that there is no part of that number in each square of 9, and none of the numbers in the horizontal and vertical columns of that house are equal.")
        msg_box.exec_()
        msg_box = QMessageBox()
        msg_box.setText("برای بردن این بازی ...\nباید خانه های خالی را با اعداد 1 تا 9 به طوری پر کنید تا در هر مربع 9 قسمتی از آن عدد نباشد و هیچ کدام از اعداد ستون های افقی و عمودی آن خانه با هم برابر نباشند.")
        msg_box.exec_()

    def About(self):
        msg_box = QMessageBox()
        msg_box.setText("sudoku \n To view the rules of the game, select Help from the menu section \n And about me...")
        msg_box.exec_()
        msg_box = QMessageBox()
        msg_box.setText("i am kiya key nia \n my Email address: kiyakeynia@gmain.com \n my Github address: https://githhub.com/kiyakeynia8")
        msg_box.exec_()

    def Solve(self):
        solution = self.puzzle.solve()
        solution_l = solution.board
        self.show_board(solution_l)

    def Dark_mode(self):
        if self.d_l == 1:
            self.btn_dark_mode.setStyleSheet("background-color: rgb(240, 240, 240);")
            for i in range(9):
                for j in range(9):
                    self.line_edits[i][j].setStyleSheet("background-color: rgb(240, 240, 240);")
            self.d_l = 0
        elif self.d_l == 0:
            self.btn_dark_mode.setStyleSheet("background-color: rgb(130, 130, 130);")
            for i in range(9):
                for j in range(9):
                    self.line_edits[i][j].setStyleSheet("background-color: rgb(130, 130, 130);")
            self.d_l = 1

        for i in range(9):
            for j in range(9):
                self.line_edits[i][j].setReadOnly(False)
                if self.puzzle.board[i][j] != None:
                    self.line_edits[i][j].setText("")
                    self.line_edits[i][j].setText(str(self.puzzle.board[i][j]))
                    self.line_edits[i][j].setReadOnly(True)
                else:
                    self.line_edits[i][j].setText("")

    def new_board(self):
        for i in range(9):
            for j in range(9):
                new_cell = QLineEdit() 
                new_cell.setMaximumHeight(50)
                new_cell.setMaximumWidth(50) 
                new_cell.setMinimumHeight(50)
                new_cell.setMinimumWidth(50)              
                self.ui.grid_layout.addWidget(new_cell,i,j)
                new_cell.textChanged.connect(partial(self.validation,i,j))
                self.line_edits[i][j] = new_cell

    def new_game(self):
        self.puzzle = Sudoku(3,seed=random.randint(1, 1000)).difficulty(0.5)  
        self.new_board()      
        self.show_board(self.puzzle.board)

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
                    self.line_edits[i][j].setReadOnly(True)
                else:
                    self.line_edits[i][j].setText("")

    def validation(self,i,j,text):
        if text not in ["1","2","3","4","5","6","7","8","9"]:
            self.line_edits[i][j].setText(None)
        self.check(i,j,text)

    def check(self,i,j,text):
        solution = self.puzzle.solve()
        solution_l = solution.board

        st = []
        for ii in range(9):
            for jj in range(9):
                if self.line_edits[ii][jj].text() == str(solution_l[ii][jj]):
                    st.append(True)
                else:
                    st.append(False)
        
        if False not in st:
            msg_box = QMessageBox()
            msg_box.setText("you win!!")
            msg_box.exec_()

        if str(solution_l[i][j]) == text and solution_l[i][j] != "":
            self.status(True,i,j)
        
        else:    
            self.status(False,i,j)

    def status(self,status,i,j):
        if status == True:
            self.line_edits[i][j].setStyleSheet("background-color: rgb(170, 255, 255);")
        elif status == False:
            self.line_edits[i][j].setStyleSheet("background-color: rgb(255, 0, 0);")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec_()