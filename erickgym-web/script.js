async function getAlunos() {
    const resposta = await fetch('https://erickgym-0xkh.onrender.com/alunos')

    const data = resposta.json()

    return data

}

async function principal() {
    const alunos = getAlunos()

    console.log(alunos)
}

principal()