window.addEventListener("beforeunload", function () {
    document.body.classList.add("fade-out");
});

document.querySelectorAll("a").forEach(function (link) {
    if (!link.classList.contains("no-fade-animation")) {
        link.addEventListener("click", function (event) {
            event.preventDefault();

            // Fade out the current page
            document.body.classList.add("fade-out");

            // Once the fade out animation is complete, navigate to the new page
            document.body.addEventListener("animationend", function () {
                window.location.href = link.href;
            });
        });
    }
});

var prevScrollpos = window.pageYOffset;

window.onscroll = function() {
    if (window.innerWidth < 767) {
        var currentScrollPos = window.pageYOffset;
        var navbar = document.getElementsByClassName("navbar")[0];

        if (prevScrollpos > currentScrollPos) {
            navbar.style.bottom = "25px";
        } else {
            navbar.style.bottom = "-64px";
        }

        prevScrollpos = currentScrollPos;
    }
}

