
var buttonInput = $("#button-input");
var inputForm = $("#action-input");

$(document).ready(function($) {
    
    buttonInput.on("click", function (e) {
    e.preventDefault();
    $.ajax({
            url: 'hello/modify',
            type: 'GET',
            data: {
                data: inputForm.val()
            },
            dataType: 'json',
            success: function (data) {
                document.getElementById("response-area").value = data.modifyData;
            }
        });
    });
    
    
});

