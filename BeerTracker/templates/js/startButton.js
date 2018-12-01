function newDoc() {
    window.location.pathname = "/web-client/Map.html";
    getLocation();
}

function getLocation() {
    var locField = document.getElementById("locField").value;
    console.log(locField);
}
