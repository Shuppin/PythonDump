import threading, _thread
from pynput import keyboard
import sys

def listen():
    def on_release(key):
        if key == keyboard.Key.f10:
            print("Closing program")
            _thread.interrupt_main()

    with keyboard.Listener(
            on_release=on_release) as listener:
        listener.join()

    listener = keyboard.Listener(
        on_release=on_release)
    listener.start()

def activate():
    x = threading.Thread(target=listen)
    x.start()

    print("Killswitch enabled")



