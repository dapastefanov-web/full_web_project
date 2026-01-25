function register(){
    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    const phone_number = document.getElementById("phone_number").value;
    if (name === ""){
        alert("type in your name");
    }
    else if (email === ""){
        alert("type in your Email");
    }
    else if (password === ""){
        alert("type in a Password");
    }
    else{
    alert("You are registered "+ name);
    document.title = "Starting page";
    document.getElementById("registration_page").style.display = "none";
    recepti();  
    }
}
async function recepti(){
    const res = await fetch('/api.json');
    const json = await res.json();
    const recepti = json.recepti;
    let html = "";
    recepti.forEach(function(recepta){
        html += `<li>
        <h1> ${recepta.title} </h1>
        <h3>sastavki:</h3>
        <ul>`;
        recepta.sastavki.forEach(function(sastavka){
            html += `<li> ${sastavka} </li>`
        });
        html += '</ul></li>'
    });
    document.getElementById("registration_page").style.display = "none";
    document.getElementById("recepti").innerHTML = `<ul>${html}</ul>`;
}
recepti();