$( document ).ready(function() {
let link = 'http://localhost:8000/marketplace/';
listCart()

$('.comprar').on("click",function(){

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
    })
    listCart()
})

function listCart() {
    $.get(`${link}list_item/`, function(data){
        if(data) {
            for (let i in data) {
                console.log(data[i].nomeproduto);
            }
            let contagem = data.length
            if((!data.length || !contagem)){
                contagem = 0;
            }
            console.log(contagem)
            countCart(contagem)
        }else{
            console.log('nada n')
        }
    });
}

function countCart(contando){
    let contagem = `${contando}`
    $('.items_menu_count').text(contagem)
}

function deleteItem(){
    $.get(`${link}delete`, function(data){
        console.log('deletado');
        countCart(0)
    });
}

$('.remove_itens').on('click',function(){
    deleteItem();
})

})

