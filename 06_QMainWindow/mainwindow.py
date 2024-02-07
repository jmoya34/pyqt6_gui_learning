from PySide6.QtWidgets import  QMainWindow, QToolBar, QPushButton, QStatusBar
from PySide6.QtCore import QSize
from PySide6.QtGui import QAction, QIcon

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app #declare an app memeber
        self.setWindowTitle("Custom MainWindow")

        # Menubar and menus
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("&File")
        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(self.quit_app)

        # adding one more menu bar option that has multiple options
        edit_menu = menu_bar.addMenu("Edit")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Cut")
        edit_menu.addAction("Paste")
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")

        # tool bar
        toolbar = QToolBar("main toolbar")
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)

        # add quit action to toolbar
        toolbar.addAction(quit_action)

        action1 = QAction("some Action", self)
        action1.setStatusTip("Status message for some action")
        action1.triggered.connect(self.toolbar_button_click)
        toolbar.addAction(action1)

        # Adding an icon
        action2 = QAction(QIcon("test.png"), "Some other action", self)
        action2.setStatusTip("Status message for some other action") # occurs when mouse hovers over item
        action2.triggered.connect(self.toolbar_button_click)
        toolbar.addAction(action2)

        # Add a pointless button
        toolbar.addSeparator()
        toolbar.addWidget(QPushButton("click me"))

        # Creating a status bar (Bottom of the screen)
        button1 = QPushButton("BUTTON1")
        button1.clicked.connect(self.button1_clicked)
        self.setCentralWidget(button1)


    def quit_app(self):
        self.app.quit()
    
    def toolbar_button_click(self):
        print("Action triggered")
        self.statusBar().showMessage("Message from app", 3000) #show message for 3 seconds (takes parameter as milliseconds)

    def button1_clicked(self):
        print("button clicked")
        