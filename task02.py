from rich.console import Console
console = Console()

def main():
    nums = [1, 2, 3, 4, 5]

    kvadrat = map(lambda x: x ** 2, nums)

    console.print(list(kvadrat),style = ' bold green')

main()