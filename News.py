import requests
from colorama import init, Fore, Style

init(autoreset=True)
api = "506769e3bb7646f18ede5b2459a5d36a"

while True:
    print(Fore.CYAN + "What do you want to see?")
    print(Fore.CYAN + "1 General News")
    print(Fore.CYAN + "2 Sports News")
    print(Fore.CYAN + "3 Technology News")
    print(Fore.CYAN + "4 Entertainment News")
    print(Fore.CYAN + "5 Health News")
    print(Fore.CYAN + "6 Science News")
    
    choose = int(input(Fore.LIGHTYELLOW_EX + "Enter your choice (1-6): "))
    
    match choose:
        case 1:
            c = "general"
        case 2:
            c = "sports"
        case 3:
            c = "technology"
        case 4:
            c = "entertainment"
        case 5:
            c = "health"
        case 6:
            c = "science"
        case _:
            print(Fore.RED + "Invalid choice")
            continue

    url = f"https://newsapi.org/v2/top-headlines?category={c}&language=en&apiKey={api}"

    # Fetch data
    response = requests.get(url)
    if response.status_code != 200:
        print(Fore.RED + "Unable to fetch news right now. Please check your internet connection or try again later.")
        continue

    data = response.json()
    articles = data.get('articles', [])
    index = 0
    total = len(articles)
    step = 5

    # Check if data has articles or not
    if not data.get('articles'):
        print(Fore.RED + "No news found. Please try again later.")
        continue

    # Print headlines
    print(Style.BRIGHT + Fore.LIGHTGREEN_EX + "-"*25 + "\nNEWS\n" + "-"*25)
    while index < total:
        for i, article in enumerate(articles[index:index+step]):
            print(Style.BRIGHT + Fore.LIGHTBLUE_EX + f"[{i+1}] " + (article.get('title') or "No title"))
            print(Fore.WHITE + (article.get('description') or "No description available"))
            print(Fore.LIGHTCYAN_EX + (article.get('url') or "No URL available"))
            print("\n" + Fore.MAGENTA + "-" * 50 + "\n")
        
        index += step
        if index < len(articles):
            more = input(Fore.YELLOW + "Do you want to dive deeper into this category? (y/n): ")
            if more.lower() != 'y':
                break
        else:
            print(Fore.GREEN + "You've seen all the latest news in this category!\n")
    
    i = input(Fore.YELLOW + "Do you want to check another category? (y/n): ")
    if i.lower() != 'y':
        print(Fore.MAGENTA + Style.BRIGHT + "Thank you for using the News App!")
        break