# Masonry Mortar Mix Estimator

A small command-line Python estimator for preliminary mortar quantities for
brick and CMU masonry walls.

## Features
- Estimate mortar volume for a wall area and selected masonry unit type.
- Select mortar designation Type N, S, or M.
- Apply a configurable joint-thickness adjustment and 10% planning allowance.
- Convert estimated wet mortar volume to cubic yards.
- Estimate bag quantities using an editable assumed bag yield.

## Files
- `main.py` — command-line user interface
- `estimator.py` — quantity estimation logic
- `mix_design.py` — mortar bag-yield assumptions
- `conversions.py` — unit conversions
- `validators.py` — input validation
- `reports.py` — formatted estimate
- `requirements.txt` — dependencies

## Run
Python 3.10+ recommended. No third-party libraries required.

```bash
python main.py
```

## Important estimating limitations
This is a preliminary planning estimator, not a mix-design tool or a substitute
for project specifications. The mortar volume per unit and bag yield are
illustrative assumptions and must be calibrated to actual masonry unit sizes,
face-shell/web geometry, joint dimensions, workmanship, mortar product and
manufacturer data. Type N/S/M selection must follow project specifications,
applicable code, exposure, and masonry design requirements. Do not infer
cement, lime, or sand proportions from this program; use a specified
preblended product or an approved mix design. Round procurement quantities
up and verify with the supplier.
