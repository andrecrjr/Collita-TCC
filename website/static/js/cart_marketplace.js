listCart()

function listCart() {
    const link = 'http://localhost:8000/marketplace/';
    fetch(`${link}list_item/`)
        .then(response => response.json())
            .then(
            result =>{
                //updateCart(result)
                if(!result){
                    countCart(0)
                }else {
                    countCart(result.length)
                }
            }
        );
}

function countCart(contando){
    let contagem = `${contando}`
    document.querySelector('.items-menu-count').innerHTML = contagem
    takeInfo()
}

