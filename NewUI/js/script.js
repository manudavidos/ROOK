function showpopup(popupname) {
    document.getElementById("unavailable").style = "display:inline";
    document.getElementById("popups").style = "display:flex";
    document.getElementById(popupname).style = "display:flex";
    document.getElementById("unavailable").setAttribute( "onClick", `closepopup('${popupname}')` );
}

function closepopup(popupname) {
    document.getElementById("popups").style = "display:none";
    document.getElementById(popupname).style = "display:none";
    document.getElementById("unavailable").style = "display:none";
    document.getElementById("unavailable").setAttribute( "onClick", "" );
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