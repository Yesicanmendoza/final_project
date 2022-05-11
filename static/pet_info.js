
function registerPet(evt) {
  evt.preventDefault();
   
  const url = '/pet_registration.json';
  const data= {
      name:document.querySelector('#name_field').value,
      animal_type:document.querySelector('#animal_type_field').value,
      pet_type_field:document.querySelector('#pet_type_field').value, 
      gender:document.querySelector('#gender_field').value,  
      breed:document.querySelector('#breed_field').value, 
      color:document.querySelector('#color_field').value, 
      zip_code:document.querySelector('#zip_code_field').value, 
      date:document.querySelector('#date_field').value, 
    }
     
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

document.querySelector('#pet_reg_field').addEventListener('submit', registerPet);