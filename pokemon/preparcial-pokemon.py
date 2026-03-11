from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()

class pokemon(BaseModel):
    id:int
    nombre:str
    life:int
    attack:int
    type:str
    leavepokeball:bool=True
    
pokemons = [
    pokemon(id=1, nombre="Bulbasaur", life=45, attack=49, type="planta/veneno"),
    pokemon(id=2, nombre="Ivysaur", life=60, attack=62, type="planta/veneno"),
    pokemon(id=3, nombre="Venusaur", life=80, attack=82, type="planta/veneno"),
    pokemon(id=4, nombre="Charmander", life=39, attack=52, type="fuego"),
    pokemon(id=5, nombre="Charmeleon", life=58, attack=64, type="fuego"),
    pokemon(id=6, nombre="Charizard", life=78, attack=84, type="fuego/volador"),
    pokemon(id=7, nombre="Squirtle", life=44, attack=48, type="agua"),
    pokemon(id=8, nombre="Wartortle", life=59, attack=63, type="agua"),
    pokemon(id=9, nombre="Blastoise", life=79, attack=83, type="agua"),
    pokemon(id=25, nombre="Pikachu", life=65, attack=55, type="electrico"),
    pokemon(id=443, nombre="Gible", life=58, attack=70, type="dragon/tierra"),
    pokemon(id=444, nombre="Gabite", life=68, attack=90, type="dragon/tierra"),
    pokemon(id=445, nombre="Garchomp", life=108, attack=130, type="dragon/tierra"),
    pokemon(id=483, nombre="Dialga", life=100, attack=120, type="acero/dragon"),
    pokemon(id=483, nombre="Giratina", life=545, attack=135, type="siniestro/dragon"),
    pokemon(id=484, nombre="Palkia", life=90, attack=120, type="agua/dragon"),
    pokemon(id=493, nombre="Arceus", life=120, attack=120, type="normal"),
    pokemon(id=384, nombre="Rayquaza", life=555, attack=150, type="dragon/volador"),
    pokemon(id=383, nombre="Groudon", life=100, attack=150, type="Tierra"),
    pokemon(id=383, nombre="Kyogren", life=100, attack=150, type="agua"),
    pokemon(id=133, nombre="Eevee", life=65, attack=55, type="normal"),
    pokemon(id=134, nombre="Vaporeon", life=130, attack=65, type="agua"),
    pokemon(id=135, nombre="Jolteon", life=65, attack=65, type="electrico"),
    pokemon(id=136, nombre="Flareon", life=65, attack=130, type="fuego"),
    pokemon(id=196, nombre="Espeon", life=65, attack=65, type="psiquico"),
    pokemon(id=197, nombre="Umbreon", life=95, attack=65, type="siniestro "),
    pokemon(id=470, nombre="Leafeon", life=65, attack=110, type="planta"),
    pokemon(id=471, nombre="Glaceon", life=65, attack=60, type="hielo"),
    pokemon(id=700, nombre="Sylveon", life=95, attack=65, type="hada"),
    pokemon(id=246, nombre="Larvitar", life=50, attack=64, type="roca/tierra"),
    pokemon(id=247, nombre="Pupitar", life=70, attack=84, type="roca/tierra"),
    pokemon(id=248, nombre="Tyranitar", life=100, attack=134, type="roca/tierra"),
    pokemon(id=95, nombre="Onix", life=35, attack=45, type="roca"),
    pokemon(id=208, nombre="Steelix", life=75, attack=85, type="acero/roca"),
    pokemon(id=280, nombre="Ralts", life=28, attack=25, type="psiquico"),
    pokemon(id=281, nombre="Kirlia", life=38, attack=35, type="psiquico"),
    pokemon(id=282, nombre="Gardevoir", life=268, attack=65, type="psiquico"),
    pokemon(id=381, nombre="Latios", life=80, attack=90, type="dragon/psiquico"),
    pokemon(id=380, nombre="Latias", life=80, attack=80, type="dragon/psiquico"),
    pokemon(id=249, nombre="Lugia", life=106, attack=90, type="psiquico/Volador"),
    pokemon(id=393, nombre="Piplup", life=53, attack=51, type="agua"),
    pokemon(id=394, nombre="Prinplup", life=64, attack=66, type="agua"),
    pokemon(id=395, nombre="Empoleon", life=84, attack=86, type="agua/acero"),
    pokemon(id=387, nombre="Turtwig", life=55, attack=68, type="planta"),
    pokemon(id=388, nombre="Grotle", life=75, attack=89, type="planta"),
    pokemon(id=389, nombre="Torterra", life=95, attack=109, type="planta/tierra"),
    pokemon(id=390, nombre="Chimchar", life=44, attack=58, type="fuego"),
    pokemon(id=391, nombre="Monferno", life=64, attack=78, type="fuego/lucha"),
    pokemon(id=392, nombre="Infernape", life=76, attack=104, type="fuego/lucha"),
    pokemon(id=129, nombre="Magikarp", life=20, attack=10, type="agua"),
    pokemon(id=130, nombre="Gyarados", life=95, attack=125, type="agua/dragon"),
    pokemon(id=447, nombre="Riolu", life=40, attack=70, type="lucha"),
    pokemon(id=448, nombre="Lucario", life=70, attack=110, type="lucha/acero"),

]

