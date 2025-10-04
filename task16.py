from rich.console import Console
console = Console()

def main():
    data = [123, "apple", 
            "banana", "cat", 
            456, "mango", "elephant"
]
    filtered_data = filter(
        lambda element:type(element) == str and len(element) > 5,
        data
)

    console.print(list(filtered_data),style = 'bold magenta')

main()