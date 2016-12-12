from PyQt4 import QtGui
import pyaudio
import wave
import sys

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()

class Lane(QtGui.QWidget):

    def __init__(self):

        super(Lane, self).__init__()

        self.hasAudio = False

        self.recBtn = QtGui.QPushButton('Record', self)
        self.playBtn = QtGui.QPushButton('Play', self)

        self.initUI()

    def initUI(self):

        layout = QtGui.QGridLayout()
        layout.addWidget(self.recBtn, 0, 4)
        layout.addWidget(self.playBtn, 0, 5)

        self.setLayout(layout)

        self.recBtn.clicked.connect(self.recordAudio)
        self.playBtn.clicked.connect(self.playAudio)

        self.setWindowTitle("Audio Lane")
        # self.setGeometry(300, 300, 100, 30)
        self.show()

    def recordAudio(self):

        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

        print("* RECORDING *")

        frames = []

        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)

        print("* DONE RECORDING *")

        stream.stop_stream()
        stream.close()
        # p.terminate()

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

        wf.close()

        self.hasAudio = True


    def playAudio(self):

        if self.hasAudio:
            print("*playing*")

            stream = p.open(format=FORMAT,
                            channels=CHANNELS,
                            rate=RATE,
                            output=True,
                            frames_per_buffer=CHUNK)

            wf = wave.open(WAVE_OUTPUT_FILENAME, 'rb')

            data = wf.readframes(wf.getnframes())

            while len(data) > 0:
                stream.write(data)
                data = wf.readframes(CHUNK)

            stream.stop_stream()
            stream.close()
            wf.close()

        else:
            print("NO AUDIO TO PLAY")


def main():

    app = QtGui.QApplication(sys.argv)

    window = QtGui.QWidget()
    lane = Lane()

    layout = QtGui.QVBoxLayout()
    layout.addWidget(lane)
    window.setWindowTitle("SpaceJam")
    window.setLayout(layout)
    window.setGeometry(300, 300, 700, 100)
    window.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()