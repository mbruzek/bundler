"""
Charm is a library to call the various charm commands.
"""

import subprocess
import yaml


class CharmTools:
    """The library class to call various charm commands and return output."""

    @staticmethod
    def charm_show(name, fields=[]):
        """Get the charm information from the charm store."""
        cmd = ['charm', 'show', '--format=yaml', name] + fields
        output = subprocess.check_output(cmd)
        if output:
            return yaml.load(output)
        else:
            return ''

    @staticmethod
    def charm_pull_source(item, destination=None):
        """Download the source code for a charm, layer or interface."""
        cmd = ['charm', 'pull-source', '-v', item]
        if destination:
            cmd.append(destination)
        return subprocess.check_call(cmd)
