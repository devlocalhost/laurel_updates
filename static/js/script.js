// scroll to top

var clickCount = 0;

document.body.addEventListener("click", function (event) {
    if (event.target === document.body) {
        clickCount++;
        navigator.vibrate(10);

        if (clickCount === 2) {
            window.scrollTo({ top: 0, behavior: "smooth" });
            navigator.vibrate(14);
            clickCount = 0;
        }
    }
});

// scroll to top

// fade in/out

window.addEventListener("beforeunload", function () {
    document.body.classList.add("fade-out");
});

document.querySelectorAll("a").forEach(function (link) {
    if (!link.classList.contains("no-fade-animation")) {
        link.addEventListener("click", function (event) {
            event.preventDefault();

            document.body.classList.add("fade-out");

            document.body.addEventListener("animationend", function () {
                window.location.href = link.href;
            });
        });
    }
});

// fade in/out

// hiding/showing navbar on scroll

var prevScrollpos = window.pageYOffset;

window.onscroll = function () {
    if (window.innerWidth < 767) {
        var currentScrollPos = window.pageYOffset;
        var navbar = document.getElementsByClassName("navbar")[0];

        if (prevScrollpos > currentScrollPos) {
            navbar.style.bottom = "25px";
        } else {
            navbar.style.bottom = "-60px";
        }

        prevScrollpos = currentScrollPos;
    }
};

// hiding/showing navbar on scroll

// copy code on code tag click

window.onload = function () {
    const codeElements = document.querySelectorAll("code");

    if (codeElements.length > 0) {
        codeElements.forEach(function (codeElement) {
            codeElement.onclick = function () {
                document.execCommand("copy");
            };

            codeElement.addEventListener("copy", function (event) {
                event.preventDefault();

                if (event.clipboardData) {
                    const textToCopy =
                        codeElement.textContent || codeElement.innerText;
                    event.clipboardData.setData("text/plain", textToCopy);
                    navigator.vibrate(10);
                    // console.log(event.clipboardData.getData("text"));
                }
            });
        });
    }
};

// copy code on code tag click

// "debug" stylesheet

function setCount(count) {
    localStorage.setItem("clickCount", count);
}

function getCount() {
    return parseInt(localStorage.getItem("clickCount")) || 0;
}

let isDebugStylesheetVisible = false;

function toggleStylesheet() {
    const clickCount = getCount();
    setCount(clickCount + 1);
    navigator.vibrate(10);

    if (clickCount % 3 === 0) {
        isDebugStylesheetVisible = !isDebugStylesheetVisible;

        const debugStylesheet = document.getElementById("debug-stylesheet");
        navigator.vibrate(14);

        debugStylesheet.disabled = !isDebugStylesheetVisible;
    }
}

// "debug" stylesheet
