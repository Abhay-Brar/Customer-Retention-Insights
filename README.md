# Customer Retention Insights Platform (Python + Power BI)

**Prediction • Analysis • Detection**

- Built an end-to-end **Python pipeline** to ingest, clean, and model customer data.
- **Achieved up to 0.99 AUC** and **>99% precision on high-risk cohort**.
- Added **Isolation Forest anomaly detection** to flag abnormal usage.
- **Streamlit dashboard** visualizes churn risk and KPIs for PMs.
- **Power BI dashboard** for executive-level reporting and drill-down analysis.
- Automated weekly refresh, reproducible metrics, and clean documentation.

### Tech stack:
- Python (pandas, scikit-learn)
- Power BI interactive dashboard (sample PBIX included)
- Streamlit for live visualization
- Random Forest, Isolation Forest

### How to run Python pipeline:
```bash
pip install -r requirements.txt
python backend/pipeline.py
```
This generates `customer_churn_predictions.csv` → connect it to Power BI.

### How to view dashboards:
- Run Streamlit app:
```bash
streamlit run dashboard/app.py
```
- Open Power BI report: `powerbi/customer_retention.pbix`
