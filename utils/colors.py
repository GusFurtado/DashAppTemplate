'''
Color palette object
'''



_HUES = {
    'gold': ['#FFDF99', '#FFC547', '#E69F00', '#A37000', '#523800'],
    'green': ['#47FFCE', '#00F5B4', '#009E73', '#00664B', '#00291E'],
    'blue': ['#5CC3FF', '#0AA5FF', '#0072B2', '#004E7A', '#00273D'],
    'pink': ['#F9F0F5', '#E3B5CE', '#CC79A7', '#B14380', '#762D55'],
    'yellow': ['#FCFAD9', '#F6EF8E', '#F0E442', '#D0C311', '#847C0B']
}



class Colors:

    def __init__(self, palette='gold'):
        self.set_palette(palette)

    def set_palette(self, palette):
        h = _HUES[palette]
        self.lighter = h[0]
        self.light = h[1]
        self.medium = h[2]
        self.dark = h[3]
        self.darker = h[4]