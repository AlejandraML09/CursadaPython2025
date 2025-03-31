# Ejercicio 10
# Hacemos una función dónde recibimos las kills, las asistencias y las muertes. Por cada kill que obtuvo lo múltiplicamos por sus 3 puntos.
# Además le agregamos la cantidad de asistencias porque valen 1. Si tuvo muertes, le restamos a esos puntos -1.
def points_gained(kills, deaths, assists):
    points = (kills * 3) + assists
    if deaths:
        points -= 1
    return points

# Función sólo para imprimir el jugador. Tiene un formato en específico para que se vea bien la tabla.
def print_player(player, kills, assists, deaths, mvp, points):
    print(f"{player:<10} {kills:<8} {assists:<12} {deaths:<8} {mvp:<6} {points:<8}")

# Función sólo para el separador que se utiliza en el header como en el footer.
def print_separator():
    print("-" * 60)

# Función para imprimir el header. Son los "títulos" de cada tabla.
def print_header(): 
    print(f"{'Jugador':<10} {'Kills':<8} {'Asistencias':<12} {'Muertes':<8} {'MVPs':<6} {'Puntos':<8}")
    print_separator()
        
# Dada una ronda y un estado previo de una partida, actualiza las estadísticas
# de cada jugador.        
def process_round(round, player_stats):
    # Es el contador que lo inicializamos en -9999 para saber quién tuvo más puntos en toda la ronda.
    # El contador se reiniciará cada vez que se vuelva a llamar la función en el for del programa principal
    # Ya que se pasará a la siguiente ronda.
    max_points = -9999
    player_mvp = ""
    # Nuestro diccionario dónde guardaremos el resultado de cada ronda.
    result_round = {}
    # Utilizamos un for en dónde le pasamos la key(player) y el value(kda) del diccionario round.
    # Le aplicamos .items() que lo que hace es convertir el diccionario en una lista de tuplas.
    for player, kda in round.items():
        # Dentro de la tupla tenemos: [string con el nombre del player][diccionario kda]
        # Por cada key del diccionario kda obtenemos su value (k(kills), d(deaths), a(assists)) de la ronda 
        # para ese player.
        k,d,a = (kda["kills"], kda["deaths"], kda["assists"])
    # Le pasamos las kills, deaths y assists a la función points_gained para que calcule los puntos.
        points = points_gained(k,d,a) 
    # A partir de los puntos obtenidos buscamos cuál fue el mvp y nos guardamos su nombre.    
        if (max_points < points):
            max_points = points 
            player_mvp = player
        # Actualizamos dentro de nuestro diccionario result_round en el player sus estadísticas usando
        # la función update_player_stats.
        result_round[player] = update_player_stats(player_stats[player],k,d,a,points)
    # Actualizamos aquél player que haya sido MVP en TODA la ronda. Lo hacemos por separado.
    result_round[player_mvp]['mvps'] += 1
    return result_round

# Función que utilizamos para actualizar las estadísticas de los jugadores
def update_player_stats(player_stats, k,d,a, points):
    # Recibimos las estadísticas del jugador en especifico y actualizamos sus asesinatos,
    # asistencias, muertes y puntos.
    player_stats['kills'] += k
    player_stats['assists'] += a
    player_stats['deaths'] += int(d)
    player_stats['points'] += points
    return player_stats

# Función para imprimir la tabla.
def print_table(result_round):
    print_header()
    # La función sorted nos organiza la tabla de manera descendiente a partir de un criterio.
    # Cómo items transforma el diccionario en una lista de tuplas, para poder 
    # utilizar el sorted, hacemos una función anónima lamba que va a tomar cada tupla
    # y lo va a ordenar con el criterio de points.
    sorted_table = (sorted(result_round.items(), key=lambda p:p[1]['points'], reverse=True))
    for player, stats in sorted_table:
        # Le pasamos a la función print_player las kills, assists, etc del jugador para imprimirlas.
        print_player(
            player, 
            stats['kills'], 
            stats['assists'], 
            stats['deaths'],
            stats['mvps'], 
            stats['points']
            )
    print_separator()
