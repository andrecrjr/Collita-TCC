const totalCart = document.querySelector('.total-market')
const tabela = document.querySelector('table')

function printTotal(result){
    let total_cart = 0;
    let item_name = 'item';

    for(let i in result) {
        total_cart += parseFloat(result[i].preco_item)
    }
    
    if(total_cart > 0){
        if (result.length > 1) {
            item_name = 'itens'
        }
        return totalCart.innerHTML = `<p>
        Você já tem ${result.length} ${item_name} no carrinho.<br>
        Total da transação: R$ ${total_cart.toFixed(2)}</p>`
    }
}

const printToCart = (nome, preco) =>{
    
    const cartList = document.querySelector('.cart-list')
    cartList.innerHTML += `<tr>
                                <td>${nome}</td>
                                <td>${preco}</td>
                           </td> `/*
    let nomeCart = document.createElement("td");
    let precoCart = document.createElement("td");
    let nameItem = document.createTextNode(nome);
    let precoItem = document.createTextNode(preco);
    nomeCart.appendChild(nameItem);
    precoCart.appendChild(precoItem);
    cartList.appendChild(nomeCart);
    cartList.appendChild(precoCart);*/
}

