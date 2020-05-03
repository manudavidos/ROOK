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
        var currentuser = localStorage.getItem("currentuser");
        if ((data['rooms'][roomcode] != null) && ((JSON.stringify(data['rooms'][roomcode]['room_status']) === JSON.stringify(data['status']['available']) || JSON.stringify(data['rooms'][roomcode]['room_status']) === JSON.stringify(data['status']['other'])) && Number(data['rooms'][roomcode]['room_occupied_seats']) < Number(data['rooms'][roomcode]['room_capacity']))) {
            userhoursofreservation = Number(document.getElementById("bookroom-hoursofreservation").value);
            userbookingmemberscount = Number(document.getElementById("bookroom-membernumber").value);
            userbookingduration = Number(document.getElementById("bookroom-hoursofreservation").value);
            horarraylength = (data['hours_of_reservation']).length;
            if (data['users'][currentuser]['booked_room'] == ""){
                if (userhoursofreservation >= data['hours_of_reservation'][0] && userhoursofreservation <= data['hours_of_reservation'][horarraylength-1]){
                    if (userbookingmemberscount >= 1 && userbookingmemberscount <= data['people_number']['maximum_number_per_group']){
                        if (((JSON.stringify(data['rooms'][roomcode]['room_status']) === JSON.stringify(data['status']['other'])) && (document.getElementById("bookroompassword").value == data['rooms'][roomcode]['room_password']))){
                            if (userbookingmemberscount <= (data['rooms'][roomcode]['room_capacity'] - data['rooms'][roomcode]['room_occupied_seats'])){
                                closepopup("bookroombox");
                                data['rooms'][roomcode]['room_occupied_seats'] += userbookingmemberscount;
                                data['users'][currentuser]['booked_for'] = userbookingmemberscount;
                                data['users'][currentuser]['booked_room'] = roomcode;
                                data['users'][currentuser]['booked_time'] = userbookingduration;
                                (data['rooms'][roomcode]['room_booked_by']).push(currentuser);
                                if (data['rooms'][roomcode]['room_capacity'] == data['rooms'][roomcode]['room_occupied_seats']){
                                    data['rooms'][roomcode]['room_status'] = data['status']['booked'];
                                }
                                document.getElementById("bookroompassword").value = "";
                                showbookedbutton();
                                allroomscount();
                                localStorage.setItem('data', JSON.stringify(data)); //write new data to localstorage
                                loadroomdetails(); //refresh room details
                                shownotification(`Success: You have booked ${roomcode}`,"#6ada0eb0");
                            } else{
                                shownotification(`There is not enough space for ${userbookingmemberscount} people`,"#292d38cc")
                            }
                        } else if ((JSON.stringify(data['rooms'][roomcode]['room_status']) === JSON.stringify(data['status']['available']))) {
                            if (userbookingmemberscount <= (data['rooms'][roomcode]['room_capacity'] - data['rooms'][roomcode]['room_occupied_seats'])){
                                closepopup("bookroombox");
                                data['rooms'][roomcode]['room_occupied_seats'] += userbookingmemberscount;
                                data['users'][currentuser]['booked_for'] = userbookingmemberscount;
                                data['users'][currentuser]['booked_room'] = roomcode;
                                data['users'][currentuser]['booked_time'] = userbookingduration;
                                (data['rooms'][roomcode]['room_booked_by']).push(currentuser);
                                if (data['rooms'][roomcode]['room_capacity'] == data['rooms'][roomcode]['room_occupied_seats']){
                                    data['rooms'][roomcode]['room_status'] = data['status']['booked'];
                                }
                                showbookedbutton();
                                allroomscount();
                                localStorage.setItem('data', JSON.stringify(data)); //write new data to localstorage
                                loadroomdetails(); //refresh room details
                                shownotification(`Success: You have booked ${roomcode}`,"#6ada0eb0");
                            } else{
                                shownotification(`There is not enough space for ${userbookingmemberscount} people`,"#292d38cc")
                            }
                        } else {
                            shownotification("Error: Wrong Password!", "#ff6347a8");
                        }
                    }else {
                        shownotification("Error: Internal Member Number Input Error, please contact us", "#ff6347a8");
                    }
                }else {
                    shownotification("Error: Internal Time Input Error, please contact us", "#ff6347a8");
                }
            } else {
                shownotification('You have already got a booked room',"#292d38cc");
            }
        } else {
            shownotification("Sorry the Room is not Available for Booking", "#292d38cc");
        }
    } else {
            shownotification("Please login before booking rooms","#292d38cc");
            closepopup("bookroombox");
            showpopup("loginbox");
        }
    }

function unbookroom(roomcode){
    if (localStorage.getItem("currentuser") != null) {
        var bookedby = data['rooms'][roomcode]['room_booked_by'];
        var currentuser = localStorage.getItem("currentuser");
        if (roomcode == data['users'][currentuser]['booked_room']) {
            removefromarray(bookedby, currentuser);
            data['rooms'][roomcode]['room_occupied_seats'] -= Number(data['users'][currentuser]['booked_for']);
            data['users'][currentuser]['booked_room'] = "";
            data['users'][currentuser]['booked_time'] = "";
            if (data['rooms'][roomcode]['room_capacity'] > data['rooms'][roomcode]['room_occupied_seats']){
                if (data['rooms'][roomcode]['room_password'] == ""){
                data['rooms'][roomcode]['room_status'] = data['status']['available'];
                } else {
                    data['rooms'][roomcode]['room_status'] = data['status']['other'];
                }
            }
            showbookedbutton();
            allroomscount();
            localStorage.setItem('data', JSON.stringify(data)); //write new data to localstorage
            loadroomdetails(); //refresh room details
        } else{
            shownotification("You Have Not Booked This Room!","#292d38cc");
        }
    } else {
        shownotification("Please login to see your booked room","#292d38cc");
        showpopup("loginbox");
    }
}

