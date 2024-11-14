import requests
from bs4 import BeautifulSoup
from time import sleep
from random import choice

all_quotes = []
base_url = "https://quotes.toscrape.com/"
url = "/page/1"

while url:
    res = requests.get(f"{base_url}{url}")
    print(f"SCRAPING: ---- >>> {base_url}{url} ...")
    soup = BeautifulSoup(res.text, "html.parser")
    quotes = soup.find_all(class_ = "quote")

    for quote in quotes:
        all_quotes.append({
            "text": quote.find(class_ = "text").get_text(),
            "author": quote.find(class_ = "author").get_text(),
            "bio-link": quote.find("a")["href"]
        })

    next_btn = soup.find(class_="next")     
    url = next_btn.find("a")["href"] if next_btn else None
    # sleep(2) # prevent from overloading the server

def start_game():
    quote = choice(all_quotes)
    remaining_quesses = 4
    guess = ''

    print(f"Here's a quote:\n{quote["text"]}")
    print(quote["author"])

    while guess.lower() != quote["author"].lower() and remaining_quesses > 0:
        guess = input(f"Who said this quote? Guesses remaining: {remaining_quesses}\n")
        if guess.lower() == quote["author"].lower():
            print("You got it! Well done!")
            break
        remaining_quesses -= 1
        if(remaining_quesses == 3):
            res = requests.get(f"{base_url}{quote['bio-link']}")
            soup = BeautifulSoup(res.text, "html.parser")
            birth_date = soup.find(class_="author-born-date").get_text()
            birth_place = soup.find(class_="author-born-location").get_text()
            print(f"Here's a hint: The author was born on {birth_date} {birth_place}")
        elif(remaining_quesses == 2):
            author_name = quote["author"]
            first_name_char = author_name[0]  
            print(f"Here's a hint: The author's first name starts with >> {first_name_char} <<")
        elif(remaining_quesses == 1):
            first_lastname_char = author_name.split(' ')[1][0]
            print(f"Here's a hint: The author's last name starts with >> {first_lastname_char} <<")
        else:
            print(f"Sorry you ran out of guesses. The answer was >> {quote['author']} <<")

    again = ''
    while again not in ('y', 'yes', 'n', 'no'):
        again = input("Do you want to play again? [y/n] \n")
    if again.lower() in ('y','yes'):
        return start_game()
    else:
        print("Thanks for playing!")

start_game()