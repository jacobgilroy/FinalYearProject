from PyQt5.QtCore import QThread
import pyaudio
from pydub import AudioSegment
import wave

class PlayThread(QThread):

    def __init__(self):

        super().__init__()

        self.audioSegments = [] # to store each lane's associated wav file
        self.output = None
        self.outputFilePath = ""

        self.playing = False

        self.CHUNK = 1024
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 2
        self.RATE = 44100
        self.p = pyaudio.PyAudio()

    def setOutputFilePath(self, path):

        self.outputFilePath = path + "/Output.wav"

    def setAudioSegments(self, wavList):

        self.audioSegments = wavList

    def overLayLanes(self):

        if len(self.audioSegments) > 0:

            longest = 0

            # find the longest audio segment (length of output segment):
            for seg in self.audioSegments:

                if len(seg) > longest:
                    longest = len(seg)

            # create a silent audio clip as a template for the output:
            template = AudioSegment.silent(duration=longest)

            # overlay the wavs from self.audioSegments
            for seg in self.audioSegments:
                template = template.overlay(seg)

            self.output = template
            self.output.export(self.outputFilePath, format="wav")

    def run(self):

        self.playing = True

        try:

            self.overLayLanes()

            if self.output is not None:

                print("*playing*")

                stream = self.p.open(format=self.FORMAT,
                                channels=self.CHANNELS,
                                rate=self.RATE,
                                output=True,
                                frames_per_buffer=self.CHUNK)

                wf = wave.open(self.outputFilePath, 'rb')

                data = wf.readframes(wf.getnframes())

                while self.playing:

                    if not len(data) > 0:
                        break

                    stream.write(data)
                    data = wf.readframes(self.CHUNK)

                print("*done playing*")

                stream.close()
                wf.close()

            else:

                print("No output to startPlaying")

        except IOError:

            print("IO Error while playing")

    def stop(self):

        self.playing = False
        self.terminate()