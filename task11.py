from rich.console import Console
console = Console()

def main():
    nums = list(range(1, 21))

    juft = filter(lambda x: x % 2 == 0, nums)

    kvadrat = map(lambda x: x ** 2, juft)

    console.print(list(kvadrat),style = 'bold magenta')

main()