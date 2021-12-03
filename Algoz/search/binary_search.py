from rich.console import Console
import datetime
from time import sleep
from data_structure.binary_tree import BinaryTree


# globals 
console = Console(width=100)
found_style = "bold white"
not_found_style = "bold white on red"
tasks = [f"Task {n}" for n in ["Building Tree...","Tree Built!", "Searching Tree..."]]


def bst_search_recursive(target,node):
    if int(node.data) == int(target):
        return True
    
    elif int(node.data) > int(target) and node.left is not None:
        return bst_search_recursive(target,node.left)
    
    elif int(node.data) < int(target) and node.right is not None:
        
        return bst_search_recursive(target,node.right)
    else:
        return False
    
        
        

def bst_search(root,target):
    if root is None:
        return False
    return bst_search_recursive(target,root)

def search(args):
    with console.status("[bold magenta]Working on tasks...") as status:
        while tasks:
            task = tasks.pop(0)
            sleep(1)
            console.log(f"[bold red]{task} complete")
            
    target = args.word    
    start_time = datetime.datetime.now()
    bst = BinaryTree()
    bst.insert_data_from_file_for_bst(args.file)
    if bst_search(bst.root,target):
        end_time = datetime.datetime.now()
        time_diff = (end_time - start_time)
        execution_time = time_diff.total_seconds() * 1000
        console.print(f"Execution Time [bold magenta]{execution_time}[/bold magenta] ms")
        console.print("Word, [bold magenta]Found[/bold magenta]!", ":vampire:", locals(),style=found_style)
        return
    else:
        console.print("Word, [bold magenta]Not Found[/bold magenta]", ":pile_of_poo:", locals(),style=not_found_style)
        return
    