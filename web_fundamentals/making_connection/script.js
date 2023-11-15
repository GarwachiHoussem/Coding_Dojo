var message=document.querySelector(".xx")
function houssem(){
    console.log(message.innerText);
    //message.innerText("mourad")
    message.innerText = "Ahmed"
    
}





// var message1=document.querySelector(".line1")
// function supprimer1(){
//     message1.remove()

// }

// var message2=document.querySelector(".line2")
// function supprimer2(){
//     message2.remove()
// }

function supprimer(el){
    el.parentNode.remove()
}

var nc = document.querySelector(".nav-y span")
function accept(e){
    e.parentNode.remove()
    console.log(nc.innerText.split('+')[0]);
    nc.innerText = parseInt(nc.innerText.split('+')[0])+1 + '+'
}

