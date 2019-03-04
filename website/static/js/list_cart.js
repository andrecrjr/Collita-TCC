totalCart = document.querySelector('.total-market')
cartList = document.querySelector('.list-cart')

function printTotal(result){
    let total_cart = 0;
            for(let i in result) {
               total_cart += parseFloat(result[i].preco_item)
            }
            if(!result){
                total_cart = 0
            }

    return totalCart.innerHTML = `<p>Total no carrinho: R$ ${total_cart.toFixed(2)}</p>`
    
}

const printToCart = (nome, preco) =>{
    const itemCart = document.createElement("li");
    const nameItem = document.createTextNode(nome)
    itemCart.appendChild(nameItem)
    cartList.appendChild(itemCart)
}


