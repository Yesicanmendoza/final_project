
const firstData=document.querySelectorAll(".gridResult"); 
const dataBase = [];
for(const item of firstData){    
    dataBase.push(item.childNodes)}; 
    //console.log(dataBase);

const i = 9;

for (const pet of dataBase){
    const name = pet[i];
    console.log(name);
    };


const list_index= [3, 9, 13 ..37];
