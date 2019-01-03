

$(document).ready(function () {

  $('#tabs li').click(function () {
    var iddiv='tab'+this.id
    console.log(iddiv)
    $('.visible').attr('class','hidden');
    $('#'+iddiv).attr('class','visible');
  });

  $('#addptype').click( function() {
    //console.log('clicked')
    var va=$('#ptyp').val()
    $.ajax({
      type:'POST',
      url:'ptyp/crt',
      data:{
        ptype: va,
        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
      },
      success: function(){
        //alert('done');
        var el=1
        if($('#tbody1 tr:last-child td:first-child').length != 0) {
          el=parseInt($('#tbody1 tr:last-child td:first-child').html())+1
        }
        $('#tbody1').append(
          "<tr>\
            <td>"+el+"</td>\
            <td>"+va+"</td>\
           </tr>"
         )

      }
    });
  });

  $('#addotype').click( function() {
      //console.log('clicked')
      var va=$('#otyp').val()
      $.ajax({
        type:'POST',
        url:'otyp/crt',
        data:{
          otype: va,
          csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function(){
          //alert('done');
          var el=1
          if($('#tbody4 tr:last-child td:first-child').length != 0) {
            el=parseInt($('#tbody4 tr:last-child td:first-child').html())+1
          }
          $('#tbody4').append(
            "<tr>\
              <td>"+el+"</td>\
              <td>"+va+"</td>\
             </tr>"
           )

        }
      });
    });


    $('#addperson').click( function() {
        //console.log('clicked')
        var pt=$('#2ptyp option:selected').val()
        var fn=$('#fn').val()
        var mn=$('#mn').val()
        var ln=$('#ln').val()
        var rstreet=$('#rstr').val()
        var rcity=$('#rc').val()
        var rstate=$('#rsta').val()
        var st=$('#2pstat option:selected').val()
        $.ajax({
          type:'POST',
          url:'person/crt',
          data:{
            'pt': pt,
            'fn': fn,
            'mn': mn,
            'ln': ln,
            'rstreet': rstreet,
            'rcity': rcity,
            'rstate': rstate,
            'st': st,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
          },
          success: function(){
            //alert('done');
            var el=1
            if($('#tbody2 tr:last-child td:first-child').length != 0) {
              el=parseInt($('#tbody4 tr:last-child td:first-child').html())+1
            }
            $('#tbody2').append(
              "<tr>\
                <td>"+el+"</td>\
                <td>"+pt+"</td>\
                <td>"+fn+"</td>\
                <td>"+mn+"</td>\
                <td>"+ln+"</td>\
                <td>"+rstreet+"</td>\
                <td>"+rcity+"</td>\
                <td>"+rstate+"</td>\
                <td>\
                  "+st+"\
                  <span style='float:right;'>\
                    <i class='fa fa-times rmov' aria-hidden='true'></i>\
                  </span>\
                </td>\
               </tr>"
             )

          }
        });
      });


    $('.rmov').click(function () {
      $(this).parent().parent().parent().remove();
    });

});
