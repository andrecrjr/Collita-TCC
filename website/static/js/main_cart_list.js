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
                            <td>R$ ${response.preco_item.toFixed(2)}</td>
                            <td>${response.quantidade}</td>
                            <td><button id="delete-button"></button></td>
                        </tr>
                    `
            })

            let deletedButtons = document.querySelectorAll('#delete-button')
            for(let i = 0; i < deletedButtons.length; i++) {
                    deletedButtons[i].addEventListener('click', function () {
                            let id_pedido = this.closest('tr').cells[0].textContent;
                            delete_cart(parseInt(id_pedido));
                            this.closest('tr').remove()
                    })
                }
        }else{
            elementCart.remove()
            elementTable.remove()
            return element.innerHTML += `
                        <div class="warning">
                        <span class="omg-warning"></span>
                            <div class="warning-inside">
                                Nenhum item adicionado ao carrinho<br> volte ao <a href="${link}">Marketplace</a>
                            </div>
                         </div>`
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
            {method:'PUT'}).then((response)=>{
                if(response){
                    document.location.reload()
                }
        })
    }catch(e){
        return element.textContent += `
            Sem conexão com o servidor tente mais tarde`
    }
}

async function sum_final(data){
    try {
        let valorFinal = []
        data.reduce(function (total, num) {
            total[num.nome_item] = parseFloat(num.quantidade) * num.preco_item;
            valorFinal.push(total[num.nome_item])
            return valorFinal
            }, {});
        console.log(valorFinal)
        let final = valorFinal.reduce((total, num)=>total+num);
        return valorFinal.length > 1 ? parseFloat(final) : parseFloat(valorFinal[0]);
    }catch{
        return 0;
    }
}



async function valor_total(valor_final){
    try{
        return elementFinal.innerHTML+= `
                                        <tr class="footer-cart"> 
                                            <td class="total-cart">Preço total:</td>
                                            <td>R$ ${valor_final.toFixed(2)}</td>
                                            <td><a href="${link}generate_boleto/"><button class="print-boleto">Gerar Boleto</button></a></td>
                                        </tr>
                                    `
    }catch{
    }
}
printMainCart()
listCart()