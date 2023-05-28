import turtle as t 
from countingstopwatch import CountingStopwatch

timer = CountingStopwatch()
def draw_watch(sw): 
    seconds = round(sw.elapsed())
    time = ""
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    time = "{0:0>2}:{1:0>2}:{2:0>2}".format(hours, minutes, seconds)
    t.clear() 
    t.penup() 
    t.setposition(-200, 0) 
    t.pendown()
    t.write(time, font=("Arial", 64, "normal"))
    t.penup() 
    t.setposition(-50, -50) 
    t.pendown()
    t.write(sw.count(), font=("Arial", 24, "normal"))

def quit():
    t.bye()

def update(): 
    draw_watch(timer)
    t.ontimer(update, 500)

t.title("Stopwatch Test")
t.onkey(timer.start, "s")
t.onkey(timer.stop, "t")
t.onkey(timer.reset, "r")
t.onkey(quit, "q")
t.listen()
t.delay(0)
t.speed(0)
t.ontimer(update, 500)
t.hideturtle() 
t.mainloop()

