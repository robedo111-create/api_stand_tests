import sender_stand_request
import data

# Función base para preparar el cuerpo del kit con un nombre específico
def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

# 1. Nombre de 1 carácter
def test_create_kit_1_char_name():
    auth_token = sender_stand_request.post_new_user().json()["authToken"]
    response = sender_stand_request.post_new_client_kit(get_kit_body("a"), auth_token)
    assert response.status_code == 201

# 2. Nombre de 511 caracteres
def test_create_kit_511_char_name():
    auth_token = sender_stand_request.post_new_user().json()["authToken"]
    response = sender_stand_request.post_new_client_kit(get_kit_body("a" * 511), auth_token)
    assert response.status_code == 201

# 3. Nombre de 0 caracteres
def test_create_kit_0_char_name():
    auth_token = sender_stand_request.post_new_user().json()["authToken"]
    response = sender_stand_request.post_new_client_kit(get_kit_body(""), auth_token)
    assert response.status_code == 400

# 4. Nombre de 512 caracteres
def test_create_kit_512_char_name():
    auth_token = sender_stand_request.post_new_user().json()["authToken"]
    response = sender_stand_request.post_new_client_kit(get_kit_body("a" * 512), auth_token)
    assert response.status_code == 400

# 5. Caracteres especiales
def test_create_kit_special_chars_name():
    auth_token = sender_stand_request.post_new_user().json()["authToken"]
    response = sender_stand_request.post_new_client_kit(get_kit_body("№%@"), auth_token)
    assert response.status_code == 201

# 6. Espacios
def test_create_kit_spaces_name():
    auth_token = sender_stand_request.post_new_user().json()["authToken"]
    response = sender_stand_request.post_new_client_kit(get_kit_body(" A A "), auth_token)
    assert response.status_code == 201

# 7. Números como texto
def test_create_kit_numbers_as_string_name():
    auth_token = sender_stand_request.post_new_user().json()["authToken"]
    response = sender_stand_request.post_new_client_kit(get_kit_body("123"), auth_token)
    assert response.status_code == 201

# 8. Sin el parámetro name
def test_create_kit_no_name():
    auth_token = sender_stand_request.post_new_user().json()["authToken"]
    kit_body = data.kit_body.copy()
    kit_body.pop("name", None) # Eliminamos la llave 'name'
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 400

# 9. Tipo de dato numérico
def test_create_kit_numeric_type_name():
    auth_token = sender_stand_request.post_new_user().json()["authToken"]
    response = sender_stand_request.post_new_client_kit(get_kit_body(123), auth_token)
    assert response.status_code == 400