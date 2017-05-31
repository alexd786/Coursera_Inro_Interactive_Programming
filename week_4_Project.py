#http://www.codeskulptor.org/#user42_g405ImP2In_0.py

# template for "Stopwatch: The Game"
import simplegui

# define global variables
t = 0
stops = 0
num_correct = 0 
running = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    m = t / 600
    s = t % 600
    if s < 10:
        z = 0
    else:
        z = str(s)[-2]
    if s < 100:
        x = 0
    else:
        x = str(s)[-3]
    return str(m) + ":" + str(x) + str(z) + "." + str(s)[-1]
    
# cleaner way

#def format(t):
#    m = t // 600
#    tens = ((t % 600) // 10) // 10
#    seconds  = ((t % 600) // 10) % 10
#    tenths = t % 10 
#    return str(m) + ":" + str(tens) + str(seconds) +"." + str(tenths)

    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_timer():
    global running
    timer.start()
    running = True
    
    
def stop_timer():
    global stops, num_correct, running
    timer.stop()
    if running:
        stops += 1
    if running and t % 10 == 0:
        num_correct += 1
    running = False
    
def reset_timer():
    global t, num_correct, stops
    t = 0
    num_correct = 0 
    stops = 0
    

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global t
    t += 1
    

# define draw handler
def draw(canvas):
    global t, stops, num_correct
    canvas.draw_text(format(t),(50,100),48,"Green")
    canvas.draw_text(str(num_correct) + "/" + str(stops),(155,25),24,"Red")
    
# create frame
frame = simplegui.create_frame("Game",200,200)

# register event handlers
timer = simplegui.create_timer(100,timer_handler)
frame.set_draw_handler(draw)
frame.add_button("Start",start_timer,100)
frame.add_button("Stop",stop_timer,100)
frame.add_button("Rest",reset_timer,100)


# start frame
frame.start()

# Please remember to review the grading rubric
