headerItems = document.querySelectorAll(".header__left-item")
headerItems.forEach(function(headerItem) {
     headerItem.addEventListener("click", function() {
          headerItems.forEach(item => {
               item.classList.remove("active");
          })
     headerItem.classList.add("active")
     });
});


var next = document.querySelector(".content__body__introduction__images__button__next")
var prev = document.querySelector(".content__body__introduction__images__button__prev")

next.addEventListener('click', function() {
     let list = document.querySelectorAll(".content__body__introduction__image")
     document.querySelector(".content__body__introduction__images").appendChild(list[0])
})

prev.addEventListener('click', function() {
     let list = document.querySelectorAll(".content__body__introduction__image")
     document.querySelector(".content__body__introduction__images").prepend(list[list.length - 1])
})

var partnerChoosen = 2
var nextPartner = document.querySelector(".content__body__partner__control--next")
nextPartner.addEventListener('click', function() {
     let list = document.querySelectorAll(".content__body__partner__item")
     document.querySelector(".content__body__partner__list").appendChild(list[0])
     let listPartner = document.querySelectorAll(".content__body__partner__inf")
     listPartner[partnerChoosen].classList.remove("active")
     if (partnerChoosen == 7) {
          partnerChoosen = 0
     }
     else {
          partnerChoosen += 1
     }
     listPartner[partnerChoosen].classList.add("active")
})
var prevPartner = document.querySelector(".content__body__partner__control--prev")
prevPartner.addEventListener('click', function() {
     let list = document.querySelectorAll(".content__body__partner__item")
     document.querySelector(".content__body__partner__list").prepend(list[list.length - 1])
     let listPartner = document.querySelectorAll(".content__body__partner__inf")
     listPartner[partnerChoosen].classList.remove("active")
     if (partnerChoosen == 0) {
          partnerChoosen = 7
     }
     else {
          partnerChoosen -= 1
     }
     listPartner[partnerChoosen].classList.add("active")
})

