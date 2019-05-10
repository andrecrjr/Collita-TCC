const link = 'http://127.0.0.1:8000/marketplace/';

async function listCart () {
    try{
        result = await fetch(`${link}list_item/`)
        data = await result.json();
        if(data === null){
                    countCart(0)
                }else{
                    counting = 0;
                    for(quantidade in data) {
                        counting = counting + parseInt(data[quantidade].quantidade);
                    }
                    countCart(counting);
                    printTotal(data);
        }

    }catch{

    }
}


function countCart(contando){
    let contagem = `${contando}`
    document.querySelector('.items-menu-count').innerHTML = contagem
}

listCart()

const boleto_await = async ()=>
{
    try {
        data = await fetch(`${link}get_transaction`)
        payment = await data.json()
        if(payment.status === 'paid'){
            console.log('pagou')
        }else{
            console.log('não pagou')
        }
    } catch (e) {
        console.log('oops', e)
    }
}

boleto_await()