font = {}
font['0'] = '\033[0m'      #default, white

# style
font['b'] = '\033[1m'      #bold
font['i'] = '\033[3m'      #italic
font['u'] = '\033[4m'      #underline
font['s'] = '\033[9m'      #strikethrough

# special chars
# suffix it with a number to add several
# ex: _t4 => add 4 tabs
font['_t'] = '\t'           #tab
font['_n'] = '\n'           #new line
font['_s'] = ' '            #space

# light colors
font['grey'] = '\033[90m'
font['red'] = '\033[91m'
font['green'] = '\033[92m'
font['yellow'] = '\033[93m'
font['blue'] = '\033[94m'
font['purple'] = '\033[95m'
font['cyan'] = '\033[96m'

# dark colors
font['dgrey'] = '\033[30m'
font['dred'] = '\033[31m'
font['dgreen'] = '\033[32m'
font['dyellow'] = '\033[33m'
font['dblue'] = '\033[34m'
font['dpurple'] = '\033[35m'
font['dcyan'] = '\033[36m'

# background
font['bg_normal'] = '\033[6m'
font['bg_white'] = '\033[7m'
font['bg_grey'] = '\033[47m'
font['bg_dark_grey'] = '\033[40m'
font['bg_red'] = '\033[41m'
font['bg_green'] = '\033[42m'
font['bg_yellow'] = '\033[43m'
font['bg_blue'] = '\033[44m'
font['bg_purple'] = '\033[45m'
font['bg_cyan'] = '\033[46m'

def style( s ):
    if len(s) == 0:
        return font['0']
    l = s.split('|')
    out = ''
    for i in range(0,len(l)):
        if len( l[i] ) == 0:
            out += font['0']
        elif len( l[i] ) >= 2 and l[i][0:1] == '*':
            char = l[i][1:2]
            count = 0
            try:
                count = int( l[i][2:] )
            except:
                count = 1
            for c in range(0,count):
                out += char
        elif len( l[i] ) >= 2 and ( l[i][0:2] == '_t' or l[i][0:2] == '_n' or l[i][0:2] == '_s' ):
            char = l[i][0:2]
            count = 0
            try:
                count = int( l[i][2:] )
            except:
                count = 1
            for c in range(0,count):
                out += font[char]
        else:
            out += font[l[i]]
    return out
