# Combined test of the lasers, button press, sound, ADC
# Written by Scott Feister
#
# Plays a sound on pressing button, and a different sound on releasing button. (Pluck rate is not limited)
# Lasers come on on button press, turn off on button release.
# Displays continuous ADC values, 2x per second.
#
# Uses the MCP3008 ADC, photoresistors + 10k resistors, 

# Must install the MCP3008 python package first. Software SPI, not hardware.
# Follow MCP3008 instructions at: https://learn.adafruit.com/raspberry-pi-analog-to-digital-converters/mcp3008
# 
# Documentation on initializing LED, Button:
#   https://gpiozero.readthedocs.io/en/latest/recipes.html

import os
from time import sleep
from datetime import datetime
import numpy as np
import pygame.mixer
from pygame.mixer import Sound
from pygame.mixer import Channel
from Adafruit_MCP3008 import MCP3008
from gpiozero import LED, Button


################## INITIALIZATION ###########################

nstrings = 5 # Number of harp strings

scriptdir = os.path.dirname(os.path.realpath(__file__)) # Directory of this script
notedir = os.path.join(scriptdir, "sounds", "guitar") # Directory containing list of audio files
#notedir = r"/home/pi/mycode/twang/sounds/guitar" # Directory containing list of audio files
notes = ["c4", "d4", "e4", "f4", "g4"]  # List of wav files in the notedir folder
ext = ".wav"

sounds = [None]*nstrings
tpluck = [None]*nstrings
holds = [None]*nstrings

## INITIALIZE THE SOUND MIXER
pygame.mixer.pre_init(44100, -16, nstrings, )
pygame.mixer.init()

for i in range(nstrings):
    sounds[i] = Sound(os.path.join(notedir, notes[i] + ext))
    chans[i] = Channel(i)
    tpluck[i] = datetime.now() # Would be better if it was not now, but 1970
    holds[i] = False

## INITIALIZE THE LASER CONTROL / CALIBRATION BUTTON
def callback_press():
    """ Button callback function, turns on lasers and plays higher note """
    global lasers
    global sounds
    global chans
    print("PRESSED. Lasers on, higher note played.")
    lasers.on() # Turn on the lasers
    chans[1].play(sounds[1]) # Play the second note (higher)

def callback_release():
    """ Button callback function, turns off lasers and plays lower note """
    global lasers
    global sounds
    global chans
    print("RELEASED. Lasers off, lower note played.")
    lasers.off() # Turn off the lasers
    chans[0].play(sounds[0]) # Play the first note (lower)

LAS = 23 # Pin on which laser circuit is relayed
lasers = LED(LAS) # Initialize the laser as LED-style digital I/O

BTN = 24
button = Button(BTN)
button.when_pressed = callback_press
button.when_released = callback_release

## SET UP THE MCP3008 ADC
# Software SPI configuration:
CLK  = 4
MISO = 17 # a.k.a. DOUT
MOSI = 27 # a.k.a. DIN
CS   = 22 # a.k.a. CS/SHDN
mcp = MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

# Allocate arrays for ADC values
nchans = 8 # Number of analog input channels on the MCP3008
raw = np.zeros((nchans,), dtype=int) # The raw ADC values

# Set up a pretty printer of ADC values
printer = np.vectorize(lambda x: str(x).zfill(4)) # Call to print raw ADC values

########## CONTINUOUS PRINT VALUES TO TERMINAL ################
print("Press and hold button to play sound, display message, and turn on lasers. ADC values will show continuously.")
print("Press Ctrl + C when you are finished testing.")

while True:
    # Read the ADC values
    for i in range(nchans):
        raw[i] = mcp.read_adc(i)
    # Print the ADC values to the terminal window
    print(printer(raw).astype('object'))
    sleep(0.5) # Limit the printing rate to help user identify values