from time import sleep
import keyboard
from CodingRider.drone import *
from CodingRider.protocol import *

drone1 = Drone()
drone2 = Drone()
drone3 = Drone()
drone1.open('COM3')
drone2.open('COM4')
drone3.open('COM5')

while True:
    if keyboard.is_pressed('enter'):
        print('이륙')
        sleep(2)
        drone1.sendTakeOff()
        drone2.sendTakeOff()
        drone3.sendTakeOff()
        sleep(5)
        print('이륙 완료')
    if keyboard.is_pressed('space'):
        print('착륙')
        drone1.sendControlWhile(0, 0, 0, 0, 500)
        drone2.sendControlWhile(0, 0, 0, 0, 500)
        drone3.sendControlWhile(0, 0, 0, 0, 500)
        drone1.sendLanding()
        drone2.sendLanding()
        drone3.sendLanding()
        sleep(3)
        print('착륙 완료')
    if keyboard.is_pressed('esc'):
        print('프로그램 종료')
        break
    if keyboard.is_pressed('1'):
        for i in range(3):
            drone1.sendControlPosition(0, 1, 0, 1, 0, 0)
            drone2.sendControlPosition(0, 0, 1, 1, 0, 0)
            drone3.sendControlPosition(0, -1, 0, 1, 0, 0)
            sleep(2)
            drone1.sendControlPosition(0, -1, 0, 1, 0, 0)
            drone2.sendControlPosition(0, 0, -1, 1, 0, 0)
            drone3.sendControlPosition(0, 1, 0, 1, 0, 0)
            sleep(2)