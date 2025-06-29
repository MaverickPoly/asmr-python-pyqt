import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QColor, QFont

from db import Db


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Window
        self.setWindowTitle("Todo List")
        self.setGeometry(300, 100, 1200, 800)

        self.red_color = QColor()
        self.red_color.setRgb(180, 0, 0, 255)
        self.green_color = QColor()
        self.green_color.setRgb(0, 180, 00, 255)
        self.white_color = QColor()
        self.white_color.setRgb(220, 220, 220, 255)

        self.db = Db()
        self.todos = []
        self.setup_ui()


    def setup_ui(self):
        central_widget = QWidget()
        layout = QVBoxLayout()

        # Form
        input_layout = QHBoxLayout()

        # Input Field
        self.line_edit = QLineEdit()
        self.line_edit.setStyleSheet(f"""
            QLineEdit {{
                border-radius: 14px;
                border: 1px solid #ddd;
                padding: 10px;
                font-size: 24px;
            }}
            QLineEdit:focus {{
                border: 1px solid #888;
            }}
        """)
        self.line_edit.setPlaceholderText("Enter todo title...")
        input_layout.addWidget(self.line_edit)

        # Add Button
        self.add_button = QPushButton("Add")
        self.add_button.setStyleSheet(f"""
            QPushButton {{
                background: rgb(40, 40, 200);
                color: white;
                border-radius: 12px;
                cursor: pointer;
                padding: 14px 40px;
                margin-left: 10px;
                font-size: 20px;
            }}
            QPushButton:hover {{
                background: rgb(0, 0, 250);
            }}
        """)
        self.add_button.clicked.connect(self.handle_add)
        input_layout.addWidget(self.add_button)

        # List
        self.task_list = QListWidget()
        self.task_list.setSpacing(6)

        # Bottom Actions
        bottom_actions = QHBoxLayout()

        # Delete button
        delete_button = QPushButton("Delete")
        delete_button.setStyleSheet(f"""
            QPushButton {{
                background: rgb(200, 0, 0);
                color: white;
                border-radius: 12px;
                cursor: pointer;
                padding: 14px 40px;
                margin-left: 10px;
                font-size: 20px;
            }}
            QPushButton:hover {{
                background: rgb(160, 0, 0);
            }}    
        """)
        delete_button.clicked.connect(self.handle_delete)
        bottom_actions.addWidget(delete_button)

        # Toggle complete button
        toggle_button = QPushButton("Toggle complete")
        toggle_button.setStyleSheet(f"""
            QPushButton {{
                background: rgb(210, 150, 0);
                color: white;
                border-radius: 12px;
                cursor: pointer;
                padding: 14px 40px;
                margin-left: 10px;
                font-size: 20px;
            }}
            QPushButton:hover {{
                background: rgb(180, 130, 0);
            }}  
        """)
        toggle_button.clicked.connect(self.toggle_complete)
        bottom_actions.addWidget(toggle_button)

        # Layout
        layout.addLayout(input_layout)
        layout.addWidget(self.task_list)
        layout.addLayout(bottom_actions)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.fetch_todos()

    def fetch_todos(self):
        self.todos = self.db.get_all_todos()
        self.task_list.clear()
        for i, todo in enumerate(self.todos):
            widget = QListWidgetItem(f"{i + 1}. {todo.title}")
            color = self.green_color if todo.completed else self.red_color
            widget.setBackground(color)
            widget.setFont(QFont("Arial", 22))
            widget.setForeground(self.white_color)
            self.task_list.addItem(widget)

    def handle_delete(self):
        for todo in self.task_list.selectedItems():
            index = int(todo.text()[0]) - 1
            todo = self.todos[index]
            self.db.delete_todo(todo.id)
            self.fetch_todos()

    def toggle_complete(self):
        for todo in self.task_list.selectedItems():
            index = int(todo.text()[0]) - 1
            todo = self.todos[index]
            self.db.toggle_complete(todo)
            self.fetch_todos()

    def handle_add(self):
        title = self.line_edit.text().strip()
        if title:
            self.db.add_todo(title)
            self.fetch_todos()
            self.line_edit.clear()


def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
