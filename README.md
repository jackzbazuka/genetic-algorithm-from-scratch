# genetic-algorithm-from-scratch

Simulation of evolution using natural selection in python.

Read more about genetic algorithms [here](https://en.wikipedia.org/wiki/Genetic_algorithm)

## Environment and organism

The container has three fixed environmental constraints defined at the initialization of evolution:

-   Temperature
-   Humidity
-   Light

The organism has six tolerance parameters:

-   Heat tolerance
-   Cold tolerance
-   Humidity tolerance
-   Dryness tolerance
-   Darkness tolerance
-   Brightness tolerance

Analogous to chromosomes, every organism has tolerance parameters for each container attribute, which collectively form the gene of the organism.The organisms adjust their tolerance over generations through evolution to the container's attributes. Every environmental constraint of the container and the tolerance parameters of the organism is scaled between 0 and 1.

Each organism can only span a single generation and has a first and last name to make the data analysis process post-evolution fun.

## Initial population

All the parameters are set randomly at the initial population generation.

## Fitness evalution

The fitness of the organism is determined by its tolerance to the environmental attributes.

## Crossover

Each single point crossover produces two children from two parents. An additional feature has been added to this process, both the children in addition to inheriting their chromosomes from both of the parents, inherit the last name of one parent who is more fit than the other.

## Mutation

Each child is mutated based on a probabilty, post crossover before passing to next generation.

## Analysis

Data for complete evolution is saved in a CSV file in the following format:

-   Full name
-   First name
-   Last Name
-   Heat tolerance
-   Cold tolerance
-   Humidity tolerance
-   Dryness tolerance
-   Dark tolerance
-   Light tolerance
-   Generation count
-   Fitness
-   Container temperature
-   Container humidity
-   Container light

Toggle the `Container` constructor parameters in `main.py` to experiment with the population.
