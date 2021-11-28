from data_structure.binary_tree import BinaryTree
from data_structure.queue_ import Queue

def search(args):
    bt = BinaryTree()
    bt.insert_data_from_file(args.file)
    
    if args.order == "level-order":
        target = args.word
        
        if bt.root.data == target:
            print("word found")
            return
        queue = Queue()
        queue.enqueue(bt.root)
        while queue.get_len():
            node = queue.dequeue()
            if node.left:
                if node.left.data == target:
                    print("word found")
                    return
                else:
                    queue.enqueue(node.left)
            if node.right:
                if node.right.data == target:
                    print("word found")
                    return
                else:
                    queue.enqueue(node.right)
        print("word not found ;( ")
        return
    print("breadth-first-search can only be used with --order 'level-order'")