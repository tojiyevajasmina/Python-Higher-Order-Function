from rich.console import Console
console = Console()

def main():
    students = [
  {"name": "Aziz", "grade": 89},
  {"name": "Kamola", "grade": 95},
  {"name": "Javlon", "grade": 76}
]

    nom = sorted(students, key=lambda student: student["grade"])

    console.print(nom,style = 'italic yellow')

main()