import board
import neopixel

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.2 

print("Make it red!")

while True:
    dot.fill((102,255,51))