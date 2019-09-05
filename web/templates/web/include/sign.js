function changeCaptcha(ths) {
    // 加 ? 会导致imag标签因改变了src而重新加载
        ths.src = ths.src + '?'
    }


function checkUsername(ths) {
    // check the username is existed or not
    $('.user-error').html('');
    $.ajax({
        url: '{% url "checkusername" %}',
        type: 'POST',
        dataType: 'JSON',
        data: {'username': ths.value},
        success: function (arg) {
            if (window.location.pathname.indexOf('signin') !== -1){
                $('.user-error').text(arg.signin_error);
            } else {
                $('.user-error').text(arg.signup_error);
            }
        }
    })
}