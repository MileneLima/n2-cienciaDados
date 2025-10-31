import os
from flask import Flask, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename
import PyPDF2
from flask_cors import CORS

# === Configurações ===
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf'}

vaga = {
    "grau_escolaridade": "Graduação completa em Engenharia de Software, Ciência da Computação ou áreas correlatas",
    "conhecimentos_desejados": ["AWS", "Docker", "Kubernetes", "CI/CD", "Metodologias Ágeis"],
    "conhecimentos_obrigatorios": ["Python", "Django", "REST APIs", "Git", "PostgreSQL"],
    "tempo_experiencia": 2,
    "observacoes": "Desejável inglês técnico e disponibilidade para modelo híbrido em São Paulo"
}

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

perfis_armazenados = []


# === Funções auxiliares ===
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def extrair_texto_pdf(filepath):
    texto = ""
    with open(filepath, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            texto += page.extract_text() or ""
    return texto


def calcular_aderencia(texto):
    score = 0
    motivos = []
    total = 0

    # Verifica conhecimentos obrigatórios
    for item in vaga["conhecimentos_obrigatorios"]:
        total += 1
        if item.lower() in texto.lower():
            score += 1
            motivos.append(f"Possui conhecimento obrigatório: {item}")

    # Verifica conhecimentos desejados
    for item in vaga["conhecimentos_desejados"]:
        total += 0.5
        if item.lower() in texto.lower():
            score += 0.5
            motivos.append(f"Possui conhecimento desejado: {item}")

    # Verifica tempo de experiência
    if str(vaga["tempo_experiencia"]) in texto:
        score += 1
        total += 1
        motivos.append("Tempo de experiência compatível")

    aderencia = round((score / total) * 100, 2) if total > 0 else 0
    motivo = "; ".join(motivos) if motivos else "Pouca aderência identificada"
    return aderencia, motivo


# === Endpoint principal ===
@app.route('/upload', methods=['POST'])
def upload():
    if 'arquivos' not in request.files:
        return jsonify({'sucesso': False, 'erro': 'Nenhum arquivo enviado.'}), 400

    arquivos = request.files.getlist('arquivos')
    if not arquivos:
        return jsonify({'sucesso': False, 'erro': 'Nenhum arquivo válido recebido.'}), 400

    try:
        for arquivo in arquivos:
            if arquivo and allowed_file(arquivo.filename):
                filename = secure_filename(arquivo.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                arquivo.save(filepath)

                texto = extrair_texto_pdf(filepath)
                aderencia, motivo = calcular_aderencia(texto)
                nome = os.path.splitext(filename)[0]  # Nome do arquivo como nome do candidato
                perfil = {'nome': nome, 'aderencia': aderencia, 'motivo': motivo}
                perfis_armazenados.append(perfil)

        # Ordena os perfis e retorna top 5
        top5 = sorted(perfis_armazenados, key=lambda x: x['aderencia'], reverse=True)[:5]
        return jsonify({'sucesso': True, 'top5': top5})

    except Exception as e:
        return jsonify({'sucesso': False, 'erro': f'Erro ao processar PDFs: {str(e)}'}), 500


# === Servir frontend ===
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_frontend(path):
    if path != "" and os.path.exists(os.path.join('frontend', path)):
        return send_from_directory('frontend', path)
    else:
        return send_from_directory('frontend', 'index.html')


if __name__ == '__main__':
    app.run(debug=True)
