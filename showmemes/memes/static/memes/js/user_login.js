$(document).ready(function () {
  $('#submit').click(function(){
    var username = $('.username').val();
    document.cookie="username=" + username + '; path=/';
  });
});
