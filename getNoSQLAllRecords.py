import requests
import pandas as pd
import json

# URL de la API
url = "https://66b4e5549f9169621ea4c38c.mockapi.io/api/v1/contactos"

# Realizar la solicitud GET a la API
response = requests.get(url)

# Comprobar si la solicitud fue exitosa
if response.status_code == 200:
    # Obtener los datos en formato JSON
    contactos_json = response.json()

    # Mostrar los registros en formato JSON formateado
    print("Registros en formato JSON formateado:")
    print(json.dumps(contactos_json, indent=4))

    # Convertir los datos a un DataFrame de pandas
    df_contactos = pd.DataFrame(contactos_json)

    # Mostrar el DataFrame
    print("\nRegistros en formato DataFrame:")
    print(df_contactos)

    # Exportar el DataFrame a un archivo CSV
    df_contactos.to_csv("contactos.csv", index=False)
    print("\nLos datos han sido exportados a 'contactos.csv'")
else:
    print(f"Error al consultar la API: {response.status_code}")
