from overkill import manager
from overkill.extra.mail import MailNotifySink
from overkill.extra.notify import Notify
from overkill.sinks import SimpleSink
from subprocess import Popen

manager.add_sink(MailNotifySink())

class BatteryNotifySink(SimpleSink, Notify):
    summary = "Battery Warning"
    subscription = "battery_percent"
    urgent_percent = 5
    critical_percent = 10
    low_percent = 15
    _current = 100

    def handle_update(self, update):
        # FIXME: It starts at zero
        if update == "0":
            return

        previous = self._current
        self._current = int(update)

        if previous > self.urgent_percent >= self._current:
            Popen(["/usr/bin/systemctl", "suspend"])
        if previous > self.critical_percent >= self._current:
            self.message = "Critical Battery: %d%%" % self._current
            self.urgency = self.notify.URGENCY_CRITICAL
            self.show()
        elif previous > self.low_percent >= self._current:
            self.message = "Low Battery: %d%%" % self._current
            self.urgency = self.notify.URGENCY_NORMAL
            self.show()

manager.add_sink(BatteryNotifySink())
