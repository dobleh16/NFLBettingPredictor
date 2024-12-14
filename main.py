def ganador(equipol, equipov, mlhome, mlvisit, lastfivel, lastfivev, homespread, visitpread, handicapl, handicapv, cantidadpartidos,
                   overunder, overunderl
                   ,overunderv, homesrecordl, visitrecordl, homesrecordv, visitrecordv, atslastseasonl,
                   atslastseasonv,
                   atsseasonl, atsseasonv, atsplayoffsl, atsplayoffsv, cuotaganadorl, cuotaganadorv, cuotahandicapl, cuotahandicapv, montoapuesta):

    sum1 = 0
    sum2 = 0

    if mlhome > mlvisit and mlhome >= 70:
        sum1 = sum1 - 2
        sum2 = sum2 + 2
        if mlhome >= 90:
            sum1 = sum1 - 1
            sum2 = sum2 + 1
    if mlhome < mlvisit and mlvisit >= 70:
        sum1 = sum1 + 2
        sum2 = sum2 - 2
        if mlvisit >= 90:
            sum1 = sum1 + 1
            sum2 = sum2 - 1
    if mlhome > mlvisit and mlhome <= 69:
        sum1 = sum1 + 2
        sum2 = sum2 - 1
    if mlhome < mlvisit and mlvisit <= 69:
        sum2 = sum2 + 2
        sum1 = sum1 - 1
    if mlhome == mlvisit:
        sum1 = sum1 + 1
        sum2 = sum2 + 1

    if lastfivel > lastfivev:
        sum1 = sum1 + 2
        sum2 = sum2 - 2
    if lastfivel < lastfivev:
        sum2 = sum2 + 2
        sum1 = sum1 - 2
    if lastfivel == lastfivev:
        sum1 = sum1 + 1
        sum2 = sum2 + 1

    if homespread > visitpread and homespread >= 70:
        sum1 = sum1 - 2
        sum2 = sum2 + 2
        if homespread >= 90:
            sum1 = sum1 - 1
            sum2 = sum2 + 1
    if homespread < visitpread and visitpread >= 70:
        sum1 = sum1 + 2
        sum2 = sum2 - 2
        if visitpread >= 90:
            sum1 = sum1 + 1
            sum2 = sum2 - 1
    if homespread > visitpread and homespread <= 69:
        sum1 = sum1 + 2
        sum2 = sum2 - 1
    if homespread < visitpread and visitpread <= 69:
        sum1 = sum1 - 1
        sum2 = sum2 + 2
    if homespread == visitpread:
        sum1 = sum1 + 1
        sum2 = sum2 + 1

    if homesrecordl > homesrecordv:
        sum1 = sum1 + 3
        sum2 = sum2 - 2
    if homesrecordl < homesrecordv:
        sum2 = sum2 + 3
        sum1 = sum1 - 2
    if homesrecordl == homesrecordv:
        sum1 = sum1 + 1
        sum2 = sum2 + 1

    if visitrecordl > visitrecordv:
        sum1 = sum1 + 2
        sum2 = sum2 - 1
    if visitrecordl < visitrecordv:
        sum2 = sum2 + 2
        sum1 = sum1 - 1
    if visitrecordl == visitrecordv:
        sum1 = sum1 + 1
        sum2 = sum2 + 1

    if atslastseasonl > atslastseasonv:
        sum1 = sum1 + 3
        sum2 = sum2 - 1
    if atslastseasonl < atslastseasonv:
        sum2 = sum2 + 3
        sum1 = sum1 - 1
    if atslastseasonl == atslastseasonv:
        sum1 = sum1 + 1
        sum2 = sum2 + 1

    if atsseasonl > atsseasonv:
        sum2 = sum2 - 2
        sum1 = sum1 + 2
    if atsseasonl < atsseasonv:
        sum2 = sum2 + 2
        sum1 = sum1 - 2
    if atsseasonl == atsseasonv:
        sum1 = sum1 + 1
        sum2 = sum2 + 1

    if atsplayoffsl > atsplayoffsv:
        sum1 = sum1 + 3
        sum2 = sum2 - 2
    if atsplayoffsl < atsplayoffsv:
        sum1 = sum1 - 2
        sum2 = sum2 + 3
    if atsplayoffsl == atsplayoffsv:
        sum1 = sum1 + 1
        sum2 = sum2 + 1

    tp = 0
    tp = (overunderl + overunderv)/cantidadpartidos

    if sum1 > sum2:
        print("===================================================================================================================================================================")
        print("Apuesta que ganaran los " + equipol)
        print("Con cuota de ")
        print(cuotaganadorl)
        print("La probabilidad de ganar esta cuota es de")
        probabilidad = (1 / cuotaganadorl) * 100
        print(probabilidad)
        print("Apuesta por el handicap de los " + equipol)
        print(handicapl)
        print("Con cuota de")
        print(cuotahandicapl)
        print("La probabilidad de ganar esta cuota es de")
        probabilidad1 = (1 / cuotahandicapl) * 100
        print(probabilidad1)
        if tp > overunder:
            print("Apuesta por el over de puntos ")
            print(overunder)
        else:
            print("Apuesta por el under de puntos ")
            print(overunder)

        print("Tu monto a apostar es de ")
        print(montoapuesta)
        print("El valor estimado a ganar si apuestas que ganan los " + equipol + "es de")
        totalcg = ((montoapuesta * cuotaganadorl) - montoapuesta)
        print(totalcg)
        print("El valor estimado a ganar si apuestas por el handicap de los " + equipol + "es de")
        totalchl = ((montoapuesta * cuotahandicapl) - montoapuesta)
        print(totalchl)

    else:
        print("===================================================================================================================================================================")
        print("Apuesta que ganaran los " + equipov)
        print("Con cuota de ")
        print(cuotaganadorv)
        print("La probabilidad de ganar esta cuota es de")
        probabilidad = (1 / cuotaganadorv) * 100
        print(probabilidad)
        print("Apuesta por el handicap de los " + equipov)
        print(handicapv)
        print("Con cuota de")
        print(cuotahandicapv)
        print("La probabilidad de ganar esta cuota es de")
        probabilidad1 = (1 / cuotahandicapv) * 100
        print(probabilidad1)
        if tp > overunder:
            print("Apuesta por el over de puntos")
            print(overunder)
        else:
            print("Apuesta por el under de puntos")
            print(overunder)

        print("Tu monto a apostar es de ")
        print(montoapuesta)
        print("El valor estimado a ganar si apuestas que ganan los " + equipov + "es de")
        totalcg = ((montoapuesta * cuotaganadorv) - montoapuesta)
        print(totalcg)
        print("El valor estimado a ganar si apuestas por el handicap de los " + equipov + "es de")
        totalchl = ((montoapuesta * cuotahandicapv) - montoapuesta)
        print(totalchl)


