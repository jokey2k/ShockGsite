/* Handler to ajaxify shoutbox posting */
function attachShoutboxHandler() {
    /* attach a submit handler to the form */
    $("form#shoutboxform").submit(function(event) {

      /* stop form from submitting normally */
      event.preventDefault();

      /* get some values from elements on the page: */
      var $form = $( this ),
        nickname = $form.find( 'input[name="nickname"]' ).val(),
        hint = $form.find( 'input[name="hint"]' ).val(),
        message = $form.find( 'textarea[name="message"]' ).val(),

        url = $form.attr( 'action' );

      /* Send the data using post and put the results in a div */
      $.post( url, { nickname: nickname, hint:hint, message:message  },
        function( data ) {
            var content = $( data )[0];
            $("div#shoutboxpost").replaceWith(content);
            refreshShoutBox();
            attachShoutboxHandler();
            scroll(0, $("div#shoutbox").offset().top);
        }
      );
    });

    //capture the return key
    $("form#shoutboxform").bind("keydown", function(event) {
        if (event.keyCode == 13) {
            $('form#shoutboxform').ajaxSubmit(options);
            return false; //prevent default behaviour
        }
    });
};

function refreshShoutBox() {
    $.get('/shoutbox/recents', function(data) {
        var content = $( data )[0];
        $("div#shoutbox").replaceWith(content);
    });
}

$(document).ready(function () {
    attachShoutboxHandler();
})