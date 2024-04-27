from enum import Enum

class ShipType(Enum):
    AIRCRAFT_CARRIER = 5
    BATTLESHIP = 4
    CRUISER = 3
    SUBMARINE = 3
    DESTROYER = 2

class Ship:
    def __init__(self, shipType: ShipType):
        self.shipType = shipType
        self.health = shipType.value

    def hit(self) -> bool:
        self.health -= 1
        return self.health == 0

    def __str__(self):
        return f"{self.shipType.name} ({self.health})"