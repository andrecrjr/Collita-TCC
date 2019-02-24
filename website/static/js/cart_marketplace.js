$( document ).ready(function() {

let valor = []
var indice_selecionado = -1;
let tbProdutos = localStorage.getItem("tbProdutos");

if(tbProdutos == null){
    tbProdutos = []
}
$('.comprar').click(function(){
    const url = "http://localhost:8000/marketplace/add_item/";
    let id_item = $(this).closest("div.item_marketplace").find("input[name='id_item']").val();
    let preco_item = $(this).closest("div.item_marketplace").find("input[name='preco_item']").val();
    let nome_item = $(this).closest("div.item_marketplace").find("input[name='nome_item']").val();
    Adicionar(id_item,preco_item,nome_item)
        
})

console.log(tbProdutos)
function Adicionar(id, preco, nome){

    let data_cart=JSON.stringify({
        'id_produto':id,
        'nome_produto':nome,
        'preco_produto':preco,
    })
    if(tbProdutos != null){
        valor.push(tbProdutos)
        valor.push(JSON.stringify(data_cart))
        localStorage.setItem("tbProdutos",valor)
    }
    else{
        tbProdutos.push(data_cart)
        localStorage.setItem("tbProdutos", JSON.stringify(data_cart))
    }
}

})

