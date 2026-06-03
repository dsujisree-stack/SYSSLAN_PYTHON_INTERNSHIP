import requests
from bs4 import BeautifulSoup

print("\n======= SMART WEBSITE SCRAPER =======\n")

website_link = input(
    "Enter website URL: "
)

try:

    response = requests.get(
        website_link
    )

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    page_title = soup.title

    print(
        "\n====== WEBSITE REPORT ======\n"
    )

    if page_title:
        print(
            f"Website Title : "
            f"{page_title.text}"
        )

    all_headings = soup.find_all(
        ["h1", "h2"]
    )

    print(
        f"\nHeadings Found : "
        f"{len(all_headings)}"
    )

    for item_number, heading in enumerate(
        all_headings,
        start=1
    ):

        print(
            f"{item_number}. "
            f"{heading.text.strip()}"
        )

except Exception as error:

    print(
        f"\n⚠️ Error: {error}"
    )
