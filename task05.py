from rich.console import Console
console = Console()

def main():
    nums = [2, 4, 6, 8]
    son = map(lambda x: x * 5, nums)

    console.print(list(son),style = 'italic blue')

    
main()