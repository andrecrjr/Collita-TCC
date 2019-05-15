const boletoPrint = document.querySelector(".print-boleto")

boletoPrint.addEventListener('click', function print(){
    let div = document.querySelector('.cada-boleto')
    return printElement(this,div)
})

const printElement = (elem, div) =>{
    elem.disabled = true
    let printPage = window.open('', 'PRINT', 'height=400, width=600')
    //printPage.document.write(div.children[1].children[1].textContent);
    //printPage.document.write(div.children[1].children[2].textContent);
    
    printPage.document.write(`
    <table style="border:1px black solid">
        <tbody>
            <tr>
                    <td>${div.children[1].children[0].textContent}</td>
            </tr>
            <tr>
                   <td>${div.children[1].children[1].textContent}</td>
            </tr>
            <tr>
                <td>${div.children[1].children[2].textContent}</td>
            </tr>
            <tr>
            </tr>
                    <td>${div.children[1].children[3].textContent}</td>
            </tr>
        </tbody>
    </table>
`)
    printPage.print()
    printPage.close()
    
    return true
}

