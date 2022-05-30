function MatchInfo(props) {
  return (
    <div className="match_pet">
      <p>Pet's id: {props.pet_id}</p>
      <p>Name: {props.name}</p>
      <p>Breed: {props.breed} </p>
      <p>Color: {props.color} </p>
      <p>Address where the pet was found: {props.location}</p>
      <p>Rescuer's name: {props.user_name}</p>
      <p>Rescuer's email: {props.user_email}</p>
    </div>
  );
};



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

const final_match = [];
const matchesList = [];

function PetMatchesContainer(){  
  for (const pet of final_match) {
    matchesList.push(
      <MatchInfo
        key={pet.pet_id}
        pet_id={pet.pet_id}
        name={pet.name}
        breed={pet.breed}
        color={pet.color}
        location={pet.location}
        user_name={pet.user_name}
        user_email={pet.user_email}        
      />,
    );
  };  
  return(
  <React.Fragment>
  <div className="matchesList">{matchesList}</div>
  </React.Fragment>
  ); 
};




fetch('/matches.json')
.then(response => response.json())
.then(Data => {  
 
  console.log(Data);
  const matches=Data.match_and_lost_pet;
  console.log(matches);
  //const final_match = [];
  
  if (matches != null){
    const lost_pet = matches.pop();
    console.log(lost_pet);    
    console.log(matches);
    const pet_id_matches = [];
    const center_lost_pet = {'lat':lost_pet.lat, 'lng':lost_pet.lng};
    
    for (const pet of matches){
      const center={};
      center['lat']=pet.lat;
      center['lng']=pet.lng;
      //console.log(center);
      const distance = getDistance(center_lost_pet, center);
      console.log(distance);
      
      if (distance <= 30){
        pet_id_matches.push(pet.pet_id);
        final_match.push(pet);
      };          
    };  
    console.log(final_match);
    console.log(pet_id_matches);
  };           
  document.querySelector('#message').innerHTML = Data.msg;
  ReactDOM.render(<PetMatchesContainer />, document.getElementById('matches'));
 });

 






