const totalCart = document.querySelector('.total-market')
const cartList = document.querySelector('.cart-list')

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
        if (cartList.childNodes[1].innerText == "Nenhum item"){
            cartList.removeChild(cartList.childNodes[1])
        }
        return totalCart.innerHTML = `<p>
        Você já tem ${result.length} ${item_name} no carrinho.<br>
        Total da transação: R$ ${total_cart.toFixed(2)}</p>`
    }
}

const printToCart = (nome, preco, quantidade) => {
    if ((nome) && (preco) && (quantidade)) {
        cartList.innerHTML += `<tr>
                                <td>${nome}</td>
                                <td>${preco}</td>
                                <td style="width:50px;">x ${quantidade}</td>
                           </td> `
        }
    if (cartList.childNodes[1].innerText == "Nenhum item"){
        cartList.removeChild(cartList.childNodes[1])
    }
}

