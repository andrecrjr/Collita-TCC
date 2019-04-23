
async function printMainCart(){
    const link = 'http://127.0.0.1:8000/marketplace/';
    let elementTable = document.querySelector('.cart-market')
    let elementCart = document.querySelector('.carrinho-main')
    const element = document.querySelector('.none-cart')
    try {
        result = await fetch(`${link}list_item/`)
        data = await result.json();
        var i = 0;
        if(data > []){
            data.map((response) => {
                i = i + 1
                return elementCart.innerHTML += `
                        <tr>
                            <td>${i} </td>
                            <td>${response.nome_item}</td>
                            <td>${response.preco_item}</td>
                            <td>${response.quantidade}</td>
                        </tr>
                    
                    `
            })
        }else{
            elementCart.remove()
            elementTable.remove()
            return element.textContent += `           
            Nenhum item adicionado ao carrinho`
        }
    }catch(err){
        elementCart.remove()
        elementTable.remove()
        return element.textContent += `
            Sem conexão com o servidor tente mais tarde`
    }
}
printMainCart()