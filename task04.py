from rich.console import Console
console = Console()

def main():
    names = ["Zafar", "Ali", "Sami", "Bekzod"]
    ismlar = sorted(names)

    console.print(ismlar,style = 'bold red')

main()