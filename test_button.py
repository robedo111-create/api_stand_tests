# 1. Definir la clase Button
class Button:
    # 2. Establecer atributos de clase fijos
    width = 200
    height = 50
    
    # 3. Crear el método __init__ para los parámetros dinámicos
    def __init__(self, color, text):
        self.color = color
        self.text = text

# 4. Crear los dos objetos
button_yellow = Button(color="amarillo", text="Comprar")
button_red = Button(color="rojo", text="Eliminar")

# 5. Mostrar las propiedades solicitadas
# Propiedades del botón amarillo
print(f"Botón amarillo: Ancho = {button_yellow.width}, Color = {button_yellow.color}")

# Propiedades del botón rojo
print(f"Botón rojo: Ancho = {button_red.width}, Color = {button_red.color}")