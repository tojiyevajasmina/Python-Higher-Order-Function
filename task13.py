from rich.console import Console
console = Console()

def main():
    sentence = "Functional programming in Python is very powerful and elegant"

    words:list[str] = sentence.spilt()
    words.sort (key = len, reverse = True)
    console.print(words,style = 'italic yellow')
    console.print(words[:3],style = 'italic blue')

main()