@app.get("/showallpokemons")
def show_all_pokemons():
    return pokemons

@app.get("/showonepokemon")
def show_one_pokemon(nombre: str):
    resultado = [p for p in pokemons if p.nombre.lower() == nombre.lower()]
    
    if resultado:
        return resultado[0]

    return {"error": "Pokemon no encontrado"}

@app.get("/showonepokemonbyid/{pokemon id}")
def show_pokemon_by_id(pokemon_id: int):
    for p in pokemons:
        if p.id == pokemon_id:
            return p
    return {"error": "Pokemon no encontrado"}

@app.get("/pokemonordered")
def pokemon_ordered(by: str = "attack", order: str = "asc"):

    if by not in ["attack", "life", "nombre"]:
        return {"error": "Parametro invalido"}

    reverse = True if order == "desc" else False

    pokemons_ordenados = sorted(
        pokemons,
        key=lambda p: getattr(p, by),
        reverse=reverse
    )

    return pokemons_ordenados

@app.get("/pokemonbattle")
def pokemon_battle(id1: int, id2: int):

    p1 = next((p for p in pokemons if p.id == id1), None)
    p2 = next((p for p in pokemons if p.id == id2), None)

    if not p1 or not p2:
        return {"error": "Pokemon no encontrado"}

    p1.leavepokeball = False
    p2.leavepokeball = False

    vida1 = p1.life
    vida2 = p2.life

    turno = 1
    historial = []

    while vida1 > 0 and vida2 > 0:

        vida2 -= p1.attack
        historial.append(
            f"Turno {turno}: {p1.nombre} ataca a {p2.nombre} (-{p1.attack} vida)"
        )

        if vida2 <= 0:
            ganador = p1.nombre
            break

        vida1 -= p2.attack
        historial.append(
            f"Turno {turno}: {p2.nombre} ataca a {p1.nombre} (-{p2.attack} vida)"
        )

        if vida1 <= 0:
            ganador = p2.nombre
            break

        turno += 1

    return {
        "pokemon1": p1.nombre,
        "pokemon2": p2.nombre,
        "batalla": historial,
        "ganador": ganador
    }

def validar_generacion(pokemon: pokemon):
    if pokemon.id < 1 or pokemon.id > 151:
        return False
    return True

@app.post("/addpokemon")
def add_pokemon(pokemon: pokemon):

    if not validar_generacion(pokemon):
        return {"error": "Solo se permiten pokemones de la primera generacion"}

    pokemons.append(pokemon)
    return {"mensaje": "Pokemon agregado"}