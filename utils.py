
def isometric(x, y, X_STRIDE, Y_STRIDE, debug=False):
    if debug:
        print("From Direct Co-ordinates (", x, y, ") with sizes (", X_STRIDE, Y_STRIDE, ")" )
    res_x = (x + y)*X_STRIDE / 2
    res_y = (y - x)*Y_STRIDE / 2
    if debug:
        print("Converted to Isometric Resolved Format (", res_x, res_y, ")")
    return res_x, res_y