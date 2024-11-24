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
# Game looping, bet changing

console = Console(style="yellow") 

class SlotMachine: 
    def __init__(self) -> None:
        self.const_list = 10*[":dollar_banknote:"] + 5*[":money_bag:"] + 1*[":gem_stone:"] 
        
        self.balance = 5000
        self.bet = 100
        self.status_message = "Spinning..."
        self.clear = lambda:system("cls")
        
        self.slot_lists = [{"name": "slot_list1", "value": sample(self.const_list, len(self.const_list))},
                           {"name": "slot_list2", "value": sample(self.const_list, len(self.const_list))},
                           {"name": "slot_list3", "value": sample(self.const_list, len(self.const_list))}]
        
        self.displayed_row0 = [self.slot_lists[0]["value"][0], self.slot_lists[1]["value"][0], self.slot_lists[2]["value"][0]]
        self.displayed_row1 = [self.slot_lists[0]["value"][1], self.slot_lists[1]["value"][1], self.slot_lists[2]["value"][1]]
        self.displayed_row2 = [self.slot_lists[0]["value"][2], self.slot_lists[1]["value"][2], self.slot_lists[2]["value"][2]]
       
        self.sleep_curve = 5*[0.25] + 4*[0.5] + 3*[0.75] + [1] + [1.5]
        self.sleep_interval = 0
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
        reward_values = [{"slot": ":dollar_banknote:", "reward": 2},
                         {"slot": ":money_bag:", "reward": 4},
                         {"slot": ":gem_stone:", "reward": 8}]
        print("1")
        if all(x == self.displayed_row1[0] for x in self.displayed_row1):
            for value in reward_values:
                if self.displayed_row1[0] == value["slot"]:
                    win_amount = self.bet * value["reward"]
                    self.balance += win_amount
                    self.status_message = f"You won {win_amount}$!"
        else:
            self.balance -= self.bet
            self.status_message = f"You lost {self.bet}$!"
    
    def update_screen(self):
        slot_table = Table(style="yellow", show_header=False)
        
        slot_table.add_row(str(self.displayed_row0[0]), str(self.displayed_row0[1]), str(self.displayed_row0[2]))
        slot_table.add_row(str(self.displayed_row1[0]), str(self.displayed_row1[1]), str(self.displayed_row1[2]))
        slot_table.add_row(str(self.displayed_row2[0]), str(self.displayed_row2[1]), str(self.displayed_row2[2]))
        
        info_grid = Table.grid(expand=True)
        info_grid.add_row(f"    Current balance: {str(self.balance)}$")
        info_grid.add_row(f"\n-   {self.status_message}")

        slot_grid = Table.grid(expand=True)
        slot_grid.add_row(slot_table, info_grid, style="yellow")
        
        return Align.center(Align.center(Panel(slot_grid, style="yellow", title="Python Slots")))

    def spin_sequence(self):
        sleep(self.sleep_curve[self.sleep_interval])
        self.sleep_interval += 1
        self.shift_list(self.slot_lists[0]["value"])
        self.shift_list(self.slot_lists[1]["value"])
        self.shift_list(self.slot_lists[2]["value"])

    def start_game(self):
        self.clear()
        #self.randomize_slots()
        with Live(refresh_per_second=24) as live:
            live.update(self.update_screen())
            for _ in range(len(self.sleep_curve)):
                self.spin_sequence() 
                live.update(self.update_screen())
            self.check_lines()
            live.update(self.update_screen())


if __name__ == "__main__":
    slotmachine = SlotMachine()
    slotmachine.start_game()
