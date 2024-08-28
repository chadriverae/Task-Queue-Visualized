import matplotlib.pyplot as plt
import time
class Task():
    def __init__(self, id, cycles_left):
        self.id = id
        self.cycles_left = cycles_left
        self.prev = self.next = None

    def reduce_cycles(self, amount):
        self.cycles_left -= amount
        if self.cycles_left < 0:
            self.cycles_left = 0
    
class TaskQueue():
    def __init__(self, cycles_per_task=1):
        self.current = None
        self.cycles_per_task = cycles_per_task
        self.length = 0
        self.id_dict = {}
        
    def len(self):
        return self.length
    
    def is_empty(self):
        return self.length == 0
    
    def add_task(self, task):
        # Case 1 (1st task to be added)
        if self.is_empty():
            self.current = self.current.prev = self.current.next = task
        # Case 2 (2nd Task to be added)
        elif self.length == 1:
            task.prev = task.next = self.current
            self.current.prev = self.current.next = task
        # Case 3 (Squeeze!)
        else:
            task.next = self.current
            task.prev = self.current.prev
            self.current.prev.next = task
            self.current.prev = task # Sandwich new task between two tasks
        
        self.id_dict[task.id] = task
        self.length += 1
    
    def remove_task(self, id):
        """Removes the task with a given id"""
        if id in self.id_dict:
            task = self.id_dict[id]
            if self.length == 1:
                self.current = None
            else: 
                if self.current == task:
                    self.current = self.current.next
                task.prev.next = task.next
                task.next.prev = task.prev
            del task    # Wipe task from existance!
            self.id_dict.pop(id)
            self.length -= 1
        else:
            raise RuntimeError(f'id {id} not in TaskQueue')
        
    def execute_tasks(self):    
        def redraw():
            plt.pie(sizes, labels = labels, startangle = 90,
            colors = colors, counterclock = False)
            plt.draw()
            plt.pause(.2)
            time.sleep(.2)
        clock_cycles = 0
        labels = []
        sizes = []
        colors = []
        amount_completed = 0
        for i in range(self.length):
                labels.append(f'Task {self.current.id}: {self.current.cycles_left}')
                self.current = self.current.next
        for i in range(len(labels)):
            sizes.append(100/len(labels))
        for i in range(len(labels)):
            colors.append('gray')
        current_idx = 0
        while self.length != 0:
            if self.length > 1:
                colors[current_idx - 1] = "gray"
            colors[current_idx] = "red"
            redraw()
            plt.close()

            if self.cycles_per_task >= self.current.cycles_left:
                temp = self.current.cycles_left
                self.current.reduce_cycles(self.cycles_per_task)

                labels[current_idx] = f'Task {self.current.id}: {self.current.cycles_left}'
                redraw()
                plt.close()
                del labels[current_idx]
                del sizes[current_idx]
                del colors[current_idx]

                clock_cycles += temp
                print(f'Finished Task {self.current.id} after {clock_cycles} clock cycles')
                self.remove_task(self.current.id)
                amount_completed += 1
               
            else: 
                self.current.reduce_cycles(self.cycles_per_task)

                labels[current_idx] = f'Task {self.current.id}: {self.current.cycles_left}'
                redraw()

                clock_cycles += self.cycles_per_task
                self.current = self.current.next
                current_idx += 1
            if current_idx == self.length:
                current_idx = 0
            
        return clock_cycles

    def show_queue(self):
        labels = []
        for i in range(self.length):
                labels.append(f'Task {self.current.id}: {self.current.cycles_left}')
                self.current = self.current.next
        sizes = []
        for i in range(len(labels)):
            sizes.append(100/len(labels))
        plt.pie(sizes, labels = labels, startangle = 90, counterclock = False)
        plt.show()
