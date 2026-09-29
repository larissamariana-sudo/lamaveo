const SITE = "https://lamaveo.laragyncity.chatgpt.site";

let livros = [];
let categoriaAtual = "Todas";

const grade = document.querySelector("#livros");
const dialogo = document.querySelector("#detalhes");

function escapar(texto) {
  return String(texto ?? "").replace(/[&<>"']/g, caractere => ({
    "&": "&amp;",
    "<": "&lt;",
    ">": "&gt;",
    '"': "&quot;",
    "'": "&#39;"
  })[caractere]);
}

function linkCompra(livro) {
  return `${SITE}/comprar?obra=${encodeURIComponent(livro.id)}`;
}

function disponivel(livro) {
  return livro.available !== false && Number(livro.stock) > 0;
}

function mostrarLivros() {
  const busca = document.querySelector("#busca").value
    .trim()
    .toLocaleLowerCase("pt-BR");

  const encontrados = livros.filter(livro => {
    const correspondeCategoria =
      categoriaAtual === "Todas" || livro.category === categoriaAtual;

    const texto = `${livro.title} ${livro.synopsis ?? ""}`
      .toLocaleLowerCase("pt-BR");

    return correspondeCategoria && texto.includes(busca);
  });

  if (encontrados.length === 0) {
    grade.innerHTML = "<p>Nenhuma obra encontrada. Tente outro termo.</p>";
    return;
  }

  grade.innerHTML = encontrados.map(livro => `
    <article class="produto">
      <div class="capa">
        ${livro.cover
          ? `<img src="${escapar(livro.cover)}"
                  alt="Capa de ${escapar(livro.title)}"
                  loading="lazy">`
          : "<span>Capa em preparação</span>"}
      </div>

      <p class="categoria">${escapar(livro.category)}</p>
      <h3>${escapar(livro.title)}</h3>
      <p class="autor">${escapar(livro.author)}</p>

      <div class="rodape-produto">
        <strong>${escapar(livro.price)}</strong>

        <div class="acoes">
          <button type="button" data-id="${escapar(livro.id)}">
            Ver detalhes
          </button>

          ${disponivel(livro)
            ? `<a href="${linkCompra(livro)}">Comprar</a>`
            : "<span>Indisponível</span>"}
        </div>
      </div>
    </article>
  `).join("");
}

grade.addEventListener("click", evento => {
  const botao = evento.target.closest("button[data-id]");
  if (!botao) return;

  const livro = livros.find(item => item.id === botao.dataset.id);
  if (!livro) return;

  document.querySelector("#conteudo-detalhes").innerHTML = `
    <div class="detalhe">
      <div class="capa">
        ${livro.cover
          ? `<img src="${escapar(livro.cover)}"
                  alt="Capa de ${escapar(livro.title)}">`
          : "Capa em preparação"}
      </div>

      <div>
        <p class="categoria">${escapar(livro.category)}</p>
        <h2>${escapar(livro.title)}</h2>
        <p>Por ${escapar(livro.author)}</p>
        <p><strong>${escapar(livro.price)}</strong> ·
           ${escapar(livro.format)}</p>
        <p class="sinopse">${escapar(livro.synopsis || "Sinopse em preparação.")}</p>
        <p>Impressão sob demanda: até 15 dias após o pagamento.</p>

        ${disponivel(livro)
          ? `<a class="comprar-detalhe" href="${linkCompra(livro)}">
               Comprar este livro
             </a>`
          : "<p>Temporariamente indisponível.</p>"}
      </div>
    </div>
  `;

  dialogo.showModal();
});

document.querySelector("#fechar").addEventListener("click", () => {
  dialogo.close();
});

dialogo.addEventListener("click", evento => {
  if (evento.target === dialogo) dialogo.close();
});

document.querySelector("#busca").addEventListener("input", mostrarLivros);

document.querySelectorAll("[data-categoria]").forEach(botao => {
  botao.addEventListener("click", () => {
    categoriaAtual = botao.dataset.categoria;

    document.querySelectorAll("[data-categoria]").forEach(item => {
      item.classList.toggle("ativo", item === botao);
    });

    mostrarLivros();
  });
});

fetch("catalogo.json")
  .then(resposta => {
    if (!resposta.ok) throw new Error("Catálogo indisponível");
    return resposta.json();
  })
  .then(dados => {
    livros = dados;
    mostrarLivros();
  })
  .catch(() => {
    document.querySelector("#erro-catalogo").hidden = false;
  });
