
function sendGeocodinfo(data){
  const url = '/pet_registration.json'; 
    fetch(url, {  
      method: 'POST',
      body: JSON.stringify(data),
      headers: {
        'Content-Type': 'application/json',
      }
    })
    .then(response =>  response.json())
    .then(jsonData => {
      document.querySelector('#message').innerHTML = jsonData.msg;
          
    });
}; 



function initMap() {
  const map = new google.maps.Map(document.querySelector('#map'), {
    center: {
      lat: 37.601773,
      lng: -122.20287,
    },
    zoom: 11,
  });

};




function registerPet(evt) {
  evt.preventDefault();

  const userAddress = document.querySelector('#location_field').value;
  const geocoder = new google.maps.Geocoder();
  geocoder.geocode({ address: userAddress }, (results, status) => {
    if (status === 'OK') {
      const lat =results[0].geometry.location.lat();      
      const lng =results[0].geometry.location.lng();
      
    const data= {
        name:document.querySelector('#name_field').value,
        animal_type:document.querySelector('#animal_type_field').value,
        pet_type:document.querySelector('#pet_type_field').value, 
        gender:document.querySelector('#gender_field').value,  
        breed:document.querySelector('#breed_field').value, 
        color:document.querySelector('#color_field').value, 
        location:document.querySelector('#location_field').value, 
        date:document.querySelector('#date_field').value, 
        lat, 
        lng,
      }
      sendGeocodinfo(data);

    }});
};

document.querySelector('#pet_reg_field').addEventListener('submit', registerPet);
