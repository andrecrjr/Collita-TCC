listCart()
cartList = document.querySelector('.list-cart')

function listCart() {
    const link = 'http://localhost:8000/marketplace/';
    fetch(`${link}list_item/`)
        .then(response => response.json())
            .then(
            result =>{
                if(!result){
                    countCart(0)
                }else{
                    countCart(result.length);
                }  
                printTotal(result);
            }
        );
}

function countCart(contando){
    let contagem = `${contando}`
    document.querySelector('.items-menu-count').innerHTML = contagem
}

