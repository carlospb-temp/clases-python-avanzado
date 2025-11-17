from dataclasses import dataclass, field

@dataclass
class Edificio:
    piso_base: int
    piso_mas_alto: int
    plantas: list = field(default_factory=list)
    
    def __post_init__(self):
        for i in range(self.piso_base, self.piso_mas_alto):
            match i:
                case _ if i < 0:
                    planta = f"S{-i}"
                case _ if i == 0:
                    planta = "B"
                case _ if i == 1:
                    planta = "E"
                case _:
                    planta = i
            print(planta)
            self.plantas.append(planta)
        self.plantas.append("A")
    
if __name__ == "__main__":
    inst = Edificio(-2, 10)
    print(inst.plantas)  # [S2, S1, B, E, 2, 3, 4, 5, 6, 7, 8, 9, A]