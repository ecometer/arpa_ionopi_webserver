$( document ).ready(function() {

    resetForm();
    checkStatus();

    // nasconde la parte di Digital Output
    $("#digOut").hide();

    // run status every 30 seconds
    setInterval(resetForm, 5000);
    setInterval(checkStatus, 5000);

    // get iono status
    $("#status").click(function(e) {

        resetForm();
        checkStatus();

        e.preventDefault();
    });

    $(".btn-mylight button").click(function(e) {

        var id = $(this).attr('id');
        console.log(id);
        var el = id.substr(id.length - 1);
        console.log(el);

        $("#light-"+el).toggleClass("light-on light-off");
        var txt = $("#light-"+el+" p").text();
        if (txt == "On"){
            $("#light-"+el+" p").text("Off");
        }else{
            $("#light-"+el+" p").text("On");
        }

        e.preventDefault();
    });


});

function resetForm() {
    $(".clear-txt").val('');
    $(".clear-txt").prop("disabled", true);

    // TOGGLE: https://gitbrent.github.io/bootstrap4-toggle/

    /*$('.bt-toggle').bootstrapToggle('enable');
    $('.bt-toggle').bootstrapToggle('off');
    $('.bt-toggle').bootstrapToggle('disable');*/

    $('.change-light').removeClass('light-off light-on');
    $('.change-light').addClass('light-off');
    $('.change-light p').text("Off");
}
// check status
function checkStatus() {
    console.log("checkStatus");

    // command
    $.ajax({
        type: 'POST',
        url: 'get_status',
        contentType: "application/json",
        dataType: "json",
        success: function(res) {
            console.dir(res);

            $('.bt-toggle').bootstrapToggle('enable');
            var di = res.digitalin;
            if(di.di1 == 1){
                $('#D1').bootstrapToggle('on');
            }else{
                $('#D1').bootstrapToggle('off');
            }
            if(di.di2 == 1){
                $('#D2').bootstrapToggle('on');
            }else{
                $('#D2').bootstrapToggle('off');
            }
            if(di.di3 == 1){
                $('#D3').bootstrapToggle('on');
            }else{
                $('#D3').bootstrapToggle('off');
            }
            if(di.di4 == 1){
                $('#D4').bootstrapToggle('on');
            }else{
                $('#D4').bootstrapToggle('off');
            }
            if(di.di5 == 1){
                $('#D5').bootstrapToggle('on');
            }else{
                $('#D5').bootstrapToggle('off');
            }
            if(di.di6 == 1){
                $('#D6').bootstrapToggle('on');
            }else{
                $('#D6').bootstrapToggle('off');
            }
            $('.bt-toggle').bootstrapToggle('disable');

            var analog = res.analog;
            $("#A1").val(analog.a1);
            $("#A2").val(analog.a2);

            var wire = res.wire;
            $("#W1").val(wire.w1);

            var dout = res.digitalout;
            if(dout.do1 == 1){
                $('#light-a').toggleClass("light-on light-off");
                $("#light-a p").text("On");
            }
            if(dout.do2 == 1){
                $('#light-b').toggleClass("light-on light-off");
                $("#light-b p").text("On");
            }
            if(dout.do3 == 1){
                $('#light-c').toggleClass("light-on light-off");
                $("#light-c p").text("On");
            }
            if(dout.do4 == 1){
                $('#light-d').toggleClass("light-on light-off");
                $("#light-d p").text("On");
            }
        },
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            console.log('An error occurred... Look at the console (F12 or Ctrl+Shift+I, Console tab) for more information!');
        },
    });
};