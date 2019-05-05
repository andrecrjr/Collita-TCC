let elementTable = document.querySelector('.cart-market')
let elementCart = document.querySelector('.carrinho-main')
const element = document.querySelector('.none-cart')
const elementFinal = document.querySelector('.valor-total')

const consume = (async()=>{
    try{
        result = await fetch(`${link}list_item/`)
        result = result.json()
        return result
    }catch{

    }
})

async function printMainCart(){
    try {
        let result = await fetch(`${link}list_item/`)
        let data = await result.json();
        if(data > []){
            res = sum_final(data)
            res.then(response=>valor_total(response))
            data.map((response) => {
                return elementCart.innerHTML += `
                       
                        <tr>
                            <td class="id_pedido">${response.id_compra}</td>
                            <td>${response.nome_item}</td>
                            <td>${response.preco_item.toFixed(2)}</td>
                            <td>${response.quantidade}</td>
                            <td><button id="delete-button">Excluir item</button></td>
                        </tr>
                    
                    `

            })

            let deletedButtons = document.querySelectorAll('#delete-button')

            for(let i = 0; i < deletedButtons.length; i++) {
                    deletedButtons[i].addEventListener('click', function () {
                            let id_pedido = this.closest('tr').cells[0].textContent;
                            elementCart.remove()
                            document.location.reload()
                            delete_cart(parseInt(id_pedido));
                    })
                }

        }else{
            elementCart.remove()
            elementTable.remove()
            return element.innerHTML += `Nenhum item adicionado ao carrinho, volte ao <a href="${link}">Marketplace</a>`
        }
    }catch(err){
        elementCart.remove()
        elementTable.remove()
        return element.textContent += `
            Sem conexão com o servidor tente mais tarde`
    }
}


async function delete_cart(id){
    try{
        fetch(`${link}delete_item/${id}/`,
            {method:'PUT'}).then(
            (response)=>{
                if(response.status == 200){
                    listCart()
                    const response = consume().then((response)=>res)
                    console.log(response)

                }
            }
        )
    }catch(e){
        return element.textContent += `
            Sem conexão com o servidor tente mais tarde`
    }
}

async function sum_final(data){
    try {
        let valor_final = []
        data.reduce(function (total, num) {
            total[num.nome_item] = parseFloat(num.quantidade) * num.preco_item;
            valor_final.push(total[num.nome_item])
            return valor_final
            }, {});
        let final = valor_final.reduce((total, num)=>total+num);
        return valor_final.length > 1 ? parseFloat(final) : parseFloat(valor_final[0]);

    }catch{
        return 0;
    }
}



async function valor_total(valor_final){
    try{
        return elementFinal.innerHTML+= `
                                        <tr> 
                                            <td>Valor total</td>
                                            <td>R$ ${valor_final.toFixed(2)}</td>
                                            <td><a href="${link}generate_boleto/"><button>Gerar boleto</button></a></td>
                                        </tr>
                                    `
    }catch{

    }
}
printMainCart()
listCart()