listCart()
    const addCartItem = document.querySelectorAll('button.comprar');
    for(let i = 0; i < addCartItem.length; i++){
        addCartItem[i].addEventListener('click', function(){
            let preco_item = this.closest("div.item-marketplace").childNodes[5].textContent;
            let id_item = this.closest("div.item-marketplace").childNodes[1].getAttribute("value");
            let nome_item = this.closest("div.item-marketplace").childNodes[3].innerText;
            console.log(preco_item)
            var data_cart = new Object()
            data_cart.id_item = id_item;
            data_cart.nome_item = nome_item
            data_cart.quantidade = 1
            printToCart(nome_item, preco_item, 1)
            data_cart.preco_item = parseFloat(preco_item.replace(',','.'));
            postCompra(data_cart)
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
