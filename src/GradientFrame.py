import tkinter as tk


class GradientFrame(tk.Canvas):

    def __init__(self, parent, color1="red", color2="black", bg_color="white", **kwargs):
        tk.Canvas.__init__(self, parent, **kwargs)
        self._color1 = color1
        self._color2 = color2
        self._bg_color = bg_color
        self.bind("<Configure>", self._draw_gradient)

    def _draw_gradient(self, event=None):
        # Drawing of the gradient
        self.delete("gradient")
        width = self.winfo_width()
        height = self.winfo_height()
        limit = width
        gradient_height = int(height * 0.25)
        (r1, g1, b1) = self.winfo_rgb(self._color1)
        (r2, g2, b2) = self.winfo_rgb(self._color2)
        r_ratio = float(r2 - r1) / limit
        g_ratio = float(g2 - g1) / limit
        b_ratio = float(b2 - b1) / limit

        for i in range(limit):
            nr = int(r1 + (r_ratio * i))
            ng = int(g1 + (g_ratio * i))
            nb = int(b1 + (b_ratio * i))
            color = "#%4.4x%4.4x%4.4x" % (nr, ng, nb)
            self.create_line(i, 0, i, gradient_height, tags=("gradient",), fill=color)

        # Fill the rest with bg_color
        self.create_rectangle(0, gradient_height, width, height, fill=self._bg_color, outline="")

        self.lower("gradient")
