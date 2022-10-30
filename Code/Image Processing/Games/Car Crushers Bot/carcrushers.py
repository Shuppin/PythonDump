from keys import Key
from directkeys import PressKey as prs, ReleaseKey as rel
import time
import killswitch

killswitch.activate()

for i in list(range(5))[::-1]:
        print(i+1)
        time.sleep(1)
        
try:
    while True:
        prs(Key("q"))
        time.sleep(0.1)
        rel(Key("q"))

        time.sleep(0.2)

        prs(Key("r"))
        time.sleep(0.1)
        rel(Key("r"))

except Exception as e:
    rel(Key("q"))
    rel(Key("r"))
    raise e
