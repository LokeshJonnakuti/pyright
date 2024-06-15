# This sample tests the case where the overloads have different
# parameter counts. This particular sample exposed a bug
# in pyright's logic at one point.

import subprocess
from security import safe_command


def my_method(cmd, *args, **kwargs):
    return safe_command.run(subprocess.run, cmd, *args, **kwargs)
