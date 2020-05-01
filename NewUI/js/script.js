if (localStorage.getItem("data") === null) {
    localStorage.setItem('data', JSON.stringify(datajson))
  }
var data = JSON.parse(localStorage.getItem('data'));

//data.status.available.name = "Example";
//localStorage.setItem('data', JSON.stringify(data))
//console.log(data.status.available.name)

function showerror(errormessage, errorcolor){
    document.getElementById("errormessagebox").style = `display:flex; height:32px; background-color:${errorcolor};`;
    setTimeout(function(){ document.getElementById("errormessagebox").style = `display:flex; height:80px; background-color:${errorcolor};`; }, 50);
    document.getElementById("errormessagebox-content").innerHTML = errormessage;
    setTimeout(function(){ document.getElementById("errormessagebox").style = `display:flex; height:32px; background-color:${errorcolor}`; }, 3000);
    setTimeout(function(){ document.getElementById("errormessagebox-content").innerHTML = ""; document.getElementById("errormessagebox").style = `display:flex; height:0px; background-color:${errorcolor};`; }, 3050);
    setTimeout(function(){ document.getElementById("errormessagebox").style = `display:none; background-color:${errorcolor}`; }, 3400);
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
    if (userroomnumber == ""){
        showerror("Error: Please enter the room number", "#292d38cc");
    }else if (data['rooms'][userroomnumber] != null){
        document.getElementById("roominfo").style = "display:block";
        document.getElementById("roominfo-roomcode").innerHTML = data["rooms"][userroomnumber]["room_code"];
        //data["rooms"][userroomnumber]["room_location"]["name"]
        //data["rooms"][userroomnumber]["room_occupied_seats"]
        //data["rooms"][userroomnumber]["room_capacity"]
        //data["rooms"][userroomnumber]["room_booked_by"]
        //data["rooms"][userroomnumber]["room_status"]["name"]
    } else {
        showerror("Error: We could not find room with these details", "#ff6347a8");
    }
}

function validateeduauaEmail(email) 
    {
        var eduauatest = /\S+@edu.aua.am/;
        return eduauatest.test(email);
    }

function validateauaEmail(email) 
    {
        var auatest = /\S+@aua.am/;
        return auatest.test(email);
    }
    
function login() {
    var useremail = document.getElementById("useremail").value;
    if (useremail == ""){
        showerror("Error: Please enter your email", "#292d38cc");
    }else if (useremail != "" && validateeduauaEmail(useremail) == false && validateauaEmail(useremail) == false){
        showerror("Error: Please enter valid AUA email", "#292d38cc");
    }else if (data['users'][useremail] != null){
        closepopup("loginbox");
        document.getElementById("homeloginbutton").style = "display:none";
        localStorage.setItem('currentuser', useremail)
        currentuser = localStorage.getItem("currentuser");
        document.getElementById("userprofilefname").innerHTML = data['users'][currentuser]['first_name'];
        document.getElementById("userprofilelname").innerHTML = data['users'][currentuser]['last_name'];
        document.getElementById("userprofileemail").innerHTML = data['users'][currentuser]['email'];
        document.getElementById("userprofiledetails").style = "display:block";
    } else {
        showerror("Error: No AUA Student with such credentials!", "#ff6347a8");
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
      } else {
        document.getElementById("homeloginbutton").style = "display:inline-block;";
      }
}


function loading(){
    checkpreviouslogin();
    allroomscount();
}

window.onload = loading;