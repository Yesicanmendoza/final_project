function ShowingMatches(props) {
  return (
    <div className="match_pet">
      <p>Name: {props.name}</p>
      <p>Breed: {props.breed} </p>
      <p>Color: {props.color} </p>
      <p>Address where he/she was found: {props.location}</p>
      <p>Rescuer's name: {props.user_name}</p>
      <p>Rescuer's email: {props.user_email}</p>
    </div>
  );
}


function degreesToRadians(degrees){
  return degrees * Math.PI / 180;
};

function getDistance(center_from, center_to){
  
  const longitudeFrom = center_from.lng;
  const longitudeTo = center_to.lng;
  const latitudeFrom = center_from.lat;
  const latitudeTo = center_to.lat;
  const R = 6378137;
  const dLat = degreesToRadians(latitudeTo - latitudeFrom);  
  const dLong = degreesToRadians(longitudeTo - longitudeFrom);  
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
  
  const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
  
  const distance = R * c * 0.000621371;

  return distance;
};


fetch('/matches.json')
  .then(response => response.json())
  .then(Data => {    
    const matches=Data.match_and_lost_pet;
    //console.log(matches);
    if (matches != null){
      const lost_pet = matches.pop();
      console.log(lost_pet);    
      console.log(matches);
      const center_lost_pet = {'lat':lost_pet.lat, 'lng':lost_pet.lng};
      const final_match = [];
      for (const pet of matches){
        const center={};
        center['lat']=pet.lat;
        center['lng']=pet.lng;
        //console.log(center);
        const distance = getDistance(center_lost_pet, center);
        console.log(distance);

        if (distance <= 30){
          final_match.push(pet);

        }           
      }
      console.log(final_match);
    };
    
      
    document.querySelector('#message').innerHTML = Data.msg;
    });


  