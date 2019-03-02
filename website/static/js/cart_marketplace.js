listCart()

function listCart() {
    const link = 'http://localhost:8000/marketplace/';
    fetch(`${link}list_item/`)
        .then(response => response.json())
            .then(
            result =>{
                //updateCart(result)
                countCart(result.length)
                if(!result.length){
                    countCart(0)
                }
            }
        );
}

function countCart(contando){
    let contagem = `${contando}`
    document.querySelector('.items-menu-count').innerHTML = contagem
}
