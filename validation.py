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
