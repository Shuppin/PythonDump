# pip install guizero
from guizero import *
import time
import sys

def quit():
    if app.yesno("Exit", "Are you sure you want to exit?"):
        app.destroy()

def click():
    ct = time.time()
    if click.counter == 0:
        click.time_start = ct
    #print(click.time_start, ct, ct - click.time_start, slider.value)
    if ct - click.time_start > slider.value:
        try:
            inputButton.disable()
            print("CPS:", click.counter/slider.value)
            print("Finished")
            #sys.exit()
            #cps_screen = Window(app, title="CPS Test", width=640, height=480,layout="grid")
            Text(app, text="            ", grid=[2,1])
            Text(app, text="            ", grid=[2,1])
            Text(app, text="CPS Test", grid=[3,1])
            Text(app, text=f"Your cps is {click.counter/slider.value}", grid=[3,2])
            PushButton(app, text="Try again", command=again, grid=[3,3])
            app.update()
            #app.destroy()
            
        except ZeroDivisionError:
            print("Slider cannot be 0!")
            app.destroy()
    click.counter += 1
    print(click.counter, ct)

def again():
    pass

def slider():
    print(slider.value)

click.counter = 0

app = App(title="CPS Test", width=640, height=480,layout="grid")
Text(app, text="CPS Test", size=35, grid=[0,1])
Text(app, text="Seconds", size=10, grid=[0,3])
slider.value = 0
print(click.counter)
slider = Slider(app, command=slider, start=1, end=30, grid=[1,3], horizontal=False)
inputButton = PushButton(app, text="Click", command=click, width="20", height="10", grid=[0,2])

app.when_closed = quit
app.display()







