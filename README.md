# CX Momentum

A customer-experience analytics case study showing how branch-level CX performance can be monitored through a reusable **Growth × Momentum** framework.

The project combines:

- Databricks SQL
- Python
- Delta Lake
- Power BI design principles
- Mobile-first executive UX
- Interactive HTML prototyping

## Dashboard Prototype

[![Live Dashboard](https://img.shields.io/badge/🚀-Live%20Dashboard-2EAFE5?style=for-the-badge)](https://cx-momentum-vercel.vercel.app)

## Business Question

> Where is customer experience improving, where is it deteriorating, and where should leadership intervene first?

CX Momentum answers this by classifying every branch into a 3×3 matrix using:

- **Growth** — current month versus previous month
- **Momentum** — whether that growth is accelerating, stable, or decelerating

The logic adapts automatically for both:

- **Higher-is-better KPIs**, such as CSAT and NPS
- **Lower-is-better KPIs**, such as complaint rate and resolution time

## Repository Structure

```text
cx-momentum/
├── dashboard/
│   └── index.html
├── data/
│   └── sample/
│       └── cx_gold_branch_kpi_monthly.csv
├── databricks/
│   ├── 01_bronze_tables.sql
│   ├── 02_silver_transformations.sql
│   ├── 03_gold_kpi_table.sql
│   └── 04_validation_queries.sql
├── docs/
│   ├── 01_BRD.md
│   ├── 02_Dataset_Brief.md
│   ├── 03_Data_Model.md
│   ├── 04_Momentum_Logic.md
│   ├── 05_Architecture.md
│   └── 06_Dashboard_Design.md
├── python/
│   └── 01_generate_source_data.py
├── .gitignore
├── LICENSE
└── README.md
```

## Dataset Grain

One row represents:

> **Branch × KPI × Observation Month**

Example:

```text
Dubai Mall Branch × CSAT × 31 May 2026
```

## Supported KPIs

- Customer Satisfaction (CSAT)
- Net Promoter Score (NPS)
- Complaint Rate
- Complaint Volume
- Resolution Time
- SLA Compliance
- First Contact Resolution
- Customer Effort Score
- Digital Adoption Rate
- Repeat Complaint Rate

## Core Measures

- CM — Current Month
- PM — Previous Month
- PPM — Previous Previous Month
- Growth
- Prior Growth
- Momentum
- Growth Category
- Momentum Category
- Reversal Indicator
- KPI Target

## Momentum Matrix

|  | Contracting | Flat | Growing |
|---|---|---|---|
| Accelerating | CA | FA | GA |
| Stable | CS | FS | GS |
| Decelerating | CD | FD | GD |

## Reversal Logic

- **Turnaround** — prior growth was negative and current growth is positive
- **Collapse** — prior growth was positive and current growth is negative
- **None** — no directional reversal

## Dashboard Features

- Dynamic KPI selector
- Month, region, area, and branch-type filters
- KPI card with CM, PM, PPM, target, delta, and 12-month trend
- Clickable 3×3 Momentum Matrix
- Matrix-driven filtering across the page
- Region performance
- Top opportunities
- Top risks
- Branch-level detail table
- Mobile-first executive layout
- Higher/lower-is-better business logic
- Reversal indicators

## Presentation Story

> I designed CX Momentum to answer one executive question: where is customer experience improving, where is it deteriorating, and where should leadership intervene first? Instead of creating a separate dashboard for each KPI, I built one centralized KPI model and one reusable momentum framework that dynamically adapts to any CX metric.

## Run Locally

Open:

```text
dashboard/index.html
```

in a browser.

## Deploy to Vercel

1. Create a new Vercel project.
2. Upload the repository.
3. Set the root directory to `dashboard`, or move `index.html` to the repository root.
4. Use framework preset **Other**.
5. Deploy.

## Data Disclaimer

The included dataset is simulated for portfolio demonstration. The current sample contains approximately 3,600 records covering 30 branches, 10 CX KPIs, and 12 observation months.
