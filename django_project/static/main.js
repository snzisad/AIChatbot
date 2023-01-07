$token = "";

function setUserInterface($message){
    var interface = `
        <div class="d-flex flex-row-reverse">
            <img style="margin-right: 10px;" src="/static/user.png" width="30" height="30">
            <div class="bg-white mr-2 p-3"><span class="text-muted">`+$message+`</span></div>
        </div>
    `;
    $(".Content").append(interface);

    var d = $('.Content');
    d.scrollTop(d.prop("scrollHeight"));
}


function setResponseInterface($response){
    var interface = `
        <div class="d-flex flex-row p-3">
            <img src="/static/ai.webp" width="30" height="30">
            <div class="chat ml-2 p-3">`+$response+`</div>
        </div>
    `;
    $(".Content").append(interface);
    
    var d = $('.Content');
    d.scrollTop(d.prop("scrollHeight"));
}

function getResponse($message){
    $.post( "/api/message", 
        { 
            token: $token, 
            message: $message 
        })
        .done(function( data ) {
            $token = data.token;
            $response = data.response;
            setResponseInterface($response);
        }
    );
}

$( document ).ready(function() {
    $("#message_box").on('keypress',function(e) {
        if(e.which == 13) {
            var message = $(this).val();
            $(this).val("");
            setUserInterface(message);
            getResponse(message);
        }
    });

    getResponse("Hi");

});