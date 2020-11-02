# coding=utf-8
from setuptools import setup

########################################################################################################################

plugin_identifier = "Ender3SDFix"
plugin_package = "Ender3_SD_fix"
plugin_name = "Convert TF to SD"
plugin_version = "2.0.0"
plugin_description = "Convert TF card to SD card for Ender 3."
plugin_author = "TT"
plugin_author_email = "me@randomplace.net"
plugin_url = "https://github.com/Tctutt/Ender-3-SD-card-fixer"
plugin_license = "AGPLv3"
plugin_additional_data = []
plugin_additional_packages = []
plugin_ignored_packages = []
additional_setup_parameters = {}

########################################################################################################################

try:
    import octoprint_setuptools
except ImportError:
    print("Could not import OctoPrint's setuptools, are you sure you are running that under "
          "the same python installation that OctoPrint is installed under?")
    import sys
    sys.exit(-1)

setup_parameters = octoprint_setuptools.create_plugin_setup_parameters(
    identifier=plugin_identifier,
    package=plugin_package,
    name=plugin_name,
    version=plugin_version,
    description=plugin_description,
    author=plugin_author,
    mail=plugin_author_email,
    url=plugin_url,
    license=plugin_license,
    additional_packages=plugin_additional_packages,
    ignored_packages=plugin_ignored_packages,
    additional_data=plugin_additional_data
)

if len(additional_setup_parameters):
    from octoprint.util import dict_merge
    setup_parameters = dict_merge(setup_parameters, additional_setup_parameters)

setup(**setup_parameters)
