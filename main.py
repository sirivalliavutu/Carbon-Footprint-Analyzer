from carbon import CarbonFootprint
from suggestions import show_suggestions
from stats import show_statistics

all_footprints = []

print("==================================================")
print("      CAMPUS CARBON FOOTPRINT ANALYZER")
print("==================================================")

while True:

    try:

        name = input("\nEnter Student Name: ")

        electricity = float(
            input("Enter monthly electricity usage (units): ")
        )

        distance = float(
            input("Enter distance travelled per week (km): ")
        )

        transport = input(
            "Transport Type (bus/bike/car/metro): "
        ).lower()

        food = input(
            "Food Preference (vegetarian/non-vegetarian): "
        ).lower()

        waste = input(
            "Waste Production (low/medium/high): "
        ).lower()

        student = CarbonFootprint(
            name,
            electricity,
            distance,
            transport,
            food,
            waste
        )

        (
            electricity_emission,
            transport_emission,
            food_emission,
            waste_emission,
            total,
            trees_required
        ) = student.calculate_footprint()

        all_footprints.append(total)

        if total < 100:
            category = "Low Carbon Footprint"

        elif total < 250:
            category = "Medium Carbon Footprint"

        else:
            category = "High Carbon Footprint"

        print("\n================ RESULT ================")

        print(f"Student Name: {name}")

        print(f"\nTotal Carbon Footprint: "
              f"{total:.2f} kg CO₂")

        print(f"Category: {category}")

        print(f"Trees Needed: "
              f"{trees_required:.2f}")

        show_suggestions(
            electricity_emission,
            transport_emission,
            food_emission,
            waste_emission,
            total
        )

        file = open("results.txt", "a")

        file.write(
            f"\n{name} | CO2: {total:.2f}"
        )

        file.close()

        choice = input(
            "\nAdd another student? (yes/no): "
        ).lower()

        if choice != "yes":
            break

    except ValueError:
        print("Invalid numeric input entered.")

    except KeyError:
        print("Invalid category entered.")

if len(all_footprints) > 0:
    show_statistics(all_footprints)

print("\nData successfully saved in results.txt")