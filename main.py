from random import sample
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
        
        #self.ease_out_curve = [""]

    def randomize_slots(self):
        self.slot_lists = [{"name": "slot_list1", "value": sample(self.const_list, len(self.const_list))},
                           {"name": "slot_list2", "value": sample(self.const_list, len(self.const_list))},
                           {"name": "slot_list3", "value": sample(self.const_list, len(self.const_list))}]

    def shift_list(self, slot_list):
        slot_list.insert(0, slot_list.pop(0))

        self.displayed_row0 = [self.slot_lists[0]["value"][0], self.slot_lists[1]["value"][0], self.slot_lists[2]["value"][0]]
        self.displayed_row1 = [self.slot_lists[0]["value"][1], self.slot_lists[1]["value"][1], self.slot_lists[2]["value"][1]]
        self.displayed_row2 = [self.slot_lists[0]["value"][2], self.slot_lists[1]["value"][2], self.slot_lists[2]["value"][2]]

        console.print(self.displayed_row0, "__", self.displayed_row1, "__", self.displayed_row2)

        console.print("____")
    def check_lines(self):
        for slot_list in self.slot_lists:
            if all(x == slot_list["value"][0] for x in slot_list["value"]):
                print(slot_list["name"])

    def start_game(self):
        self.randomize_slots()
        self.check_lines()
        self.shift_list(self.slot_lists[0]["value"])
        self.shift_list(self.slot_lists[1]["value"])
        self.shift_list(self.slot_lists[2]["value"])
        self.draw_screen()

    def draw_screen(self):
       #slot_table = Table(style="yellow", show_header=False)
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
