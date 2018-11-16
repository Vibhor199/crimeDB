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
});
