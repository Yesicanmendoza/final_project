function MatchInfo(props) {
  return (
    <div className="match_pet">
      <p>Pet's id: {props.pet_id}</p>
      <p>Name: {props.name}</p>
      <p>Breed: {props.breed} </p>
      <p>Gender: {props.gender} </p>
      <p>Color: {props.color} </p>
      <p>Address where the pet was lost\found: {props.location}</p>
      <p>Rescuer\Owner's name: {props.user_name}</p>
      <p>Rescuer\Owner's's email: {props.user_email}</p>
      <img src={props.img} alt="profile" />
    </div>
  );
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
        gender={pet.gender}
        color={pet.color}
        location={pet.location}
        user_name={pet.user_name}
        user_email={pet.user_email} 
        img={pet.img}       
      />,
    );
  };  
  return(
  <React.Fragment>
  <div className="matchesList">{matchesList}</div>
  </React.Fragment>
  ); 
};

const pet_id_matches = [];
function AskIfPetWasFound() {
  let selectOption = [];
  for (let petId of pet_id_matches){
    selectOption.push(<option key={petId} name ='pet_id_match' value={petId}>{petId}</option>);
  };
  return ( 
        <section id="found_pet"> 
          <form className="found_pet">
            <h2>Did you find your pet? </h2>
              <label>
                If you found your pet, please select the pet's id we should remove from the database: 
              <select id="match_pet_id" name="match_pet_id">
                {selectOption}
              </select>        
              </label>      
            <button type="submit">Submit</button>
          </form>  
        </section>   
  );
};


function changePetType(evt) {
  evt.preventDefault();

  const data= {match_pet_id:document.querySelector('option[name="pet_id_match"').value,};
  //console.log(data);
  
  const url = '/change_pet_type.json'; 
  fetch(url, {  
    method: 'POST',
    body: JSON.stringify(data),
    headers: {
      'Content-Type': 'application/json',
    }
  })
  .then(response =>  response.json())
  .then(jsonData => {
    document.querySelector('#message2').innerHTML = jsonData.msg2;
          
  });    
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


fetch('/matches.json')
.then(response => response.json())
.then(Data => {  
  let msg = Data.msg;
  //console.log(msg);
  //console.log(Data);
  const matches=Data.matches_and_pet_to_look;
  //console.log(matches);
    
  if (matches != null){
    const petToLook = matches.pop();
    //console.log(petToLook);    
    //console.log(matches);    
    const centerPetToLook = {'lat':petToLook.lat, 'lng':petToLook.lng};
    
    for (const pet of matches){
      const center={};
      center['lat']=pet.lat;
      center['lng']=pet.lng;
      //console.log(center);
      const distance = getDistance(centerPetToLook, center);
      //console.log(distance);
      
      if (distance <= 30){
        pet_id_matches.push(pet.pet_id);
        final_match.push(pet);
      };          
    };  
    //console.log(final_match);
    //console.log(pet_id_matches);

    if (final_match === []){
      msg = 'There are not matches around 30 miles';
    }else {
      ReactDOM.render(<PetMatchesContainer />, document.getElementById('matches'));
      ReactDOM.render(<AskIfPetWasFound />, document.getElementById('foundPet'));
      document.querySelector('#found_pet form').addEventListener('submit', changePetType);
           
    };
  };   
  

  document.querySelector('#message').innerHTML = msg;
 });

 






