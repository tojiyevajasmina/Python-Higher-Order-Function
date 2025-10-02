from rich.console import Console
console = Console()

def main():
    numbers = [4, -2, 0, 7, -9, 3, -1, 5]

    musbat_sonlar = filter(lambda x: x > 0, numbers)

    console.print(list(musbat_sonlar), style = 'italic yellow')


main()
