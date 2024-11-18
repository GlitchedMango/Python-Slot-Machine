from random import shuffle, sample
from numpy import array, compress
from rich.panel import Panel
from rich.table import Table
from rich import padding, print, box
from rich.console import Console
import os
# TODO:
# Niet cooked UI
# Spinning
# 

console = Console(style="") 

class SlotMachine: 
    def __init__(self) -> None:

        self.const_list = 10*["A"] + 5*["B"] + 1*["C"] 

        self.clear = lambda:os.system("cls")
    def randomize_slots(self):
        self.slot_lists = [{"name": "slot_list1", "value": sample(self.const_list, len(self.const_list))},
                           {"name": "slot_list2", "value": sample(self.const_list, len(self.const_list))},
                           {"name": "slot_list3", "value": sample(self.const_list, len(self.const_list))}]

    def shift_slot_lists(self):
        for slot_list in self.slot_lists:
            console.print(slot_list)
            slot_list["value"].append(slot_list["value"].pop(0))
            console.print(slot_list["name"], slot_list["value"])

    def check_lines(self):
        for slot_list in self.slot_lists:
            if all(x == slot_list["value"][0] for x in slot_list["value"]):
                print(slot_list["name"])

    def start_game(self):
        console.print(self.const_list)
        self.randomize_slots()
        self.shift_slot_lists()
        self.check_lines()
        self.draw_screen()

    def draw_screen(self):
       # slot_table = Table(style="yellow", show_header=False)
        #slot_table.add_row(str(self.lines[-1]["value"][0]), str(self.lines[0]["value"][1]), str(self.lines[0]["value"][2]))
        #slot_table.add_row(str(self.lines[0]["value"][0]), str(self.lines[1]["value"][1]), str(self.lines[1]["value"][2]))
        #slot_table.add_row(str(self.lines[1]["value"][0]), str(self.lines[2]["value"][1]), str(self.lines[2]["value"][2]))

       # gui_grid = Table.grid(expand=True)
       # gui_grid.add_row(Panel(":snake: Python Slot Machine :snake:"))
       # gui_grid.add_row(Panel(slot_table, expand=True))

        #console.print(gui_grid, style="yellow", justify="center")
        return

if __name__ == "__main__":
    slotmachine = SlotMachine()
    slotmachine.start_game()
    slotmachine.check_lines()
