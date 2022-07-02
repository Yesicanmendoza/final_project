
function sendGeocodInfo(data){
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

      document.querySelector('.msg').innerHTML=jsonData.msg;   
          
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


fetch("/show_reg_form")
  .then(response => response.json())
  .then(jsonData=> {
    const msg=jsonData.msg;
    if (msg==='Please log in.'){
      document.querySelector('.login_msg').innerHTML = msg;
      document.querySelector('.reg_form_title').style.display = "none";
      document.querySelector('.register_pet_form').style.display = "none";
      //document.querySelector('#register_pet').style.display = "none"; 
      //document.querySelector('#register_pet_2').style.display = "none";    
    }
  });


function registerPet(evt) {
evt.preventDefault();
const location = document.querySelector('#location_field').value;
const data= {
  name:document.querySelector('#name_field').value,
  animal_type:document.querySelector('#animal_type_field').value,
  pet_type:document.querySelector('#pet_type_field').value, 
  gender:document.querySelector('#gender_field').value,  
  breed:document.querySelector('#breed_field').value, 
  color:document.querySelector('#color_field').value,  
  date:document.querySelector('#date_field').value, 
  location,
};
console.log(data);
const geocoder = new google.maps.Geocoder();
geocoder.geocode({ address: location }, (results, status) => {
  if (status === 'OK') {
      data['lat']=results[0].geometry.location.lat();      
      data['lng']=results[0].geometry.location.lng();
    }else{
      data['lat'] = '';
      data['lng']= '';    
    }  
  sendGeocodInfo(data);  
  }); 
};

document.querySelector('#pet_reg_field form').addEventListener('submit', registerPet);



//fetch("/show_reg_form_2")
 // .then(response => response.json())
  //.then(jsonData=> {
   // const new_pet_id=jsonData.new_pet_id;
   // if (new_pet_id != null){    
   //   document.querySelector('#register_pet_2').style.display = "block";
   //}
  //});