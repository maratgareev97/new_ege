import librosa
import matplotlib.pyplot as plt
import librosa.display
import numpy as np
spisok = ['export.wav']
for i in range(len(spisok)):
  audio_data = spisok[i]
  x , sr = librosa.load(audio_data)
  S = np.abs(librosa.stft(x, n_fft=4096))**2
  chroma = librosa.feature.chroma_stft(S=S, sr=sr)
  for i in range(len(chroma)-1,-1,-1):
      for j in range(len(chroma[i])):
          if chroma[i][j]<0.95:
            chroma[i][j]=0
          else:
            chroma[i][j] = 1
  # fig, ax = plt.subplots()
  # img = librosa.display.specshow(chroma, y_axis='chroma', x_axis='time', ax=ax)
  # fig.colorbar(img, ax=ax)
  # ax.set(title='Chromagram')
  print(chroma)
  fig, ax = plt.subplots(nrows=2, sharex=True)
  img = librosa.display.specshow(librosa.amplitude_to_db(S, ref=np.max),
                               y_axis='log', x_axis='time', ax=ax[0])
  img = librosa.display.specshow(chroma, y_axis='chroma', x_axis='time', ax=ax[1])
  fig.colorbar(img, ax=[ax[1]])