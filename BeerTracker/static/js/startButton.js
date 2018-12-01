function newDoc() {
    window.location.pathname = "/templates/Map.html";
    getLocation();
}

function getLocation() {
    var locField = document.getElementById("locField").value;
    console.log(locField);
}
