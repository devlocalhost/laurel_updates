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
