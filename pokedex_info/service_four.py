import pokebase as pb
from service_three import pokedex_entry, move_entry

# IMPLEMENTATION ONE
class DisplayPokemon:
    def __init__(self, dex, name, slot1, slot2=None, **kwargs):
        self.dex = dex
        self.name = name
        self.slot1 = slot1
        self.slot2 = slot2
        self.sprite = kwargs
        
    def __str__(self):
        if self.slot2 == None:
            return f'{self.dex} {self.name}\n{self.slot1}\n{self.sprite}\n'
        else:
            return f'{self.dex} {self.name}\n{self.slot1} {self.slot2}\n{self.sprite}\n'
          
    def display():
        poke = pb.pokemon(pokedex_entry.num) # RANDOM POKEMON
        dex_id = f'#{str(poke.id)}' # POKEDMON ID
        name = poke.name.title() # POKEMON NAME
        sprite = poke.sprites.front_default # SPRITE URL

        # LOGIC FOR DIFFERENTIATING BETWEEN SINGLE AND DOUBLE TYPED POKEMON
        types = []
        for t in poke.types:
            types.append(t.type.name.title())
            
        if len(types) == 1:
            type_one = types[0]
            return DisplayPokemon(dex_id, name, type_one, url=sprite)
        else:
            type_one, type_two = [*types]
            return DisplayPokemon(dex_id, name, type_one, type_two, url=sprite)
        

display_pokemon = DisplayPokemon.display()
print(display_pokemon)


#IMPLEMENTATION TWO