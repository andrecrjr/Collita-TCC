const boletoPrint = document.querySelector(".print-boleto")


const convertValorBoleto = () =>{
    const valorBoleto = document.querySelector(".valor-boleto")
    const valorFloat = parseFloat(valorBoleto.textContent).toFixed(2)
    return valorBoleto.textContent = valorFloat
}
convertValorBoleto()


boletoPrint.addEventListener('click', function print(e){
    let div = document.querySelector('.cada-boleto')
    this.disabled = true
    setTimeout(()=>{ this.disabled = false; }, 5000);
    printElement(div)
})

const printElement = (div) =>{
    let printPage = window.open('', "Print Boleto", 'height=750, width=1000')

    printPage.document.write(`
    <title>Boleto MageHut Collita </title>
    <table style="margin:0 auto; margin-top:15px;">
        <tr>
            <td>BOLETO MAGEHUT - COLLITA</td>
            <td style="border-left:1px; font-size:25px; text-indent:3px; text-align:center">${div.children[1].children[1].children[1].textContent}</td>
        </tr>
        <tr>
            <td style="padding-left:5px;">Pagável em qualquer banco até o vencimento.</td><td><img src=""/></td>
        </tr>
    </table>
        <table style="border:1px black solid; margin:0 auto; font-size:16px; margin-top:20px;">
        <tr>
            <td>
                <table>
                <tr>
                    <td style="border-right:1px black solid;">Beneficiário:</td>
                    <td style="text-align:center">${div.children[1].children[6].value}</td>   
                </tr>
                <tr>
                    <td style="border-right:1px black solid;">E-mail do beneficiário:</td>
                    <td style="text-align:center">${div.children[1].children[7].value}</td>   
                </tr>
                </table>
            </td>
            <td>
                <table  style="text-align:center; border-left:1px black solid">
                    <tr>
                        <td>${div.children[1].children[5].children[0].textContent}</td>
                        <td style="border-left:1px black solid;">${div.children[1].children[5].children[1].textContent}</td>
                    </tr>
                    <tr>
                        <td >${div.children[1].children[1].children[0].textContent}</td>
                        <td style="border-left:1px black solid; padding-left:5px; padding-right:5px;">${div.children[1].children[1].children[1].textContent}</td>
                    </tr>
                    <tr>
                        <td>${div.children[1].children[0].children[0].textContent}</td>
                        <td style="border-left:1px black solid;">${div.children[1].children[0].children[1].textContent}</td>
                    </tr>
                    <tr>
                        <td>${div.children[1].children[2].children[0].textContent}</td>
                        <td style="border-left:1px black solid;">${div.children[1].children[2].children[1].textContent}</td>
                    </tr>
                    <tr>
                        <td>${div.children[1].children[4].children[0].textContent}</td>
                        <td style="border-left:1px black solid;">${div.children[1].children[4].children[1].textContent}</td>
                    </tr>
                    </table>
            </td>
        </tr>
        </table>
        <table style="margin: 0 auto;">
            <tbody>
            <tr>
                <td>
                    <img src="https://codigosdebarrasbrasil.com.br/wp-content/uploads/2016/10/1-codigo-de-barras.jpg" style="width:400px" heigth="180px"/>
                </td>
            </tr>
            </tbody>
        </table>
`)

    printPage.print()
    printPage.close()
}

