import random

# IMPLEMENTATION ONE: CLASS FOR GENERATING A RANDOM REGION
class Region:
    def __init__(self, name, generation):
        self.name = name
        self.generation = generation

    def __str__(self):
        return f'Region: {self.name}\nGeneration: {self.generation}'

    def get_region():
        # DICTIONARY OF REGIONS
        regions = {1:('Kanto', 'Gen I'), 
                   2:('Johto', 'Gen II'), 
                   3:('Hoenn', 'Gen III'), 
                   4:('Sinnoh', 'Gen IV'),
                   5:('Unova', 'Gen V'), 
                   6:('Kalos', 'Gen VI'), 
                   7:('Alola', 'Gen VII'), 
                   8:('Galar', 'Gen VIII')}
        choice = regions.get(random.randrange(1, 9)) # GRABS A REGION 
        region_name, region_gen = [*choice] # UNPACKS REGION NAME AND GEN INTO VARIABLES
        return Region(region_name, region_gen) # APPLIES VARIABLES AS ARGS TO CLASS
      
random_region = Region.get_region() # CALL CLASS TO GET REGION INFO
print(random_region) 












# # IMPLEMENTATION TWO: CLASS FOR GENERATING A RANDOM TYPE
# class Type:
#     def __init__(self, name):
#         self.name = name
        
#     def __str__(self):
#         return f'{self.name}'
    
#     def get_type():
#         # LIST OF TYPES
#         types = ['Normal', 'Fire', 'Fighting', 
#                 'Water', 'Flying', 'Grass',
#                 'Poison', 'Electric', 'Ground', 
#                 'Psychic', 'Rock', 'Ice', 
#                 'Bug', 'Dragon', 'Ghost', 
#                 'Dark', 'Steel', 'Fairy'] 
#         choice = random.choice(types) # SELECTS A RANDOM TYPE FROM TYPES LIST
#         return Type(choice)
        
# random_type = Type.get_type() # CALL CLASS TO GET TYPE INFO
# # print(random_type)