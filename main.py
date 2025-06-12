from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

MONEDAS_COMUNES = ["USD", "EUR", "COP", "MXN", "GBP", "JPY", "AUD", "CAD", "CNY",
                   "INR", "BRL", "RUB", "ZAR", "KRW", "NZD", "CHF", "HKD", "SGD",
                   "SEK", "NOK", "TRY", "PLN", "TWD", "THB", "IDR", "MYR", "PHP",
                   "VND", "AED", "SAR", "QAR", "KWD", "BHD", "OMR", "JOD", "DZD",
                   "MAD", "EGP", "TND", "LYD", "IQD", "IRR", "AFN", "PKR", "BDT",
                   "LKR", "MMK", "KHR", "LAK", "MNT", "KGS", "TJS", "UZS", "GEL",
                   "AMD", "AZN", "BYN", "RSD", "MKD", "BAM", "HRK", "CZK", "HUF",
                   "RON", "BGN", "ISK", "FJD", "PGK", "WST", "TVD", "VUV", "XPF",
                   "XAF","XOF", "XPF", "XCD", "USD", "EUR", "GBP", "JPY", "CNY",
                   "INR","AUD", "CAD", "CHF", "NZD", "ZAR", "KRW", "SGD", "HKD",
                   "SEK"
]


def obtener_tasa(origen, destino):
    url = f"https://api.exchangerate.host/latest?base={origen}&symbols={destino}"
    respuesta = requests.get(url)
    if respuesta.status_code != 200:
        return None
    datos = respuesta.json()
    if "rates" not in datos or destino not in datos["rates"]:
        return None
    return datos["rates"].get(destino)

@app.route('/')
def index():
    return render_template('index.html', monedas=MONEDAS_COMUNES)

@app.route('/convertir', methods=['POST'])
def convertir():
    try:
        cantidad = float(request.form['cantidad'])
        if cantidad <= 0:
            return jsonify({"error": "La cantidad debe ser un número positivo"}), 400
    except ValueError:
        return jsonify({"error": "La cantidad debe ser un número válido"}), 400

    origen = request.form['origen']
    destino = request.form['destino']

    if destino == "TODAS":
        url = f"https://api.exchangerate.host/latest?base={origen}"
        respuesta = requests.get(url)
        if respuesta.status_code != 200:
            return jsonify({"error": "No se pudo obtener las tasas de cambio"}), 500
        tasas = respuesta.json()["rates"]
        if not tasas:
            return jsonify({"error": "No se encontraron tasas de cambio"}), 404
        resultados = {moneda: cantidad * tasa for moneda, tasa in tasas.items()}
        return jsonify(resultados)
    else:
        tasa = obtener_tasa(origen, destino)
        if tasa is None:
            return jsonify({"error": "No se pudo obtener la tasa de cambio"}), 500
        resultado = cantidad * tasa
        return jsonify({"resultado": f"{cantidad} {origen} son {resultado:.2f} {destino}"})

if __name__ == '__main__':
    app.run(debug=True)