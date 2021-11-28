from rich.console import Console
import datetime
from time import sleep
from data_structure.binary_tree import BinaryTree

# globals 
console = Console(width=100)
found_style = "bold white"
not_found_style = "bold white on red"
tasks = [f"Task {n}" for n in ["Building Tree...","Tree Built!", "Searching Tree..."]]

"""
    traversal:
            root -> left -> right
"""
def pre_order_search(target,root):
    if root:
        if root.data == target:
            return True
        
        if pre_order_search(target,root.left):
            return True
        
        if pre_order_search(target,root.right):
            return True
          
    return False

"""
    traversal:
            left -> right -> root
"""
def post_order_search(target,root):
    if root:
        if post_order_search(target,root.left):
            return True
        
        if post_order_search(target,root.right):
            return True

        if root.data == target:
            return True
    return False


"""
    traversal:
            left -> root -> right
"""
def in_order_search(target,root):
    if root:
        if in_order_search(target,root.left):
            return True
        
        if root.data == target:
            return True
        
        if in_order_search(target,root.right):
            return True
        
    return False
def search(args):
    with console.status("[bold magenta]Working on tasks...") as status:
        while tasks:
            task = tasks.pop(0)
            sleep(1)
            console.log(f"[bold red]{task} complete")
            
    target = args.word
    
    if args.order == 'pre-order':
        start_time = datetime.datetime.now()
        bt = BinaryTree()
        bt.insert_data_from_file(args.file)
        if pre_order_search(target,bt.root):
            end_time = datetime.datetime.now()
            time_diff = (end_time - start_time)
            execution_time = time_diff.total_seconds() * 1000
            console.print(f"Execution Time [bold magenta]{execution_time}[/bold magenta] ms")
            console.print("Word, [bold magenta]Found[/bold magenta]!", ":vampire:", locals(),style=found_style)
            return
        else:
            console.print("Word, [bold magenta]Not Found[/bold magenta]", ":pile_of_poo:", locals(),style=not_found_style)
            return
                               
    if args.order == 'post-order':
        start_time = datetime.datetime.now()
        bt = BinaryTree()
        bt.insert_data_from_file(args.file)
        if post_order_search(target,bt.root):
            end_time = datetime.datetime.now()
            time_diff = (end_time - start_time)
            execution_time = time_diff.total_seconds() * 1000
            console.print(f"Execution Time [bold magenta]{execution_time}[/bold magenta] ms")
            console.print("Word, [bold magenta]Found[/bold magenta]!", ":vampire:", locals(),style=found_style)
            return
        else:
            console.print("Word, [bold magenta]Not Found[/bold magenta]", ":pile_of_poo:", locals(),style=not_found_style)
            return
        
    if args.order == 'in-order':
        start_time = datetime.datetime.now()
        bt = BinaryTree()
        bt.insert_data_from_file(args.file)
        if in_order_search(target,bt.root):
            end_time = datetime.datetime.now()
            time_diff = (end_time - start_time)
            execution_time = time_diff.total_seconds() * 1000
            console.print(f"Execution Time [bold magenta]{execution_time}[/bold magenta] ms")
            console.print("Word, [bold magenta]Found[/bold magenta]!", ":vampire:", locals(),style=found_style)
            return
        else:
            console.print("Word, [bold magenta]Not Found[/bold magenta]", ":pile_of_poo:", locals(),style=not_found_style)
            return
        