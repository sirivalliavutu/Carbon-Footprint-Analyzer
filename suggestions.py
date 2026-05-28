def show_suggestions(electricity_emission,
                     transport_emission,
                     food_emission,
                     waste_emission,
                     total):

    print("\n============= SUGGESTIONS =============")

    if electricity_emission > 100:
        print("- Reduce electricity usage.")

    if transport_emission > 50:
        print("- Use public transport or carpool.")

    if food_emission >= 60:
        print("- Reduce meat consumption.")

    if waste_emission >= 20:
        print("- Practice recycling.")

    if total < 100:
        print("- Great job! Your carbon footprint is low.")