from rich.console import Console
from data_structure.binary_tree import BinaryTree
from data_structure.queue_ import Queue
from time import sleep
import datetime

# globals 
console = Console(width=100)
found_style = "bold white"
not_found_style = "bold white on red"
tasks = [f"Task {n}" for n in ["Building Tree...","Tree Built!", "Searching Tree..."]]


def search(args):
    with console.status("[bold magenta]Working on tasks...") as status:
        while tasks:
            task = tasks.pop(0)
            sleep(1)
            console.log(f"[bold red]{task} complete")
    start_time = datetime.datetime.now()        
    bt = BinaryTree()
    bt.insert_data_from_file(args.file)
    if args.order == "level-order":
        target = args.word
        
        if bt.root.data == target:
            console.print("Word, [bold magenta]Found[/bold magenta]!", ":vampire:", locals())
            return
        queue = Queue()
        queue.enqueue(bt.root)
        while queue.get_len():
            node = queue.dequeue()
            if node.left:
                if node.left.data == target:
                    end_time = datetime.datetime.now()
                    time_diff = (end_time - start_time)
                    execution_time = time_diff.total_seconds() * 1000
                    console.print(f"Execution Time [bold magenta]{execution_time}[/bold magenta] ms")
                    console.print("Word, [bold magenta]Found[/bold magenta]!", ":vampire:", locals(),style=found_style)          
                    return
                else:
                    queue.enqueue(node.left)
            if node.right:
                if node.right.data == target:
                    end_time = datetime.datetime.now()
                    time_diff = (end_time - start_time)
                    execution_time = time_diff.total_seconds() * 1000
                    console.print(f"Execution Time [bold magenta]{execution_time}[/bold magenta] ms")
                    console.print("Word, [bold magenta]Found[/bold magenta]!", ":vampire:", locals())                    
                    return
                else:
                    queue.enqueue(node.right)
        end_time = datetime.datetime.now()
        time_diff = (end_time - start_time)
        execution_time = time_diff.total_seconds() * 1000
        console.print(f"Execution Time [bold magenta]{execution_time}[/bold magenta] ms")            
        console.print("Word, [bold magenta]Not Found[/bold magenta]", ":pile_of_poo:", locals(),style=not_found_style)
        return
    console.print("[bold underline red]breadth-first-search can only be used with --order level-order[/bold underline red]", ":raccoon:", locals())

        
        