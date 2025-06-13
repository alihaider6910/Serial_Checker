import wmi
from colorama import Fore, Style, init
import os

init(autoreset=True)
c = wmi.WMI()

def print_section(title, color):
    print(color + title + Style.RESET_ALL)
    print("=" * 30)

os.system('cls' if os.name == 'nt' else 'clear')

print_section("Disk Number", Fore.RED)
for disk in c.Win32_DiskDrive():
    print("Serial Number:")
    print(f"    {getattr(disk, 'SerialNumber', 'N/A')}")
    print(f"    Model: {getattr(disk, 'Model', 'N/A')}")
    print(f"    DeviceID: {getattr(disk, 'DeviceID', 'N/A')}")
    print(f"    PNPDeviceID: {getattr(disk, 'PNPDeviceID', 'N/A')}")
    print()

print_section("Motherboard", Fore.YELLOW)
for board in c.Win32_BaseBoard():
    print("SerialNumber")
    print(getattr(board, 'SerialNumber', 'N/A'))
print()

print_section("SMBios", Fore.GREEN)
for sys in c.Win32_ComputerSystemProduct():
    print("UUID")
    print(getattr(sys, 'UUID', 'N/A'))
print()

print_section("GPU", Fore.CYAN)
for gpu in c.Win32_VideoController():
    print("Description\tPNPDeviceID")
    print(f"{gpu.Name}\t{gpu.PNPDeviceID}")
print()

print_section("RAM", Fore.BLUE)
for mem in c.Win32_PhysicalMemory():
    print("SerialNumber")
    print(getattr(mem, 'SerialNumber', 'N/A'))
print()

print_section("Bios", Fore.MAGENTA)
for bios in c.Win32_BIOS():
    print("UUID")
    print(getattr(bios, 'SerialNumber', 'N/A'))
print()

print_section("CPU", Fore.RED)
for cpu in c.Win32_Processor():
    print("ProcessorId")
    print(getattr(cpu, 'ProcessorId', 'N/A'))
print()

input("Press any key to get your hardware serials again.") 