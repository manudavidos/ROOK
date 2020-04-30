function showloginbox() {
    document.getElementById("unavailable").style = "display:inline";
    document.getElementById("popups").style = "display:flex";
    document.getElementById("loginbox").style = "display:flex";
    document.getElementById("unavailable").setAttribute( "onClick", "closeloginbox()" );
}

function closeloginbox() {
    document.getElementById("popups").style = "display:none";
    document.getElementById("loginbox").style = "display:none";
    document.getElementById("unavailable").style = "display:none";
    document.getElementById("unavailable").setAttribute( "onClick", "" );
    document.getElementById("loginboxtitle").innerHTML = "Login";
}

function gototheroom() {
    document.getElementById("roominfo").style = "display:inline";
}

function validateeduauaEmail(email) 
    {
        var re = /\S+@edu.aua.am/;
        return re.test(email);
    }

function validateauaEmail(email) 
    {
        var re = /\S+@aua.am/;
        return re.test(email);
    }
    
function login() {
    var useremail = document.getElementById("useremail").value;
    console.log(validateauaEmail(useremail));
}