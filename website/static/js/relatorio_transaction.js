let findMonthAndYear = /\d+/g;
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

const responseRelatorio = (data) =>{
    console.log(data)
    rootRelatorio.innerHTML = `<button onClick="()">Gerar relatorio</button>`
}

const mountQueryFilter = (month) =>{
    let query= ``
    const qtd_trans = document.querySelector(".qtd")
    const date = month.match(findMonthAndYear)
    query = query + `?mes=${date[1]}`
    query = query + `&ano=${date[0]}`
    //captura o valor de quantidade e coloca dentro da query
    parseInt(qtd_trans.value) > 0 ? query = query + `&qtd=${qtd_trans.value}` : ``
    console.log(query)
    return query
}

const requestTransactions = async (query) =>{
    try{
        const result = await fetch(`${link}filter${query}`)
        const response = await result.json()
        return response
    }catch (err){
        console.log(err)
    }
}

filterRelatorio()