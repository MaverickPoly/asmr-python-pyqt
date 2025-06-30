import sys
import markdown

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


"""
text, addText
"""


class ActionButton:
    def __init__(self, text: str, add_text: str):
        self.text = text
        self.add_text = add_text


action_buttons = (
    ActionButton("Heading 1", "# "),
    ActionButton("Heading 2", "## "),
    ActionButton("Heading 3", "### "),
    ActionButton("Heading 4", "#### "),
    ActionButton("Heading 5", "##### "),
    ActionButton("Heading 6", "###### "),

    ActionButton("Bold", "**"),
    ActionButton("Italic", "*"),
    ActionButton("Link", "[]()"),
)


class StickyNotes(QWidget):
    def __init__(self):
        super().__init__()

        # Window
        self.setWindowTitle("Sticky Notes")
        self.setGeometry(300, 200, 900, 700)

        self.markdown_enabled = False

        # UI
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.switch = QCheckBox("Markdown Preview")
        self.switch.clicked.connect(self.change_md)
        layout.addWidget(self.switch)

        self.text_edit = QTextEdit()
        layout.addWidget(self.text_edit)

        self.md_preview = QTextBrowser()
        self.md_preview.hide()
        layout.addWidget(self.md_preview)

        button_row = QHBoxLayout()
        for action in action_buttons:
            btn = QPushButton(action.text)
            btn.clicked.connect(lambda _, a=action: self.handle_md_action(a.add_text))
            button_row.addWidget(btn)
        layout.addLayout(button_row)

    def change_md(self, _):
        if self.switch.isChecked():
            self.markdown_enabled = True
            text = self.text_edit.toPlainText()
            html = markdown.markdown(text)
            self.md_preview.setHtml(html)
            self.text_edit.hide()
            self.md_preview.show()
        else:
            self.markdown_enabled = False
            self.md_preview.hide()
            self.text_edit.show()

    def handle_md_action(self, markdown_syntax):
        cursor = self.text_edit.textCursor()
        cursor.insertText(markdown_syntax)
        self.text_edit.setTextCursor(cursor)


def main():
    application = QApplication(sys.argv)
    sticky_notes = StickyNotes()
    sticky_notes.show()
    sys.exit(application.exec_())


if __name__ == '__main__':
    main()
