from overkill.extra.sources import *
from overkill import manager
import os

MAIL_BASE = os.path.expanduser("~/.mail")
MAIL_DIRS = [
    os.path.join(MAIL_BASE, f)
    for f in os.listdir(MAIL_BASE)
    if f[0] != "."
]

MAIL_QUEUE = os.path.expanduser("~/.mail.queue")

manager.add_source(BSPWMSource())
manager.add_source(PulseaudioSource())
manager.add_source(ConkySource())
manager.add_source(TimeSource())
manager.add_source(MaildirSource(MAIL_DIRS))
manager.add_source(MailqueueSource(MAIL_QUEUE))
