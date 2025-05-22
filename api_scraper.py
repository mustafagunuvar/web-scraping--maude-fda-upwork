import requests
import os
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

# Get base URL and PCode list from environment variables
BASE_URL = os.getenv("OPENFDA_URL")
PCODES = os.getenv("PCODE_LIST").split(",")

# Output directory
OUTPUT_DIR = "data"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Main scraping loop
for pcode in PCODES:
    print(f"Fetching data for PCode: {pcode}")
    params = {
        "search": f"device.device_report_product_code:{pcode}",
        "limit": 100,
        "skip": 0
    }
    
    page = 1
    all_results = []

    while True:
        try:
            response = requests.get(BASE_URL, params=params)
            response.raise_for_status()
            data = response.json()

            results = data.get("results", [])
            if not results:
                break

            all_results.extend(results)
            print(f"  → Page {page} | Records: {len(results)}")

            params["skip"] += params["limit"]
            page += 1

        except requests.exceptions.RequestException as e:
            print(f"  [!] Error fetching data for {pcode}: {e}")
            break

    # Save results
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = os.path.join(OUTPUT_DIR, f"{pcode}_{timestamp}.json")

    with open(output_file, "w", encoding="utf-8") as f:
        import json
        json.dump(all_results, f, indent=2)

    print(f"  ✔ Saved {len(all_results)} records to {output_file}\n")
