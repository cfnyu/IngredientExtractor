import requests
from bs4 import BeautifulSoup

def main():
    url = "https://www.tasteofhome.com/recipes/pressure-cooker-fabulous-fajitas/"
    
    data = requests.get(url)
    soup = BeautifulSoup(data.text, 'html.parser')
    
    for ul in soup.find_all('ul'):
        print ul.attrs['class']
        
        if "recipe-ingredients__list" in ul.attrs['class']:
            print ul.text

if __name__ == "__main__":
    main()
