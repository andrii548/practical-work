from enum import Enum


class PlanetType(Enum):
    TERRESTRIAL = "Terrestrial"
    JOVIAN = "Jovian"


class Planet:
    def __init__(self, name, mass, orbital_velocity, mean_temperature, length_of_day, distance_from_sun, planet_type):
        if mass <= 0:
            raise ValueError("The mass of a planet cannot be negative.")
        if orbital_velocity < 0:
            raise ValueError("Orbital velocity cannot be negative.")
        if length_of_day < 0:
            raise ValueError("The length of a day cannot be negative.")
        if distance_from_sun < 0:
            raise ValueError("The distance from the Sun cannot be negative.")

        self.name = name
        self.mass = mass
        self.orbital_velocity = orbital_velocity
        self.mean_temperature = mean_temperature
        self.length_of_day = length_of_day
        self.distance_from_sun = distance_from_sun
        self.planet_type = planet_type

    def __repr__(self):
        return (
            f"Planet(name='{self.name}', mass={self.mass}, "
            f"orbital_velocity={self.orbital_velocity}, "
            f"mean_temperature={self.mean_temperature}, "
            f"length_of_day={self.length_of_day}, "
            f"distance_from_sun={self.distance_from_sun}, "
            f"planet_type={self.planet_type})"
        )

    def __str__(self):
        return (
            f"{self.name} ({self.planet_type}): "
            f"mass={self.mass} kg, temperature={self.mean_temperature}°C, "
            f"day={self.length_of_day}г, "
            f"distance from sun={self.distance_from_sun} million km"
        )


class Planetary:
    def __init__(self, name, planets):
        self.name = name
        self.planets = planets

    def sort_by_day_length(self):
        self.planets.sort(key=lambda planet: planet.length_of_day)

    def __str__(self):
        planet_count = len(self.planets)
        planets_list = ", ".join(planet.name for planet in self.planets)
        return (
            f"Planetary system '{self.name}': "
            f"{planet_count} planets \n"
            f"Planets list: {planets_list}"
        )

    @staticmethod
    def find_distance_between(planet_a, planet_b):
        return abs(planet_a.distance_from_sun - planet_b.distance_from_sun)

    @staticmethod
    def find_averega_mass(*planets):
        return sum(planet.mass for planet in planets) / len(planets)


def main():
    mercury = Planet("Mercury", 0.330e24, 47.87, 167,4222.6, 57.9, PlanetType.TERRESTRIAL)
    venus = Planet("Venus", 4.87e24, 35.02, 464, 2802.0,108.2, PlanetType.TERRESTRIAL)
    earth = Planet("Earth", 5.97e24, 29.78, 15, 24.0,149.6, PlanetType.TERRESTRIAL)
    mars = Planet("Mars", 0.642e24, 24.07, -65, 24.7,227.9, PlanetType.TERRESTRIAL)
    jupiter = Planet("Jupiter", 1898e24, 13.07, -110,9.9, 778.6, PlanetType.JOVIAN)
    saturn = Planet("Saturn", 568e24, 9.68, -139,10.7, 1433.5, PlanetType.JOVIAN)
    uranus = Planet("Uranus", 86.8e24, 6.80, -197,17.2, 2872.5, PlanetType.JOVIAN)
    neptune = Planet("Neptune", 102e24, 5.43, -201,16.1, 4495.1, PlanetType.JOVIAN)

    solar_system = Planetary("Solar System", [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune])
    print(solar_system)
    print("Sorted by day lenght:")
    solar_system.sort_by_day_length()
    for planet in solar_system.planets:
        print(f"{planet.name}: {planet.length_of_day} hours")
    print("-"*20)

    print(f"Average mass of planets:{Planetary.find_averega_mass(*solar_system.planets)} kg")
    print("-"*20)

    print(f"distance between Earth and Uranus: {Planetary.find_distance_between(earth, uranus)} million km")

if __name__ == "__main__":
    main()
