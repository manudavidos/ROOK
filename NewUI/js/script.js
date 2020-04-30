if (localStorage.getItem("data") === null) {
    localStorage.setItem('data', JSON.stringify(datajson))
  }
var data = JSON.parse(localStorage.getItem('data'));

//data.status.available.name = "Example";
//localStorage.setItem('data', JSON.stringify(data))
//console.log(data.status.available.name)

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
    
function login() {
    var useremail = document.getElementById("useremail").value;
    if (data['users'][useremail] != null){
        console.log(data['users'][useremail]['first_name'])
    }
}