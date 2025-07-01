import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class Question:
    def __init__(self, question: str, options: list[str], correct: int):
        self.question = question
        self.options = options
        self.correct = correct


questions = [
    Question("What is the capital of Russia?", ["Moscow", "Tashkent", "Baku", "Minsk"], 0),
    Question("Which country is the largest?", ["Brasil", "China", "Russia", "Turkey"], 2),
    Question("What is the longest river in the world?", ["Volga", "Nile", "Amazon", "Congo"], 1),
    Question("Who is the Founder of Python?", ["Maverick", "Pavel Durov", "Bjarne Stroustrup", "Guido Van Rossum"], 1),
]


class QuizApp(QWidget):
    def __init__(self):
        super().__init__()

        # Window
        self.setWindowTitle("Quiz App")
        self.setGeometry(300, 200, 800, 700)

        self.current = 0
        self.score = 0

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.setup_ui()

    def clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)

            widget = item.widget()
            if widget is not None:
                widget.setParent(None)
                widget.deleteLater()

            # If it's a nested layout
            child_layout = item.layout()
            if child_layout is not None:
                self.clear_layout(child_layout)

    def setup_ui(self):
        self.clear_layout(self.layout)
        question = questions[self.current]
        title = QLabel(question.question)
        self.layout.addWidget(title)

        self.group = QButtonGroup(self)
        for i, option in enumerate(question.options):
            radio = QRadioButton(f"{i + 1}. {option}")
            self.group.addButton(radio)
            self.layout.addWidget(radio)

        button = QPushButton("Next")
        button.clicked.connect(self.quiz_next)
        self.layout.addWidget(button)

    def end_screen(self):
        self.clear_layout(self.layout)

        title = QLabel("Quiz has ended!")
        title.setStyleSheet("font-size: 40px; font-weight: 600");
        title.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(title)

        score_text = QLabel(f"Score: {self.score}/{len(questions)}")
        score_text.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.layout.addWidget(score_text)

    def quiz_next(self):
        checked = self.group.checkedButton().text()
        id = int(checked[0]) - 1
        question = questions[self.current]

        if question.correct == id:
            self.score += 1
            print("Correct")
        self.current += 1
        if self.current == len(questions):
            self.end_screen()
        else:
            self.setup_ui()


def main():
    app = QApplication(sys.argv)
    window = QuizApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
