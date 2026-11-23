import logging
import os

from smarties4planck.classes import *
from smarties4planck.core_functions import *
from smarties4planck.external_qp_planck import *


def setup_logging(level=None):
    """Log smarties4planck and smarties messages to stderr; call once from your script.

    `level` defaults to $SMARTIES4PLANCK_LOGLEVEL, else INFO.
    """
    level = (level or os.environ.get("SMARTIES4PLANCK_LOGLEVEL", "INFO")).upper()
    for name in ("smarties4planck", "smarties"):
        logger = logging.getLogger(name)
        if not any(isinstance(h, logging.StreamHandler) for h in logger.handlers):
            handler = logging.StreamHandler()
            handler.setFormatter(
                logging.Formatter("%(asctime)s %(levelname)s %(name)s: %(message)s")
            )
            logger.addHandler(handler)
        logger.setLevel(level)
        logger.propagate = False
