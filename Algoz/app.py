import argparse
from Algoz.algorithms.search.breadth_first_search import search

def main():
    """
        created a argparser for the CLI app with sorts of sub commands within it
    """
    parser = argparse.ArgumentParser(
        usage="search a word with the help of different sets of searching algorithms",
        description="A CLI Application helps to perform searching operation on the given input file",
        exit_on_error=False
    )
    
    # sub commands (using flags)
    
    # 1. input string to be search
    parser.add_argument("-w", "--word", required=True, help="Input String To Be Searched For")
    
    # 2. file path from where to be searched
    parser.add_argument("-f", "--file", required=True, help="Path To File That To Be Searched")
    
    # 3. searching algorithms
    parser.add_argument("-sa", "--search-algorithm",choices=["binary-search","depth-first-search","breadth-first-search"], required=True, help="The Algorithm To Be Used To Perform Search")
        
    # 4. order at what searching will be performed
    parser.add_argument("-o", "--order",choices=["pre-order","post-order","level-order"], required=True, help="The Order In Which To Traverse Tree")
    
    args = parser.parse_args()
    
    if args.search_algorithm == "binary-search": 
        search()
    
    if args.search_algorithm == "depth-first-search": 
        pass
    
    if args.search_algorithm == "breadth-first-search": 
        pass
    


if __name__ == "__main__":
    main()
    
    
    