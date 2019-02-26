$( document ).ready(function() {
let link = 'http://localhost:8000/marketplace/';
let newProduct = false
$('.comprar').click(function(){

    let id_item = $(this).closest("div.item_marketplace").find("input[name='id_item']").val();
    let preco_item = $(this).closest("div.item_marketplace").find("input[name='preco_item']").val();
    let nome_item = $(this).closest("div.item_marketplace").find("input[name='nome_item']").val();
    let csrf_token = $(this).closest("div.item_marketplace").find("input[name='csrf']").val();

    var data_cart = new Object()
    data_cart.id_produto = id_item;
    data_cart.nomeproduto = nome_item
    data_cart.precoitem = preco_item

    $.ajax({
        method: "POST",
        beforeSend: function(xhrObj){
            xhrObj.setRequestHeader("Content-Type","application/json");
            xhrObj.setRequestHeader("Accept","application/json");
        },
        url: `${link}add_item/`,
        dataType: "json",
        data: JSON.stringify(data_cart)
      }).done(function( msg ) {
          console.log('success')
      })
    console.log(newProduct)
})
    listCart()
    function listCart() {
    let productsCart = 0
        $.get(`${link}list_item/`, function(data){
            if(data) {
                for (let i in data) {
                    console.log(data[i].nomeproduto);
                }
                productsCart = data.length
            }else{
            console.log('nada n')
            }
        })
        console.log(productsCart)
    }


})

