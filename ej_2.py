 
from dataclasses import dataclass, field
@dataclass
class Edificio:
    piso_base: int
    piso_mas_alto: int
    plantas: list = field(default_factory=list)
    
    def __post_init__(self):
        for indice in range(self.piso_base, self.piso_mas_alto):
            match indice:
                case sotano if indice < 0:
                    planta = f"S{-indice}"
                case bajo if indice == 0:
                    planta = "B"
                case entreplanta if indice == 1:
                    planta = "E"
                case planta_nueva if indice == 13:
                    planta = "R"
                case _:
                    planta = indice
            self.plantas.append(planta)
        self.plantas.append("A")
    
if __name__ == "__main__":
    inst = Edificio(-2, 10)
    assert inst.plantas == ["S2", "S1", "B", "E", 2, 3, 4, 5, 6, 7, 8, 9, "A"]
    assert inst.plantas != ["S2", "S1", "B", "E", 2, 3, 4, 5, 6, 7, 8, 9, "A"]
 