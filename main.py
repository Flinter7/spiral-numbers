# Esercizio
def main():
    # Inserimento grandezza della tabella con controllo
    ROWS = int(input('Inserisci grandezza della tabella: '))
    while ROWS < 1:
        print('Valore non valido. Ritenta')
        ROWS = int(input('Inserisci grandezza della tabella: '))
    COLUMNS = ROWS


    # Creazione tabella di valori nulli, i quali andranno successivamente modificati
    table = []
    row = []
    for i in range(ROWS):
        for j in range(COLUMNS):
            row.append(0)
        table.append(row)
        row = []


    # Calcolo del numero di anelli che contiene la tabella (ad esempio, una tabella 5x5 contiene tre anelli concentrici)
    # con distinzione tra numero pari e dispari di anelli
    print('Tabella risultante:')
    print()
    if ROWS % 2 == 0:
        rings = int(ROWS / 2)
        newTable = evenTable(table, rings)
        for i in range(ROWS):
            for j in range(COLUMNS):
                print('%5d' % newTable[i][j], end='')
            print()
    else:
        rings = int((ROWS/2) + 0.5)
        newTable = oddTable(table, rings)
        for i in range(ROWS):
            for j in range(COLUMNS):
                print('%5d' % newTable[i][j], end='')
            print()

# Questa funzione calcola la tabella risultante nel caso di un numero di anelli pari
def evenTable(tabella, anelli):
    a = list(tabella)
    x = 0
    count = 1
    for r in range(anelli, 0, -1):
        for j in range(x, (r*2) + x):
            a[x][j] = count
            count += 1
        for i in range(x+1, (r*2) + x):
            a[i][(r*2)+x-1] = count
            count += 1
        for j in range((r*2)+x-2, x-1, -1):
            a[(r*2)+x-1][j] = count
            count += 1
        for i in range((r*2)+x-2, x, -1):
            a[i][x] = count
            count += 1
        x += 1

    return a

# Questa funzione calcola la tabella risultante nel caso di un numero di anelli dispari
def oddTable(tabella, anelli):
    a = list(tabella)
    x = 0
    count = 1
    for r in range(anelli, 0, -1):
        for j in range(x, (r*2) + x - 1):
            a[x][j] = count
            count += 1
        for i in range(x+1, (r*2) + x - 1):
            a[i][(r*2)+x-2] = count
            count += 1
        for j in range((r*2) + x - 3, x - 1, -1):
            a[(r*2)+x-2][j] = count
            count += 1
        for i in range((r*2) + x - 3, x, -1):
            a[i][x] = count
            count += 1
        x += 1
    return a

main()
