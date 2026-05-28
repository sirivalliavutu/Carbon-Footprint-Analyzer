import numpy as np

class CarbonFootprint:

    def __init__(self, name, electricity, distance,
                 transport, food, waste):

        self.name = name
        self.electricity = electricity
        self.distance = distance
        self.transport = transport
        self.food = food
        self.waste = waste

    def calculate_footprint(self):

        transport_factors = {
            "bus": 0.05,
            "bike": 0.12,
            "car": 0.21,
            "metro": 0.03
        }

        food_factors = {
            "vegetarian": 30,
            "non-vegetarian": 60
        }

        waste_factors = {
            "low": 10,
            "medium": 20,
            "high": 40
        }

        electricity_emission = np.multiply(
            self.electricity, 0.85
        )

        transport_emission = np.multiply(
            self.distance,
            transport_factors[self.transport]
        )

        food_emission = food_factors[self.food]

        waste_emission = waste_factors[self.waste]

        total = np.add.reduce([
            electricity_emission,
            transport_emission,
            food_emission,
            waste_emission
        ])

        trees_required = total / 21

        return (
            electricity_emission,
            transport_emission,
            food_emission,
            waste_emission,
            total,
            trees_required
        )