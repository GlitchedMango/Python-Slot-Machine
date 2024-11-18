from random import randint 
from numpy import array, compress
from rich.panel import Panel
from rich.table import Table
from rich import padding, print, box
from rich.console import Console
import os

console = Console(style="") 

class SlotMachine: 
    def __init__(self) -> None: 
        self.lines = [{"name": "hor_line_1", "value": [randint(1, 3), randint(1, 3), randint(1, 3)]},
             {"name": "hor_line_2", "value": [randint(1, 3), randint(1, 3), randint(1, 3)]},
             {"name": "hor_line_3", "value": [randint(1, 3), randint(1, 3), randint(1, 3)]}]
        self.clear = lambda:os.system("cls")
    
    def check_lines(self):
        for line in self.lines:
            if all(x == line["value"][0] for x in line["value"]):
                print(line["name"])

    def start_game(self):
        self.check_lines()
        self.draw_screen()

    def draw_screen(self):
        slot_table = Table(style="yellow", show_header=False)
        slot_table.add_row(str(self.lines[-1]["value"][0]), str(self.lines[0]["value"][1]), str(self.lines[0]["value"][2]))
        slot_table.add_row(str(self.lines[0]["value"][0]), str(self.lines[1]["value"][1]), str(self.lines[1]["value"][2]))
        slot_table.add_row(str(self.lines[1]["value"][0]), str(self.lines[2]["value"][1]), str(self.lines[2]["value"][2]))

        gui_grid = Table.grid(expand=True)
        gui_grid.add_row(Panel(":snake: Python Slot Machine :snake:"))
        gui_grid.add_row(Panel(slot_table, expand=True))

        console.print(gui_grid, style="yellow", justify="center")

if __name__ == "__main__":
    slotmachine = SlotMachine()
    slotmachine.start_game()
    slotmachine.check_lines()
