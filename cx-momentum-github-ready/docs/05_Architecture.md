# Solution Architecture

```text
Python synthetic data generation
            |
            v
Raw CSV files
            |
            v
Databricks Bronze tables
            |
            v
Databricks Silver transformations
            |
            v
Gold CX KPI table
            |
            +--------------------+
            |                    |
            v                    v
       Power BI model      HTML prototype
```

## Tool Split

### Python

- generate realistic branch and KPI history
- create repeatable test data
- simulate improving, declining, stable, recovering, and volatile scenarios

### Databricks SQL

- ingest raw data
- standardize data types
- join branch and KPI dimensions
- create CM, PM, and PPM using window functions
- validate duplicates and missing values

### Power BI / HTML Prototype

- apply dynamic KPI selection
- calculate business growth and momentum
- present the 3×3 matrix
- filter branch detail
- provide mobile-first executive experience
