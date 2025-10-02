from rich.console import Console
console = Console()

def main():
    names = ["Ali", "Valijon", "Sami", "Diyorbek"]

    mx = max(names, key = len)
    console.print(mx,style = 'italic cyan')

main()