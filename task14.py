from rich.console import Console
console = Console()

def main():
    words = ["sun", "mountain", "a", "apple"]

    words.sort(key=lambda word: len(word))

    console.print(words,style = 'bold red')

main()