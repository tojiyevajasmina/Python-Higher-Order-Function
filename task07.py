from rich.console import Console
console = Console()

def main():
    prices = ["$120", "$340", "$50", "$90"]

    faqat_raqamlar = map(lambda p: p.replace("$",""), prices)

    console.print(list(faqat_raqamlar),style = 'italic yellow')

main()