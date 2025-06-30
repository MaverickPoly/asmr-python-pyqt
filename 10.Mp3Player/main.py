from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl, Qt



class MusicPlayer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Music Player")
        self.setGeometry(200, 200, 700, 400)

        self.player = QMediaPlayer()

        url = QUrl.fromLocalFile(".\\wanttheworld.mp3")
        content = QMediaContent(url)
        self.player.setMedia(content)
        self.player.positionChanged.connect(self.update_slider)
        self.player.durationChanged.connect(self.set_duration)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setTickInterval(1000)
        self.slider.valueChanged.connect(self.set_position)

        self.label = QLabel("")
        self.label.setAlignment(Qt.AlignCenter)

        self.play_button = QPushButton("Play")
        self.play_button.clicked.connect(self.player.play)

        self.pause_button = QPushButton("Pause")
        self.pause_button.clicked.connect(self.player.pause)

        self.stop_button = QPushButton("Stop")
        self.stop_button.clicked.connect(self.player.stop)
        self.player.setPosition(10000)

        horizontal_box = QHBoxLayout()

        layout = QVBoxLayout()
        layout.addWidget(self.slider)
        layout.addWidget(self.label)
        horizontal_box.addWidget(self.play_button)
        horizontal_box.addWidget(self.pause_button)
        horizontal_box.addWidget(self.stop_button)
        layout.addLayout(horizontal_box)
        self.setLayout(layout)

    def update_slider(self, duration):
        self.slider.setValue(duration)

        seconds = int(duration / 1000) % 60
        minutes = int(duration / 1000) // 60
        self.label.setText(f"{minutes:02}:{seconds:02}")

    def set_duration(self, value):
        self.slider.setMaximum(value)

    def set_position(self, value):
        self.player.setPosition(value)


def main():
    app = QApplication([])
    music_player = MusicPlayer()
    music_player.show()
    app.exec_()


if __name__ == '__main__':
    main()
