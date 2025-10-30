import requests
import json
import os

BARCODES_FILE = "../barcodes.txt"

# Folio token 
TOKEN_FILE = os.path.join(os.path.dirname(__file__), "../FOLIO_TOKEN.txt")

# Read access token safely
try:    
    with open(TOKEN_FILE, "r") as f:
        ACCESS_TOKEN = f.read().strip()
except FileNotFoundError:
    raise FileNotFoundError(
        f"Missing token file: {TOKEN_FILE}\n"
        "Please create it and paste your access token."
    )

# Response header template
headers = {
    "x-okapi-token": ACCESS_TOKEN,  # fixed variable name
    "x-okapi-tenant": "scu",
    "Content-Type": "application/json",
}

BASE_URL = "https://scu-okapi.folio.indexdata.com/inventory/items"

def get_item_status(barcode: str) -> str:
    """
    Requests item status from FOLIO API using personal access token.
    Returns item[i].status.name, or "NULL" if not found or bad response.
    """
    params = {"query": f"barcode=={barcode}"}
    try:
        response = requests.get(BASE_URL, headers=headers, params=params, timeout=10)
    except requests.exceptions.RequestException as e:
        print(f"Request error for barcode {barcode}: {e}")
        return "NULL"

    if response.status_code != 200:
        print(f"Error {response.status_code} for barcode {barcode}: {response.text}")
        return "NULL"

    data = response.json()
    items = data.get("items", [])
    if not items:
        print(f"No item found for barcode {barcode}")
        return "NULL"

    return items[0].get("status", {}).get("name", "NULL")


def main():
    # Read barcodes from barcodes.csv (one barcode per line)
    with open(BARCODES_FILE, "r") as f:
        barcodes = [line.strip() for line in f if line.strip()]

    results = {}

    # Get statuses
    for barcode in barcodes:
        status = get_item_status(barcode)
        results[barcode] = status
        print(f"{barcode}: {status}")

    # Prompt user for filename
    print("\nAll barcodes processed.")
    filename = input("Enter a filename for the results (without extension): ").strip()
    if not filename:
        filename = "status"

    # Build results directory path
    results_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../results"))
    os.makedirs(results_dir, exist_ok=True)

    output_path = os.path.join(results_dir, f"{filename}.json")

    # Save to ../../results/<filename>.json
    with open(output_path, "w") as f:
        json.dump(results, f, indent=2)

    print(f"\n Results saved to {output_path}\n")


if __name__ == "__main__":
    main()
