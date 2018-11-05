
$("#contact-form").submit(function(){
    var csrftoken = ($"[name=csrfmiddlewaretoken]").val();
    alert("imin");
    $.ajax({
        url : $(this).attr("data-validate-username-url"), // the endpoint
        type : "POST", // http method
        data : {$(this).serialize(), 'csrfmiddlewaretoken':{% csrf_token%} }, // data sent with the post request

        // handle a successful response
        success : function(json) {
            console.log(json); // log the returned json to the console
            console.log("success"); // another sanity check
        },
        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
});
