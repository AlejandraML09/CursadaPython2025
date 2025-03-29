# Hacemos una función dónde recibimos las kills, las asistencias y las muertes. Por cada kill que obtuvo lo múltiplicamos por sus 3 puntos.
# Además le agregamos la cantidad de asistencias porque valen 1. Si tuvo muertes, le restamos a esos puntos -1.
def points_gained(kills, deaths, assists):
    points = (kills * 3) + assists
    if deaths:
        points -= 1
    return points

def print_player(player, kills, assists, deaths, mvp, points):
    print(f"{player:<10} {kills:<8} {assists:<12} {deaths:<8} {mvp:<6} {points:<8}")

def print_separator():
    print("-" * 60)

def print_header():
    print(f"{'Jugador':<10} {'Kills':<8} {'Asistencias':<12} {'Muertes':<8} {'MVPs':<6} {'Puntos':<8}")
    print_separator()

def print_round(round):
    for player, stats in round.items():
        print(player, stats["kills"], stats["assists"], 
            stats["deaths"], stats["mvps"], stats["points"])
        
# Dada una ronda y un estado previo de una partida, actualiza las estadísticas
# de cada jugador.        
def process_round(round, player_stats):
    max_points = -9999
    player_mvp = ""
    result_round = {}
    for player, kda in round.items():
        k,d,a = (kda["kills"], kda["deaths"], kda["assists"])
        points = points_gained(k,d,a) 
        if (max_points < points):
            max_points = points 
            player_mvp = player
        result_round[player] = update_player_stats(player_stats[player],k,d,a,points)
    result_round[player_mvp]['mvps'] += 1
    return result_round

# Función que utilizamos para actualizar las estadísticas de los jugadores
def update_player_stats(player_stats, k,d,a, points):
    player_stats['kills'] += k
    player_stats['assists'] += a
    player_stats['deaths'] += int(d)
    player_stats['points'] += points
    return player_stats

def print_table(result_round):
    print_header()
    sorted_table = (sorted(result_round.items(), key=lambda p:p[1]['points'], reverse=True))
    for player, stats in sorted_table:
        print_player(
            player, 
            stats['kills'], 
            stats['assists'], 
            stats['deaths'],
            stats['mvps'], 
            stats['points']
            )
    print_separator()
