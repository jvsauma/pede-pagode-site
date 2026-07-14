document.addEventListener("DOMContentLoaded", function () {

    const form = document.getElementById("form-pedido");
    const sucesso = document.getElementById("pedido-sucesso");
    const sucessoNome = document.getElementById("pedido-sucesso-nome");
    const sucessoMusica = document.getElementById("pedido-sucesso-musica");
    const btnOutroPedido = document.getElementById("btn-outro-pedido");
    const listaItens = document.getElementById("pedidos-itens");
    const contador = document.getElementById("pedidos-contador");

    if (form) {
        form.addEventListener("submit", function (evento) {
            evento.preventDefault();

            const dados = new FormData(form);

            fetch(form.action, {
                method: "POST",
                body: dados,
                headers: { "X-Requested-With": "fetch" }
            })
                .then(function (resposta) {
                    if (!resposta.ok) {
                        throw new Error("Falha ao enviar o pedido");
                    }

                    sucessoNome.textContent = dados.get("nome_cliente");
                    sucessoMusica.textContent = dados.get("musica");

                    form.hidden = true;
                    sucesso.hidden = false;
                })
                .catch(function () {
                    form.submit();
                });
        });
    }

    if (btnOutroPedido) {
        btnOutroPedido.addEventListener("click", function () {
            window.location.reload();
        });
    }

    function atualizarContador() {
        if (!contador || !listaItens) {
            return;
        }

        const total = listaItens.querySelectorAll(".pedido-item").length;
        contador.textContent = total + (total === 1 ? " pedido recebido" : " pedidos recebidos");
    }

    if (listaItens) {
        listaItens.addEventListener("click", function (evento) {
            const botao = evento.target.closest("button[data-acao]");

            if (!botao) {
                return;
            }

            const item = botao.closest(".pedido-item");
            const id = item.dataset.id;
            const acoes = item.querySelector(".pedido-item__acoes");

            if (botao.dataset.acao === "aceitar") {
                fetch(`/pedido/${id}/aprovar`, { method: "POST" })
                    .then(function (resposta) {
                        if (!resposta.ok) {
                            throw new Error("Falha ao aceitar o pedido");
                        }

                        item.classList.remove("pedido-item--pendente");
                        item.classList.add("pedido-item--aceito");

                        item.querySelector(".pedido-item__status").textContent = "Aceito";

                        item.querySelector(".pedido-item__icone").innerHTML =
                            '<svg viewBox="0 0 24 24"><path d="M20 6 9 17l-5-5"></path></svg>';

                        acoes.innerHTML =
                            '<span class="pedido-item__resultado pedido-item__resultado--aceito">' +
                            '<svg viewBox="0 0 24 24"><path d="M20 6 9 17l-5-5"></path></svg>Na fila!</span>';
                    });
                return;
            }

            if (botao.dataset.acao === "rejeitar") {
                item.classList.remove("pedido-item--pendente");
                item.classList.add("pedido-item--rejeitado");

                item.querySelector(".pedido-item__status").textContent = "Rejeitado";

                item.querySelector(".pedido-item__icone").innerHTML =
                    '<svg viewBox="0 0 24 24"><path d="M18 6 6 18"></path><path d="M6 6l12 12"></path></svg>';

                acoes.innerHTML =
                    '<span class="pedido-item__resultado pedido-item__resultado--rejeitado">' +
                    '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"></circle><path d="M12 6v6l4 2"></path></svg>Removendo...</span>';

                setTimeout(function () {
                    fetch(`/pedido/${id}/delete`, { method: "POST" })
                        .then(function () {
                            item.remove();
                            atualizarContador();
                        });
                }, 5000);
            }
        });
    }
});