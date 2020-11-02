from __future__ import absolute_import

def convert_TF_SD(comm, line, *args, **kwargs):
    if "TF" not in line:
        return line
    goodline = line.replace("TF","SD")
    return goodline




__plugin_hooks__ = {
    "octoprint.comm.protocol.gcode.received": convert_TF_SD
}


