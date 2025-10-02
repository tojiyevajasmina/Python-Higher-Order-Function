from rich.console import Console
console = Console()

def main():
    emails = ["ali@gmail.com",
               "vali@yahoo.com", 
               "sami@gmail.com", 
               "bek@outlook.com"
]
    
    gmail = filter(lambda email: email.endswith("@gmail.com"), emails)

    console.print(list(gmail),style = 'italic black')

main()