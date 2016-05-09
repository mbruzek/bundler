# Bundler

A tool that makes working with Juju bundles easier.

Bundles are a collection of charms their configuration and relations to other
charms captured in a flat file.

## Requires
This tool requires the 2.1 or higher charm-tools and charm packages installed,
along with a connection to the Juju charm store.

The Python ruamel yaml is required for preserving yaml comments, and file
structure. Install the python-ruamel.yaml or python3-ruamel.yaml package.

It may also be useful to have the standard Juju environment variables set.


## update
Bundles contain charms that are often locked to a revision number. During
maintenance of a bundle I often find the need to rectify the bundle with the
latest revision of all its related charms. The Juju charm store has the
information on which revision of the charm is the latest. The update feature
reads in an existing bundle, and checks the charm store for the latest
`Revision` in the charm store.

## local
When making changes to a bundle it may be useful to deploy charms that have
been local changes in them. The local feature reads in an existing bundle, and
makes all the charm references local so you can deploy the same bundle but with
local charms.

## build
Layers build charms, and a collection of charms are in bundles. The build
feature will read in a bundle, use charm-tools to download all the charms
layers or source, and convert the bundle to use local references. This allows
you to make changes to the layers, charms, or bundles.
