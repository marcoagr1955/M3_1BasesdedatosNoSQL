import requests

# URL de la API
url = "https://66b4e5549f9169621ea4c38c.mockapi.io/api/v1/contactos"

# Datos del nuevo registro que deseas agregar
nuevo_registro = {
    "nombre": "Juan Pérez",
    "email": "juan.perez@example.com",
    "telefono": "+52 123 456 7890",
    "direccion": "Calle Falsa 123, Ciudad de México"
}

# Realizar la solicitud POST para agregar el nuevo registro
response = requests.post(url, json=nuevo_registro)

# Comprobar si la solicitud fue exitosa
if response.status_code == 201:
    print("Registro agregado exitosamente:")
    print(response.json())  # Mostrar el registro agregado
else:
    print(f"Error al agregar el registro: {response.status_code}")
