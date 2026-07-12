function reagir(musicaId, tipo) {

    fetch(`/repertorio/${tipo}/${musicaId}`, {

        method: "POST"

    })

    .then(resposta => resposta.json())

    .then(dados => {

        if (dados.status === 200) {

            const card =
                document.querySelector(`[data-id="${musicaId}"]`);

            const contador =
                card.querySelector(`.contador-${tipo}`);

            contador.textContent =
                parseInt(contador.textContent) + 1;

            const btnLike = card.querySelector(".btn-like");

            const btnDislike = card.querySelector(".btn-dislike");

            btnLike.disabled = true;

            btnDislike.disabled = true;
        }

    });

}