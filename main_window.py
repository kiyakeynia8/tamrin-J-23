# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_window(object):
    def setupUi(self, window):
        if not window.objectName():
            window.setObjectName(u"window")
        window.resize(339, 422)
        window.setStyleSheet(u"")
        self.menu_new = QAction(window)
        self.menu_new.setObjectName(u"menu_new")
        self.menu_Openfile = QAction(window)
        self.menu_Openfile.setObjectName(u"menu_Openfile")
        self.menuAbout = QAction(window)
        self.menuAbout.setObjectName(u"menuAbout")
        self.menuHelp = QAction(window)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuexit_2 = QAction(window)
        self.menuexit_2.setObjectName(u"menuexit_2")
        self.menusolve = QAction(window)
        self.menusolve.setObjectName(u"menusolve")
        self.centralwidget = QWidget(window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.menu = QHBoxLayout()
        self.menu.setObjectName(u"menu")

        self.verticalLayout.addLayout(self.menu)

        self.grid_layout = QGridLayout()
        self.grid_layout.setObjectName(u"grid_layout")

        self.verticalLayout.addLayout(self.grid_layout)

        window.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 339, 21))
        self.menufile = QMenu(self.menubar)
        self.menufile.setObjectName(u"menufile")
        self.menuabout = QMenu(self.menubar)
        self.menuabout.setObjectName(u"menuabout")
        self.menuhelp = QMenu(self.menubar)
        self.menuhelp.setObjectName(u"menuhelp")
        self.menuExit = QMenu(self.menubar)
        self.menuExit.setObjectName(u"menuExit")
        self.menuSolve = QMenu(self.menubar)
        self.menuSolve.setObjectName(u"menuSolve")
        window.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(window)
        self.statusbar.setObjectName(u"statusbar")
        window.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menufile.menuAction())
        self.menubar.addAction(self.menuabout.menuAction())
        self.menubar.addAction(self.menuhelp.menuAction())
        self.menubar.addAction(self.menuExit.menuAction())
        self.menubar.addAction(self.menuSolve.menuAction())
        self.menufile.addAction(self.menu_new)
        self.menufile.addSeparator()
        self.menufile.addAction(self.menu_Openfile)
        self.menuabout.addAction(self.menuAbout)
        self.menuhelp.addAction(self.menuHelp)
        self.menuExit.addAction(self.menuexit_2)
        self.menuSolve.addAction(self.menusolve)

        self.retranslateUi(window)

        QMetaObject.connectSlotsByName(window)
    # setupUi

    def retranslateUi(self, window):
        window.setWindowTitle(QCoreApplication.translate("window", u"sudoku", None))
        self.menu_new.setText(QCoreApplication.translate("window", u"new game", None))
        self.menu_Openfile.setText(QCoreApplication.translate("window", u"Open file", None))
        self.menuAbout.setText(QCoreApplication.translate("window", u"About", None))
        self.menuHelp.setText(QCoreApplication.translate("window", u"Help", None))
        self.menuexit_2.setText(QCoreApplication.translate("window", u"Exit", None))
        self.menusolve.setText(QCoreApplication.translate("window", u"solve ", None))
        self.menufile.setTitle(QCoreApplication.translate("window", u"Game", None))
        self.menuabout.setTitle(QCoreApplication.translate("window", u"about", None))
        self.menuhelp.setTitle(QCoreApplication.translate("window", u"help", None))
        self.menuExit.setTitle(QCoreApplication.translate("window", u"Exit", None))
        self.menuSolve.setTitle(QCoreApplication.translate("window", u"Solve", None))
    # retranslateUi

