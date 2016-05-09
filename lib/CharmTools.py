"""
Charm is a library to call the various charm commands.
"""

import subprocess
import yaml


class CharmTools:
    """The library class to call various charm commands and return output."""

    @staticmethod
    def charm_show(name):
        """Get the charm information from the charm store."""
        cmd = ['charm', 'show', '--format=yaml', name]
        output = subprocess.check_output(cmd)
        if output:
            return yaml.load(output)
        else:
            return ''
