from countingstopwatch import CountingStopwatch 
from time import sleep

timer = CountingStopwatch() 
timer.start()
sleep(10)
timer.stop()
print("Time:", timer.elapsed(), " Number:", timer.count())

timer.start() 
sleep(5)
timer.stop() 
print("Time:", timer.elapsed(), " Number:", timer.count())

timer.start() 
sleep(20)
timer.stop() 
print("Time:", timer.elapsed(), " Number:", timer.count())


