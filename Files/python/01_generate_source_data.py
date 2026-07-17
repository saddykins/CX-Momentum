from __future__ import annotations

import csv
import math
import random
from calendar import monthrange
from dataclasses import dataclass
from datetime import date
from pathlib import Path

random.seed(42)

OUTPUT_DIR = Path(__file__).resolve().parents[1] / "data" / "raw"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

NUM_BRANCHES = 30
NUM_MONTHS = 18
START_MONTH = date(2025, 1, 31)

REGIONS = {
    "Dubai": ["Central Dubai", "New Dubai", "Deira"],
    "Abu Dhabi": ["Abu Dhabi City", "Khalifa City", "Al Ain"],
    "Sharjah": ["Al Majaz", "Al Nahda", "Muwaileh"],
    "Northern Emirates": ["Ajman", "Ras Al Khaimah", "Fujairah"],
}

BRANCH_NAMES = [
    "Downtown Main", "Dubai Mall", "Business Bay", "Jumeirah", "Marina",
    "Deira Main", "Mirdif", "Al Barsha", "Silicon Oasis", "Jebel Ali",
    "Abu Dhabi Main", "Corniche", "Khalifa City", "Yas Island", "Mussafah",
    "Al Ain Main", "Al Reem", "Al Raha", "Sharjah Main", "Al Majaz",
    "Al Nahda", "Muwaileh", "University City", "Ajman Main", "Al Nuaimiya",
    "Ras Al Khaimah Main", "Al Hamra", "Fujairah Main", "Dibba", "Umm Al Quwain",
]

MANAGERS = [
    "Ahmed Khan", "Fatima Noor", "Sara Ali", "Omar Siddiqui", "Maya Joseph",
    "Hassan Raza", "Nadia Karim", "Kareem Abbas", "Rania Saleh", "Imran Malik",
    "Zara Hussain", "Bilal Ahmed", "Lina Farooq", "Sameer Nair", "Amina Yusuf",
    "Tariq Bashir", "Reem Qureshi", "Fadi Mansour", "Hiba Saeed", "Naveed Akram",
    "Salma Tariq", "Yusuf Rahman", "Mariam Khan", "Adnan Shah", "Noor Abbas",
    "Rashid Ali", "Sana Mir", "Waleed Omar", "Farah Nasser", "Khalid Mahmoud",
]

BRANCH_TYPES = ["Flagship", "Premium", "Standard", "Digital Hub"]
SCENARIOS = ["Improving", "Declining", "Stable", "Recovering", "Volatile"]


@dataclass(frozen=True)
class KPI:
    kpi_id: str
    kpi_name: str
    direction: str
    unit: str
    minimum: float
    maximum: float
    base_low: float
    base_high: float
    target: float
    decimals: int


KPIS = [
    KPI("KPI01", "CSAT", "HIGHER", "%", 55, 98, 72, 90, 85, 1),
    KPI("KPI02", "NPS", "HIGHER", "Score", -20, 80, 15, 55, 40, 1),
    KPI("KPI03", "Complaint Rate", "LOWER", "Per 1,000 customers", 0.4, 8.0, 1.2, 4.5, 2.0, 2),
    KPI("KPI04", "Complaint Volume", "LOWER", "Count", 10, 450, 45, 220, 100, 0),
    KPI("KPI05", "Resolution Time", "LOWER", "Days", 0.5, 10.0, 2.0, 6.5, 3.0, 2),
    KPI("KPI06", "SLA Compliance", "HIGHER", "%", 55, 100, 78, 97, 95, 1),
    KPI("KPI07", "First Contact Resolution", "HIGHER", "%", 45, 98, 65, 90, 85, 1),
    KPI("KPI08", "Customer Effort Score", "LOWER", "Score", 1.0, 7.0, 2.0, 5.2, 3.0, 2),
    KPI("KPI09", "Digital Adoption Rate", "HIGHER", "%", 25, 98, 52, 88, 75, 1),
    KPI("KPI10", "Repeat Complaint Rate", "LOWER", "%", 1, 35, 5, 20, 8, 1),
]


def month_end(year: int, month: int) -> date:
    return date(year, month, monthrange(year, month)[1])


