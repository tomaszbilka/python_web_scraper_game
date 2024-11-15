### Scraping Project

It visites the website: https://quotes.toscrape.com/ and grab bunch of info abouyt quotes and its authors. Then it starts a game where you have to guess the author of the quote. You hav 4 attempts to guess the right author, each step exept first one include a clue. Quotes are saved in a csv file.

#### How to run

1. Install Python 3.x
2. Install pip
3. Run `python3 -m pip install bs4`
4. Run `python3 -m pip install requests`

#### Auto scrap and play

run in game folder:

```bash
`python3 scraping.py`
```

#### Scrap manually, save data to csv and play

run in game folder:

```bash
`python3 csv_scraper.py`
```

and play with command:

```bash
`python3 csv_scrape_game.py`
```
