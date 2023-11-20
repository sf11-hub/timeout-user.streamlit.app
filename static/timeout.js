const TIMEOUT_MS = 1000; //this constant is replaced in v0-app

function timeoutHandler() {
    alert("User inactive for too long");
    console.log("User inactivity timed out")
    //call the equivalent function
}

// Set up the timer
let timeoutTimer;

function resetTimer() {
    clearTimeout(timeoutTimer);
    timeoutTimer = setTimeout(timeoutHandler, TIMEOUT_MS);
    console.log("timeout user: reset")
}

document.addEventListener("mousemove", resetTimer);
document.addEventListener("keypress", resetTimer);
resetTimer();
