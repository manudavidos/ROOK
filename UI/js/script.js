function showloginbox() {
    document.getElementById("unavailable").style = "display:inline";
    document.getElementById("loginbox").style = "display:block";
    document.getElementById("unavailable").setAttribute( "onClick", "closeloginbox()" );
}

function closeloginbox() {
    document.getElementById("loginbox").style = "display:none";
    document.getElementById("unavailable").style = "display:none";
    document.getElementById("unavailable").setAttribute( "onClick", "" );
    document.getElementById("loginboxtitle").innerHTML = "Login";
}

function gototheroom() {
    document.getElementById("roominfo").style = "display:inline";
}

function login() {
    document.getElementById("loginboxtitle").innerHTML = "Sorry this feature is not ready yet";
}