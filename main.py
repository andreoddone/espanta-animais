import RPi.GPIO as GPIO
import time
import pygame

GPIO.setmode(GPIO.BCM)
sensor_pin = 17
GPIO.setup(sensor_pin, GPIO.IN)

pygame.mixer.init()

def tocar_som():
    pygame.mixer.music.load("/home/pi/som_espanta_animais.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)

try:
    print("Sistema pronto. Aguardando detecção de movimento.")
    while True:
        if GPIO.input(sensor_pin):
            print("Movimento detectado! Tocando som.")
            tocar_som()
            time.sleep(10)
        else:
            print("Nenhum movimento detectado.")
        
        time.sleep(1)

except KeyboardInterrupt:
    print("Programa encerrado.")
    
finally:
    GPIO.cleanup()
