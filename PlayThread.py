from PyQt5.QtCore import QThread
import pyaudio
import wave

class PlayThread(QThread):

    def __init__(self):

        super().__init__()

        self.playing = False

        self.CHUNK = 1024
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 2
        self.RATE = 44100
        self.p = pyaudio.PyAudio()

    def run(self):

        print("*playing*")

        stream = self.p.open(format=self.FORMAT,
                        channels=self.CHANNELS,
                        rate=self.RATE,
                        output=True,
                        frames_per_buffer=self.CHUNK)

        wf = wave.open("test.wav", 'rb')

        data = wf.readframes(wf.getnframes())

        while len(data) > 0:
            stream.write(data)
            data = wf.readframes(self.CHUNK)

        stream.stop_stream()
        stream.close()
        wf.close()

