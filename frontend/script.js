const form = document.getElementById("form");
const lista = document.getElementById("lista");
const resultados = document.getElementById("resultados");

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const formData = new FormData();
  const arquivos = document.getElementById("arquivos").files;

  if (arquivos.length === 0) {
    alert("Envie pelo menos um arquivo PDF.");
    return;
  }

  for (let i = 0; i < arquivos.length; i++) {
    formData.append("arquivos", arquivos[i]);
  }

  lista.innerHTML = "<li>⏳ Processando currículos...</li>";

  try {
    const resp = await fetch("/upload", { method: "POST", body: formData });
    const data = await resp.json();

    if (data.sucesso) {
      lista.innerHTML = "";
      data.top5.forEach((p, i) => {
        const li = document.createElement("li");
        li.innerHTML = `<strong>${i + 1}. ${p.nome}</strong> — <b>${p.aderencia}%</b><br><small>${p.motivo}</small>`;
        lista.appendChild(li);
      });
    } else {
      lista.innerHTML = `<li>❌ Erro: ${data.erro}</li>`;
    }
  } catch (err) {
    lista.innerHTML = `<li>⚠️ Falha ao conectar ao servidor: ${err.message}</li>`;
  }
});
