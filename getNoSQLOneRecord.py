import requests

# URL base de la API
url_base = "https://66b4e5549f9169621ea4c38c.mockapi.io/api/v1/contactos"

# ID del registro que deseas consultar
registro_id = "2"  # Cambia "1" por el ID del registro que quieres consultar

# Construir la URL para consultar un registro específico
url_registro = f"{url_base}/{registro_id}"

# Realizar la solicitud GET a la API
response = requests.get(url_registro)

# Comprobar si la solicitud fue exitosa
if response.status_code == 200:
    # Obtener los datos del registro en formato JSON
    registro_json = response.json()

    # Mostrar todos los campos en formato plano
    print("Registro en formato plano:")
    for key, value in registro_json.items():
        print(f"{key}: {value}")
else:
    print(f"Error al consultar la API: {response.status_code}")
