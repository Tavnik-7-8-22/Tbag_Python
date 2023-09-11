# How it works
# print((color / style) + "text" + END)

END = '\33[0m'
# END is default text color
BOLD = '\33[1m'
# FAINT = '\33[2m'
# ITALIC = '\33[3m'
UNDERLINE = '\33[4m'
# BLINK = '\33[5m' # blink slow
# BLINK2 = '\33[6m' # blink fast
SELECTED = '\33[7m'
# CONCEAL = '\33[8m'
STRIKETHROUGH = '\33[9m'
BOLDUNDERLINE = '\33[21m'

BLACK = '\33[30m'
RED = '\33[31m'
GREEN = '\33[32m'
YELLOW = '\33[33m'
BLUE = '\33[34m'
VIOLET = '\33[35m'
BEIGE = '\33[36m'
WHITE = '\33[37m'

BLACKBG = '\33[40m'
REDBG = '\33[41m'
GREENBG = '\33[42m'
YELLOWBG = '\33[43m'
BLUEBG = '\33[44m'
VIOLETBG = '\33[45m'
BEIGEBG = '\33[46m'
WHITEBG = '\33[47m'

BOXEDIN = '\33[51m'
BOXEDIN2 = '\33[52m'

GREY = '\33[90m'
RED2 = '\33[91m'
GREEN2 = '\33[92m'
YELLOW2 = '\33[93m'
BLUE2 = '\33[94m'
VIOLET2 = '\33[95m'
BEIGE2 = '\33[96m'
WHITE2 = '\33[97m'

GREYBG = '\33[100m'
REDBG2 = '\33[101m'
GREENBG2 = '\33[102m'
YELLOWBG2 = '\33[103m'
BLUEBG2 = '\33[104m'
VIOLETBG2 = '\33[105m'
BEIGEBG2 = '\33[106m'
WHITEBG2 = '\33[107m'


def print_color_test():
    x = 0
    for i in range(24):
        colors = ""
        for j in range(5):
            code = str(x+j)
            colors = colors + "\33[" + code + "m\\33[" + code + "m\033[0m "
        print(colors)
        x = x + 5


# Run if testing for color
# print_color_test()
