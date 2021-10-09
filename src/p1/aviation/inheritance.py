class Pojazd:
    x: int = 0
    y: int = 0
    v: float = 0.0


class TransorterOsob:
    liczba_miejsc_siedzacych: int


class Samochod(Pojazd):
    engine: str
    nadwozie: str


class SamochodOsobowy(Samochod, TransorterOsob):
    pass


class SamochodCiezarowy(Samochod):
    ladownosc_ton: float


s = SamochodOsobowy()
print(s.x, s.y, s.v)
print(type(s))
print(isinstance(s, Pojazd))
print(isinstance(s, Samochod))
print(isinstance(s, SamochodOsobowy))
print(isinstance(s, SamochodCiezarowy))
