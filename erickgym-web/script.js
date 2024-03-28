const lista = document.getElementById('alunos')

function criarAluno(aluno) {
    const li = document.createElement('li')
    li.textContent = aluno
    lista.appendChild(li)
}

async function postAluno(e) {
    e.preventDefault()

    const cx_nome = document.getElementById('nome')

    const cx_idade = document.getElementById('idade')

    const nome = cx_nome.value
    const idade = Number(cx_idade.value)

    if (nome === "") {
        alert("Preecha todos os campos!")
    }

    const data = {nome, idade}

    const response = await fetch('https://erickgym-0xkh.onrender.com/alunos', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })

    if (response.status === 201) {
        alert('Criado com sucesso!')
        cx_nome.value = ""
        cx_idade.value = ""
        const aluno = await response.json()
        criarAluno(aluno.nome)
    } else {
        alert("Deu ruim")
    }
}

async function getAlunos() {
    const resposta = await fetch('https://erickgym-0xkh.onrender.com/alunos')

    const data = resposta.json()

    return data

}

async function principal() {
    const alunos = await getAlunos()

    alunos.map((aluno) => criarAluno(aluno.nome))
}

principal()

document.getElementById('form').addEventListener('submit', postAluno)