# KBO IT Companies Analysis – SQL Challenge

This repository contains the analysis of Belgian IT companies based on the official KBO (Kruispuntbank van Ondernemingen) data. The analysis was performed as part of a data science SQL challenge.

## 📁 Repository Structure

```
.
├── kbo_explore.ipynb     # Main notebook with all queries and plots
├── requirements.txt      # Python packages needed for the notebook
├── figures/              # All output plots saved as PNGs
└── src/                  # Supporting code and data
```

## 🚀 How to Run the Project

1. **Clone this repository**  
   ```bash
   git clone https://github.com/Marcvg69/challenge-data-analysis-sql.git
   cd <repo-folder>  (with repo-folder = name of your repo folder)
   ```

2. **Set up a virtual environment (optional but recommended)**  
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # or .venv\Scripts\activate on Windows
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the main notebook**  
   Open `kbo_explore.ipynb` in Jupyter or VS Code and run the cells sequentially.

## 📊 What’s Inside?

This project investigates:

- The yearly creation of new IT companies by legal form.
- The evolution of different IT activities (e.g. programming, consulting, hosting).
- Regional “hotspots” of IT firms by municipality.
- Company age profiles across sectors.
- Visual insights saved in `figures/`.
- Results presentation stored in pdf file KBO_IT_Companies_Analysis.pdf

## 📄 Data

The project uses a local SQLite database (`kbo_database.db`) constructed from KBO data exports and joined with address and activity information. The analysis is focused on active companies (`Status = 'AC'`) with NACE codes relevant to the IT sector.

## 👤 Author

**Marc Van Goolen**  
Solo contributor for this challenge

---

_For more information, see the challenge brief in `sql_kbo.md` and the summary in the Word document._
