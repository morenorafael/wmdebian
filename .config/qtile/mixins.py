from libqtile import widget


def separator(foreground, background):
    return widget.TextBox(
        foreground=foreground,
        background=background,
        text="\ue0b2",
        font="Inconsolata for powerline",
        fontsize=27,
        padding=-1
    )
