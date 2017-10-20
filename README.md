# TerminalStyler

![screenshot](http://frankiezafe.org/images/6/63/TerminalStyler_screenshot.png)

A simple script, easy to copy/paste next to your python folder, to style the output of print() function: colors, tabs, returns, repetition of characters, etc.

To use efficiently terminal styling, you have to keep in mind that styles overwrites each others sequentially. This behaviour is similar to the opengl one: it keeps the preset as long as you don't reset it. There is only one "global state", while in CSS for instance the context is important. Therefore, if you set the background to red in the first print() and never touch it again, the rest of the print will keep the same style. See inheritance in style_example.py.

Developped on linux, tested in gnome terminal and terminator.

If you need something more advanced, have a look at [colorconsole](https://github.com/lskbr/colorconsole).
