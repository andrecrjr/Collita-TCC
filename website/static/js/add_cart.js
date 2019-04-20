listCart()
const link = 'http://127.0.0.1:8000/marketplace/';

    const addCartItem = document.querySelectorAll('button.comprar');
    for(let i = 0; i < addCartItem.length; i++) {
        addCartItem[i].addEventListener('click', function () {
            let preco_item = this.closest("div.item-marketplace").childNodes[5].textContent;
            let id_item = this.closest("div.item-marketplace").childNodes[1].getAttribute("value");
            let nome_item = this.closest("div.item-marketplace").childNodes[3].innerText;
            let quantidade = this.closest("div.item-marketplace").children[4].value
            let data_cart = new Object()
            data_cart.id_item = id_item;
            data_cart.nome_item = nome_item
            data_cart.quantidade = quantidade
            let existent = verifyItemExists(id_item, quantidade)
            printToCart(nome_item, preco_item, quantidade)
            existent.then(response => {
                if(!response) {
                    data_cart.preco_item = parseFloat(preco_item.replace(',', '.'));
                    postCompra(data_cart)
                    listCart()
                }
            }).catch(response=>{
                console.log('pulou fora')
            })
            listCart()
        })
    }

    async function verifyItemExists(id_item, quantidade_item){
        try{
            let response = await fetch(`${link}list_item/`)
            let data = await response.json()
            for(let id = 0; id <= data.length; id++){
                if(id_item.toString() === data[id].id_item){
                    updateItemExists(id,quantidade_item)
                    return true;
                }
            }
        }catch{
            return false
        }
    }

    const updateItemExists = (id_json, quantidade_item) => {
        fetch(`${link}update_item_cart/${id_json}/${quantidade_item}/`,{
          method:'PUT'
        }).then(result=>{
             listCart()
        })
    }


    const postCompra = (data_cart) =>(
        fetch(`http://127.0.0.1:8000/marketplace/add_item/`,{
            method:'POST',
            body: JSON.stringify(data_cart),
            headers: new Headers({
                'Content-Type': 'text/plain'
              })
        }).then(function(response){
            listCart()
        })
    )

    // delete cart

    const deleteButton = document.querySelector('.remove-itens')
    deleteButton.addEventListener('click', ()=>{
        fetch(`delete/`)
            .then(function(){
            countCart(0)
            cart = document.querySelector('.total-market')
        })
        const cartList = document.querySelector('.cart-list')
        const marketTotal = document.querySelector('.total-market')
        while (cartList.firstChild) {
            cartList.removeChild(cartList.firstChild);
        }
        while(marketTotal.firstChild){
            marketTotal.removeChild(marketTotal.firstChild);
        }

        cartList.innerHTML += `<tr>
                                        <td>Nenhum item</td>
                                  </tr>`
    })
