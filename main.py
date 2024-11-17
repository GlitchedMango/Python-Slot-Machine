from random import randint 
from numpy import array, compress
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
import os

console = Console

class SlotMachine: 
    def __init__(self) -> None: 
        self.test_array = array([[randint(1, 3), randint(1, 3), randint(1, 3)],
                        [randint(1, 3), randint(1, 3), randint(1, 3)],
                        [randint(1, 3), randint(1, 3), randint(1, 3)]])

        self.lines = [{"name": "horizontal_line_0", "value": compress([True, False, False], self.test_array, axis=0)},
             {"name": "horizontal_line_1", "value": compress([False, True, False], self.test_array, axis=0)},
             {"name": "horizontal_line_2", "value": compress([False, False, True], self.test_array, axis=0)}]
    
    def check_lines(self):

        for line in self.lines:
            if all(x == line["value"][0][0] for x in line["value"][0]):
                print(line["name"])
        print(self.test_array)


if __name__ == "__main__":
    slotmachine = SlotMachine()
    slotmachine.check_lines()
