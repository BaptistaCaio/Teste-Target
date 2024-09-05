def verificar_letra_a(texto):
    texto = texto.lower()  # Converte a string para minúsculas
    quantidade = texto.count('a')
    
    if quantidade > 0:
        return f"A letra 'a' foi encontrada {quantidade} vez(es) no texto fornecido."
    else:
        return "A letra 'a' não foi encontrada na string."

entrada = input("Forneça um texto ou frase para verificar a ocorrência da letra 'a': ")

resultado = verificar_letra_a(entrada)
print(resultado)
