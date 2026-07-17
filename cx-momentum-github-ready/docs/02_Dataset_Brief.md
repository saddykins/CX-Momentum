# Dataset Brief — CX Branch KPI Monthly

## Purpose

The CX Branch KPI Monthly dataset is the primary analytical dataset used to monitor customer-experience performance across bank branches.

## Grain

One row represents one:

> Branch × KPI × Observation Month

## Sources

- Branch Master
- KPI Master
- Monthly KPI Values

## Key Dimensions

- Region
- Area
- Branch
- Branch Type
- Branch Manager
- KPI
- Observation Date

## Key Measures

- CM
- PM
- PPM
- Target
- Growth
- Momentum
- Growth Category
- Momentum Category
- Reversal Indicator

## Design Principle

All KPIs are stored in one centralized fact table with a KPI column. This avoids creating a separate dataset for each metric and enables one reusable dashboard.
