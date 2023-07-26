import pyautogui
import time
import random
from threading import Thread


# Datos principales
tiempoMascota = 5
speed = 1
tiempoAfk = 200
veces = 600

posX = 596
posY = 214
factorX = 30
factorY = 40
inventarioIconPosX = 545
inventarioIconPosY = 555
equipoIconPosX = 614
equipoIconPosY = 124
recursoIconPosX = 658
recursoIconPosY = 124
cerrarInventarioIconPosX = 716
cerrarInventarioIconPosY = 62
mascotaPosX = 530
mascotaPosY = 220
sentarseIconPosX = 50
sentarseIconPosY = 540
gremioChatPosX = 820
gremioChatPosY = 660


def AbrirInventario():
    pyautogui.click(inventarioIconPosX, inventarioIconPosY)
    time.sleep(1 * speed)


def AbrirEquipo():
    pyautogui.click(equipoIconPosX, equipoIconPosY)
    time.sleep(1 * speed)


def AbrirRecurso():
    pyautogui.click(recursoIconPosX, recursoIconPosY)
    time.sleep(1 * speed)


def CerrarInventario():
    pyautogui.click(cerrarInventarioIconPosX, cerrarInventarioIconPosY)
    time.sleep(1 * speed)


def EquiparMascota(x, y):
    pyautogui.moveTo(posX + (factorX * x), posY + (factorY * y))
    pyautogui.mouseDown(button='left')
    time.sleep(0.5 * speed)
    pyautogui.moveTo(mascotaPosX, mascotaPosY, 0.5)
    pyautogui.mouseUp(button='left')
    time.sleep(0.5 * speed)


def DesEquiparMascota():
    pyautogui.moveTo(mascotaPosX, mascotaPosY, 0.5)
    pyautogui.mouseDown(button='left')
    time.sleep(0.5 * speed)
    pyautogui.moveTo(posX, posY, 0.5)
    pyautogui.mouseUp(button='left')
    time.sleep(0.5 * speed)


def AlimentarMascota():
    pyautogui.moveTo(posX, posY, 0.5)
    pyautogui.mouseDown(button='left')
    time.sleep(0.5 * speed)
    pyautogui.moveTo(mascotaPosX, mascotaPosY, 0.5)
    pyautogui.mouseUp(button='left')
    time.sleep(0.5 * speed)


def HablarGremio():
    r = random.randint(1, 4)

    if(r == 1):
        pyautogui.click(gremioChatPosX, gremioChatPosY)
        pyautogui.typewrite('Que hacen\n', interval=0.2)

    if(r == 2):
        pyautogui.click(gremioChatPosX, gremioChatPosY)
        pyautogui.typewrite('Me dio un hambre\n', interval=0.2)

    if(r == 3):
        pyautogui.click(gremioChatPosX, gremioChatPosY)
        pyautogui.typewrite('xd\n', interval=0.2)

    if(r == 4):
        pyautogui.click(gremioChatPosX, gremioChatPosY)
        pyautogui.typewrite('<3\n', interval=0.2)


def Sentarse():
    pyautogui.click(sentarseIconPosX, sentarseIconPosY)
    time.sleep(3)
    pyautogui.click(sentarseIconPosX, sentarseIconPosY)


def AntiAfk():
    while(True):
        r = random.randint(tiempoAfk, 550)
        time.sleep(r)
        ran = random.randint(1, 2)
        if(ran == 1):
            Sentarse()
        if(ran == 2):
            HablarGremio()




if __name__ == '__main__':

    hilo = Thread(target=AntiAfk)
    hilo.start()

    for i in range(veces):
        AbrirInventario()
        for y in range(9): # Cantidad de Casillas en el eje Y
            for x in range(4): # Cantidad de casillas en el eje X
                AbrirEquipo()
                EquiparMascota(x, y)
                AbrirRecurso()
                AlimentarMascota()
        DesEquiparMascota()
        CerrarInventario()
        time.sleep(3600 * tiempoMascota + 5)
