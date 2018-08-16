def validate_point(point, coords=None, check_duplicate=False):
    rows = "ABCDEFGH"
    columns = "12345678"
    if len(point) != 2:
        raise Exception("Invalid point")
    if point[0] not in rows or point[1] not in columns:
        raise Exception("Point out of bounds")
    if check_duplicate:
        if point in coords.keys():
            raise Exception("Point already set")

def check_ship_type_amount(input_counter, ship_amount):
    if input_counter < ship_amount:
        return True

# def not_enough_space(coords):
#     pass


