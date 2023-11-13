import platform
import psutil
from datetime import datetime

def get_system_info():
    system_info = {
        'System': platform.system(),
        'Release': platform.release(),
        'Version': platform.version(),
        'Architecture': platform.machine(),
        'CPU': platform.processor(),
        'Hostname': platform.node(),
    }

    return system_info

def get_resource_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    memory_usage = {
        'Total Memory (MB)': round(memory.total / (1024 ** 2), 2),
        'Available Memory (MB)': round(memory.available / (1024 ** 2), 2),
        'Memory Usage (MB)': round(memory.used / (1024 ** 2), 2),
        'Memory Usage (%)': memory.percent
    }

    disk = psutil.disk_usage('/')
    disk_usage = {
        'Total Disk Space (GB)': round(disk.total / (1024 ** 3), 2),
        'Free Disk Space(GB)': round(disk.free / (1024 ** 3), 2),
        'Disk Usage (GB)': round(disk.used / (1024 ** 3), 2),
        'Disk Usage (%)': disk.percent
    }

    return cpu_usage, memory_usage, disk_usage

if __name__ == "__main__":
    system_info = get_system_info()
    cpu_usage, memory_usage, disk_usage = get_resource_usage()

    # Obtener la fecha y hora actual
    now = datetime.now()
    date_time = now.strftime("%Y%m%d_%H%M%S")  # Formato de nombre de archivo: YYYYMMDD_HHMMSS

    # Crear el nombre del archivo con la fecha y hora actual
    file_name = f"./report_{platform.node()}_{date_time}.txt"

    # Escribir la información en el archivo
    with open(file_name, 'w') as file:
        file.write("--- System Information ---\n")
        for key, value in system_info.items():
            file.write(f"\t{key}: {value}\n")

        file.write("\n--- Resource Usage ---\n")
        file.write(f"\tCPU Usage (%): {cpu_usage}\n")
        for key, value in memory_usage.items():
            file.write(f"\t{key}: {value}\n")
        for key, value in disk_usage.items():
            file.write(f"\n\t{key}: {value}")

    print(f"Information stored in: {file_name}")
