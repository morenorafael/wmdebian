from settings.screens.laptop import screen as laptop
from settings.screens.monitor_a import screen as monitor_a
# from settings.screens.monitorb_b import screen as monitor_b

widget_defaults = dict(
    font='FiraCode Nerd Font',
    fontsize=14,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [laptop, monitor_a]
