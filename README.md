# Google Doc Grid Decoder

A Python script that fetches a published Google Doc containing coordinate-based character data, parses the table, and renders it as a grid of characters in the terminal.

## Example Output for sample file: https://docs.google.com/document/d/e/2PACX-1vTMOmshQe8YvaRXi6gEPKKlsC6UpFJSMAk4mQjLm_u1gmHdVVTaeh7nBNFBRlui0sTZ-snGwZM4DBCT/pub
█▀▀▀
█▀▀
█
```

## Requirements

- Python 3.8+
- [Playwright](https://playwright.dev/python/) (headless browser for rendering JavaScript-dependent Google Docs)
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/) (HTML parsing)

## Installation

```bash
pip install playwright beautifulsoup4
playwright install chromium
```

## Usage

```bash
python decode.py <url_to_published_google_doc>
```

### Example

```bash
python decode.py https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub
```

## How It Works

1. **Fetch** — Uses Playwright to launch a headless Chromium browser and navigate to the published Google Doc URL. This is necessary because published Google Docs use client-side JavaScript to render their content, so a simple HTTP request returns an empty page.

2. **Parse** — Extracts the HTML table from the rendered page using BeautifulSoup. Each row contains three columns: an x-coordinate, a character, and a y-coordinate. The data is stored in a sparse 2D grid.

3. **Render** — Prints the grid to the terminal, iterating from the highest y-coordinate down to zero (since y=0 represents the bottom of the grid), producing correctly oriented uppercase letters.

## Input Format

The Google Doc should contain a table with three columns per row:

| Column | Description |
|--------|-------------|
| 1 | x-coordinate (integer) |
| 2 | Character to display |
| 3 | y-coordinate (integer) |

The header row is automatically skipped.
