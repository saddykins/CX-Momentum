<div align="center">

# CX Momentum

### Executive Customer Experience Analytics Platform

A mobile-first analytics solution that helps Customer Experience leaders identify improving, stable and deteriorating branches using a reusable **Growth × Momentum** framework.

[![Live Dashboard](https://img.shields.io/badge/🚀-Live%20Dashboard-2EAFE5?style=for-the-badge)](https://cx-momentum-vercel.vercel.app)

![HTML](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![Databricks](https://img.shields.io/badge/Databricks-FF3621?style=flat-square)
![SQL](https://img.shields.io/badge/SQL-336791?style=flat-square)
![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=flat-square)
![Vercel](https://img.shields.io/badge/Vercel-000000?style=flat-square)

</div>

---

# Live Prototype

### 🌐 https://cx-momentum-vercel.vercel.app

---

# Dashboard Preview

<p align="center">

<img src="screenshots/home.png" width="260">

<img src="screenshots/matrix.png" width="260">

<img src="screenshots/branch-detail.png" width="260">

<img src="screenshots/info.png" width="260">

</p>

---

# Business Problem

Customer Experience teams monitor dozens of KPIs across hundreds of branches.

Traditional dashboards show current performance but often fail to answer the questions executives care about most:

- Which branches are improving?
- Which branches are deteriorating?
- Is performance accelerating or slowing?
- Which branches require immediate intervention?
- Which KPI is driving the change?

CX Momentum was designed to answer those questions through a reusable Growth × Momentum framework.

---

# Solution

CX Momentum classifies every branch into a **3 × 3 Momentum Matrix** by comparing:

- Current Month (CM)
- Previous Month (PM)
- Previous Previous Month (PPM)

The framework supports both:

- Higher-is-better KPIs
- Lower-is-better KPIs

allowing one reusable analytical model across multiple Customer Experience metrics.

---

# Features

✅ Mobile-first executive dashboard

✅ Interactive Momentum Matrix

✅ Executive KPI Card

✅ Dynamic KPI Switching

✅ Higher / Lower Is Better logic

✅ Reversal Indicators

✅ Region Performance

✅ Top Opportunities

✅ Top Risks

✅ Branch Detail Drilldown

---

# Dataset

The solution uses one centralized Gold dataset.

### Grain

One row represents:

Branch × KPI × Observation Month

### Supported KPIs

- Customer Satisfaction
- Net Promoter Score
- Complaint Rate
- Complaint Volume
- Resolution Time
- SLA Compliance
- First Contact Resolution
- Customer Effort Score
- Digital Adoption Rate
- Repeat Complaint Rate

---

# Architecture

```
Python
      │
      ▼
Raw CSV
      │
      ▼
Bronze
      │
      ▼
Silver
      │
      ▼
Gold Dataset
      │
      ▼
Power BI
      │
      ▼
Executive Dashboard
```

---

# Tech Stack

| Layer | Technology |
|--------|------------|
| Data Generation | Python |
| Data Engineering | Databricks |
| Transformation | SQL |
| Data Storage | Delta Lake |
| Visualization | Power BI |
| Prototype | HTML / CSS / JavaScript |
| Deployment | Vercel |

---

# Repository Structure

```text
CX-Momentum
│
├── docs
├── data
├── sql
├── databricks
├── prototype
├── screenshots
└── powerbi
```

---

# Roadmap

- [x] Mobile Prototype
- [x] Growth × Momentum Framework
- [x] Gold Dataset
- [x] Executive UX
- [ ] Databricks Pipeline
- [ ] Power BI Implementation
- [ ] AI Branch Insights
- [ ] Automated Data Refresh

---

# Author

**Sadia Ahmed**

Senior Business Intelligence & Analytics Professional

Dubai, UAE
