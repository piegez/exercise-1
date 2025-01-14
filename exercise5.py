def inverted_string(text):
    length = len(text)
    inverted_text = ""

    for i in range(length - 1, -1, -1):
        inverted_text += text[i]
    
    return inverted_text

input = input("Digite a string que quer inverter: ")

output = inverted_string(input)

print(f"String inicial: {input}")
print(f"String invertida: {output}")
