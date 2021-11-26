import random
import pokebase as pb
from service_two import random_region, random_type


class PokemonId:
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return f'#{str(self.num)}'
    
    def get_id():
        # DICTIONARY OF REFIONS WITH RANGES APPLIED
        region_ranges = {'Kanto':random.randrange(1, 152), 'Johto':random.randrange(152, 252), 'Hoenn':random.randrange(252, 387), 'Sinnoh':random.randrange(387, 494),
                        'Unova':random.randrange(494, 650), 'Kalos':random.randrange(650, 722), 'Alola':random.randrange(722, 810), 'Galar':random.randrange(810, 902)}
        
        region = random_region #Region.get_region()
        poke_id = region_ranges.get(region.name)
        return PokemonId(poke_id)
    
    
pokedex_entry = PokemonId.get_id()
print(f'\nRetrieving pokedex entry for number: {pokedex_entry}\n')
    
    
    
# class Move:
#     def __init__(self, name, hyphen, move_type):
#         self.name = name
#         self.hyphen = hyphen
#         self.move_type = move_type
        
#     def __str__(self):
#         return f'Move: {self.name}\nType: {self.move_type}'
    
#     def get_move():
#         type_name = random_type #Type.get_type() # ASSIGNS RANDOM TYPE FROM TYPE CLASS
#         type_moves = [move.name.split() for move in pb.type_(type_name.name.lower()).moves] # RETRIEVES NESTED LIST OF MOVES WITH THE SAME TYPE
#         type_moves = [word for move in type_moves for word in move] # REMOVES OUTER LIST AND INNER LISTS TO CREATE A LIST OF STRINGS

#         choice = random.choice(type_moves) # SELECTS A RANDOM MOVE
#         hyphen = choice
        
#         # REMOVES HYPHENS AND ADDS TITLE CASE FOR READABILITY i.e devastating-drake--special > Devastating Drake: Special
#         if '--' and '-' in choice:
#             choice = choice.replace('--', ': ')
#             choice = choice.replace('-', ' ')
            
#         elif '--' in choice:
#             choice = choice.replace('--', ': ')

#         elif '-' in choice:
#             choice = choice.replace('-', ' ')
            
#         choice = choice.title()
#         return Move(choice, hyphen, type_name.name) # APPLIES MOVE AND TYPE TO CLASS ARGS
        
        
# move_entry = Move.get_move()
# print(move_entry)