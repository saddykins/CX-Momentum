-- Bronze tables
CREATE SCHEMA IF NOT EXISTS bronze;

CREATE OR REPLACE TABLE bronze.branches
USING CSV
OPTIONS (
  path '/Volumes/cx_momentum/raw/branches.csv',
  header 'true',
  inferSchema 'true'
);

CREATE OR REPLACE TABLE bronze.kpi_master
USING CSV
OPTIONS (
  path '/Volumes/cx_momentum/raw/kpi_master.csv',
  header 'true',
  inferSchema 'true'
);

CREATE OR REPLACE TABLE bronze.branch_kpi_monthly
USING CSV
OPTIONS (
  path '/Volumes/cx_momentum/raw/branch_kpi_monthly.csv',
  header 'true',
  inferSchema 'true'
);
