from typing import List, Tuple
from random import choices, randint, random
from csv import writer
import names


class Organism:
    def __init__(
        self,
        heat_tolerance: float,
        cold_tolerance: float,
        humidity_tolerance: float,
        dryness_tolerance: float,
        light_tolerance: float,
        dark_tolerance: float,
        organism_name: str,
    ) -> None:
        self.heat_tolerance = heat_tolerance  # 0 - 1 low value, cannot tolerate heat i.e. temperature above 0.5
        self.cold_tolerance = cold_tolerance  # 0 - 1 low value, cannot tolerate cold i.e. temperature below 0.5
        self.humidity_tolerance = humidity_tolerance  # 0 - 1
        self.dryness_tolerance = dryness_tolerance  # 0 - 1
        self.light_tolerance = light_tolerance  # 0 - 1
        self.dark_tolerance = dark_tolerance  # 0 - 1
        self.organism_name = organism_name

    def mutate(self) -> None:
        """Mutate self attributes"""
        choice_int = randint(0, 6)
        if choice_int == 0:
            self.heat_tolerance = max(0, min(random(), 1))
        elif choice_int == 1:
            self.cold_tolerance = max(0, min(random(), 1))
        elif choice_int == 2:
            self.humidity_tolerance = max(0, min(random(), 1))
        elif choice_int == 3:
            self.dryness_tolerance = max(0, min(random(), 1))
        elif choice_int == 4:
            self.light_tolerance = max(0, min(random(), 1))
        elif choice_int == 5:
            self.dark_tolerance = max(0, min(random(), 1))
        # else:
        # print("No mutation")

    def get_data(self) -> List:
        """Return list of organism attributes"""
        return [
            self.organism_name,
            self.organism_name.split()[0],
            self.organism_name.split()[-1],
            self.heat_tolerance,
            self.cold_tolerance,
            self.humidity_tolerance,
            self.dryness_tolerance,
            self.dark_tolerance,
            self.light_tolerance,
        ]

    def __str__(self) -> str:
        return f"""
        Name: {self.organism_name}
        Heat tolerance: {self.heat_tolerance}
        Cold tolerance: {self.cold_tolerance}
        Humidity tolerance: {self.humidity_tolerance}
        Dryness tolerance: {self.dryness_tolerance}
        Light tolerance: {self.light_tolerance}
        Dark tolerance: {self.dark_tolerance}
        """


class Container:
    def __init__(
        self,
        temperature: float,
        light: float,
        humidity: float,
        initial_population_count: int,
        generation_limit: int,
    ) -> None:
        self.temperature = temperature  # 0 - 1
        self.light = light  # 0 - 1
        self.humidity = humidity  # 0 - 1
        self.population_list = []
        self.initial_population_count = initial_population_count
        self.generation_limit = generation_limit

    def change_temperature(self) -> None:
        """Tweak temperature of the container randomly"""
        self.temperature = max(0, min(random(), 1))

    def change_light(self) -> None:
        """Tweak light of the container randomly"""
        self.temperature = max(0, min(random(), 1))

    def change_humidity(self) -> None:
        """Tweak humidity of the container randomly"""
        self.temperature = max(0, min(random(), 1))

    def generate_population(self, count: int) -> None:
        """Generate population for a given count"""
        for _ in range(count):
            self.population_list.append(
                Organism(
                    random(),
                    random(),
                    random(),
                    random(),
                    random(),
                    random(),
                    names.get_full_name(),
                )
            )

    def calculate_fitness(self, org: Organism) -> float:  # 0
        """Calculate fitness of an individual"""
        fitness = 0

        # Checking fitness of organism for current container temperature
        if self.temperature < 0.5:  # Container is cold
            fitness += org.cold_tolerance
        else:  # Container is hot
            fitness += org.heat_tolerance

        # Checking fitness of organism for current light in container
        if self.light < 0.5:  # Container is dark
            fitness += org.dark_tolerance
        else:  # Container is bright
            fitness += org.light_tolerance

        # Checking fitness of organism for current humidity in container
        if self.humidity < 0.5:  # Container is dry
            fitness += org.dryness_tolerance
        else:  # Container is humid
            fitness += org.humidity_tolerance

        return fitness

    def select_pair(self) -> Tuple[Organism, Organism]:
        """Return two fittest parents of type Organism for crossover"""

        return choices(
            self.population_list,
            weights=[self.calculate_fitness(org) for org in self.population_list],
            k=2,
        )

    def single_point_crossover(
        self, parent_a: Organism, parent_b: Organism
    ) -> Tuple[Organism, Organism]:
        """Return two children of type Organism after crossover"""
        child_a = Organism(
            parent_a.heat_tolerance,
            parent_a.cold_tolerance,
            parent_a.humidity_tolerance,
            parent_b.dryness_tolerance,
            parent_b.light_tolerance,
            parent_b.dark_tolerance,
            names.get_first_name() + " " + parent_a.organism_name.split()[-1],
        )
        child_b = Organism(
            parent_b.heat_tolerance,
            parent_b.cold_tolerance,
            parent_b.humidity_tolerance,
            parent_a.dryness_tolerance,
            parent_a.light_tolerance,
            parent_a.dark_tolerance,
            names.get_first_name() + " " + parent_a.organism_name.split()[-1],
        )

        return (child_a, child_b)

    def run_evolution(self) -> None:
        """Run complete evolution"""

        # Generate initial population
        self.generate_population(self.initial_population_count)

        with open("ga_data.csv", "w") as f:
            # Instantiate csv_writer object
            obj = writer(f)

            obj.writerow(
                [
                    "Full name",
                    "First name",
                    "Last name",
                    "Heat tolerance",
                    "Cold tolerance",
                    "Humidity tolerance",
                    "Dryness tolerance",
                    "Dark tolerance",
                    "Light tolerance",
                    "Generation",
                    "Fitness",
                    "Container temperature",
                    "Container humidity",
                    "Container light",
                ]
            )

            # Each iteration is a generation
            for i in range(self.generation_limit):

                # Sort population by their fitness
                self.population_list = sorted(
                    self.population_list,
                    key=lambda org: self.calculate_fitness(org),
                    reverse=True,
                )

                print(f"-> Writing generation {i} data to csv")

                for k in self.population_list:
                    obj.writerow(
                        k.get_data()
                        + [
                            i,
                            self.calculate_fitness(k),
                            self.temperature,
                            self.humidity,
                            self.light,
                        ]
                    )

                # print(self.population_list[0])

                # Pick two fittest individuals from the population
                # next_generation = self.population_list[:2]
                next_generation = []

                for _ in range(
                    int(len(self.population_list) / 2)  # -1
                ):  # -1 because we have already copied one pair of fit individuals from the population
                    parent_a, parent_b = self.select_pair()
                    child_a, child_b = self.single_point_crossover(parent_a, parent_b)
                    child_a.mutate()
                    child_b.mutate()
                    next_generation += [child_a, child_b]

                # Replace old generation with newer generation
                self.population_list = next_generation
