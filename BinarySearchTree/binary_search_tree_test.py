from binary_search_tree import BinarySearchTree

data = [
    {
		"id": 1,
		"val": 100,
 	},
    {
		"id": 2,
		"val": 200
	},
    {
		"id": 3,
		"val": 300
	}
    
]

bst = BinarySearchTree()
for d in data:
    bst.insert({
		"id": d["id"],
		"val": d["val"]	
	})

print(bst.search(1))