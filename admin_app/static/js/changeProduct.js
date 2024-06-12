let listChangeImage = document.querySelectorAll(".change-image")
let listChangeName = document.querySelectorAll(".change-name")
let listDeleteButton = document.querySelectorAll(".delete-product")
let modalWindowImage = document.querySelector(".modal-image")
let sendButton = document.querySelector(".send-button")

for (let count = 0; count < listChangeImage.length; count++ ){
    let button = listChangeImage[count]
    button.addEventListener(
      type = "input",
      listener = (event) =>{
        document.querySelector(".newName").style.display = "none"
        modalWindowImage.style.display = 'block';
        document.querySelector(".newImage").files = button.files
        document.querySelector(".saveId").value = button.id.split("-")[2]
        sendButton.textContent = "Зберегти нове зображення"
        window.scrollTo(0, 0);
      }
    )
}

for (let count = 0; count < listChangeName.length; count++ ){
  let button = listChangeName[count]
  button.addEventListener(
    type = "click",
    listener = (event) =>{
      document.querySelector(".newName").style.display = "block"
      modalWindowImage.style.display = 'block';
      document.querySelector(".saveId").value = button.id.split("-")[2]
      sendButton.textContent = "Зберегти нову назву"
      window.scrollTo(0, 0);
    }
  )
}

for (let count = 0; count < listDeleteButton.length; count++ ){
  let button = listDeleteButton[count]
  button.addEventListener(
    type = "click",
    listener = (event) =>{
      modalWindowImage.style.display = 'block';
      document.querySelector(".newName").style.display = "none"
      document.querySelector(".saveId").value = button.id.split("-")[1]
      sendButton.textContent = "Видалити продукт"
      window.scrollTo(0, 0);
    }
  )
}

