from rich.console import Console
console = Console()

def main():
    people = [
  {"name": "Ali", "age": 25},
  {"name": "Sami", "age": 19},
  {"name": "Lola", "age": 31}
]

    ism= sorted(people, key=lambda p: p['age'])

    console.print(ism,style = 'bold yellow')

main()