import tkinter as tk

class DrawingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Notepad with Ink")

        # Create Canvas
        self.canvas = tk.Canvas(self.master, bg="white", width=800, height=600)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Bind mouse events
        self.canvas.bind("<B1-Motion>", self.draw)

        # Initialize drawing attributes
        self.prev_x = None
        self.prev_y = None
        self.color = "black"
        self.pen_size = 2

    def draw(self, event):
        x, y = event.x, event.y
        if self.prev_x and self.prev_y:
            self.canvas.create_line(self.prev_x, self.prev_y, x, y, fill=self.color, width=self.pen_size)
        self.prev_x, self.prev_y = x, y

    def clear_canvas(self):
        self.canvas.delete("all")

def main():
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()