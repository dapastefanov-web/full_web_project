function register(){
    //save personal info to constats when "register" button is clicked
    const name = document.getElementById ( "name" ).value;
    const email = document.getElementById ( "email" ).value;
    const password = document.getElementById ( "password" ).value;
    const phone_number = document.getElementById ( "phone_number" ).value;
    //check if the person has entered all the info that is needed
    switch ( true ){
        case name == null:
            alert ( "type in your name" );
            break;
        case email == null:
            alert ( "type in your Email" );
            break;
        case password == null:
            alert ( "type in a Password" );
            break;
        default:
            alert ( `You are registered ${ name }` );
            document.title = "Starting page";
            show_recipes();
    }
}
async function show_recipes(){
    //remove the registration page
    document.getElementById( "registration_page" ).style.display = "none";
    //fetch recipes from json file
    const response = await fetch ( "/api.json" );
    const json = await response.json();
    const recipes = json.recipes;
    let html = "";
    //put every recipe title with it's ingrediants in an html variable as list elements
    recipes.forEach ( function ( recipe ){
            html += `<h1> ${ recipe.title } </h1>
                <h3> ingredients: </h3>`;
            recipe.ingredients.forEach ( function ( ingredient ){
                html += `<ul> <li> ${ ingredient } </li> </ul>`
        });
    });
    //puting the html variable in to the HTML as an unsorted list
    document.getElementById ( "recipes" ).innerHTML = `<ul> ${ html } </ul>`;
}
//uncomment the next line to skip the registration page while testing
//show_recipes()