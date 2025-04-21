// Example: Add a loading spinner during scans
document.querySelector("form").addEventListener("submit", function() {
    const button = document.querySelector("button");
    button.innerHTML = "Scanning...";
    button.disabled = true;
});