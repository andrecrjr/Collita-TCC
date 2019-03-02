
const addCartItem = document.querySelectorAll('button.comprar');
for(let i = 0; i < addCartItem.length; i++){
    addCartItem[i].addEventListener('click', function(){
        let preco_item = this.closest("div.item-marketplace").childNodes[5].textContent;
        let id_item = this.closest("div.item-marketplace").childNodes[1].getAttribute("value");
        let nome_item = this.closest("div.item-marketplace").childNodes[3].textContent;
        console.log(preco_item)
        var data_cart = new Object()
        data_cart.id_item = id_item;
        data_cart.nome_item = nome_item
        data_cart.preco_item = parseFloat(preco_item.replace(',','.'));
        requestData(data_cart)
    })
}

const requestData = (data_cart) =>(
    fetch(`add_item/`,{
        method:'POST',
        body: JSON.stringify(data_cart),
        headers: new Headers({
            'Content-Type': 'text/plain'
          })
    }).then(function(response){
        console.log(response)
        listCart()
    })
)

// delete cart

const deleteButton = document.querySelector('.remove-itens')
deleteButton.addEventListener('click', ()=>{
    fetch(`delete/`)
        .then(function(ok){
        countCart(0)
            cart = document.querySelector('.total-market')
            cart.innerHTML = ''
    })
})