def datosUno():
    equipol = get_valid_input("Digita el nombre del equipo local: ")
    equipov = get_valid_input("Digita el nombre del equipo visitante: ")
    mlhome = int(input(f"Digita el porcentaje en Moneyline de los {equipol}: "))
    mlvisit = int(input(f"Digita el porcentaje en Moneyline de los {equipov}: "))
    homespread = int(input(f"Digita el porcentaje del handicap o spread de los {equipol}: "))
    visitpread = int(input(f"Digita el porcentaje del handicap o spread de los {equipov}: "))
    lastfivel = input(f"Digita el record de los {equipol} en los ultimos 5 partidos: ")
    lastfivev = input(f"Digita el record de los {equipov} en los ultimos 5 partidos:  ")
    handicapl = float(input(f"Digita el numero del handicap de los {equipol} en la casa de apuestas: "))
    handicapv = float(input(f"Digite el numero del handicap de los {equipov} en la casa de apuestas: "))
    cantidadpartidos = float(input(f"Cual es el numero de partidos que han jugado ambos equipos por igual: "))
    overunderl = float(input(f"Cuantos puntos ha marcado en lo que va del torneo los {equipol}: "))
    overunderv = float(input(f"Cuantos puntos ha marcado en lo que va del torneo los {equipov}: "))
    overunder = float(input(f"Cual es el over/under de puntos del partido? "))
    homesrecordl = float(input(f"Cuantos partidos han ganado en casa los {equipol}: "))
    visitrecordl = float(input(f"Cuantos partidos han ganado de visitante los {equipol}: "))
    homesrecordv = float(input(f"Cuantos partidos han ganado en casa los {equipov}: "))
    visitrecordv = float(input(f"Cuantos partidos han ganado de visitante los {equipov}: "))
    atslastseasonl = float(input(f"Porcentaje ATS de la temporada pasada de los {equipol}: "))
    atslastseasonv = float(input(f"Porcentaje ATS de la temporada pasada de los {equipov}: "))
    atsseasonl = float(input(f"Porcentaje ATS de la temporada actual de los {equipol}: "))
    atsseasonv = float(input(f"Porcentaje ATS de la temporada actual de los {equipov}: "))
    cuotaganadorl = float(input(f"Cual es la cuota en la casa de apuestas que ganaran los {equipol} "))
    cuotaganadorv = float(input(f"Cual es la cuota en la casa de apuestas que ganaran los {equipov} "))
    cuotahandicapl = float(input(f"Cual es la cuota en la casa de apuestas del handicap de {equipol} "))
    cuotahandicapv = float(input(f"Cual es la cuota en la casa de apuestas del handicap de {equipov} "))
    atsplayoffsl = 0
    atsplayoffsv = 0
    montoapuesta = float(input(f"Cuanto Dinero Apostaras? "))


    return ganador(equipol, equipov, mlhome, mlvisit, lastfivel, lastfivev, homespread, visitpread, handicapl, handicapv, cantidadpartidos,
                   overunder, overunderl
                   ,overunderv, homesrecordl, visitrecordl, homesrecordv, visitrecordv, atslastseasonl,
                   atslastseasonv,
                   atsseasonl, atsseasonv, atsplayoffsl, atsplayoffsv, cuotaganadorl, cuotaganadorv, cuotahandicapl, cuotahandicapv, montoapuesta)

