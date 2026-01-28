function register(){
    //save personal info to constats when "register" button is clicked
    const name = document.getElementById ( "name" ).value;
    const email = document.getElementById ( "email" ).value;
    const password = document.getElementById ( "password" ).value;
    const phone_number = document.getElementById ( "phone_number" ).value;
    //check if the person has entered all the info that is needed
    switch ( true ){
        case name == null:
            window.alert ( "type in your name" );
            break;
        case email == null:
            window.alert ( "type in your Email" );
            break;
        case password == null:
            window.alert ( "type in a Password" );
            break;
        default:
            window.alert ( `You are registered` );
            document.title = "Starting page";
            location="/recepti"
    }
}