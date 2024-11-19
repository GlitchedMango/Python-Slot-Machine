from random import sample
from rich.panel import Panel
from rich.table import Table
from rich import print, box
from rich.live import Live
from rich.console import Console
from rich.align import Align
from os import system
from time import sleep
# TODO:
# Niet cooked UI
# Spinning
# 

console = Console(style="yellow") 

class SlotMachine: 
    def __init__(self) -> None:

        self.const_list = 10*["A"] + 5*["B"] + 1*["C"] 

        self.clear = lambda:system("cls")
        
        #self.ease_out_curve = [""]

    def randomize_slots(self):
        self.slot_lists = [{"name": "slot_list1", "value": sample(self.const_list, len(self.const_list))},
                           {"name": "slot_list2", "value": sample(self.const_list, len(self.const_list))},
                           {"name": "slot_list3", "value": sample(self.const_list, len(self.const_list))}]

    def shift_list(self, slot_list):
        slot_list.insert(0, slot_list.pop(len(slot_list) - 1))
        self.displayed_row0 = [self.slot_lists[0]["value"][0], self.slot_lists[1]["value"][0], self.slot_lists[2]["value"][0]]
        self.displayed_row1 = [self.slot_lists[0]["value"][1], self.slot_lists[1]["value"][1], self.slot_lists[2]["value"][1]]
        self.displayed_row2 = [self.slot_lists[0]["value"][2], self.slot_lists[1]["value"][2], self.slot_lists[2]["value"][2]]

    def check_lines(self):
        if all(self.displayed_row1):
            console.print("&")
        else:
            console.print("a")

    def update_screen(self):
        slot_table = Table(style="yellow", show_header=False)

        self.shift_list(self.slot_lists[0]["value"])
        slot_table.add_column("")
        slot_table.add_column("")
        slot_table.add_column("")
        slot_table.add_column("")
        slot_table.add_row(str(self.displayed_row0[0]), str(self.displayed_row0[1]), str(self.displayed_row0[2]), style="dim yellow")
        slot_table.add_row(str(self.displayed_row1[0]), str(self.displayed_row1[1]), str(self.displayed_row1[2]), style="yellow")
        slot_table.add_row(str(self.displayed_row2[0]), str(self.displayed_row2[1]), str(self.displayed_row2[2]), style="dim yellow")

        gui_grid = Table.grid(expand=True)
        gui_grid.add_row(Panel(":snake: Python Slot Machine :snake:"), style="yellow")
        gui_grid.add_row(Align.center(Panel(slot_table, style="yellow")))
        
        #console.print(gui_grid, style="yellow", justify="center")
        return Align.center(gui_grid)
    def start_game(self):
        self.randomize_slots()
        with Live() as live:
            while True:
                sleep(1)
                live.update(self.update_screen())
                self.check_lines()

if __name__ == "__main__":
    slotmachine = SlotMachine()
    slotmachine.start_game()
