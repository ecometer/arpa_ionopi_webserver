$( document ).ready(function() {

    resetLog();
    checkLog();

    // run status every 30 seconds
    setInterval(checkLog, 30000);

    // get iono status
    $("#log").click(function(e) {

        resetLog();
        checkLog();

        e.preventDefault();
    });

});

function resetLog() {
    // $(".clear-txt").val('');
    // $(".clear-txt").prop("disabled", true);

    $("#all-log").html('');
}
// check status
function checkLog() {
    console.log("checkLog");

    // command
    $.ajax({
        type: 'POST',
        url: 'get_log',
        contentType: "application/json",
        dataType: "json",
        success: function(res) {
            console.dir(res);

            $("#all-log").html(res.data);

        },
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            console.log('An error occurred... Look at the console (F12 or Ctrl+Shift+I, Console tab) for more information!');
        },
    });
};