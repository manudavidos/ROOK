if (localStorage.getItem("data") === null) {
    localStorage.setItem('data', JSON.stringify(datajson))
  }
var data = JSON.parse(localStorage.getItem('data'));

//data.status.available.name = "Example";
//localStorage.setItem('data', JSON.stringify(data))
//console.log(data.status.available.name)

function shownotification(notificationmessage, notificationcolor){
    document.getElementById("notificationmessagebox").style = `display:flex; height:32px; background-color:${notificationcolor};`;
    setTimeout(function(){ document.getElementById("notificationmessagebox").style = `display:flex; height:80px; background-color:${notificationcolor};`; }, 50);
    document.getElementById("notificationmessagebox-content").innerHTML = notificationmessage;
    setTimeout(function(){ document.getElementById("notificationmessagebox").style = `display:flex; height:32px; background-color:${notificationcolor}`; }, 3000);
    setTimeout(function(){ document.getElementById("notificationmessagebox-content").innerHTML = ""; document.getElementById("notificationmessagebox").style = `display:flex; height:0px; background-color:${notificationcolor};`; }, 3050);
    setTimeout(function(){ document.getElementById("notificationmessagebox").style = `display:none; background-color:${notificationcolor}`; }, 3400);
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
    location.reload();
}

function removefromarray(arrayname, valuetoremove){
    for( var i = 0; i < (arrayname).length; i++){
         if ( arrayname[i] == valuetoremove) { 
            arrayname = (arrayname).splice(i, 1);
        }
    }
}

function bookroom(roomcode){
    if (localStorage.getItem("currentuser") != null){
        if ((data['rooms'][roomcode] != null) && (JSON.stringify(data['rooms'][roomcode]['room_status']) === JSON.stringify(data['status']['available']) && Number(data['rooms'][roomcode]['room_occupied_seats']) < Number(data['rooms'][roomcode]['room_capacity']))){
            closepopup("bookroombox");
            data['rooms'][roomcode]['room_occupied_seats'] += 1;
            (data['rooms'][roomcode]['room_booked_by']).push(localStorage.getItem("currentuser"));
            localStorage.setItem('data', JSON.stringify(data));
            loadroomdetails(roomcode); //refresh room details
            shownotification(`Success: You have booked ${roomcode}`,"#6ada0eb0");
        }
    } else {
            shownotification("Please login before booking rooms","#292d38cc")
            closepopup("bookroombox");
            showpopup("loginbox");
        }
    }

function unbookroom(roomcode){
    var bookedby = data['rooms'][roomcode]['room_booked_by'];
    var currentuser = localStorage.getItem("currentuser");
    removefromarray(bookedby, currentuser);
    data['rooms'][roomcode]['room_occupied_seats'] -= 1;
    localStorage.setItem('data', JSON.stringify(data));
    loadroomdetails(roomcode); //refresh room details
}

function bookroomq(roomcode){
    document.getElementById("bookroombox-roomcode").innerHTML = roomcode;
    document.getElementById("decline-booking-btn").setAttribute( "onClick", `closepopup("bookroombox")` );
    document.getElementById("accept-booking-btn").setAttribute( "onClick", `bookroom('${roomcode}')` );
    showpopup("bookroombox");
}

function loadroomdetails() {
    document.getElementById("roominfo").style = "display:none";
    document.getElementById("roomlist").style = "display:none";
    document.getElementById("userroomnumber").style ="";
    var userroomnumber = (document.getElementById("userroomnumber").value).toUpperCase();
    if (userroomnumber == ""){
        shownotification("Error: Please enter the room number", "#292d38cc");
    }else if (data['rooms'][userroomnumber] != null){
        document.getElementById("roominfo").style = "display:block";
        document.getElementById("roominfo-roomcode").innerHTML = data["rooms"][userroomnumber]["room_code"];
        document.getElementById("roominfo-roomlocation").innerHTML = data["rooms"][userroomnumber]["room_location"]["name"]
        document.getElementById("roominfo-roomoccupiedseats").innerHTML = data["rooms"][userroomnumber]["room_occupied_seats"]
        document.getElementById("roominfo-roomcapacity").innerHTML = data["rooms"][userroomnumber]["room_capacity"]
        document.getElementById("roominfo-roombookedby").innerHTML = data["rooms"][userroomnumber]["room_booked_by"]
        document.getElementById("roominfo-status").innerHTML = data["rooms"][userroomnumber]["room_status"]["name"]
        document.getElementById("roombookbutton").setAttribute( "onClick", `bookroomq('${userroomnumber}')` );
    } else {
        shownotification("Error: We could not find room with these details", "#ff6347a8");
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
    
function handleenter(e, functionname){
    if(e.keyCode == 13){
        eval(functionname);
    }
}

function login() {
    var useremail = (document.getElementById("useremail").value).toLowerCase();
    if (useremail == ""){
        shownotification("Error: Please enter your email", "#292d38cc");
    }else if (useremail != "" && validateeduauaEmail(useremail) == false && validateauaEmail(useremail) == false){
        shownotification("Error: Please enter valid AUA email", "#292d38cc");
    }else if (data['users'][useremail] != null){
        closepopup("loginbox");
        document.getElementById("homeloginbutton").style = "display:none";
        localStorage.setItem('currentuser', useremail)
        currentuser = localStorage.getItem("currentuser");
        document.getElementById("userprofilefname").innerHTML = data['users'][currentuser]['first_name'];
        document.getElementById("userprofilelname").innerHTML = data['users'][currentuser]['last_name'];
        document.getElementById("userprofileemail").innerHTML = data['users'][currentuser]['email'];
        document.getElementById("userprofiledetails").style = "display:block";
        document.getElementById("useremail").value = "";
    } else {
        shownotification("Error: No AUA Student with such credentials!", "#ff6347a8");
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