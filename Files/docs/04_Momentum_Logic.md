# Momentum Logic

## 1. Growth

```text
Growth = (CM - PM) / ABS(PM)
```

## 2. Prior Growth

```text
Prior Growth = (PM - PPM) / ABS(PPM)
```

## 3. Direction Adjustment

For higher-is-better KPIs:

```text
Business Growth = Growth
```

For lower-is-better KPIs:

```text
Business Growth = Growth × -1
```

## 4. Momentum

```text
Momentum = Business Growth - Prior Business Growth
```

## 5. Growth Category

Using a ±2% threshold:

- Growing: Business Growth > 2%
- Contracting: Business Growth < -2%
- Flat: otherwise

## 6. Momentum Category

- Accelerating: Momentum > 2%
- Decelerating: Momentum < -2%
- Stable: otherwise

## 7. Matrix Codes

- CA — Contracting + Accelerating
- FA — Flat + Accelerating
- GA — Growing + Accelerating
- CS — Contracting + Stable
- FS — Flat + Stable
- GS — Growing + Stable
- CD — Contracting + Decelerating
- FD — Flat + Decelerating
- GD — Growing + Decelerating

## 8. Reversal Indicator

- Turnaround: prior business growth < 0 and current business growth > 0
- Collapse: prior business growth > 0 and current business growth < 0
- None: no reversal
