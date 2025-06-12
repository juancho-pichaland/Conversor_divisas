# Tasa de cambio respecto a 1 unidad de moneda base
tasas = {
    "USD": 1.0,         # Dólar americano
    "EUR": 0.92,        # Euro
    "COP": 4170.61,      # Peso colombiano
    "MXN": 18.0,        # Peso mexicano
    "JPY": 157.0,        # Yen japonés
    "GBP": 0.82,         # Libra esterlina
    "CNY": 6.45,         # Yuan chino
    "INR": 82.0,         # Rupia india
    "BRL": 5.25,         # Real brasileño
    "ARS": 350.0,        # Peso argentino
    "CLP": 800.0,        # Peso chileno
    "AUD": 1.5,         # Dólar australiano
    "CAD": 1.35,         # Dólar canadiense
    "CHF": 0.95,         # Franco suizo
    "ZAR": 18.0,         # Rand sudafricano
    "RUB": 75.0,         # Rublo ruso
    "KRW": 1300.0,       # Won surcoreano
    "TRY": 18.0,         # Lira turca
    "AED": 3.67,         # Dirham de los Emiratos Árabes Unidos
    "SAR": 3.75,         # Riyal saudí
    "NOK": 9.0,          # Corona noruega
    "SEK": 10.0,         # Corona sueca
    "DKK": 6.5,         # Corona danesa
    "PLN": 4.0,          # Zloty polaco
    "HUF": 350.0,        # Forinto húngaro
    "CZK": 22.0,         # Corona checa
    "THB": 35.0,         # Baht tailandés
    "IDR": 15000.0,      # Rupia indonesia
    "MYR": 4.5,          # Ringgit malayo
    "PHP": 55.0,         # Peso filipino
    "VND": 23000.0,      # Dong vietnamita
    "SGD": 1.35,         # Dólar de Singapur
    "NZD": 1.6,          # Dólar neozelandés
    "HKD": 7.85,         # Dólar de Hong Kong
    "TWD": 30.0,         # Nuevo dólar taiwanés
    "MXV": 18.0,         # Unidad de inversión mexicana (UDI)
    "XAU": 0.0005,       # Onza de oro (aproximadamente)
    "XAG": 0.01,         # Onza de plata (aproximadamente)
    "XBT": 0.00005,      # Bitcoin (aproximadamente)
    "XRP": 0.5,          # Ripple (aproximadamente)
    "LTC": 0.01,         # Litecoin (aproximadamente)
    "ADA": 1.0,          # Cardano (aproximadamente)
    "DOT": 0.5,          # Polkadot (aproximadamente)
    "SOL": 0.2,          # Solana (aproximadamente)
    "DOGE": 5.0,         # Dogecoin (aproximadamente)
    "BNB": 0.1          # Binance Coin (aproximadamente)
}

def convertir_moneda(cantidad, moneda_origen, moneda_destino):
    """
    Convierte una cantidad de dinero de una moneda a otra.

    :param cantidad: Cantidad de dinero a convertir.
    :param moneda_origen: Moneda de origen (clave en el diccionario tasas).
    :param moneda_destino: Moneda de destino (clave en el diccionario tasas).
    :return: Cantidad convertida a la moneda de destino.
    """
    if moneda_origen not in tasas or moneda_destino not in tasas:
        raise ValueError("Moneda no soportada.⚠️")

    # Convertir a USD y luego a la moneda destino
    cantidad_en_usd = cantidad / tasas[moneda_origen]
    cantidad_convertida = cantidad_en_usd * tasas[moneda_destino]

    return cantidad_convertida
def main():
    while True:
        print("Bienvenido al conversor de monedas. 🌍💱")
        print("Monedas disponibles:", ", ".join(tasas.keys()))
        print("Escriba 'salir' para terminar.")

        opcion = input("¿Desea realizar una conversión? (s/n): ").strip().lower()
        if opcion == 'n':
            print("Gracias por usar el conversor de monedas. ¡Hasta luego! 👋")
            break
        elif opcion != 's':
            print("Opción no válida. Por favor, intente de nuevo.")
            continue

        break
    try:
        cantidad = float(input("Ingrese la cantidad a convertir: "))
        moneda_origen = input("Ingrese la moneda de origen (ej. USD, EUR, COP): ").upper()
        moneda_destino = input("Ingrese la moneda de destino (ej. USD, EUR, COP): ").upper()

        resultado = convertir_moneda(cantidad, moneda_origen, moneda_destino)
        print(f"{cantidad} {moneda_origen} son {resultado:.2f} {moneda_destino}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
if __name__ == "__main__":
    main()