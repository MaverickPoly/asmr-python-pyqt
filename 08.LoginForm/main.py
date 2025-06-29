import sys

from PyQt5.QtWidgets import *


class LoginForm(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login Form")

    def handle_submit(self):
        pass



def main():
    application = QApplication(sys.argv)
    login_form = LoginForm()
    login_form.show()
    application.exec()


if __name__ == '__main__':
    main()
