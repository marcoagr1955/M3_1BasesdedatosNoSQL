import requests

# URL base de la API
url_base = "https://66b4e5549f9169621ea4c38c.mockapi.io/api/v1/contactos"

# ID del registro que deseas eliminar
registro_id = "1"  # Cambia "1" por el ID del registro que quieres eliminar

# URL completa para el registro específico
url_registro = f"{url_base}/{registro_id}"

# Realizar la solicitud DELETE para eliminar el registro
response = requests.delete(url_registro)

# Comprobar si la solicitud fue exitosa
if response.status_code == 200:
    print(f"Registro con ID {registro_id} eliminado exitosamente.")
else:
    print(f"Error al eliminar el registro: {response.status_code}")
