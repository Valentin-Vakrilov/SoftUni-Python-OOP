from pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon):
        if pokemon in self.pokemons:
            return "This pokemon is already caught"

        self.pokemons.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name):
        try:
            pokemon = next(filter(lambda x: x.name == pokemon_name, self.pokemons))
        except StopIteration:
            return "Pokemon is not caught"

        self.pokemons.remove(pokemon)
        return f"You have released {pokemon_name}"

    def trainer_data(self):
        result = [f"Pokemon Trainer {self.name}"+"\n"
                  f"Pokemon count {len(self.pokemons)}"]
        for current_pokemon in self.pokemons:
            result.append(f"- {current_pokemon.pokemon_details()}")

        return "\n".join(result)


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
