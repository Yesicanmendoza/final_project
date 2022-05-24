
url='/lost_pet/<pet_id>/'
fetch('url')
  .then(response => response.json())
  .then(Data => {
    msg=Data.msg;
    match_pet_list=Data.match_pet_list;
    document.querySelector('#message').innerHTML = Data.msg;
  });