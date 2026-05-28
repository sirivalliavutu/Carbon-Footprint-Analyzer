import numpy as np

def show_statistics(all_footprints):

    print("\n================ STATISTICS ================")

    print(f"Average Carbon Footprint: "
          f"{np.mean(all_footprints):.2f} kg CO₂")

    print(f"Maximum Carbon Footprint: "
          f"{np.max(all_footprints):.2f} kg CO₂")

    print(f"Minimum Carbon Footprint: "
          f"{np.min(all_footprints):.2f} kg CO₂")