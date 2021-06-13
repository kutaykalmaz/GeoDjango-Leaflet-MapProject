function our_layers(map, options) {
    var points = new L.GeoJSON.AJAX("marked_data/", {
        onEachFeature: function (feature, layer) {
            layer.bindPopup(feature.properties.name.toString())
        }
    });


    points.addTo(map);
}

window.addEventListener("map:init", function (e) {
    var detail = e.detail;
    googleStreets = L.tileLayer('http://{s}.google.com/vt/lyrs=m&x={x}&y={y}&z={z}', {
        subdomains: ['mt0', 'mt1', 'mt2', 'mt3']
    });
    googleStreets.addTo(detail.map);

}, false);

k




