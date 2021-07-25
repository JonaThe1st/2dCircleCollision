import tkinter as tk
import numpy as np
import random
import time
from tkinter import messagebox

from vector import Vector2d
from ball import Ball

class Main(tk.Canvas):

    def __init__(self, master, size, ball_count, dt, height=450, width=800):
        super().__init__(master, height=height, width=width)

        self.size = size
        self.ball_count = ball_count
        self.height = height
        self.width = width
        self.dt = dt
        self.time = 0

        self.pack()

        self.create_rectangle(2, 2, self.width, self.height)

        self.balls = []
        for i in range(self.ball_count):
            
            pos = Vector2d(random.randrange(self.width-self.size), random.randrange(self.height-self.size))

            ok = False
            start = time.time()
            while not ok:
                ok = True
                for j in range(i):
                    if abs(pos - self.balls[j].pos) <= self.size+2:
                        pos = Vector2d(random.randrange(self.width-self.size), random.randrange(self.height-self.size))
                        ok = False
                if time.time() - start > .2:
                    self.destroy()

                    messagebox.showinfo("Fehler", "das sind zu viele oder zu große Kugeln für den Bildschirm")
                    del self
                    return

            
            if i == 0:
                b = Ball(self.create_oval(pos.x-self.size/2, pos.y-self.size/2, pos.x+self.size/2, pos.y+self.size/2, outline="red", fill="red"), pos, Vector2d())
                self.balls.append(b)
            else:        
                b = Ball(self.create_oval(pos.x-self.size/2, pos.y-self.size/2, pos.x+self.size/2, pos.y+self.size/2, fill="black"), pos, Vector2d())
                self.balls.append(b)

        self.balls = np.array(self.balls)

        self.after(self.dt, self.loop)
        self.bind("<1>", self.boost)

    def loop(self):

        # Move objects
        for ball in self.balls:
            if ball.pos.x > self.width-self.size/2:
                ball.v = Vector2d(-abs(ball.v.x), ball.v.y)
            elif ball.pos.x < self.size/2:
                ball.v = Vector2d(abs(ball.v.x), ball.v.y)
            elif ball.pos.y > self.height-self.size/2:
                ball.v = Vector2d(ball.v.x, -abs(ball.v.y))
            elif ball.pos.y < self.size/2:
                ball.v = Vector2d(ball.v.x, abs(ball.v.y))
        
            self.move(ball.id, ball.v.x*self.dt, ball.v.y*self.dt)
            ball.pos += ball.v*self.dt
        
        kinetic = 0
        # Detect Collisions
        for i, ball in enumerate(self.balls):
            for j in range(i+1, self.ball_count):
                if abs(ball.pos - self.balls[j].pos) <= self.size:

                    vges = ball.v - self.balls[j].v
                    if abs(ball.pos - self.balls[j].pos) < abs(ball.pos+ball.v - (self.balls[j].pos + self.balls[j].v)):
                        continue

                    v2 = (self.balls[j].pos - ball.pos)
                    v2 = Vector2d(v2/abs(v2))
                    v1 = Vector2d(-v2.y, v2.x)


                    # Solve v1 + v2 = vges
                    v2 = Vector2d(v2 * (vges.y*v1.x-vges.x*v1.y)/(v1.x*v2.y-v1.y*v2.x))
                    v1 = vges - v2

                    # transform to resting reference system
                    ball.v = v1 + self.balls[j].v
                    self.balls[j].v += v2

            kinetic += .5*ball.v**2

        self.time += self.dt

        '''if self.time % 500 == 0:
           print(kinetic)'''
           
        self.after(self.dt, self.loop)

    def boost(self, event):
        bm = self.balls[0].pos - Vector2d(event.x, event.y)

        bm = Vector2d((bm / abs(bm)) * 0.1)

        self.balls[0].v -= bm

def start(main_frame):
    print("start")

    m = Main(main_frame, 50, 20, 10)

if __name__ == "__main__":
    root = tk.Tk()

    main_frame = tk.Frame(root, height=450, width=800)
    main_frame.pack(side=tk.LEFT)

    control_frame = tk.Frame(root)

    tk.Button(control_frame, text="Starten", command=lambda: start(main_frame)).pack()

    control_frame.pack(side=tk.LEFT)

    tk.mainloop()
