import logging
import os

from smarties4planck.classes import *
from smarties4planck.core_functions import *
from smarties4planck.external_qp_planck import *

_pkg = logging.getLogger("smarties4planck")

# Give smarties4planck its own stderr output if the user doesn't setup logging.
if not _pkg.handlers:
    handler = logging.StreamHandler()
    handler.setFormatter(
        logging.Formatter("%(asctime)s %(levelname)s %(name)s: %(message)s")
    )
    _pkg.addHandler(handler)

_pkg.propagate = False
_pkg.setLevel(os.environ.get("smarties4planck_LOGLEVEL", "INFO").upper())
