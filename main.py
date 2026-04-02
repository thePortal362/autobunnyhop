import keyboard
import asyncio #using async functions to detect if key is pressed while doing bunny hopping
import os
import time

doit = False

def write(txt):
    for char in txt:
        print(char, end="", flush=True)
        time.sleep(0.07)
    print()

def toggle():
    global doit
    doit = not doit
    #print("Toggled:", doit)

async def press_loop():
    global doit
    while True:
        if doit:
            #print("pressing", flush=True)
            keyboard.press_and_release('space')
            await asyncio.sleep(0.75) #time needed to complete jump
        else:
            await asyncio.sleep(0.01)

async def main():
    print("\033[31mOnly for schedule 1\033[0m")
    time.sleep(2)
    os.system("cls")
    time.sleep(1)
    write("\033[32mAuto Bunny Hop active...\033[0m")

    keyboard.on_release_key('ctrl', lambda e: toggle())

    await press_loop()

asyncio.run(main())