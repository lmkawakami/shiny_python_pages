from shiny import render, ui
from shiny.express import input

ui.panel_title("Hello Shiny!")
ui.input_slider("n", "N", 0, 100, 20)
ui.input_slider("x", "X", 0, 100, 20)


@render.text
def txt_n():
    return f"n*2 is {input.n() * 2}"

@render.text
def txt_x():
    return f"x² is {input.x() ** 2}"