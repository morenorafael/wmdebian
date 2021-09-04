from os import path
from libqtile import bar, widget
from libqtile.config import Screen

from settings.path import qtile_path
from mixins import separator
from themes.material.oceanic.colors import colors as ocean


screen = Screen(
    top=bar.Bar(
        [
            widget.GroupBox(
                foreground=ocean["foreground"],
                background=ocean["background"],
                font='Ubuntu Nerd Font',
                fontsize=19,
                margin_y=3,
                margin_x=0,
                padding_y=30,
                padding_x=15,
                borderwidth=2,
                active=ocean["foreground"],
                inactive=ocean["foreground"],
                rounded=False,
                highlight_method='line',
                highlight_color=ocean["background"],
                this_current_screen_border=ocean["accent"],
                this_screen_border=["#5c5c5c", "#5c5c5c"],
                other_current_screen_border=ocean["background"],
                other_screen_border=ocean["background"],
                hide_unused=True,
            ),
            widget.WindowName(
                foreground=ocean["accent"],
                background=ocean["background"],
                font='UbuntuMono Nerd Font Bold',
                fontsize=14,
            ),
            widget.Chord(
                chords_colors={
                    'launch': ("#ff0000", "#ffffff"),
                },
                name_transform=lambda name: name.upper(),
            ),
            widget.Sep(
                background=ocean["background"],
                linewidth=0,
                padding=5
            ),

            # LAYOUT
            separator(ocean["purple"], ocean["background"]),
            widget.CurrentLayoutIcon(
                foreground=ocean["background"],
                background=ocean["purple"],
                scale=0.65
            ),
            widget.CurrentLayout(
                foreground=ocean["background"],
                background=ocean["purple"],
            ),
            widget.Sep(
                background=ocean["purple"],
                linewidth=0,
                padding=5
            ),

            # BATTERY
            separator(ocean["green"], ocean["purple"]),
            widget.Battery(
                foreground=ocean["background"],
                background=ocean["green"],
                discharge_char="",
                charge_char="",
                full_char="",
                unknown_char="",
                format="{char} {percent:2.0%}",
                low_percentage=0.2,
                low_foreground=ocean["red"][0],
                show_short_text=False
            ),
            widget.Sep(
                background=ocean["green"],
                linewidth=0,
                padding=5
            ),

            # NET
            separator(ocean["blue"], ocean["green"]),
            widget.TextBox(
                foreground=ocean["background"],
                background=ocean["blue"],
                text="直 "
            ),
            widget.Net(
                foreground=ocean["background"],
                background=ocean["blue"],
                interface="wlp61s0",
                format="WiFi: {up} ↑↓ {down}",
            ),
            widget.Sep(
                background=ocean["blue"],
                linewidth=0,
                padding=5
            ),

            # Keyboard Layout
            separator(ocean["orange"], ocean["blue"]),
            widget.TextBox(
                foreground=ocean["background"],
                background=ocean["orange"],
                text=" "
            ),
            widget.KeyboardLayout(
                foreground=ocean["background"],
                background=ocean["orange"],
                configured_keyboards=["us", "latam"],
            ),
            widget.Sep(
                background=ocean["orange"],
                linewidth=0,
                padding=5
            ),

            # FECHA Y HORA
            separator(ocean["cyan"], ocean["orange"]),
            widget.TextBox(
                foreground=ocean["background"],
                background=ocean["cyan"],
                font='Ubuntu Nerd Font',
                text=" "
            ),
            widget.Clock(
                foreground=ocean["background"],
                background=ocean["cyan"],
                padding=5,
                format='%d de %B - %I:%M %p'
            ),
            # widget.QuickExit(),
        ],
        30,
        background=ocean["background"],
        opacity=1,
    ),
)
