from styler import *

print( style("_n2|b|**5") + "STYLES"  + style("**5||_n")  )
print( style("b") + "bold"  + style("") + " and reset"  )
print( style("i") + "italic"  + style("") + " and reset"  )
print( style("u") + "underline"  + style("") + " and reset"  )
print( style("s") + "strikethrough"  + style("") + " and reset"  )

print( style("_n2|b|**5") + "COLORS"  + style("**5||_n")  )
print( style("red") + "red"  + style("") + " and reset"  )
print( style("dgreen") + "dark green"  + style("") + " and reset"  )
print( style("bg_red") + "red background"  + style("") + " and reset"  )
print( style("bg_cyan|yellow") + "yellow on cyan background"  + style("") + " and reset"  )

print( style("_n2|b|**5") + "SPECIAL CHARS"  + style("**5||_n|bg_blue")  )
print( style("_s3") + "3 spaces in front"  )
print( style("_s5") + "5 spaces in front"  )
print( style("_t") + "1 tab"  )
print( style("_t2") + "2 tabs" + style("bg_red") )
print( style("_t2|bg_green|_s3") + "2 tabs & 3 spaces" + style("") )

print( style("_n2|b|**5") + "CHAR REPEAT"  + style("**5||_n")  )
print( "10 times '*': " + style("**10")  )
print( "25 times '_': " + style("*_25")  )
print( "50 times '#': " + style("*#50")  )
print( "you got the idea, prefix with '*' any character to repeat"  )

print( style("_n2|b|**5") + "INHERITANCE"  + style("**5|_n|bg_blue")  )
print( "style is kept" )
print( style("") + "reseting string style, but not line" )
print( "background is gone thanks to previous line" )
print( style("_n2") )
