
function initMap() {
  const map = new google.maps.Map(document.querySelector('#map'), {
    center: {
      lat: 37.601773,
      lng: -122.20287,
    },
    zoom: 11,
  });

};

function degreesToRadians(degrees){
  return degrees * Math.PI / 180;
};

function getDistance(center_from, center_to){
  // El radio del planeta tierra en metros.
  const longitudeFrom = center_from.lng;
  //console.log(longitudeFrom);
  const longitudeTo = center_to.lng;
  console.log(longitudeTo);
  const latitudeFrom = center_from.lat;
  //console.log(latitudeFrom);
  const latitudeTo = center_to.lat;
  console.log(latitudeTo)

  const R = 6378137;
  const dLat = degreesToRadians(latitudeTo - latitudeFrom);
  //console.log(dLat);
  const dLong = degreesToRadians(longitudeTo - longitudeFrom);
  //console.log(dLong);
  const a = (Math.sin(dLat / 2)
          *
          Math.sin(dLat / 2) 
          +
          Math.cos(degreesToRadians(latitudeTo)) 
          * 
          Math.cos(degreesToRadians(latitudeTo)) 
          *
          Math.sin(dLong / 2) 
          * 
          Math.sin(dLong / 2));
  
  //console.log(a);

  const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
  //console.log(c);

  const distance = R * c * 0.000621371;

  return distance;
}


fetch('/matches.json')
  .then(response => response.json())
  .then(Data => {    
    const matches=Data.match_and_lost_pet;
    console.log(matches);
    //const len =match_lost_list.length;    
    const lost_pet = matches.pop();
    console.log(lost_pet);    
    console.log(matches);
    const center_lost_pet = {'lat':lost_pet.lat, 'lng':lost_pet.lng};

    for (const pet of matches){
      const center={};
      center['lat']=pet.lat;
      center['lng']=pet.lng;
      //console.log(center);
      const distance = getDistance(center_lost_pet, center);
      console.log(distance);
    }

    document.querySelector('#message').innerHTML = Data.msg;
  });


  