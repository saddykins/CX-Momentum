-- Validation checks

-- 1. Row count
SELECT COUNT(*) AS row_count
FROM gold.gold_branch_kpi_monthly;

-- 2. Duplicate grain check
SELECT
    branch_id,
    kpi_id,
    observation_date,
    COUNT(*) AS record_count
FROM gold.gold_branch_kpi_monthly
GROUP BY branch_id, kpi_id, observation_date
HAVING COUNT(*) > 1;

-- 3. Missing dimensions
SELECT *
FROM gold.gold_branch_kpi_monthly
WHERE branch_name IS NULL
   OR kpi IS NULL;

-- 4. Missing period values
SELECT *
FROM gold.gold_branch_kpi_monthly
WHERE cm IS NULL
   OR pm IS NULL
   OR ppm IS NULL;

-- 5. KPI direction validation
SELECT DISTINCT kpi, direction
FROM gold.gold_branch_kpi_monthly
ORDER BY kpi;
