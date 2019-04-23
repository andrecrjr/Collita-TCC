
async function printMainCart(){
     const link = 'http://127.0.0.1:8000/marketplace/';
     elementTable = document.querySelector('.cart-market')
     elementCart = document.querySelector('.carrinho-main')
    try {
        result = await fetch(`${link}list_item/`)
        data = await result.json();
        var i = 0;
        console.log(data)
        if(data > []){
        data.map((response) => {
            i = i + 1
            return elementCart.innerHTML += `
                    <tr>
                        <td>${i} </td>
                        <td>${response.nome_item}</td>
                        <td>${response.preco_item}</td>
                        <td>${response.quantidade}</td>
                    </tr>
                
                `
        })}else{
            elementCart.remove()
            elementTable.remove()
            const element = document.querySelector('.none-cart')
            return element.textContent += `           
            Nenhum item adicionado ao carrinho`
        }
    }catch(err){
        return elementCart.innerHTML += `
            <tbody>Sem conexão com o servidor tente mais tarde</tbody>
        `
    }
}
printMainCart()