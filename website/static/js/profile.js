const convertStatusBoleto = () =>{
    const statusBoleto = document.querySelector(".status-boleto")
    if(statusBoleto.textContent === "True"){
        statusBoleto.textContent = "Boleto pago"
        statusBoleto.className = "boleto-pago"
    }else{
        statusBoleto.textContent = "Aguardando pagamento"
        statusBoleto.className = "aguarda-pagamento"
    }
}

convertStatusBoleto()