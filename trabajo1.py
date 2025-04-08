# Esto es un diccionario que te explica expresiones que tal vez no sepas que hacer
meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL": "una respuesta a una broma",
            "SHEESH": "ligera desaprobación",
            "CREEPY": "aterrador, siniestro",
            "AGGRO": "ponerse agresivo/enojado"
            "PARCE": "amigo/amiga"
            "BACANO": "bueno/divertido"
            }
# Una lista
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

# Una variable 
if word in meme_dict.keys():
    print(word)
else:
    # ¿Qué hacer si no se encuentra la palabra?
    print("Esa palabra no esta en nuestro diccionario")
