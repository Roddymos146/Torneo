import time

class TorneoFutbol:
    def __init__(self):
        # Diccionario para almacenar los equipos y su información detallada
        # Clave: Nombre del equipo, Valor: Diccionario con jugadores y detalles
        self.equipos = {}
        
        # Conjunto para almacenar los nombres de todos los jugadores inscritos (evita duplicados globales)
        self.jugadores_totales = set()
        
        # Mapa (Diccionario) para relacionar jugador con su equipo respectivo
        self.jugador_a_equipo = {}

    def registrar_equipo(self, nombre_equipo):
        if nombre_equipo in self.equipos:
            print(f"El equipo '{nombre_equipo}' ya está registrado.")
        else:
            self.equipos[nombre_equipo] = {
                "jugadores": set(),
                "goles": 0
            }
            print(f"Equipo '{nombre_equipo}' registrado exitosamente.")

    def registrar_jugador(self, nombre_equipo, nombre_jugador):
        if nombre_equipo not in self.equipos:
            print(f"Error: El equipo '{nombre_equipo}' no existe.")
            return
        
        if nombre_jugador in self.jugadores_totales:
            print(f"Error: El jugador '{nombre_jugador}' ya está inscrito en otro equipo.")
            return

        # Añadir al conjunto del equipo y al conjunto global
        self.equipos[nombre_equipo]["jugadores"].add(nombre_jugador)
        self.jugadores_totales.add(nombre_jugador)
        
        # Mapear jugador con su equipo
        self.jugador_a_equipo[nombre_jugador] = nombre_equipo
        print(f"Jugador '{nombre_jugador}' agregado a '{nombre_equipo}'.")

    def mostrar_reporte(self):
        print("\n--- REPORTE GENERAL DEL TORNEO ---")
        if not self.equipos:
            print("No hay equipos registrados.")
            return

        for equipo, datos in self.equipos.items():
            print(f"\nEquipo: {equipo}")
            print(f"  - Total Goles: {datos['goles']}")
            print(f"  - Jugadores ({len(datos['jugadores'])}):")
            for jugador in datos['jugadores']:
                print(f"    * {jugador}")
        
        print(f"\nTotal de jugadores únicos en el torneo: {len(self.jugadores_totales)}")


# --- Bloque de ejecución y análisis de rendimiento ---
if __name__ == "__main__":
    inicio = time.time()

    torneo = TorneoFutbol()
    
    # 1. Registrar equipos
    torneo.registrar_equipo("Barcelona FC")
    torneo.registrar_equipo("Real Madrid")
    
    # 2. Registrar jugadores
    torneo.registrar_jugador("Barcelona FC", "Moscoso Roddy")
    torneo.registrar_jugador("Barcelona FC", "David Gómez")
    torneo.registrar_jugador("Barcelona FC", "Perez Jorge")
    torneo.registrar_jugador("Barcelona FC", "Snaider Castillo")
    torneo.registrar_jugador("Barcelona FC", "Corozo Juan")
    torneo.registrar_jugador("Barcelona FC", "Messi Leonel")
    torneo.registrar_jugador("Barcelona FC", "Lamine Yamal")
    torneo.registrar_jugador("Barcelona FC", "Leones Jorge")
    torneo.registrar_jugador("Barcelona FC", "Matinez Jefferson")
    torneo.registrar_jugador("Barcelona FC", "Moscoso Stalin")
    torneo.registrar_jugador("Barcelona FC", "Garcia Erick")
    torneo.registrar_jugador("Barcelona FC", "Sedamanos Franklin")
    torneo.registrar_jugador("Real Madrid", "Rosa Reyes")
    
    # 3. Mostrar reporte (Reportería)
    torneo.mostrar_reporte()

    fin = time.time()
    # print(f"\nTiempo de ejecución del script: {fin - inicio:.6f} segundos")j