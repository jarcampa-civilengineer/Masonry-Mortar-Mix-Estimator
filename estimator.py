from dataclasses import dataclass
from conversions import cubic_feet_to_cubic_yards
from mix_design import estimate_bag_counts

@dataclass
class MortarEstimate:
    wall_area_sqft: float
    unit_count: float
    unit_type: str
    mortar_type: str
    joint_thickness_in: float
    wet_mortar_cf: float
    dry_material_cf: float
    mortar_cy: float
    bag_counts: dict
    waste_percent: float

class MortarEstimator:
    """
    Preliminary estimator using a configurable mortar-volume allowance
    per masonry unit. Calibrate this allowance to actual unit dimensions,
    joint geometry, tooling, and project experience.
    """
    WET_MORTAR_CF_PER_BRICK = 0.020
    WET_MORTAR_CF_PER_CMU = 0.040

    def __init__(self, wall_area_sqft, unit_count, unit_type,
                 joint_thickness_in, mortar_type, waste_percent=10):
        self.wall_area_sqft = wall_area_sqft
        self.unit_count = unit_count
        self.unit_type = unit_type
        self.joint_thickness_in = joint_thickness_in
        self.mortar_type = mortar_type
        self.waste_percent = waste_percent

    def calculate(self):
        per_unit = (self.WET_MORTAR_CF_PER_BRICK if self.unit_type == "brick"
                    else self.WET_MORTAR_CF_PER_CMU)
        wet_cf = self.unit_count * per_unit
        wet_cf *= self.joint_thickness_in / 0.375
        wet_cf *= 1 + self.waste_percent / 100

        # Approximate dry ingredient volume factor. Actual yield varies by product.
        dry_cf = wet_cf * 1.33
        bags = estimate_bag_counts(dry_cf, self.mortar_type)
        return MortarEstimate(
            self.wall_area_sqft, self.unit_count, self.unit_type,
            self.mortar_type, self.joint_thickness_in, wet_cf, dry_cf,
            cubic_feet_to_cubic_yards(wet_cf), bags, self.waste_percent
        )
