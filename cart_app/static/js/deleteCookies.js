let listButtonsMinus = document.querySelectorAll(".minus")
//
for (let count = 0; count < listButtonsMinus.length; count++ ){
    let button = listButtonsMinus[count]
    button.addEventListener(
      type = "click",
      listener = (event) =>{
        // 'products=1 1 1 1 2 2 2 2 3 3 3 3' => ['products', '1 1 1 1 2 2 2 2 3 3 3 3'] => '1 1 1 1 2 2 2 2 3 3 3 3'
        let cookiesProducts = document.cookie.split('=')[1] 
        // '1 1 1 1 2 2 2 2 3 3 3 3' => ['1', '1', '1', '1', '2', '2', '2', '2', '3', '3', '3', '3']
        let listIdProducts = cookiesProducts.split(" ")
        // 
        for (let index = 0; index < listIdProducts.length; index++){
        // 
          if (button.id == listIdProducts[index]){
            listIdProducts.splice(index, 1) //
            // 
            button.nextElementSibling.textContent = Number(button.nextElementSibling.textContent) - 1
            break
          }
        }
        // 
        if (button.nextElementSibling.textContent == 0){
            document.querySelector(`#product-${button.id}`).remove() //
        }
        document.cookie = `products = ${listIdProducts.join(" ")}; path = /`
        // 
        if (document.cookie.split('=')[1] == ''){
            let h2 = document.createElement('h2') //
            h2.textContent = 'Корзина порожня' //
            document.body.append(h2) //
        }
      }
    )
}