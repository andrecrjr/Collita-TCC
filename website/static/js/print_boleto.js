const boletoPrint = document.querySelector(".print-boleto")


const convertValorBoleto = () =>{
    const valorBoleto = document.querySelector(".valor-boleto")
    const valorFloat = parseFloat(valorBoleto.textContent).toFixed(2)
    return valorBoleto.textContent = valorFloat
}
convertValorBoleto()


const status = {'print':false}

boletoPrint.addEventListener('click', function print(e){
    let div = document.querySelector('.cada-boleto')
    this.disabled = true
    setTimeout(()=>{ this.disabled = false; }, 5000);
    printElement(div)
})

const printElement = (div) =>{
    let printPage = window.open('', "Print Boleto", 'height=600, width=1000')

    printPage.document.write(`
    <title>Boleto MageHut Collita </title>
    <div>
    <table style="margin:0 auto;">
        <tr>
            <td>
                <img src="https://codigosdebarrasbrasil.com.br/wp-content/uploads/2016/10/1-codigo-de-barras.jpg" style="width:400px"/>
            </td>
        </tr>
        <tr>
            <td>Pagável em qualquer banco</td>
        </tr>
    </table>
        <table style="border:1px black solid; margin:0 auto; font-size:16px">
            <thead>
                <tr>
                    <td style="text-align:center;border-bottom:1px black solid">BOLETO MAGEHUT - COLLITA</td>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td style="border-bottom:1px black solid">${div.children[1].children[0].textContent}</td>
                </tr>
                <tr>
                    <td>${div.children[1].children[1].textContent}</td>
                </tr>
                <tr>
                    <td>${div.children[1].children[2].textContent}</td>
                </tr>
                    <td>${div.children[1].children[3].textContent}</td>
                </tr>
                </tr>
                    <td>${div.children[1].children[4].textContent}</td>
                </tr>
                </tr>
                    <td>${div.children[1].children[5].textContent}</td>
                </tr>
            </tbody>
        </table>
    </div>
`)
console.log(div.children[1].children[5].textContent)
    printPage.print()
    printPage.close()
}

