import sender_stand_request
import data

# Esta función cambia el nombre en el cuerpo de la solicitud
def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

# Aserción para pruebas positivas (código 201)
def positive_assert(kit_body):
    # Obtener el token (deberás tener esta función definida en sender_stand_request)
    auth_token = sender_stand_request.get_new_user_token()
    # Enviar solicitud
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    # Validaciones
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == kit_body["name"]

# Aserción para pruebas negativas (código 400)
def negative_assert_code_400(kit_body):
    auth_token = sender_stand_request.get_new_user_token()
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert kit_response.status_code == 400

# --- EJEMPLO DE PRUEBAS ---

# Prueba 1: Éxito (nombre de 1 letra)
def test_create_kit_1_letter_in_name_get_success_response():
    kit_body = get_kit_body("a")
    positive_assert(kit_body)

# Prueba 8: Error (parámetro vacío)
def test_create_kit_no_name_get_error_response():
    kit_body = {} # O usa tu lógica para enviar cuerpo vacío
    negative_assert_code_400(kit_body)