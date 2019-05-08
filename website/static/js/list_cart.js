const totalCart = document.querySelector('.total-market')
const cartList = document.querySelector('.cart-list')

function printTotal(result){
    let total_cart = 0;
    let unity_cart = 0;
    let item_name = 'item';


    for(let i = 0; i <= result.length-1; i++) {
        total_cart += parseFloat(result[i].preco_item) * result[i].quantidade
        unity_cart += parseInt(result[i].quantidade)
    }

    if(total_cart > 0){
         result.lengt > 1 ? item_name = 'items' : 'item'

        return totalCart.innerHTML =
            `<p>
                Você já tem ${result.length} ${item_name} no total de ${unity_cart} unidades.<br>
                Total da transação: R$ ${total_cart.toFixed(2)}
            </p>`

    }else{
        return totalCart.innerHTML = `<span>Nenhum item</span>`
    }
}

const printToCart = (nome, preco, quantidade) => {
    if ((nome) && (preco) && (quantidade)) {
        cartList.innerHTML += `<tr>
                                <td>${nome}</td>
                                <td>R$ ${preco}</td>
                                <td style="width:50px;">x ${quantidade}</td>
                           </td> `
    }
    else{
        cartList.innerHTML += `<tr><td>Nenhum item</td></tr>`
    }
    if (cartList.innerHTML.includes("Nenhum item")){
        cartList.removeChild(cartList.firstChild)
    }
}
