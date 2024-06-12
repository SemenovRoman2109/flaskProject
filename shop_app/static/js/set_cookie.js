const buttonList = document.body.querySelectorAll('.buy')

for (let count = 0; count < buttonList.length; count++){
    let button = buttonList[count]

    button.addEventListener('click', listener = function (event)
        {
            if (document.cookie == ''){
                document.cookie = `products = ${button.id}; path = /`
            }else{
                id_product = document.cookie.split('=')[1]
                document.cookie = `products = ${id_product} ${button.id}; path = /`
            }

        }
    )
}