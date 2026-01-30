from dataclass import dataclass


@dataclass
class Product:
    name: str
    price: float

    def __post_init__(self):
        if self.price <= 0:
            raise ValueError("Price must be positive")