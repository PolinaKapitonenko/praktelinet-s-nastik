# Функция для чтения данных из файла и возврата в виде списка
def luge_fail(faili_nime):
    with open(faili_nime, 'r', encoding='utf-8-sig') as f:
        data = [line.strip() for line in f]
    return data

# Функция для записи данных в файл
def kirjuta_fail(faili_nime, data):
    with open(faili_nime, 'w', encoding='utf-8') as f:
        f.write('\n'.join(data))

# Функция перевода с русского на эстонский и наоборот
def tõlgi_sona(sõna, mis_keelest, mis_keele, dictionary):
    if mis_keelest == 'rus' and mis_keele == 'est':
        key = sõna.lower()
