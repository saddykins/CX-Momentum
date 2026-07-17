-- Gold KPI table
CREATE SCHEMA IF NOT EXISTS gold;

CREATE OR REPLACE TABLE gold.gold_branch_kpi_monthly
USING DELTA
AS

WITH joined_data AS (
    SELECT
        b.region_name,
        b.area_name,
        b.branch_manager_name,
        b.branch_id,
        b.branch_name,
        b.branch_type,
        k.kpi_id,
        k.kpi_name AS kpi,
        k.direction,
        k.unit,
        k.target_value,
        CAST(m.observation_date AS DATE) AS observation_date,
        m.kpi_value
    FROM silver.branch_kpi_monthly m
    LEFT JOIN bronze.branches b
        ON m.branch_id = b.branch_id
    LEFT JOIN bronze.kpi_master k
        ON m.kpi_id = k.kpi_id
),

period_values AS (
    SELECT
        *,
        LAG(kpi_value, 2) OVER (
            PARTITION BY branch_id, kpi_id
            ORDER BY observation_date
        ) AS ppm,
        LAG(kpi_value, 1) OVER (
            PARTITION BY branch_id, kpi_id
            ORDER BY observation_date
        ) AS pm,
        kpi_value AS cm
    FROM joined_data
)

SELECT
    region_name,
    area_name,
    branch_manager_name,
    branch_id,
    branch_name,
    branch_type,
    kpi_id,
    kpi,
    direction,
    unit,
    target_value,
    ppm,
    pm,
    cm,
    observation_date
FROM period_values
WHERE pm IS NOT NULL
  AND ppm IS NOT NULL;
