function login(){
    //save personal info to constats when "register" button is clicked
    const email = document.getElementById ( "email" ).value;
    const password = document.getElementById ( "password" ).value;
    //check if the person has entered all the info that is needed
    switch ( true ){
        case email == null:
            window.alert ( "type in your Email" );
            break;
        case password == null:
            window.alert ( "type in a Password" );
            break;
        default:
            window.alert ( `You are loged in` );
            document.title = "Starting page";
            location="/recepti"
    }
}
