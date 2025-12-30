import mido
import time
import pygame.midi

# --- 初期化 ---
pygame.midi.init()
player = pygame.midi.Output(0)  # デフォルトの出力デバイス
instrument = 0  # 0: Acoustic Grand Piano
player.set_instrument(instrument)

# --- MIDIファイル読み込み ---
midi_file = mido.MidiFile('example.mid')

# --- 再生 ---
print("再生開始...")
for msg in midi_file.play():  # 自動でsleepを入れながら再生してくれる
    if msg.type == 'note_on':
        player.note_on(msg.note, msg.velocity)
    elif msg.type == 'note_off':
        player.note_off(msg.note, msg.velocity)

print("再生終了")

# --- 後処理 ---
del player
pygame.midi.quit()