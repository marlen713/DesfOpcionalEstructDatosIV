import requests


# 1. CON EL GET NOSOTROS VAMOS A CONSUMIR LOS DATOS
url = "https://reqres.in/api/users"
response = requests.get(url)
users_data = response.json()

print("AQUI ESTOY CONSUMIENDO A API")
print(users_data)



# 2.  AQUI ESTOY CREANDO A IGNACIO
# CON EL POST NOSOTROS VAMOS A ENVIAR DATOS AQUI ESTAMOS ENVIANDO 
# CON EL CREATE_USERS ESTAMOS ENVIANDO DATOS NUEVOS QUE CUANDO REVISAMOS ABAJO APARECEN
new_user = {    
    'name': 'Ignacio', 
    'word': 'Profesor',
}
response = requests.post(url, json=new_user)
created_user = response.json()
print("AGREGANDO DATOS A LA API")
print(created_user)



# 3. CON EL PUT se llamara morpheus para que tenga un campo llamado residence igual a zion.  
# El id 1 
update_data = { 
    "name": "morpheus",
    "residence": "zion"
}
response = requests.put(f"https://reqres.in/api/users/2", json=update_data)
update_user= response.json()
print("CAMBIANDO DATOS A LA API")
print(update_user)


# 4. ELIMINAR el ID del usuario Tracey es (6). Realizar la solicitud DELETE
url = 'https://reqres.in/api/users/6' 
response = requests.delete(url)

# Imprimir el código de respuesta en pantalla
print("Eliminando usuario Tracey...")
print("Código de respuesta:", response.status_code)