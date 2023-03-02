import tkinter as tk

class App:
    def __init__(self, size, bg):
        self.title = "Game"
        self.size = size
        self.bg_color = bg
        self.running = True

    def create_canvas(self):
        self.window = tk.Tk()
        self.window.geometry(str(self.size) + "x" + str(self.size))
        self.window.title(self.title)
        self.window.resizable(0, 0)

        self.c = tk.Canvas(self.window, width = self.size, height = self.size, bg = self.bg_color)
        self.c.place(relx = 0.5, rely = 0.5, anchor = "center")

        self.window.bind("<Escape>", self.end)
    
    def run(self):
        while self.running:
            self.window.update()

    def end(self, event):
        self.running = False

if __name__ == "__main__":
    app = App(500, "grey")
    app.create_canvas()
    app.run()
