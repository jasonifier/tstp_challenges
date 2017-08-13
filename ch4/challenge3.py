#!/usr/bin/env python3

def coffee_order(temp, size, add_milk, flavor=None, whip_cream=False):
    """
    Returns string describing coffee order from a customer.
    :param temp: str. ex- 'hot' 'cold'.
    :param size: str. ex- 'grande' 'venti'.
    :param add_milk: bool.
    :param flavor: str. Default None. ex- 'vanilla' 'pumpkin'.
    :param whip_cream: bool. Default False.
    :return: str describing the coffee order. 
    """
    order_str = size + ' ' + temp + ' coffee '
    if add_milk:
        order_str += 'with milk'
    else:
        order_str += 'with no milk'
    
    if flavor is not None and whip_cream:
        order_str += ' plus ' + flavor + ' and whipped cream'
    elif whip_cream:
        order_str += ' plus whipped cream'
    elif flavor is not None:
        order_str += ' plus ' + flavor
    else:
        pass

    return order_str

print(coffee_order('hot', 'grande', False))
print(coffee_order('iced', 'venti', True, flavor='vanilla'))
print(coffee_order('hot', 'small', False, whip_cream=True))
print(coffee_order('Hot', 'large', True, flavor='hazelnut', whip_cream=True))
