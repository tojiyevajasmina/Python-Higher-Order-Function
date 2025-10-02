from rich.console import Console
console = Console()

def main():
    numbers = [18, 29, 3, 45, 7, 12]

    eng_kichik = min(numbers)
    eng_katta = max(numbers)

    console.print("Eng kichik son:", eng_kichik,style = 'italic magenta')
    console.print("Eng katta son:", eng_katta,style = 'italic cyan')

main()