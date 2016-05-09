"""
BundleChecker helps manage your Juju bundle files.
"""
import os
from ruamel import yaml
from CharmTools import CharmTools

JUJU_REPOSITORY = os.getenv('JUJU_REPOSITORY')


class Bundler:
    """The library class to check and update bundles."""

    def __init__(self, path):
        """Create a BundleChecker by reading in an existing bundle."""
        self.bundle_path = path
        self.bundle = self.read_bundle(path)

    def dump_bundle(self):
        """Convert the python structure into a yaml representation."""
        return yaml.dump(self.bundle, Dumper=yaml.RoundTripDumper)

    def read_bundle(self, path):
        """Read the bundle yaml and convert it to python objects."""
        if not os.path.isfile(path):
            raise Exception('File {0} not found'.format(path))
        with open(path) as stream:
            return yaml.load(stream, yaml.RoundTripLoader)

    def build(self, options={}):
        """Pull the layers for each charm and compile each on this machine,
        and return a local bundle that will deploy the compiled charms."""
        services = self.bundle['services']
        for service in services:
            charm = self.bundle['services'][service]['charm']
            print('Pull source for: ' + charm)

    def update(self, options={}):
        """Update the bundle with the optional options."""
        services = self.bundle['services']
        for service in services:
            charm = self.bundle['services'][service]['charm']
            name, revno = charm.rsplit('-', 1)
            cs_revno = str(CharmTools.charm_show(name)['id']['Revision'])
            if cs_revno != revno:
                print('{0} revision number {1}'.format(name, cs_revno))
                new_charm = name + '-' + cs_revno
                self.bundle['services'][service]['charm'] = new_charm
        return self.dump_bundle()

    def make_local(self, bundle, options={}):
        """Make the bundle have local references."""
        services = self.bundle['services']
        for service in services:
            charm = self.bundle['services'][service]['charm']
            if not charm.startswith('local:'):
                # Logic must handle:
                # cs:~usernamespace/series/charm-name-revno#
                # cs:trusty/charm-name-revno#
                # trusty/charm-name-revno#
                # mysql
                # <repository>:<series>/<service>
                name, revno = charm.rsplit('-', 1)
                prefix, basename = name.rsplit('/', 1)
                if '/' in prefix:
                    prefix, series = prefix.rsplit('/', 1)
                elif ':' in prefix:
                    prefix, series = prefix.rsplit(':', 1)
                new_name = 'local:{0}/{1}'.format(series, basename)
                self.bundle['services'][service]['charm'] = new_name
        return self.dump_bundle()
