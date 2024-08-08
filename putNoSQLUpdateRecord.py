import requests

# URL base de la API
url_base = "https://66b4e5549f9169621ea4c38c.mockapi.io/api/v1/contactos"

# ID del registro que deseas modificar
registro_id = "1"  # Cambia "1" por el ID del registro que quieres modificar

# URL completa para el registro específico
url_registro = f"{url_base}/{registro_id}"

# Datos que deseas actualizar en el registro
registro_modificado = {
    "nombre": "Juan Pérez Modificado",
    "email": "juan.perez.modificado@example.com",
    "telefono": "+52 987 654 3210",
    "direccion": "Avenida Siempre Viva 742, Ciudad de México"
}

# Realizar la solicitud PUT para modificar el registro
response = requests.put(url_registro, json=registro_modificado)

# Comprobar si la solicitud fue exitosa
if response.status_code == 200:
    print("Registro modificado exitosamente:")
    print(response.json())  # Mostrar el registro modificado
else:
    print(f"Error al modificar el registro: {response.status_code}")
