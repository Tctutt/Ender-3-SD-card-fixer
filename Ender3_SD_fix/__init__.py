from __future__ import absolute_import

def convert_TF_SD(comm, line, *args, **kwargs):
    if "TF" not in line:
        return line
    goodline = line.replace("TF","SD")
    return goodline

__plugin_name__ = "Convert TF to SD"
__plugin_version__ = "1.0.0"
__plugin_description__ = "Convert TF to SD in printer responses"
__plugin_hooks__ = {
    "octoprint.comm.protocol.gcode.received": convert_TF_SD
}
__plugin_author__ = "Tyler Tuttle"
__plugin_url__ = "https://github.com/Tctutt/Ender-3-SD-card-fixer/"
