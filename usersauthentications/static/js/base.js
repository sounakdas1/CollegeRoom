document.addEventListener("DOMContentLoaded", function() {
    const text = "Welcome to GCECT's Classroom";
    const typewriter = document.getElementById("typewriter");
    let index = 0;
    const typingSpeed = 900;

    function type() {
        if (index < text.length) {
            typewriter.innerHTML += text.charAt(index);
            index += 1;
            setTimeout(type, typingSpeed);
        } else {
            setTimeout(() => {
                typewriter.innerHTML = "";
                index = 0;
                type();
            }, 700);
        }
    }

    type(); 
});
document.addEventListener("DOMContentLoaded",function(){
    var acc = document.getElementsByClassName("accordion");
    var i;
    
    for (i = 0; i < acc.length; i++) {
    acc[i].addEventListener("click", function() {
        
        /* Toggle between adding and removing the "active" class,
        to highlight the button that controls the panel */
        this.classList.toggle("active");
        var ic = this.querySelector(".fa-angle-down");
        ic.classList.toggle("rotated")
        /* Toggle between hiding and showing the active panel */
        var panel = this.nextElementSibling;
        if (panel.style.display === "block") {
        panel.style.display = "none";
        } else {
        panel.style.display = "block";
        }
    });
    }
})

