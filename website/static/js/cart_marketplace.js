$( document ).ready(function() {
let link = 'http://localhost:8000/marketplace/';
listCart()

const requestData = (data_cart) =>( 
    fetch(`${link}add_item/`,{
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

$('.comprar').on("click",function(){
    let id_item = $(this).closest("div.item_marketplace").find("input[name='id_item']").val();
    let preco_item = $(this).closest("div.item_marketplace").find("input[name='preco_item']").val();
    let nome_item = $(this).closest("div.item_marketplace").find("input[name='nome_item']").val();
    let csrf_token = $(this).closest("div.item_marketplace").find("input[name='csrf']").val();

    var data_cart = new Object()
    data_cart.id_produto = id_item;
    data_cart.nomeproduto = nome_item
    data_cart.precoitem = preco_item
    requestData(data_cart)
})

function listCart() {
    $.get(`${link}list_item/`, function(data){
        if(data) {
            for (let i in data) {
                console.log(data[i].nomeproduto);
            }
            countCart(data.length)
        }else{
            countCart(0)
        }
    });
}

function countCart(contando){
    let contagem = `${contando}`
    $('.items-menu-count').text(contagem)
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

