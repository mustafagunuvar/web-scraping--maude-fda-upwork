# MAUDE FDA Web Scraper and Analysis

This project demonstrates a complete end-to-end pipeline for web scraping, data preprocessing, and analysis using real-world data from the [openFDA MAUDE API](https://open.fda.gov/apis/device/event/). It was designed to collect and analyze medical device adverse event reports based on specific product codes (PCODEs).

## 🔍 Project Overview

The project includes:
- Scraping data from openFDA's Device Adverse Event API
- Saving structured JSON files per PCODE
- Data transformation and cleaning
- Exploratory data analysis and visualizations using Pandas and Seaborn

## 📁 Project Structure

web-scraping--maude-fda-upwork/

1-) data/ # Raw data saved in JSON format

2-) venv/ # Virtual environment (excluded in .gitignore)

3-) api_scraper.py # Python script for collecting data from the API

4-) maude_fda_scraper_analysis.ipynb # Jupyter notebook for EDA and visualization

5-) requirements.txt # List of required Python packages

6-) .env # Environment file for base URL and PCODE list

## ⚙️ Technologies Used

- Python 3
- openFDA API
- Requests
- Pandas
- Matplotlib & Seaborn
- Jupyter Notebook
- dotenv

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/mustafagunuvar/web-scraping--maude-fda-upwork.git
   cd web-scraping--maude-fda-upwork
   ``` 
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\Activate 
   ``` 
3. Install dependencies:
   ```bash 
   pip install -r requirements.txt
   ``` 
4. Configure your .env file:
   ```bash 
   OPENFDA_URL= https://api.fda.gov/device/event.json
   PCODE_LIST= LLZ,OSH,GEH 
   ``` 
5. Run the scraper: 
   ```bash
   python api_scraper.py
   ```
6. Open the notebook for analysis:
   ```bash
   jupyter notebook maude_fda_scraper_analysis.ipynb
   ```

---

## 📦 Scraped Files Overview

| Product Code | File Name                      | Previewable on GitHub | Notes                             |
|--------------|--------------------------------|------------------------|-----------------------------------|
| LLZ          | `LLZ_20250520_011418.json`     | ❌ Too Large           | Fully accessible via repo clone  |
| GEH          | `GEH_20250520_011518.json`     | ❌ Too Large           | File is in repository             |
| OSH          | `OSH_20250520_011623.json`     | ✅ Yes                 | Available in `data/` folder      |

> ⚠️ **Note**: GitHub does not allow in-browser preview of large JSON files.  
> These files are still available in the repository and can be downloaded by cloning.

---

## 💡 Proof of Scraping

This repository includes:
- Raw `.json` files fetched directly via openFDA API.
- Reproducible scraping logic inside `api_scraper.py`.
- Timestamped and structured file naming for clarity.
- Pagination and error-handling integrated into the scraper.

---

🧑‍💻 Author
Mustafa Günüvar

Junior Data Scientist | Web Scraping | Data Analysis


This project was created as a freelance-ready, entry-level portfolio project demonstrating reliable scraping, error handling, and data analysis skills using public health data.
