import simpleaudio as sa


def play_alarm():
    wave_obj = sa.WaveObject.from_wave_file("mixkit-alert-alarm-1005.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()