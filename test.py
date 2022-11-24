from gensound import WAV, test_wav
from gensound import Sine
from gensound import Gain


def sound1():
    wav = WAV(test_wav)

    wav[0], wav[1] = wav[1], wav[0]
    wav = wav[1, 5e3:] # 5 seconds onwards, R channel only

def sound2():
    wav = WAV(test_wav)
    wav.play(sample_rate=32000) # original sample rate 44.1 kHz
    
def sound3():
    wav = WAV(test_wav)
    wav[1].play() # wav[0] is L channel, wav[1] is R

def sound4():
    wav = WAV(test_wav)
    wav[0] *= 0.5 # amplitude halved; wav[1] amplitude remains the same
    wav.play()
    
def sound5():
    wav = WAV(test_wav)
    wav = 0.5*wav[0] + 0.5*wav[1] # sums up L and R channels together, halving the amplitudes
    wav.play()

def sound6():
    wav = WAV(test_wav)
    wav = wav[5e3:] # since 5e3 is float, gensound knows we are not talking about channels
    wav.play()

def sound7():
    wav = WAV(test_wav)
    wav = wav[1, 5e3:] # 5 seconds onwards, R channel only
    wav.play()

def sound8():
    wav = WAV(test_wav)
    wav = wav[:,:1000] # grabs first 1000 samples in both channels; samples are in ints
    wav.play()
    
def sound9():
    wav = WAV(test_wav)
    wav = wav**5
    wav.play() 

def sound10():
    wav = WAV(test_wav)
    wav[0,4e3:] += Sine(frequency=440, duration=2e3)*Gain(-9) #Mix a 440Hz (middle A) sine wave to the L channel, 4 seconds after the beginning:
    wav.play()

