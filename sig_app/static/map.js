
let regions = JSON.parse(document.getElementById("regions").textContent) // récupération des données regions depuis le script JSON
let communes=JSON.parse(document.getElementById("communes").textContent) // récupération des données communes depuis le script JSON
// variables
var geojsonlayer;


let mouseoverFunction = function(e){
    let layer = e.target  
    layer.setStyle({
        weight: 8,
        color: 'orange',
        dashArray: ''
    })
    layer.bringToFront()
}

let mouseoutFunction = function(e){
    geojsonLayer.resetStyle(e.target)
    // layer.setStyle({
    //     weight: 2,
    //     color: 'darkblue',

    // })
}

let clickFunction = function(e){
    let layer = e.target
    // console.log(layer.feature.properties)

    layer.setStyle({
        weight: 5,
        color: 'blue',
    })
   
}


let onEachFeature = function(feature, layer){
    layer.on({
        "mouseover": mouseoverFunction,
        "mouseout": mouseoutFunction,
        "click": clickFunction
    })
    let popupContent = "<div class='popup'><h4>"+layer.feature.properties.name+"</h4><p>Code: "+layer.feature.properties.code+"</p></div>"
    layer.bindPopup(popupContent)
    
}


window.addEventListener("map:init" ,function(e){
    let map = e.detail.map; // récupération de l'objet map
    let lc = map.layerscontrol //récupération de l'objet layercontrol
    // ajout de données
    geojsonLayer = L.geoJSON(JSON.parse(regions),{
        style: { color: 'darkblue', weight: 2}, //leaflet: https://leafletjs.com/examples/choropleth/
        onEachFeature: onEachFeature
    })

    let com_layer = L.geoJSON(JSON.parse(communes),{
        style:{color:"darkblue",weight:2},
        onEachFeature: onEachFeature
    })
    lc.addOverlay(com_layer,"Communes")



    geojsonLayer.addTo(map)
    lc.addOverlay(geojsonLayer, "regions").addTo(map)
    map.fitBounds(geojsonLayer.getBounds())


    // ajout d'une couche WMS avec geoserver

    let overlay = L.tileLayer.wms("http://localhost:8080/geoserver/wms",{
        layers:"cite:sig_app_commune",
        format:"image/png",
        transparent:true,
        srs:"EPSG:32628",
        attribution:"Limites administratives des communes du Sénégal",
    })
    
    lc.addOverlay(overlay, "Commune_geoserver").addTo(map)

    

})
