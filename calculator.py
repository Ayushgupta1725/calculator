import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QGridLayout
from PyQt5.QtGui import QFont

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Modern Calculator')
        self.setFixedSize(300, 400)
        self.init_ui()

    def init_ui(self):
        # Layouts
        main_layout = QVBoxLayout()
        self.display = QLineEdit()
        self.display.setFont(QFont("Arial", 24))
        self.display.setReadOnly(True)
        self.display.setStyleSheet("background-color: white; color: black;")
        
        main_layout.addWidget(self.display)
        
        # Button Layout
        button_layout = QGridLayout()
        buttons = {
            '7': (0, 0),
            '8': (0, 1),
            '9': (0, 2),
            '/': (0, 3),
            '4': (1, 0),
            '5': (1, 1),
            '6': (1, 2),
            '*': (1, 3),
            '1': (2, 0),
            '2': (2, 1),
            '3': (2, 2),
            '-': (2, 3),
            '0': (3, 0),
            'C': (3, 1),
            '=': (3, 2),
            '+': (3, 3),
        }

        for btn_text, pos in buttons.items():
            button = QPushButton(btn_text)
            button.setFont(QFont("Arial", 18))
            button.setFixedSize(60, 60)
            button.setStyleSheet("background-color: #f2f2f2; border-radius: 10px;")
            button.clicked.connect(self.on_button_click)
            button_layout.addWidget(button, pos[0], pos[1])

        main_layout.addLayout(button_layout)
        self.setLayout(main_layout)

    def on_button_click(self):
        button = self.sender()
        text = button.text()

        if text == "C":
            self.display.clear()
        elif text == "=":
            try:
                result = str(eval(self.display.text()))
                self.display.setText(result)
            except Exception:
                self.display.setText("Error")
        else:
            self.display.setText(self.display.text() + text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
