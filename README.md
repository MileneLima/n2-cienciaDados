# 🧠 Analisador de Aderência de Currículos

Este projeto analisa currículos em formato **PDF** e calcula o **percentual de aderência de cada candidato** a uma vaga descrita.  
O sistema permite enviar **vários currículos de uma vez** e retorna o **Top 5 candidatos mais aderentes**, com explicações sobre o motivo da pontuação.

![Tela do sistema](/foto.png)

---

## 🚀 Tecnologias utilizadas

- **Python 3**  
- **Flask** – Servidor web  
- **Flask-CORS** – Comunicação com o frontend  
- **PyPDF2** – Leitura e extração de texto dos PDFs  
- **HTML / CSS / JavaScript** – Interface simples e responsiva no navegador  

---

## 🗂 Estrutura do projeto

```
projeto-aderencia/
│
├── backend.py              # Servidor Flask
├── /uploads                # PDFs enviados são salvos aqui
└── /frontend
    ├── index.html          # Interface do usuário
    ├── style.css           # Estilos
    └── script.js           # Lógica de envio e exibição dos resultados
```

---

## ⚙️ Como rodar o projeto localmente

### 1️⃣ Clonar ou extrair o projeto

Se baixou o `.zip`, extraia em uma pasta local, por exemplo:
```
C:\projetos\projeto-aderencia
```

ou clone do GitHub:
```bash
git clone https://github.com/seuusuario/projeto-aderencia.git
cd projeto-aderencia
```

---

### 2️⃣ Criar um ambiente virtual

No terminal (dentro da pasta do projeto):

```bash
python -m venv .venv
```

Ative o ambiente:

- **Windows**
  ```bash
  .venv\Scripts\activate
  ```
- **macOS / Linux**
  ```bash
  source .venv/bin/activate
  ```

---

### 3️⃣ Instalar as dependências

```bash
pip install flask flask-cors PyPDF2
```

---

### 4️⃣ Rodar o servidor

```bash
python backend.py
```

Se tudo estiver certo, você verá algo como:

```
 * Running on http://127.0.0.1:5000
```

---

### 5️⃣ Acessar no navegador

Abra o navegador e vá para:

👉 [http://localhost:5000](http://localhost:5000)

Você verá a página do analisador.

---

## 💼 Como usar

1. Clique em **“Selecionar arquivos”** e envie até **5 currículos PDF**.  
2. O sistema extrai automaticamente o texto dos currículos.  
3. Ele calcula o **percentual de aderência** com base nos requisitos da vaga definidos no backend.  
4. O resultado mostra o **Top 5 candidatos** com:
   - Nome detectado (ou nome do arquivo)  
   - Percentual de aderência  
   - Motivos da pontuação  

---

## 🧩 Exemplo de saída

```
1. Maria da Silva
Aderência: 92.5%
Motivo: Possui conhecimento obrigatório: Python; Tempo de experiência compatível

2. João Lima
Aderência: 81.0%
Motivo: Possui conhecimento obrigatório: Git; Possui conhecimento desejado: Docker
```

---

## 🧰 Personalização

No arquivo **`backend.py`**, edite o dicionário `vaga` para ajustar os requisitos da vaga:

```python
vaga = {
    "grau_escolaridade": "Graduação completa em Ciência da Computação",
    "conhecimentos_desejados": ["Scrum", "Docker", "Kubernetes"],
    "conhecimentos_obrigatorios": ["Python", "Git", "SQL"],
    "tempo_experiencia": 2,
    "observacoes": "Inglês intermediário"
}
```

---

## 🏁 Pronto!

Agora é só enviar currículos e ver os candidatos mais aderentes à vaga 🎯
