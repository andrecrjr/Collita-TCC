listCart()

function listCart() {
    const link = 'http://127.0.0.1:8000/marketplace/';
    fetch(`${link}list_item/`)
        .then(response => response.json())
            .then(
            result =>{

                if(result === null){
                    countCart(0)
                }else{
                    counting = 0
                    for(quantidade in result) {
                        counting = counting + parseInt(result[quantidade].quantidade)
                    }
                    countCart(counting);
                    printTotal(result);
                }

            }
        );
}

function countCart(contando){
    let contagem = `${contando}`
    document.querySelector('.items-menu-count').innerHTML = contagem
}
