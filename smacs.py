import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QComboBox, QFileDialog, QMessageBox, QTableWidget, QTableWidgetItem, QScrollArea, QTabWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import pandas as pd
import pyodbc
import csv
class HomeScreen(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("SMACS Tool Application")
        self.setGeometry(100, 100, 1000, 800)

        # Create a label for the title
        self.title_label = QLabel("Welcome to SMACS", self)
        self.title_label.setGeometry(200, 20, 200, 50)

        # Create a button
        self.button = QPushButton("Click Me", self)
        self.button.setGeometry(250, 370, 100, 30)
        self.button.clicked.connect(self.button_clicked)

    def button_clicked(self):
        print("Button Clicked!")
    def init_ui(self):
        tab_widget = QTabWidget()

        # Main Window Tab
        main_window_tab = QWidget()
        main_layout = QVBoxLayout()
        # Reduce margins and spacing
        main_layout.setContentsMargins(10, 10, 10, 10)  # Set margins to 10 pixels
        main_layout.setSpacing(5)  # Set spacing between elements to 5 pixels

        # Version Label
        version_label = QLabel("Version:1.0.1.0")
        version_label.setStyleSheet("font-size: 10pt;")
        main_layout.addWidget(version_label, alignment=Qt.AlignTop | Qt.AlignLeft)

        # Welcome Image
        img_path = "image.png"  # Update this with the correct path to your image
        pixmap = QPixmap(img_path)
        welcome_image_label = QLabel()
        welcome_image_label.setPixmap(pixmap)
        main_layout.addWidget(welcome_image_label, alignment=Qt.AlignHCenter)

        # Welcome Text
        welcome_label = QLabel("Welcome to the ETU Configuration-Generation Tool")
        welcome_label.setStyleSheet("font-size: 18pt; font-weight: bold;")
        main_layout.addWidget(welcome_label, alignment=Qt.AlignHCenter)

        main_window_tab.setLayout(main_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HomeScreen()
    window.show()
    sys.exit(app.exec_())