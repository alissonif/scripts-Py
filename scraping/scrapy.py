import requests
from bs4 import BeautifulSoup

def get_monitors():
    url = "https://www.kabum.com.br/busca/ips-27"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        products = soup.find_all("div", class_="sc-d79c9c3f-0 nlmfp sc-d55b419d-16 giuuaP nameCard")
        monitor_list = []

        for product in products:
            title = product.find("h2", class_="sc-d79c9c3f-2 hmnUBT").text.strip()
            price = product.find("strong", class_="sc-3b515ca1-2 chPrxA priceCard").text.strip()
            
            if "144hz" in title.lower():
                monitor_list.append((title, price))

        return monitor_list

    else:
        print("Failed to fetch the page.")
        return []

def main():
    monitors = get_monitors()
    
    if monitors:
        monitors.sort(key=lambda x: float(x[1].replace("R$", "").replace(".", "").replace(",", ".")))
        for title, price in monitors:
            print(f"{title} - {price}")
    else:
        print("No monitors found.")

if __name__ == "__main__":
    main()
