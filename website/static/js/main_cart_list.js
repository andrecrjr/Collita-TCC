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
        let i = -1;
        if(data > []){
            res = sum_final(data)
            res.then(response=>valor_total(response))
            data.map((response) => {
                i = i + 1
                return elementCart.innerHTML += `
                        <tr>
                            <td>${i} </td>
                            <td>${response.nome_item}</td>
                            <td>${response.preco_item.toFixed(2)}</td>
                            <td>${response.quantidade}</td>
                            <td><button onClick="delete_cart(${i})">Excluir item</button></td>
                        </tr>
                    
                    `

            })
        }else{
            elementCart.remove()
            elementTable.remove()
            return element.textContent += `           
            Nenhum item adicionado ao carrinho`
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
                    elementCart.remove()
                    elementCart.children[id].remove()
                    elementFinal.children[0].remove()
                    let total = sum_final(response)
                    consume().then((response)=>console.log(response))
                    if (elementCart.children.length == 0){
                        printMainCart()
                    }
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
printMainCart().then((response)=> response)


async function valor_total(valor_final){
    try{
        return elementFinal.innerHTML+= `
                                        <tr> 
                                            <td>Valor total</td>
                                            <td>${valor_final}</td>
                                        </tr>
                                    `
    }catch{

    }
}