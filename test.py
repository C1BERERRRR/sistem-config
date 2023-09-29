import platform
import wmi


wmi_obj = wmi.WMI()


for gpu in wmi_obj.Win32_VideoController():
    print("Название видеокарты: ", gpu.Caption)
    print("Память видеокарты: ", gpu.AdapterRAM, "байт")
    print("Тип видеокарты: ", gpu.VideoProcessor)

def get_system_info():
    processor = platform.processor()
    video_card = platform.system()
    motherboard = platform.machine()
    
    return processor, video_card, motherboard

def main():
    processor, video_card, motherboard = get_system_info()
    
    print("Processor:", processor)
    print("Motherboard:", motherboard)

if __name__ == "__main__":
    main()
