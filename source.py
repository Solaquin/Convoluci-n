import numpy as np
import sounddevice as sd
import librosa
from scipy.signal import convolve

audios_source = ["baño_mezcla.wav", "salon_mezcla.wav", "saxofon.wav"]

def loadAudio(archivo):
    data, samplerate = librosa.load(archivo, sr = None)
    return data, samplerate

def playAudio(data, sr):
    sd.play(data, sr)
    sd.wait()

def convolucionar_audio(audio_in, impulso):
    # Realizamos la convolución usando 'full' para obtener toda la señal resultante
    audio_convolucionado = convolve(audio_in, impulso, mode='full')
    # Normalizamos el audio para evitar saturación
    audio_convolucionado /= np.max(np.abs(audio_convolucionado))
    return audio_convolucionado

def main():
    opcion = 0
    data, sr = loadAudio(audios_source[2]) #Señal original
    playAudio(data, sr)
    
    while(True):
        print("Seleccione que con que impulso desea realizar la convolución.\n1. Baño\n2. Salon\n3. Salir")
        opcion = int(input("---> "))
        if opcion == 1:
            impulso = loadAudio(audios_source[0])[0]
            convolucion = convolucionar_audio(data, impulso)
            playAudio(convolucion, sr)
        elif opcion == 2:
            impulso = loadAudio(audios_source[1])[0]
            convolucion = convolucionar_audio(data, impulso)
            playAudio(convolucion, sr)
        elif opcion == 3:
            break
        else: 
            print("\nOpción invalida")

if __name__ == "__main__":
    main()