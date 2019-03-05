listCart()
cartList = document.querySelector('.cart_list')

function listCart() {
    const link = 'http://127.0.0.1:8000/marketplace/';
    fetch(`${link}list_item/`)
        .then(response => response.json())
            .then(
            result =>{
                if(result === null){
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
