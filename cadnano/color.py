try:
    from PyQt5.QtGui import QColor as Color
except:
    class Color(object):
        def __init__(self, *args):
            """ use Color(r, g, b) or
            Color('#rrggbb') for hex or
            """
            largs = len(args)
            if largs == 1:
                # clip the `#`
                arg = args[0]
                if isinstance(arg, str):
                    raise ValueError("color doesn't support ints")
                color_number = int(arg[1:], 16)
                r = (color_number >> 16) & 0xFF
                g = (color_number >> 8) & 0xFF
                b = color_number & 0xFF
                self.setRgb(r, g, b, 255)
            elif largs == 3:
                r, g, b = args
                self.setRgb(r, g, b, 255)
            else:
                r, g, b, a = args
                self.setRgb(r, g, b, a)
        # end def

        def __repr__(self):
            return self.hex()

        def setRgb(self, r, g, b, a=255):
            self.r = r
            self.g = g
            self.b = b
            self.a = a
        # end def

        def setAlpha(self, a):
            self.a = a

        def name(self):
            return self.hex()

        def hex(self):
            return "#{:02X}{:02X}{:02X}{:02X}".format(self.r, self.g, self.b, self.a)
    #end def

def intToColor(color_number):
    """ legacy color support
    """
    return Color('#' + hex(color_number)[2:])

def intToColorHex(color_number):
    return '#' + hex(color_number)[2:]
