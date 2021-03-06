
#    Copyright (C) 2018 Soikat Hasan Ahmed
#
#    Project Name:
#    Author: Soikat Hasan Ahmed
#    Author's Email: soikathasan15@gmail.com
#
#    Redistribution and use in source and binary forms, with or without modification,
#    are permitted provided that the following conditions are met:
#
#    1. Redistributions of source code must retain the above copyright notice, this
#       list of conditions and the following disclaimer.
#
#    2. Redistributions in binary form must reproduce the above copyright notice, this
#       list of conditions and the following disclaimer in the documentation and/or
#       other materials provided with the distribution.
#
#    3. Neither the name of the copyright holder nor the names of the contributors may
#       be used to endorse or promote products derived from this software without
#       specific prior written permission.
#
#    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
#    ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
#    WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
#    IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
#    INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING
#    BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
#   DATA, OR PROFITS; OR BUSINESS INTERRUPTIONS) HOWEVER CAUSED AND ON ANY THEORY OF
#    LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
#    OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
#    OF THE POSSIBILITY OF SUCH DAMAGE.
from builtins import print

import pygame
import serial
import time
import pyttsx3
import threading
from voice import *

engine = pyttsx3.init()
engine.setProperty('rate', 125)
#thread for voice class
t = threading.Thread(target=voice)
t.start()

#init serial
arduino = serial.Serial("/dev/ttyACM1",9600,timeout=5)


def send_to_arduino(fb, rl,brk_key,brk_release_key,center):


        arduino.write(chr(100).encode())
        arduino.write(chr(fb).encode())
        arduino.write(chr(rl).encode())
        arduino.write(chr(brk_key).encode())
        arduino.write(chr(brk_release_key).encode())
        arduino.write(chr(center).encode())


time.sleep(1)
print('init serial')

#init gamepad
pygame.display.init()
pygame.joystick.init()
pygame.joystick.Joystick(0).init()
print('init gamepad')
engine.say('command initiated')
engine.say('welcome back sir')
engine.runAndWait()

while True:

        pygame.event.pump()
        bx = int((pygame.joystick.Joystick(0).get_axis(2))*50+50)
        ay = int((pygame.joystick.Joystick(0).get_axis(1))*50+50)

        print('control  :'+str(ay) + '  ' + str(bx))
        # button 5 for break (front right up)
        brk = int(pygame.joystick.Joystick(0).get_button(5))
        print('break  :'+ str(brk))
        # button 7 for release (front right down)
        brk_release =int( pygame.joystick.Joystick(0).get_button(7))
        print('break  release "'+str(brk_release))
        # button 1 for VOICE KEY (BUTTON 2 )
        voice_key =int( pygame.joystick.Joystick(0).get_button(1))
        print('voice_key : '+str(voice_key))
        # button 0 for steer center KEY (BUTTON 1 )
        steer_center = int(pygame.joystick.Joystick(0).get_button(0))
        print('steer center : ' + str(steer_center))

        send_to_arduino(ay,bx,brk,brk_release,steer_center)
        time.sleep(.1)



