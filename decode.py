import sys
from collections import namedtuple
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

GridData = namedtuple('GridData', ['maxY', 'grid'])

def fetchPublishedGoogleDoc( url: str) -> str: 
    with sync_playwright() as pw: 

        #print(f"Fetching: {url}")
        browser = pw.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, wait_until="networkidle")
        html = page.content()
        browser.close()

        return html

def parseGoogleDoc( content: str):
    soup = BeautifulSoup(content,"html.parser")
    data = []
    maxY = -1

    tables = soup.find_all("table")
    #Validate Data
    if not tables:
        print("Error: No table")
        return []
    rows = tables[0].find_all("tr")
    
    if not rows:
        print("Error: Table has no rows")
        return []

    for row in rows:
        cols = row.find_all("td")
        try:
            x = int(cols[0].get_text(strip=True))
            y = int(cols[2].get_text(strip=True))
            char = cols[1].get_text(strip=True)
        except ValueError:
            continue
        
        while len(data) <= x:
                data.append([])
        while len(data[x]) <= y:
            data[x].append(" ")
        if y>maxY:
            maxY=y

        data[x][y]=char

    #return [maxY,data]
    return GridData(maxY, data)

def printCode(data):
    if not data or data.maxY == -1 :
        print("Error: No data")
        return
    
    
    
    y = data.maxY

    while y >= 0:
        x = 0
        line=""
        while x < len(data.grid):
            if y>=len(data.grid[x]):
                line+=" "
            else:
                line+=data.grid[x][y]
            x+=1
        print(line)
        y-=1

        
def solve(url: str):
    printCode(parseGoogleDoc(fetchPublishedGoogleDoc(url)))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: python decode.py <url to published google doc>')
        sys.exit(1)

    solve(sys.argv[1])
