const divmap = document.getElementById("map")

window.addEventListener("map:init" ,function(e){
    let map = e.detail.map;

    // ajout de données

    let overlay = L.tileLayer.wms("http://localhost:8080/geoserver/cite/wms",{
        layers:"cite:sig_app_commune",
        format:"image/png",
        transparent:true,
        srs:"EPSG:32628",
        attribution:"Données de la région"
    })
    let lc = map.layerscontrol
    lc.addOverlay(overlay, "Commune").addTo(map)
    console.log("map:init event fired")

})
