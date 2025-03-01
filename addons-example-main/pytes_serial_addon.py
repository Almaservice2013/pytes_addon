import bpy
import serial

class PytesSerialAddon(bpy.types.Operator):
    bl_idname = "wm.pytes_serial_addon"
    bl_label = "Pytes Serial Addon"

    def execute(self, context):
        ser = serial.Serial('/dev/ttyUSB0', 115200)
        while True:
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
        return {'FINISHED'}

def menu_func(self, context):
    self.layout.operator(PytesSerialAddon.bl_idname)

def register():
    bpy.utils.register_class(PytesSerialAddon)
    bpy.types.TOPBAR_MT_app_system.append(menu_func)

def unregister():
    bpy.utils.unregister_class(PytesSerialAddon)
    bpy.types.TOPBAR_MT_app_system.remove(menu_func)

if __name__ == "__main__":
    register()