def add_months(d: date, months: int) -> date:
    month_index = d.year * 12 + d.month - 1 + months
    year, month_zero = divmod(month_index, 12)
    return month_end(year, month_zero + 1)


def clamp(value: float, low: float, high: float) -> float:
    return max(low, min(high, value))


def write_csv(path: Path, rows: list[dict]) -> None:
    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def create_branches() -> list[dict]:
    region_names = list(REGIONS)
    rows = []

    for i in range(NUM_BRANCHES):
        region = region_names[i % len(region_names)]
        area = REGIONS[region][i % len(REGIONS[region])]

        rows.append({
            "branch_id": f"BR{i + 1:03d}",
            "branch_name": BRANCH_NAMES[i],
            "region_name": region,
            "area_name": area,
            "branch_type": BRANCH_TYPES[i % len(BRANCH_TYPES)],
            "branch_manager_name": MANAGERS[i],
            "scenario": SCENARIOS[i % len(SCENARIOS)],
            "active_flag": "Y",
        })

    return rows


def create_kpi_master() -> list[dict]:
    return [
        {
            "kpi_id": k.kpi_id,
            "kpi_name": k.kpi_name,
            "direction": k.direction,
            "unit": k.unit,
            "target_value": k.target,
            "minimum_valid_value": k.minimum,
            "maximum_valid_value": k.maximum,
            "decimals": k.decimals,
        }
        for k in KPIS
    ]


def favorable_delta(kpi: KPI, scenario: str, month_index: int) -> float:
    scale = kpi.maximum - kpi.minimum

    if scenario == "Improving":
        favorable = 0.010 * scale
    elif scenario == "Declining":
        favorable = -0.010 * scale
    elif scenario == "Stable":
        favorable = 0.0
    elif scenario == "Recovering":
        favorable = -0.010 * scale if month_index < 8 else 0.015 * scale
    else:
        favorable = math.sin(month_index * 1.25) * 0.015 * scale

    return favorable if kpi.direction == "HIGHER" else -favorable


def create_monthly_history(branches: list[dict]) -> list[dict]:
    rows = []
    months = [add_months(START_MONTH, i) for i in range(NUM_MONTHS)]

    for branch in branches:
        for kpi in KPIS:
            value = random.uniform(kpi.base_low, kpi.base_high)

            if branch["branch_type"] == "Flagship":
                adjustment = 0.02 * (kpi.maximum - kpi.minimum)
                value += adjustment if kpi.direction == "HIGHER" else -adjustment

            if branch["branch_type"] == "Digital Hub" and kpi.kpi_name == "Digital Adoption Rate":
                value += 7

            for month_index, observation_date in enumerate(months):
                delta = favorable_delta(kpi, branch["scenario"], month_index)
                noise = random.gauss(0, 0.007 * (kpi.maximum - kpi.minimum))

                if observation_date == date(2025, 9, 30) and branch["branch_type"] == "Digital Hub":
                    if kpi.kpi_name in {"CSAT", "NPS"}:
                        delta -= 4
                    elif kpi.kpi_name in {"Complaint Rate", "Complaint Volume"}:
                        delta += 0.10 * (kpi.maximum - kpi.minimum)

                value = clamp(value + delta + noise, kpi.minimum, kpi.maximum)

                rows.append({
                    "branch_id": branch["branch_id"],
                    "kpi_id": kpi.kpi_id,
                    "observation_date": observation_date.isoformat(),
                    "kpi_value": round(value, kpi.decimals),
                })

    return rows


def main() -> None:
    branches = create_branches()
    kpi_master = create_kpi_master()
    monthly_history = create_monthly_history(branches)

    write_csv(OUTPUT_DIR / "branches.csv", branches)
    write_csv(OUTPUT_DIR / "kpi_master.csv", kpi_master)
    write_csv(OUTPUT_DIR / "branch_kpi_monthly.csv", monthly_history)

    print(f"Created {len(branches)} branch rows")
    print(f"Created {len(kpi_master)} KPI rows")
    print(f"Created {len(monthly_history)} monthly KPI rows")


if __name__ == "__main__":
    main()
