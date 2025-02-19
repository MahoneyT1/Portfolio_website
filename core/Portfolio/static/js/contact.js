

document.addEventListener('DOMContentLoaded', ()=> {
    console.log("working")

    const alertMessages = document.querySelectorAll('.alert');

    alertMessages.forEach((alert)=> {

        setTimeout(()=> {
            alert.style.opacity = 0;

            setTimeout(()=> {
                alert.style.display = "none";
            }, 500)
        }, 3000)
    })
})