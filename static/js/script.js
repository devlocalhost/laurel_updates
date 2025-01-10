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

// progress bar

document.addEventListener("DOMContentLoaded", function () {
    const progressBar = document.getElementById("progress-bar");

    function updateProgressBar() {
        const totalHeight = document.body.scrollHeight - window.innerHeight;
        const progress = (window.scrollY / totalHeight) * 100;
        progressBar.style.width = `${progress}%`;
    }

    updateProgressBar();

    window.addEventListener("scroll", updateProgressBar);
    window.addEventListener("resize", updateProgressBar);
});

// progress bar
