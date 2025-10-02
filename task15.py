from rich.console import Console
console = Console()

def main():
    votes = [
  {"option": "A", "votes": 123},
  {"option": "B", "votes": 145},
  {"option": "C", "votes": 97}
]

    ovoz = max(votes, key=lambda x: x["votes"])

    console.print(ovoz,style = 'italic cyan')

main()