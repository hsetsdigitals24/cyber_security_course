"""Start simulator with temporary tokens entered without echo."""
import getpass
import os
import runpy
from pathlib import Path
for role in ("READER", "WRITER"):
    os.environ["HSETS_" + role + "_TOKEN"] = getpass.getpass(role + " temporary token: ")
runpy.run_path(str(Path(__file__).with_name("object_service.py")), run_name="__main__")

