# Print a line_________________________________________________________________:
def linha(tam=42):
    return '-' * tam


# Headline_____________________________________________________________________:
def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


# Check the ashwer to the menu_________________________________________________:
def resp(res):
    while True:
        try:
            n = int(input(res))
        except (ValueError, TypeError):
            print('Error, please type an valid number')
        else:
            return n


# Print the menu options_______________________________________________________:
def menu(lista):
    print('Escolha uma opção: ')
    print()
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = resp('R: ')
    return opc
