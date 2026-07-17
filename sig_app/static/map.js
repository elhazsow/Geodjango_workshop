const divmap = document.getElementById("map")
let communes =JSON.parse(document.getElementById("communes").textContent)


let fetch_wfs = async function(url,params){
    let queryString = new URLSearchParams(params).toString();
    let response = await fetch(url+"?"+queryString)
    let data = await response.json()
    return data
}
let mouseoverFunction = function(e){
    let layer = e.target
    layer.setStyle({
        weight: 8,
        color: 'orange',
        dashArray: ''
    })
}

let mouseoutFunction = function(e){
    let layer = e.target
    layer.setStyle({
        weight: 2,
        color: 'darkblue',

    })
}

let clickFunction = function(e){
    let layer = e.target
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
    // let popupContent = "<h3>"+feature.properties.name+"</h3><p>Code: "+feature.properties.code+"</p>"
    // layer.bindPopup(popupContent)
}


window.addEventListener("map:init" ,function(e){
    let map = e.detail.map; // récupération de l'objet map
    // ajout de données
    let geojsonLayer = L.geoJSON(JSON.parse(communes),{
        style: { color: 'darkblue', weight: 2},
        onEachFeature: onEachFeature
    })
    geojsonLayer.addTo(map)
    map.fitBounds(geojsonLayer.getBounds())

    
    // ajout d'une couche WMS avec geoserver

    let overlay = L.tileLayer.wms("http://localhost:8080/geoserver/cite/wms",{
        layers:"cite:sig_app_commune",
        format:"image/png",
        transparent:true,
        srs:"EPSG:32628",
        attribution:"Données de la région"
    })
    let lc = map.layerscontrol
    lc.addOverlay(overlay, "Commune_geoserver").addTo(map)

    

})
