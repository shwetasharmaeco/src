############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""

        self.pairings = []
        self.name = name
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller

        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code



def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []
    melon_codes = []

    Melonmusk = MelonType ("musk", 1998, "green", True, True, "Melonmusk")
    Melonmusk.add_pairing("mint")
    all_melon_types.append(Melonmusk)
    melon_codes.append("musk")

    Casaba = MelonType("cas", 2003, "orange", True, False, "Casaba")
    Casaba.add_pairing("strawberries and mint")
    all_melon_types.append(Casaba)
    melon_codes.append("cas")

    Yellow_watermelon = MelonType("yw", 2013, "yellow", True, True, "Yellow_watermelon")
    Yellow_watermelon.add_pairing("icecream")
    all_melon_types.append(Yellow_watermelon)
    melon_codes.append("yw")

    Crenshaw = MelonType("cren", 1996, "green", True, False, "Crenshaw" )
    Crenshaw.add_pairing("proscuitto")
    all_melon_types.append(Crenshaw)
    melon_codes.append("cren")

    
    return all_melon_types

def print_pairing_info(melon_types):
    for melon in melon_types:
        for elem in melon.pairings:
            print(melon.name + " " + "pairs with\n" + "-" + elem)
            print("\n")

        
   

  

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    
    melon_dict = {}

    for melon in melon_types:
            melon_dict[melon.code] = melon 


    return melon_dict


melon_types = make_melon_types()
print_pairing_info(melon_types)
melon_dict = make_melon_type_lookup(melon_types)

print(melon_dict)





############
# Part 2   #
############

class Melon():
       
    def __init__(self, shape_rating, color_rating, harvested_field, harvested_by, melon_type):
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvested_field = harvested_field
        self.harvested_by = harvested_by
        self.melon_type = melon_type
    """A melon in a melon harvest."""

    def sellable(self):

        if (self.shape_rating>5 and self.color_rating>5 and self.harvested_field != 3) == True:
            return ("can be sold")

        else:
            return ("cannot be sold")
          
    # Needs __init__ and is_sellable methods


def make_melons():
    """Returns a list of Melon objects."""

    all_melon_objects=[]

    melon_dict = make_melon_type_lookup(melon_types)

    Melon_1 = Melon(8,7,2,"Sheila",melon_dict["yw"])
    Melon_2 = Melon(3,4,2,"Sheila",melon_dict["yw"])
    Melon_3 = Melon(9,8,3,"Sheila",melon_dict["yw"])
    Melon_4 = Melon(10,6,35,"Sheila",melon_dict["cas"])
    Melon_5 = Melon(8,9,35,"Michael",melon_dict["cren"])
    Melon_6 = Melon(8,2,35,"Michael",melon_dict["cren"])
    Melon_7 = Melon(2,3,4,"Michael",melon_dict["cren"])
    Melon_8 = Melon(6,7,4,"Michael",melon_dict["musk"])
    Melon_9 = Melon(7,10,3,"Sheila",melon_dict["yw"])

    all_melon_objects.extend([Melon_1,Melon_2,Melon_3, Melon_4, Melon_5, Melon_6,Melon_7, Melon_8, Melon_9])

    return all_melon_objects

# def get_sellability_report(melons):
#     """Given a list of melon object, prints whether each one is sellable."""
#     for melon in melons:
        
#         if melon.sellable()==True:
#             return ("can be sold")

#         else:
#             return("cannot be sold")

def final_output(melons):

    for melon in melons:
        print(f"Harvested by {melon.harvested_by} from Field {melon.harvested_field} {melon.sellable()}")


melons = make_melons() 
answer = final_output(melons)



