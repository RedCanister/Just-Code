from pydub import AudioSegment
from pathlib import Path
from os import path
#CORREÇÕES
"""
No seu desafio o frame rate foi setado no arquivo mp3, 
o que faz com que na conversão de um áudio com maior frame rate 
o resultado fique desacelerado. O correto seria setar após conversão.
"""
#FEITO
"""
As três partes do desafio agora foram separadas em 4 funções diferentes,
cada uma realizando uma parte do desafio
Na ordem:
- read_mp3 lê um arquivo qualquer .mp3 para um objeto AudioSegment
- read_wav lê o arquivo .wav
- apply_Rate16K opera a taxa de amostragem do arquivo para 16000
- export_wav gera o arquivo .wav do AudioSegment que estiver sendo operado
  no formato .wav, sempre com o nome 'Teste.wav'
E no final, a alteração no volume foi feito através da sintaxe do pydub
sobre o objeto AudioSegment: audio += gain 
"""

def read_mp3(path):
    mp3 = AudioSegment.from_mp3(path)
    return mp3

def read_wav():
    wav = AudioSegment.from_file('Teste.wav', 'wav')
    return wav

def apply_Rate16K(audio):
    audio.frame_rate = 16000

def export_wav(file):
    #curPath = str(Path(__file__).parent.resolve())
    wav = file.export("Teste.wav", format="wav")
    return wav

# A música utilizada nos testes foi Palco de Gilberto Gil!

#Primeiro bloco fazendo a conversão do arquivo .mp3 para .wav e guardando o volume
file = str(input("Caminho do arquivo .mp3: "))
gain = int(input("Volume a ajustar (int)(+/-): "))
mp3 = read_mp3(file)
export_wav(mp3)

#Mostrando os dados do arquivo para evidenciar as alterações
print("Volume mp3:",mp3.dBFS)
print("Frame rate mp3: ",mp3.frame_rate)

#Segundo bloco de código fazendo as alterações no arquivo Teste.wav
wav = read_wav()
apply_Rate16K(wav)
wav += gain
export_wav(wav)

#Confirmando as alterações
print("Volume wav:",wav.dBFS)
print("Frame rate wav: ",wav.frame_rate)