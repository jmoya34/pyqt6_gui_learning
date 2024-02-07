from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QMessageBox

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QMessageBox")
        button_hard = QPushButton("Hard")
        button_hard.clicked.connect(self.button_clicked_hard)
        
        button_critical = QPushButton("Critical")
        button_critical.clicked.connect(self.button_clicked_critical)
        
        button_question = QPushButton("Question")
        button_question.clicked.connect(self.button_clicked_question)
        
        button_information = QPushButton("Information")
        button_information.clicked.connect(self.button_clicked_information)

        button_warning = QPushButton("Warning")
        button_warning.clicked.connect(self.button_clicked_warning)
        
        button_about = QPushButton("About")
        button_about.clicked.connect(self.button_clicked_about)

        layout = QVBoxLayout()
        layout.addWidget(button_hard)
        layout.addWidget(button_critical)
        layout.addWidget(button_question)
        layout.addWidget(button_information)
        layout.addWidget(button_warning)
        layout.addWidget(button_about)
        self.setLayout(layout)

    """
    This is the hard method to creating a message box because you have to repeat a lot of the same code for other message box types
    """
    def button_clicked_hard(self):
        print("Hard")
        message = QMessageBox()
        message.setMinimumSize(700, 200)
        message.setWindowTitle("Message title")
        message.setText("Something Happened")
        message.setInformativeText("This is additional information")
        message.setIcon(QMessageBox.Critical)
        message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        message.setDefaultButton(QMessageBox.Ok)

        # This will return the button that was clicked
        ret = message.exec()
        if ret == QMessageBox.Ok:
            print("User chose ok")
        else:
            print("User chose cancel")
    
    """
    All the other methods are the easy way to create a message box using slight varitation to the QMessageBox class method
    """
    def button_clicked_critical(self):
        print("Critical")
        ret = QMessageBox.critical(self, "Message title", 
                                   "Crititcal message", 
                                   QMessageBox.Ok | QMessageBox.Cancel)
        if ret == QMessageBox.Ok:
            print("User chose ok")
        else:
            print("User chose cancel")
    
    def button_clicked_question(self):
        print("Question")
        ret = QMessageBox.question(self, "Message title", 
                                   "Crititcal message", 
                                   QMessageBox.Ok | QMessageBox.Cancel)
        if ret == QMessageBox.Ok:
            print("User chose ok")
        else:
            print("User chose cancel")
    
    def button_clicked_information(self):
        print("Information")
        ret = QMessageBox.information(self, "Message title", 
                                   "Crititcal message", 
                                   QMessageBox.Ok | QMessageBox.Cancel)
        if ret == QMessageBox.Ok:
            print("User chose ok")
        else:
            print("User chose cancel")
    
    def button_clicked_warning(self):
        print("Warning")
        ret = QMessageBox.warning(self, "Message title", 
                                   "Crititcal message", 
                                   QMessageBox.Ok | QMessageBox.Cancel)
        if ret == QMessageBox.Ok:
            print("User chose ok")
        else:
            print("User chose cancel")
    
    def button_clicked_about(self):
        print("About")
        ret = QMessageBox.about(self, "Message title", 
                                   "Crititcal message")
        if ret == QMessageBox.Ok:
            print("User chose ok")
        else:
            print("User chose cancel")
