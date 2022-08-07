import tkinter as tk
from time import sleep


class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.status = tk.StringVar()
        tk.Label(self, textvariable=self.status).pack()
        tk.Button(self, text="Run Process",
            command=self.run_process).pack()

    def run_process(self):
        self.status.set("Starting process")
        self.after(50, self._run_phases)

    def _run_phases(self):
        for phase in range(1, 5):
            self.status.set(f"Phase {phase}")
            self.update_idletasks()
            self.process_phase(phase, 2)
        self.status.set('Complete')

    def process_phase(self, n, length):
        sleep(length)


App().mainloop()
