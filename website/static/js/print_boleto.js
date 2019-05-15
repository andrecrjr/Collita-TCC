const boletoPrint = document.querySelector(".print-boleto")

boletoPrint.addEventListener('click', function print(){
    let div = document.querySelector('.cada-boleto')
    return printElement(div)
})

const printElement = (div) =>{
    let printPage = window.open('', 'PRINT', 'height=400, width=600')
    printPage.document.write(div.children[1].innerHTML);
    
/*
    printPage.document.write(`<tbody>
    <tr>
            <td>Código:</td>
            <td> ${div.children}</td>
    </tr>
    <tr>
            <td>Status do boleto:</td>
            <td>{{ boleto.status_boleto }}</td>
    </tr>
    <tr>
        <td>Data de expedição:</td>
        <td>{{ boleto.data_boleto_criado }}</td>
    </tr>
    <tr>
    </tr>
            <td>Data de vencimento:</td>
            <td>{{ boleto.expiration_boleto_date }}</td>
    </tr>
</tbody>`)
*/
    printPage.print()
    printPage.close()
    return true
}

