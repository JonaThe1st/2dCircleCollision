import tkinter as tk

from main import Main

class Gui(tk.Tk):

  def __init__(self):
    super().__init__()
    self.m = None
    self.size = tk.IntVar(self, 50)
    self.ball_count = tk.IntVar(self, 20)
    self.dt = tk.IntVar(self, 10)


    self.main_frame = tk.Frame(self, height=450, width=800)
    self.main_frame.pack(side=tk.LEFT)

    control_frame = tk.Frame(self)

    tk.Label(control_frame, text="Größe der Kugeln").pack()
    tk.Entry(control_frame, textvariable=self.size).pack()

    tk.Label(control_frame, text="Anzahl der Bälle").pack()
    tk.Entry(control_frame, textvariable=self.ball_count).pack()

    tk.Label(control_frame, text="dt").pack()
    tk.Entry(control_frame, textvariable=self.dt).pack()

    tk.Button(control_frame, text="Starten", command=self.start).pack()

    control_frame.pack(side=tk.LEFT)


  def start(self):
    if isinstance(self.m, Main):
      self.m.destroy()
    self.m = Main(self.main_frame, self.size.get(), self.ball_count.get(), self.dt.get())

if __name__ == "__main__":
  window = Gui()

  tk.mainloop()