function bookroomq(roomcode){
    if (localStorage.getItem("currentuser") != null){
        if (data['users'][localStorage.getItem("currentuser")]['booked_room'] == ""){
            if ((data['rooms'][roomcode] != null) && ((JSON.stringify(data['rooms'][roomcode]['room_status']) === JSON.stringify(data['status']['available']) || JSON.stringify(data['rooms'][roomcode]['room_status']) === JSON.stringify(data['status']['other'])) && Number(data['rooms'][roomcode]['room_occupied_seats']) < Number(data['rooms'][roomcode]['room_capacity']))) {
                document.getElementById("bookroombox-roomcode").innerHTML = roomcode;
                document.getElementById("bookroom-hoursofreservation").innerHTML = "";
                if (JSON.stringify(data['rooms'][roomcode]['room_status']) === JSON.stringify(data['status']['other'])){
                    document.getElementById("bookroompassword").style = "display:block;";
                } else {
                    document.getElementById("bookroompassword").style = "display:none;";
                }
                for (i = 0; i < (data['hours_of_reservation']).length; i++) {
                    var timeoption = data['hours_of_reservation'][i];
                    var timeoptiontohours = ((data['hours_of_reservation'][i])/60);
                    var timeoptionhtml = `<option value="${timeoption}">${timeoptiontohours} hour(s)</option>`;
                    document.getElementById("bookroom-hoursofreservation").innerHTML += timeoptionhtml;
                  }
                  document.getElementById("bookroom-membernumber").innerHTML = "";
                  for (i = 1; i <= data['people_number']['maximum_number_per_group']; i++) {
                    if (i == 1){
                        memberhtml = "Only Me";
                    } else {
                        memberhtml = i + ' Members';
                    }
                    var memberoption = `<option value="${i}">${memberhtml}</option>`;
                    document.getElementById("bookroom-membernumber").innerHTML += memberoption;
                  }
                document.getElementById("decline-booking-btn").setAttribute( "onClick", `closepopup("bookroombox")` );
                document.getElementById("accept-booking-btn").setAttribute( "onClick", `bookroom('${roomcode}')` );
                showpopup("bookroombox");
            }else{
                shownotification("Sorry this Room is Fully Booked","#292d38cc")
            }
        }else{
            shownotification('You have already got a booked room',"#292d38cc")
        }
    } else {
            shownotification("Please login before booking rooms","#292d38cc")
            showpopup("loginbox");
    }
}

function loadroomdetails() {
    document.getElementById("roominfo").style = "display:none";
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
        document.getElementById("allroominfo").style ="display:none;";
        document.getElementById("goback-btn").style ="display:block;";
        document.getElementById("roomunbookbutton").style ="display:none;";
        document.getElementById("roombookbutton").style ="display:block;";
        if (localStorage.getItem("currentuser") != null){
            if (userroomnumber == (data['users'][localStorage.getItem("currentuser")]['booked_room'])){
                document.getElementById("roomunbookbutton").setAttribute( "onClick", `unbookroom('${userroomnumber}')` );
                document.getElementById("roombookbutton").style ="display:none;";
                document.getElementById("roomunbookbutton").style ="display:block;";
            }
        }
    } else {
        shownotification("Error: We could not find room with these details", "#ff6347a8");
    }
}

function loadallroominfo() {
    document.getElementById("roominfo").style = "display:none";
    document.getElementById("goback-btn").style ="display:none;";
    document.getElementById("allroominfo").style ="display:flex;";
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

function openroomtab(roomcode) {
    document.getElementById("userroomnumber").value = roomcode;
    loadroomdetails();
}

function showbookedbutton(){
    if (localStorage.getItem("currentuser") != null) {
        currentuser = localStorage.getItem("currentuser");
        if (data['users'][currentuser]['booked_room'] != ""){
            var mybookedroom = data['users'][currentuser]['booked_room'];
            document.getElementById("mybookedroom").innerHTML = `My Booked Room: ${mybookedroom}`;
            document.getElementById("mybookedroom").setAttribute( "onClick", `openroomtab('${mybookedroom}')` );
            document.getElementById("mybookedroom").style = "display: inline-block;";
        } else {
            document.getElementById("mybookedroom").style = "display:none";
            document.getElementById("mybookedroom").value = "";
            document.getElementById("mybookedroom").setAttribute( "onClick", "" );
        }
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
        showbookedbutton();
        allroomscount();
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
        showbookedbutton();
        allroomscount();
        resetall();
    }
}

function allroomscount() {
    var allroomscount = Object.keys(data['rooms']).length;
    var fullyoccupiedrooms = 0;
    for (i = 0; i < allroomscount; i++) {
        var roomcode = ((Object.keys(data['rooms']))[i]);
        if (JSON.stringify(data['rooms'][roomcode]['room_status']) === JSON.stringify(data['status']['booked'])){
            fullyoccupiedrooms += 1;
        }
      }
    document.getElementById("allroomsoccupied").innerHTML = fullyoccupiedrooms;
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
        showbookedbutton();
        allroomscount();
      } else {
        document.getElementById("homeloginbutton").style = "display:inline-block;";
      }
}

function loading(){
    checkpreviouslogin();
    allroomscount();
}

window.onload = loading;