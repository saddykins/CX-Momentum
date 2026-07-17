# Data Model

## Logical Model

```text
dim_branch
    |
    | branch_id
    v
fact_branch_kpi_monthly
    ^
    | kpi_id
    |
dim_kpi
```

## Tables

### dim_branch

- branch_id
- branch_name
- region_name
- area_name
- branch_type
- branch_manager_name
- active_flag

### dim_kpi

- kpi_id
- kpi_name
- direction
- unit
- target_value
- minimum_valid_value
- maximum_valid_value

### fact_branch_kpi_monthly

- branch_id
- kpi_id
- observation_date
- kpi_value

### gold_branch_kpi_monthly

- branch attributes
- KPI attributes
- PPM
- PM
- CM
- target
- observation_date

## Why Dimension Tables Are Used

Dimension tables centralize descriptive attributes and business rules. This keeps the fact table narrow, avoids duplication, improves maintainability, and supports reusable filtering.
