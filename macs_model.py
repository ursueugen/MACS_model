import math
import warnings


class Cell:

    def __init__(
        self,
        radius: float = 2.5,
        radius_sd: float = 0.1,
        receptor_density: float = 1000.0,
        receptor_density_sd: float = 50.0):
        
        self.radius = radius  # um
        self.radius_sd = radius_sd
        self.receptor_density = receptor_density  # receptors / um2
        self.receptor_density_sd = receptor_density_sd

        # TODO
        self.magnet_label_concentration = None  # magnets / uL?
        self.magnet_label_size = None
        self.magnet_receptor_Kd = None

        self.area = self.compute_sphere_area()
        self.receptor_number = self.compute_receptor_number()

    def compute_sphere_area(self) -> float:
        warnings.warn("Compute as a random variable!")
        return 4 * math.pi * self.radius**2
    
    def compute_receptor_number(self) -> float:
        warnings.warn("Compute as a random variable!")
        return self.receptor_density * self.area
    
    def compute_magnet_receptor_fraction(self) -> float:
        raise NotImplementedError


if __name__ == "__main__":
    c = Cell()
