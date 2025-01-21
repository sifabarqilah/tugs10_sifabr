from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    probability = None
    formula = None
    n = k = p = None
    if request.method == 'POST':
        try:
            # Ambil data dari form input
            n = int(request.form['n'])  # Jumlah mahasiswa yang mengikuti ujian
            k = int(request.form['k'])  # Jumlah mahasiswa yang lulus ujian
            p = float(request.form['p'])  # Probabilitas kelulusan setiap mahasiswa

            # Debugging: Print data yang diterima server
            print(f"n: {n}, k: {k}, p: {p}")

            # Perhitungan distribusi binomial
            prob = (math.comb(n, k)) * (p ** k) * ((1 - p) ** (n - k))
            probability = round(prob, 6)  # Pembulatan hasil
            formula = f"P(X = {k}) = C({n}, {k}) * ({p})^{k} * (1 - {p})^{({n} - {k})}"

        except ValueError as e:
            # Menangani error jika input tidak valid
            print(f"Error: {e}")
            probability = "Input tidak valid, pastikan semua field terisi dengan benar."

    return render_template('index.html', probability=probability, formula=formula, n=n, k=k, p=p)

if __name__ == '__main__':
    app.run(debug=True)