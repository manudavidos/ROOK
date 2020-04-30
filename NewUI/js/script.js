if (localStorage.getItem("data") === null) {
    localStorage.setItem('data', JSON.stringify(datajson))
  }
var data = JSON.parse(localStorage.getItem('data'));

//data.status.available.name = "Example";
//localStorage.setItem('data', JSON.stringify(data))
//console.log(data.status.available.name)

function showerror(errormessage){
    document.getElementById("errormessagebox").style = "display:flex; height:32px;";
    setTimeout(function(){ document.getElementById("errormessagebox").style = "display:flex; height:80px;"; }, 50);
    document.getElementById("errormessagebox-content").innerHTML = errormessage;
    setTimeout(function(){ document.getElementById("errormessagebox").style = "display:flex; height:32px;"; }, 3000);
    setTimeout(function(){ document.getElementById("errormessagebox-content").innerHTML = ""; document.getElementById("errormessagebox").style = "display:flex; height:0px;"; }, 3050);
    setTimeout(function(){ document.getElementById("errormessagebox").style = "display:none;"; }, 3400);
}

function showpopup(popupname) {
    document.getElementById("unavailable").style = "display:flex";
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

function resetall() {
    document.getElementById("roominfo").style = "display:none";
    document.getElementById("roomlist").style = "display:none";
    document.getElementById("popups").style = "display:none";
    document.getElementById("unavailable").style = "display:none";
}

function findtheroom() {
    document.getElementById("roominfo").style = "display:none";
    document.getElementById("roomlist").style = "display:none";
    document.getElementById("userroomnumber").style ="";
    var userroomnumber = document.getElementById("userroomnumber").value;
    if (data['rooms'][userroomnumber] != null){
        document.getElementById("roominfo").style = "display:inline";
        document.getElementById("roominfo").innerHTML += "<h1>" + data["rooms"][userroomnumber]["room_code"] +"</h1>";
    } else {
        showerror("Error: We could not find room with these details");
    }
}
    
function login() {
    var useremail = document.getElementById("useremail").value;
    if (data['users'][useremail] != null){
        closepopup("loginbox");
        document.getElementById("homeloginbutton").style = "display:none";
        localStorage.setItem('currentuser', useremail)
        currentuser = localStorage.getItem("currentuser");
        document.getElementById("userprofilefname").innerHTML = data['users'][currentuser]['first_name'];
        document.getElementById("userprofilelname").innerHTML = data['users'][currentuser]['last_name'];
        document.getElementById("userprofileemail").innerHTML = data['users'][currentuser]['email'];
        document.getElementById("userprofiledetails").style = "display:block";
    } else {
        showerror("Error: No AUA Student with such credentials!");
    }
}

function logout() {
    if (localStorage.getItem("currentuser") != null) {
        localStorage.removeItem("currentuser");
        document.getElementById("userprofiledetails").style = "display:none";
        document.getElementById("userprofilefname").innerHTML = "";
        document.getElementById("userprofilelname").innerHTML = "";
        document.getElementById("userprofileemail").innerHTML = "";
        document.getElementById("homeloginbutton").style = "display:block";
    }
}

function allroomscount() {
    var allroomscount = Object.keys(data.rooms).length;
    document.getElementById("allroomscount").innerHTML = allroomscount;
}

function checkpreviouslogin() {
    if (localStorage.getItem("currentuser") != null) {
        currentuser = localStorage.getItem("currentuser");
        document.getElementById("homeloginbutton").style = "display:none";
        document.getElementById("userprofilefname").innerHTML = data['users'][currentuser]['first_name'];
        document.getElementById("userprofilelname").innerHTML = data['users'][currentuser]['last_name'];
        document.getElementById("userprofileemail").innerHTML = data['users'][currentuser]['email'];
        document.getElementById("userprofiledetails").style = "display:block";
      }
}


function loading(){
    checkpreviouslogin();
    allroomscount();
}

window.onload = loading;