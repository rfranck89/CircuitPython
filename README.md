# CircuitPython
This repository will actually serve as a aid to help you get started with your own template.  You should copy the raw form of this readme into your own, and use this template to write your own.  If you want to draw inspiration from other classmates, feel free to check [this directory of all students!](https://github.com/chssigma/Class_Accounts).
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [NextAssignmentGoesHere](#NextAssignment)
---

## Hello_CircuitPython

### Description & Code
in this assignment, we had to make an LED blink red, and for the spicy part, we had to make the LED change colors.



```python
import time
import board
from rainbowio import colorwheel

if hasattr(board, "APA102_SCK"):
    import adafruit_dotstar

    led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
else:
    import neopixel

    led = neopixel.NeoPixel(board.NEOPIXEL, 1)

led.brightness = 0.3

i = 0
while True:
    i = (i + 1) % 256  # run from 0 to 255
    led.fill(colorwheel(i))
    time.sleep(0.01)
    led.fill((0, 0, 0))
    time.sleep(0.05)

```


### Evidence




https://user-images.githubusercontent.com/113116288/193276612-0931fee5-91f0-47a9-a4f0-216d54c9bee1.mp4




[.](https://www.youtube.com/watch?v=dQw4w9WgXcQ&scrlybrkr=8931d0bc)



### Wiring
![Screenshot (1)](https://user-images.githubusercontent.com/113116288/193279830-ef8dde32-f2db-4713-8ab5-5f8bee88cbbc.png)
### Reflection
nothing went wrong with this assignment.



## CircuitPython_Servo

### Description & Code

```python
import time
import board
import pwmio
from adafruit_motor import servo

# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.D7, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

while True:
    for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)
    for angle in range(180, 0, -5): # 180 - 0 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)

```

### Evidence

https://user-images.githubusercontent.com/113116288/197533735-7926cbf8-e1cd-405d-8b05-e31c03525451.mp4

### Wiring
![Screenshot (3)](https://user-images.githubusercontent.com/113116288/197535954-68af3b4b-abf7-45cd-b7a8-6f944809a3c9.png)
### Reflection

nothing really challenging happened on this assignment

## CircuitPython_Ultrasonic

### Description & Code

```python
import board
import adafruit_hcsr04
import neopixel
import time
import simpleio

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D7, echo_pin=board.D6)
Ryan = neopixel.NeoPixel(board.NEOPIXEL, 1)
Ryan.brightness = .1
red = 0
green = 0 
blue = 0
while True:
    try:
        cm = sonar.distance
        print((sonar.distance))
   
        time.sleep(0.001)
        if cm < 5:
            Ryan.fill((255, 0, 0))
        if cm > 5 and cm < 20:
            green = 0
            red = simpleio.map_range(cm, 5, 20, 255, 0)
            blue = simpleio.map_range(cm, 5, 20, 0, 255)
            Ryan.fill((red, green, blue))
        if cm > 20 and cm < 35:
            red = 0
            blue = simpleio.map_range(cm, 20, 35, 255, 0)
            green = simpleio.map_range(cm, 20, 35, 0, 255)
            Ryan.fill((red, green, blue))   
        
    except RuntimeError:
        print("Retrying")
        pass

    time.sleep(0.01)
```

### Evidence


https://user-images.githubusercontent.com/113116288/197537439-a1462548-17d4-47c9-9468-7531e6add570.mp4




### Wiring
![Screenshot (4)](https://user-images.githubusercontent.com/113116288/197538494-35c138d6-2a9f-4c77-9174-2dc58c95dff7.png)


### Reflection


## CircuitPython_LCD

### Description & Code

```python
Code goes here

```

### Evidence



### Wiring


### Reflection





## NextAssignment

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection
