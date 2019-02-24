$( document ).ready(function() {

$('.comprar').click(function(){
    const url = "http://localhost:8000/marketplace/add_item/";
    let id_item = $(this).closest("div.item_marketplace").find("input[name='id_item']").val();
    let preco_item = $(this).closest("div.item_marketplace").find("input[name='preco_item']").val();
    let nome_item = $(this).closest("div.item_marketplace").find("input[name='nome_item']").val();
    let csrf_token = $(this).closest("div.item_marketplace").find("input[name='csrf']").val();

    var data_cart = new Object()
    data_cart.id_produto = id_item;
    data_cart.nomeproduto = nome_item
    data_cart.precoitem = preco_item
        /*
    $.post(url,{data:data_cart,'csrfmiddlewaretoken':csrf_token}, function(data){
        console.log('foi')
    }).fail(function(data){
        console.log('failled', data)
    })*/
    console.log(JSON.stringify(data_cart))
    $.ajax({
        method: "POST",
        beforeSend: function(xhrObj){
            xhrObj.setRequestHeader("Content-Type","application/json");
            xhrObj.setRequestHeader("Accept","application/json");
        },
        url: url,
        dataType: "json",
        data: JSON.stringify(data_cart)
      }).done(function( msg ) {
          alert( "Data Saved: " + msg );
        })
})

    


})

