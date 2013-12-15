from overkill import manager
from overkill.extra.bar import *
from overkill.extra.bar.widgets import *

bar = Bar()

arrows = r'\f7 << \fr'

bar.set_widget(Layout([
    MultiMonitorWidget(),
    Layout([
        CPUWidget(),
        MemWidget(),
        TempWidget(),
        AudioWidget(),
        BatteryWidget(),
        ExtendedMailCountWidget(),
        NetWidget(("eth0", "wlan0")),
        ClockWidget(" ".join(("%Y{faded}.{normal}%m{faded}.{normal}%d{focus}/{faded}%a{normal}",
                              "{highlight}%H{faded}:{highlight}%M{normal}")).format(
                                  faded = r"\f3",
                                  normal = r"\fr",
                                  focus = r"\f7",
                                  highlight = r"\f5"
                              ))
    ], prefix=r"\r"+arrows, postfix=arrows, separator=arrows, debounce_params=(.1, 1))
], postfix="   "*5, ))

manager.add_sink(bar)
