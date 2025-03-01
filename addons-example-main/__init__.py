
bl_info = {
    "name": "Pytes Serial Addon",
    "blender": (2, 80, 0),
    "category": "System",
}

from . import pytes_serial_addon

def register():
    pytes_serial_addon.register()

def unregister():
    pytes_serial_addon.unregister()
