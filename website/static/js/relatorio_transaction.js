let rootRelatorio = document.querySelector('section.root-relatorio')

const filterRelatorio = ()=>{
    const botao = document.querySelector('.get-relatorio')
    
    botao.addEventListener("click", function(){
        const month = document.querySelector("input[type=month]")
        if(month.value.length > 0){
            const dados = requestTransactions(mountQueryFilter(month.value))
            dados.then((response)=>{
                return responseRelatorio(response)
            })
        }else{
            rootRelatorio.innerHTML = `<div class="warning">
                                            <span class="omg-warning"></span>
                                                <div class="warning-inside">Está faltando mês ou ano</div>
                                        </div>`
        }
    })
}

const responseRelatorio = (response) =>{
    const { data } = response
    if(data.length > 0){
        rootRelatorio.innerHTML = `<button class="generate_relatorio">Gerar relatorio</button>`
        renderRelatorio(data)
    }else{
        rootRelatorio.innerHTML = `<div class="warning">
                                            <span class="omg-warning"></span>
                                                <div class="warning-inside">Não há relatórios no mês e ano selecionados</div>
                                        </div>`
    }
}


const renderRelatorio = (data) =>{
    rootRelatorio.innerHTML +=  `<table class="relatorio" style="width:100%"><tbody class="tabela"></tbody></table>`
    let tabela = document.querySelector("tbody.tabela")
    data.map((response)=>{
        estrutura = `<tr>
                        <td>${response.id}</td>
                        <td>${response.codigo_boleto}</td>
                        <td>${response.nome_completo}</td>
                        <td>${response.data_boleto_criado}</td>
                        <td>${parseFloat(response.valor_boleto).toFixed(2)}</td>
                    </tr>`
        tabela.innerHTML += estrutura
    })
    mountPrintRelatorio(data)
}


const mountPrintRelatorio = (data) =>{
    const botaoRelatorio = document.querySelector('.generate_relatorio')
    botaoRelatorio.addEventListener("click", ()=>{
        return tabelaRelatorio(data)
    })
}

function tabelaRelatorio(data){
    const month = document.querySelector("input[type=month]")
    let relatorioPage = window.open('', "Relatório Collita", 'height=750, width=1000')
        tabela = `
        <h1>MageHut - Relatório de Transações ${month.value}</h1>
        <table style="margin: 0 auto; border:1px black solid; width:100%">
                    <tbody>
                            ${data.map((response)=>{
                                return (`
                                    <tr>
                                        <td>${response.id}</td>
                                        <td>${response.codigo_boleto}</td>
                                        <td>${response.nome_completo}</td>
                                        <td>${response.data_boleto_criado}</td>
                                        <td>${parseFloat(response.valor_boleto).toFixed(2)}</td>
                                    </tr>
                                    `     
                                    )
                            })}
                    </tbody>
                </table>`
        tabela = tabela.replace(/,/g, "")
        relatorioPage.document.write(tabela)
        relatorioPage.print()
        relatorioPage.close()
}

const mountQueryFilter = (data) =>{
    let query= ``
    const qtd_trans = document.querySelector(".qtd")
    const date = data.split('-')
    query = query + `?mes=${date[1]}`
    query = query + `&ano=${date[0]}`
    //captura o valor de quantidade e coloca dentro da query
    parseInt(qtd_trans.value) > 0 ? query = query + `&qtd=${qtd_trans.value}` : ``
    return query
}

const requestTransactions = async (query) =>{
    try{
        const result = await fetch(`${link}filter${query}`)
        const response = await result.json()
        return response
    }catch (err){
        console.log(err)
        rootRelatorio.innerHTML = `<div class="warning">
                                            <span class="omg-warning"></span>
                                                <div class="warning-inside">Servidor fora do ar tente novamente mais tarde</div>
                                        </div>`
    }
}

filterRelatorio()
