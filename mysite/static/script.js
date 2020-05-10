setTimeout(function(){
    $(".loading").fadeOut();    
}, 1000)
$(document).ready(function(){
    $('.sidenav').sidenav();
    radioBtnDefault = document.getElementById("radiobutton1");
    radioBtnDefault.checked = true

    $("#radiobutton1").click( function () {
        $("body").css({"background-color": "white"});
        $("nav").css({"background-color": "#ee6e73"});
        $(".navicon>a").css({"color": "darkslategrey"});
        $("span").css({"color": "darkslategrey"});

    });
    $("#radiobutton2").click( function () {
        $("body").css({"background-color": "darksalmon"});
        $("nav").css({"background-color": "darkslategrey"});
        $(".navicon>a").css({"color": "#ee6e73"});
        $("span").css({"color": "#ee6e73"});

    });
    
    $('a').click(function(){
        $('html, body').animate({
            scrollTop: $( $(this).attr('href')).offset().top
        },1000);
        return false;
    })

    //Object containing image URLs
    const IMAGE_URLS = {
        mountainAndRiver: 'https://images.pexels.com/photos/206660/pexels-photo-206660.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260',
        work: 'https://images.pexels.com/photos/796602/pexels-photo-796602.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260',
        aboutMe: 'https://images.pexels.com/photos/399160/pexels-photo-399160.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260',
    };
    //Set background image for home section 
    var homeSection = document.getElementById("homeSection");
    const setHomeBackground = (image) => {
        // document.window.style.backgroundImage = "url('"+IMAGE_URLS[image]+"')";
        homeSection.style.backgroundImage = "url('"+IMAGE_URLS[image]+"')";
    };
    var aboutMeSection = document.getElementById("aboutMeSection");
    const setAboutMeBackground = (image) => {
        aboutMeSection.style.backgroundImage = "url('"+IMAGE_URLS[image]+"')";
    }
    // Check time of the day
    var now = new Date();
    if (window.location.pathname == '/') {
        setAboutMeBackground('aboutMe');
        if ((now.getHours() >= 9) && (now.getHours() <= 17 && now.getMinutes() <=30) ) {
            setHomeBackground('mountainAndRiver');
        } else {
            setHomeBackground('work');
        }
    }
    
        
    window.addEventListener('scroll', function(e) {
        let offset = window.pageYOffset;
        homeSection.style.backgroundPositionY = -offset*0.5 + "px";
        aboutMeSection.style.backgroundPositionY = -offset*0.17 + "px";

    }) 
        
    $(".btn").mouseup(function(){
        $(this).blur();
    })

    

    var acc = document.getElementsByClassName("accordion");
    var i;

    for (i = 0; i < acc.length; i++) {
        acc[i].addEventListener("click", function() {
            this.classList.toggle("active");
            var panel = this.nextElementSibling;
            if (panel.style.display === "block") {
                panel.style.display = "none";
            } else {
                panel.style.display = "block";
            }
        });
    }

    
    

    $("#searchbox-form").submit(function() {
        console.log("xxx")
        event.preventDefault();
        $.ajax({
            url: "https://www.googleapis.com/books/v1/volumes?q=" + $("#searchbox").val(),
            success: function(result){
                console.log(result.items[0].volumeInfo.title);
                $("tbody").empty();
                for(var x=0; x<result.items.length; x++){
                    $("tbody").append(
                        '<tr>\
                            <th scope="row">'+ (x+1) +'</th>\
                            <td><img src="' +result.items[x].volumeInfo.imageLinks.thumbnail + '"></td>\
                            <td>'+ result.items[x].volumeInfo.title + '</td>\
                            <td>' + result.items[x].volumeInfo.authors + '</td>\
                            <td>'+ result.items[x].volumeInfo.publisher +'</td>\
                            <td><span id="fav-button" "><i class="material-icons">star\
                            </i></span></td>\
                        </tr>'  
                    );  
                    
                }
                window.history.replaceState("", "", "?q=" + $("#searchbox").val());
                
            }  

        })        
    })   
    var counter = 0;
    $(document).on("click", "#fav-button", function() {
        if($(event.target).hasClass("fav-active")){
            counter--;
            $(this).css("color", "#222");
        }else{
            counter++;        
            $(this).css("color", "yellow");

        }
        $(event.target).toggleClass("fav-active");
        console.log("TEST");
        console.log(counter);
        $("#counter").html(counter);

    })   

    $(document).on("hover", "#fav-button", function(){
        $(this).css("background-color", "yellow");
    });        
        

    $.ajax({
        url: "https://www.googleapis.com/books/v1/volumes?q=quilting",
        success: function(result){
            console.log(result.items[0].volumeInfo.title);
            for(var x=0; x<result.items.length; x++){
                $("tbody").append(
                    '<tr>\
                        <th scope="row">'+ (x+1) +'</th>\
                        <td><img src="' +result.items[x].volumeInfo.imageLinks.thumbnail + '"></td>\
                        <td>'+ result.items[x].volumeInfo.title + '</td>\
                        <td>' + result.items[x].volumeInfo.authors + '</td>\
                        <td>'+ result.items[x].volumeInfo.publisher +'</td>\
                        <td><span id="fav-button" "><i class="material-icons">star\
                        </i></span></td>\
                    </tr>'  
                );  
                
            }
        }
        

    })

    function csrftokenSafeMethod(method){ return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method)); }

 
        

    function validateEmail(email){
        var emailregex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
            return emailregex.test(email);
    }

    function isValid(){
        if(($("#email").val()==null || $("#email").val()=="") ||
        ($("#password").val()==null || $("#password").val()=="") ||
        ($("#firstname").val()==null || $("#firstname").val()=="") ||
        ($("#lastname").val()==null || $("#lastname").val()=="")){
            return false;
        }

        return true;
        
    }


    $("#email").keyup(function(){
        email = $(this).val();
        console.log("HIII KEY UP WORKS")
        $.ajax({
            method: "POST",
            url:'/ppw_app/emailValidation/',
            data: {
                'email' : email
            },
            dataType: 'json',
            success: function(data){
                if(validateEmail(email)==false){
                    $("#email").css("color", "red");
                    valid = false;
                }
                else if(data.isExist){
                    console.log("ALREADY EXISTS")
                    alert("Email already exists");
                    $("#email").css("color", "red");
                    valid = false;
                }
                else{
                    if(validateEmail){
                        console.log("EMAIL IS RIGHT")
                        $("#email").css("color", "green");
                        valid = true;
                    }
                }
            }
        })


    })

    $("#regisform").submit(function(){
    	event.preventDefault();			// prevents default submit action
        firstname = $("#firstname").val();
        lastname = $("#lastname").val();
        email = $("#email").val();
        password = $("#password").val();
        csrftoken = $('input[name="csrfmiddlewaretoken"]').val();	// get csrf token value
        $.ajax({		// check email again before submitting form
            method: "POST",
            url:'/ppw_app/emailValidation/',
            data: {
                'email' : email
            },
            dataType: 'json',
            success: function(data){
                if(validateEmail(email)==false){
                    // $("#submitbutton").attr('disabled', 'disabled');
                    $("#email").css("color", "red");
                    valid = false;
                }
                else if(data.isExist){
                    console.log("ALREADY EXISTS")
                    alert("Email already exists");
                    $("#email").css("color", "red");
                    // $("#submitbutton").attr('disabled', 'disabled');
                    valid = false;
                }
                else{
                    if(validateEmail){
                        console.log("EMAIL IS RIGHT")
                        $("#email").css("color", "green");
                        valid = true;
                    	$.ajax({		// email OK, submit form
							method: "POST",
							url: '/ppw_app/runForm/',
							data:{
								'firstname' : firstname,
								'lastname' : lastname,
								'email' : lastname,
								'password' : password
							},
							beforeSend: function(xhr, settings){ 	// include CSRF
								if(!csrftokenSafeMethod(settings.type) && !this.crossDomain){ 
									xhr.setRequestHeader("X-CSRFToken", csrftoken); 
								} 
							},
							dataType: 'json',
							success: function(data){
								// if(isValid() && valid){
                                console.log("whole form works")
								// }
                                $("#regisform :input").each(function(i, input){
                                    if($(input).attr("name") != "csrfmiddlewaretoken"){
                                        $(input).val("");
                                    }
                                })
							}
						})
                    }
                }
            }
        })
    })
   

})
 