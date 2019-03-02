takeInfo()

function takeInfo(){
    fetch(`list_item/`)
        .then(response => response.json())
            .then(
            result => {
                //updateCart(result)
               printTotal(result)
            }
        );

}

function printTotal(result){
    let total_cart = 0;
            for(let i in result) {
               total_cart += parseFloat(result[i].preco_item)
            }
            if(!result){
                total_cart = 0
            }
    cart = document.querySelector('.total-market')
    if (total_cart >  0) {
        cart.innerHTML = `<p>Total no carrinho: R$ ${total_cart}</p>`
    }

}

