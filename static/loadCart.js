function loadCart() {
    var size = fetch('/getCartSize',
        { method: 'POST' }
    ).then((response) => response.json())
        .then((data) => {
            const cartSize = document.getElementById('cartSize')
            console.log(data)
            cartSize.innerHTML = data
        })
}

loadCart();
