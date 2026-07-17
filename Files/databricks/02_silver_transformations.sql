-- Silver transformations
CREATE SCHEMA IF NOT EXISTS silver;

CREATE OR REPLACE TABLE silver.branch_kpi_monthly
USING DELTA
AS
SELECT
    CAST(branch_id AS STRING) AS branch_id,
    CAST(kpi_id AS STRING) AS kpi_id,
    CAST(observation_date AS DATE) AS observation_date,
    CAST(kpi_value AS DOUBLE) AS kpi_value
FROM bronze.branch_kpi_monthly
WHERE branch_id IS NOT NULL
  AND kpi_id IS NOT NULL
  AND observation_date IS NOT NULL
  AND kpi_value IS NOT NULL;
