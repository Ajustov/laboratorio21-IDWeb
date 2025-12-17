import json

equipos = [
    {"nombre": "Alianza Lima", "pais": "Perú", "nivelAtaque": 80, "nivelDefensa": 70},
    {"nombre": "River Plate", "pais": "Argentina", "nivelAtaque": 85, "nivelDefensa": 75}
]

texto_json = json.dumps(equipos, indent=4)
print(texto_json)

