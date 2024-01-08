$(document).ready(function(){
  $('.btn-submit-reg').click(function(){
    var email = $('.email').val();
    var contact = $('.phn').val();
    var card_number = $('.card_number').val();
    var cvv = $('.cvv').val();
    var expiry = $('.expiry').val();
    var flag = true;
    var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;    
    if(!regex.test(email)){
        flag = false    
        alert("invalid email id");   
    }   
    if(contact.length != 10){
        flag = false
        alert("invalid contact");
    }
    if(card_number.length != 16){
      flag = false    
      alert("invalid card number");   
  }
  else if(cvv.length != 3){
    flag = false    
    alert("invalid cvv number");   
    }
  else if(expiry.length != 5){
        flag = false    
        alert("invalid expiry date");   
    }
    if(!flag) 
    {
        return false;
    }
  })
  $('#id_activities').on('change', function(){
    calcPrice()
  })
  $('#id_no_of_days').on('focusout', function(){
    if($(this).val() == 0 ||$(this).val() == '') {
      $(this).val(1);
    }
    calcPrice()
  })
  function calcPrice() {
    if($('#id_activities').val()) {
      $.ajax({
        url: '/get-price',
        type: 'post',
        data: {
          'i': $('#id_activities').val(),
          'csrfmiddlewaretoken':$( "form [name='csrfmiddlewaretoken']" ).val()
        },
        success: function (data) {
          var price = parseInt($('.tot-price').attr('data-price'));
          if($('#id_no_of_days').length > 0) {
            price = price *($('#id_no_of_days').val() == 0 ||$('#id_no_of_days').val() == ''?1:parseInt($('#id_no_of_days').val()))
          }
          price = price + parseInt(data.price)
          $('.tot-price').val(price)
        },
        error: function(err){
          console.log(err);
        }
      })
    }
    else {
      var price = parseInt($('.tot-price').attr('data-price'));
      if($('#id_no_of_days').length > 0) {
        price = price *($('#id_no_of_days').val() == 0 ||$('#id_no_of_days').val() == ''?1:parseInt($('#id_no_of_days').val()))
      }
      $('.tot-price').val(price)
    }
  }

});

