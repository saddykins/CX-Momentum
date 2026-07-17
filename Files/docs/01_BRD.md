# Business Requirements Document — CX Momentum

## 1. Purpose

CX Momentum is an executive customer-experience monitoring solution designed to identify which branches are improving, deteriorating, stable, or showing a change in performance direction.

## 2. Business Problem

Traditional CX dashboards show current KPI values but often fail to answer:

- Is the branch improving or declining?
- Is the improvement accelerating or slowing?
- Which branches require immediate intervention?
- Is a negative trend reversing?
- Which KPI is driving the change?

## 3. Objective

Provide a single reusable analytical framework that:

- compares CM, PM, and PPM
- supports multiple CX KPIs
- applies higher/lower-is-better logic
- classifies branches into a 3×3 matrix
- enables drill-down from executive summary to branch detail
- works on desktop and phone

## 4. Primary Users

- Head of Customer Experience
- CX Strategy Lead
- Regional CX Manager
- Branch Performance Manager
- Business Analytics Team

## 5. Functional Requirements

1. Users must be able to select a KPI.
2. Users must be able to filter by month, region, area, and branch type.
3. The KPI card must display CM, PM, PPM, target, and delta.
4. The solution must display a 12-month trend.
5. The matrix must classify every branch into one of nine buckets.
6. Clicking a matrix cell must filter all downstream visuals.
7. Lower-is-better KPIs must reverse the performance interpretation.
8. Reversal indicators must identify Turnaround and Collapse.
9. A branch detail table must support investigation.
10. The design must be optimized for mobile executive use.

## 6. Success Criteria

- A senior CX user understands the branch network status within 15 seconds.
- A user can identify priority branches within two interactions.
- One data model supports all KPIs.
- The dashboard remains readable on mobile.
