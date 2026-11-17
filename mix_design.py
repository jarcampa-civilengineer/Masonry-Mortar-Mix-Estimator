"""
Illustrative bag-yield assumptions for planning only.
Replace with the actual manufacturer's published yield for the selected product.
"""

BAG_YIELDS_CU_FT = {
    "N": 0.75,
    "S": 0.75,
    "M": 0.75,
}

def estimate_bag_counts(dry_material_cf, mortar_type):
    if mortar_type not in BAG_YIELDS_CU_FT:
        raise ValueError("Mortar type must be N, S, or M.")
    yield_per_bag = BAG_YIELDS_CU_FT[mortar_type]
    bags = dry_material_cf / yield_per_bag
    return {
        "mortar_type": mortar_type,
        "assumed_yield_cf_per_bag": yield_per_bag,
        "estimated_bags": bags,
        "whole_bags_to_order": int(bags) + (1 if bags % 1 else 0),
    }
