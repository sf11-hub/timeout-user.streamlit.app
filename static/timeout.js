const TIMEOUT_MS = 1000;

function timeoutHandler() {
    alert("User inactive for too long");
    //call the equivalent function
}

// Set up the timer
let timeoutTimer;

function resetTimer() {
    clearTimeout(timeoutTimer);
    timeoutTimer = setTimeout(timeoutHandler, TIMEOUT_MS);
}

document.addEventListener("mousemove", resetTimer);
document.addEventListener("keypress", resetTimer);
resetTimer();