def datosDos():
    equipol = get_valid_input("Digita el nombre del equipo local: ")
    equipov = get_valid_input("Digita el nombre del equipo visitante: ")
    mlhome = int(input(f"Digita el porcentaje de Moneyline de los {equipol}: "))
    mlvisit = int(input(f"Digita el porcentaje de Moneyline de los {equipov}: "))
    homespread = int(input(f"Digita el porcentaje del handicap o spread de los {equipol}: "))
    visitpread = int(input(f"Digita el porcentaje del handicap o spread de los {equipov}: "))
    lastfivel = input(f"Digita el record de los {equipol} en los ultimos 5 partidos: ")
    lastfivev = input(f"Digita el record de los {equipov} en los ultimos 5 partidos: ")
    handicapl = float(input(f"Digita el valor del handicap de los {equipol} en la casa de apuestas: "))
    handicapv = float(input(f"Digite el valor del handicap de los {equipov} en la casa de apuestas: "))
    cantidadpartidos = float(input(f"Cual es el numero de partidos que han jugado ambos equipos por igual: "))
    overunderl = float(input(f"Cuantos puntos ha marcado en lo que va del torneo los {equipol}: "))
    overunderv = float(input(f"Cuantos puntos ha marcado en lo que va del torneo los {equipov}: "))
    overunder = float(input(f"Cual es el over/under de puntos del partido? "))
    homesrecordl = float(input(f"Cuantos partidos han ganado en casa los {equipol}: "))
    visitrecordl = float(input(f"Cuantos partidos han ganado de visitante los {equipol}: "))
    homesrecordv = float(input(f"Cuantos partidos han ganado en casa los {equipov}: "))
    visitrecordv = float(input(f"Cuantos partidos han ganado de visitante los {equipov}: "))
    atslastseasonl = float(input(f"Porcentaje ATS de la temporada pasada de los {equipol}: "))
    atslastseasonv = float(input(f"Porcentaje ATS de la temporada pasada de los {equipov}: "))
    atsplayoffsl = float(input(f"Porcentaje ATS de la temporada pasada en los playoffs de los {equipol}: "))
    atsplayoffsv = float(input(f"Porcentaje ATS de la temporada pasada en los playoffs de los {equipov}: "))
    atsseasonl = float(input(f"Porcentaje ATS de la temporada actual de los {equipol}: "))
    atsseasonv = float(input(f"Porcentaje ATS de la temporada actual de los {equipov}: "))
    cuotaganadorl = float(input(f"Cual es la cuota en la casa de apuestas que ganaran los {equipol} "))
    cuotaganadorv = float(input(f"Cual es la cuota en la casa de apuestas que ganaran los {equipov} "))
    cuotahandicapl = float(input(f"Cual es la cuota en la casa de apuestas del handicap de {equipol} "))
    cuotahandicapv = float(input(f"Cual es la cuota en la casa de apuestas del handicap de {equipov} "))
    montoapuesta = float(input(f"Cuanto Dinero Apostaras? "))

    return ganador(equipol, equipov, mlhome, mlvisit, lastfivel, lastfivev, homespread, visitpread, handicapl, handicapv, cantidadpartidos,
                   overunder, overunderl
                   ,overunderv, homesrecordl, visitrecordl, homesrecordv, visitrecordv, atslastseasonl,
                   atslastseasonv,
                   atsseasonl, atsseasonv, atsplayoffsl, atsplayoffsv, cuotaganadorl, cuotaganadorv, cuotahandicapl, cuotahandicapv, montoapuesta)

