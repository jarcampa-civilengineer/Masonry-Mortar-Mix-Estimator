from estimator import MortarEstimator
from validators import ask_positive, ask_choice
from reports import print_estimate

def main():
    print("\n=== MASONRY MORTAR MIX ESTIMATOR ===")
    print("Preliminary material estimate for masonry mortar.\n")

    wall_area = ask_positive("Wall area (square feet): ")
    joint_thickness = ask_positive("Assumed mortar joint thickness (inches) [e.g. 0.375]: ")
    joint_thickness_ft = joint_thickness / 12

    unit_type = ask_choice(
        "Masonry unit type (1=standard modular brick, 2=CMU block): ",
        {"1": "brick", "2": "cmu"}
    )
    mix_type = ask_choice(
        "Mortar type (N, S, or M): ",
        {"N": "N", "S": "S", "M": "M"}
    )

    # User-supplied planning assumptions; edit for actual unit dimensions/joints.
    units_per_sqft = {"brick": 6.86, "cmu": 1.125}
    unit_count = wall_area * units_per_sqft[unit_type]

    estimator = MortarEstimator(
        wall_area_sqft=wall_area,
        unit_count=unit_count,
        unit_type=unit_type,
        joint_thickness_in=joint_thickness,
        mortar_type=mix_type
    )
    result = estimator.calculate()
    print_estimate(result)

if __name__ == "__main__":
    main()
