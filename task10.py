from rich.console import Console
console = Console()

def main():
    text = ["apple", "34", "banana", "100", "abc", "75"]

    son = filter(lambda x: x.isdigit(), text)

    console.print(list(son),style = 'bold green')

main()