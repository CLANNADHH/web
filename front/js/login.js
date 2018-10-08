var host = "http://127.0.0.1:8000/";
function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

var user_login = function(){
    alert(123457);
    const params = {
        "username": $("#username").val(),
        "password": $("#password").val()
    };
    console.log(params);
    $.ajax({
        type:"post",
        url:host +'users/auths/',
        contentType: "application/json",
        headers: {
            "X-CSRFToken": getCookie("csrf_token")
        },
        data: JSON.stringify(params),

    })
    .done(function (resp) {
            alert("登录成功")
        })
    .fail(function (resp) {
        alert("登录失败")
    })
};

$(function () {
    $(".main-content-agile .sub-main-w3 .login_form").submit(function (e){
        e.preventDefault();
        user_login();
    })
});