def Overunderprediction(equipol, equipov, golesl, golesv, numpartidos, totalgolesou):
    tg = (golesl + golesv) / numpartidos
    if tg > totalgolesou:
        print("============================================================================================================================================")
        print("Apuesta por el Over de puntos")
        print(totalgolesou)
    if tg <= totalgolesou:
        print("============================================================================================================================================")
        print("Apuesta por el Under de puntos")
        print(totalgolesou)
def get_valid_input(prompt, allowed_values=None, data_type=str):
    while True:
        user_input = input(prompt).strip()
        if not user_input:
            print("Error: El valor no puede estar vacío.")
            continue

        if allowed_values is not None and user_input not in allowed_values:
            print("Error: Valor inválido. Debes ingresar uno de los siguientes valores: ", allowed_values)
            continue

        try:
            return data_type(user_input)
        except ValueError:
            print("Error: Tipo de dato inválido. Debes ingresar un valor válido para el tipo de dato requerido.")
def datosTres():
    equipol = get_valid_input("Digita el nombre del equipo local: ")
    equipov = get_valid_input("Digita el nombre del equipo visitante: ")
    golesl = get_valid_input("Cuantos puntos ha marcado en lo que va del torneo o competicion " + equipol + ": ", data_type=float)
    golesv = get_valid_input("Cuantos puntos ha marcado en lo que va del torneo o competicion " + equipov + ": ", data_type=float)
    numpartidos = get_valid_input("Cuantos partidos han jugado por igual en el torneo ambos equipos " + ": ", data_type=float)
    totalgolesou = get_valid_input("Cual es el valor over/under de puntos en la casa de apuestas " + ": ", data_type=float)
    return Overunderprediction(equipol, equipov, golesl, golesv, numpartidos, totalgolesou)

def datosCuatro():
    cuota = float(input("Digita la cuota para convertirla en probabilidad de ganar la apuesta: "))
    probabilidad = (1/cuota)*100
    print("La probabilidad% de ganar la apuesta es de ")
    print(probabilidad)
def k():
    op = input("Tipos de apuestas: \n1. Ganador del partido & Over/Under de puntos & Handicap \n2. Predecir una eliminatoria de playoffs \n3. Solo predecir el over o el under de puntos en un partido \n4. Convertir cuota a probabilidad de ganar \n Cual deseas hacer? ")
    op = int(op)  # Convertir la entrada a un entero
    if op == 1:
        return datosUno()
    if op == 2:
        return datosDos()
    if op == 3:
        return datosTres()
    if op == 4:
        return datosCuatro()
    else:
        print("Opción inválida")

def main():
    d = "1"  # Inicializamos d como una cadena "1" en lugar de un entero 1
    while d == "1":  # Comparamos con la cadena "1" en lugar de con el entero 1
        print(" Bienvenido al predictor de NFL ")
        k()
        print("===================================================================================================================================================================")
        decision = input("¿Quieres predecir otro partido? Digita 1 para SÍ, digita 2 para NO: ")
        d = decision
main()



