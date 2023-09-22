import platform
import psutil
from datetime import datetime

def get_system_info():
    system_info = {
        'Sistema': platform.system(),
        'Release': platform.release(),
        'Versión': platform.version(),
        'Arquitectura': platform.machine(),
        'Procesador': platform.processor(),
        'Hostname': platform.node(),
    }

    return system_info

def get_resource_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    memory_usage = {
        'Memoria Total (MB)': round(memory.total / (1024 ** 2), 2),
        'Memoria Disponible (MB)': round(memory.available / (1024 ** 2), 2),
        'Memoria Ocupada (MB)': round(memory.used / (1024 ** 2), 2),
        'Uso de Memoria (%)': memory.percent
    }

    disk = psutil.disk_usage('/')
    disk_usage = {
        'Espacio de Disco Total (GB)': round(disk.total / (1024 ** 3), 2),
        'Espacio de Disco Libre(GB)': round(disk.free / (1024 ** 3), 2),
        'Espacio de Disco Usado (GB)': round(disk.used / (1024 ** 3), 2),
        'Uso de Disco (%)': disk.percent
    }

    return cpu_usage, memory_usage, disk_usage

if __name__ == "__main__":
    system_info = get_system_info()
    cpu_usage, memory_usage, disk_usage = get_resource_usage()

    # Obtener la fecha y hora actual
    now = datetime.now()
    date_time = now.strftime("%Y%m%d_%H%M%S")  # Formato de nombre de archivo: YYYYMMDD_HHMMSS

    # Crear el nombre del archivo con la fecha y hora actual
    file_name = f"C:/Users/aaron/Documents/Informes/informe_{platform.node()}_{date_time}.txt"

    # Escribir la información en el archivo
    with open(file_name, 'w') as file:
        file.write("--- Información de Sistema ---\n")
        for key, value in system_info.items():
            file.write(f"{key}: {value}\n")

        file.write("\n--- Uso de Recursos ---\n")
        file.write(f"Uso de CPU (%): {cpu_usage}\n")
        for key, value in memory_usage.items():
            file.write(f"{key}: {value}\n")
        for key, value in disk_usage.items():
            file.write(f"{key}: {value}\n")

    print(f"Información guardada en el archivo: {file_name}")