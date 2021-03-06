from PyQt5.QtCore import QThread
import pyaudio
import wave

class RecordThread(QThread):

    def __init__(self):

        super().__init__()

        self.recording = False

        self.CHUNK = 1024
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 2
        self.RATE = 44100
        self.OUTPUT_PATH = ""
        self.outputFileName = ""
        self.p = pyaudio.PyAudio()

    def setOutputFileName(self, name):

        self.outputFileName = name

    def setOutputPath(self, path):

        self.OUTPUT_PATH = path + "/clips/" + "/"

    def run(self):

        try:

            self.recording = True
            fullPath = str(self.OUTPUT_PATH + "/" + self.outputFileName + ".wav")

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

            stream.close()

            print(fullPath)
            wf = wave.open(fullPath, 'wb')
            wf.setnchannels(self.CHANNELS)
            wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
            wf.setframerate(self.RATE)
            wf.writeframes(b''.join(frames))

            wf.close()

        except IOError:

            print("IO Error while recording")