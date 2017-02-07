from PyQt5.QtCore import QThread
import pyaudio
import wave

class RecordThread(QThread):

    def __init__(self, laneNum):

        super().__init__()

        self.recording = False

        self.CHUNK = 1024
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 2
        self.RATE = 44100
        self.p = pyaudio.PyAudio()

    def run(self):

        self.recording = True

        stream = self.p.open(format=self.FORMAT,
                        channels=self.CHANNELS,
                        rate=self.RATE,
                        input=True,
                        frames_per_buffer=self.CHUNK)

        print("* RECORDING *")

        frames = []

        while self.recording:

            data = stream.read(self.CHUNK)
            frames.append(data)

        print("* DONE RECORDING *")

        stream.stop_stream()
        stream.close()
        self.p.terminate()

        wf = wave.open("test.wav", 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(frames))

        wf.close()

        return wf

