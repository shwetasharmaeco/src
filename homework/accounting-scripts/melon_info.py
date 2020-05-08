"""Print out all the melons in our inventory."""


from melons import melon_names, melon_seedlessness, melon_prices

melon_dict = {}
def print_melon(name, seedless, price):
    """Print each melon with corresponding attribute information."""
    for i, melon in melon_names.items():
        melon_dict[melon]={}

    have_or_have_not = 'have'
    if seedless:
        have_or_have_not = 'do not have'

    print(f'{name}s {have_or_have_not} seeds and are ${price:.2f}')


for i in melon_names:
    print_melon(melon_names[i], melon_seedlessness[i], melon_prices[i])
