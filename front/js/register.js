// var host = "http://api.clannadhh.club:8000/";
var host = "http://127.0.0.1:8000/";
var error_name = false;
var error_mobile = false;
var sending_flag = false;


function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

var username_flag = false;

var check_username = function() {

    var name = $("#username").val();
    var name_length = name.length;
    if ((name == '用户名') || (name_length < 5) || (name_length > 20)) {
        error_name = true;
        $("#username").val('');
        $("#username").attr('class','errinput');
        $("#username").attr('placeholder','请输入合法的用户名,5-20位英文字母或数字');
    }
    else {
        error_name = false;
        $.ajax({

            type:"get",
            url:host +'users/usernames/' + name + '/count/',
            contentType: "application/json",
            headers: {
                "X-CSRFToken": getCookie("csrf_token")
            },
        })
        .done(function(resp){
            if (resp.count > 0) {
                console.log(resp['count']);
                console.log(resp.count);
                $("#username").val('');
                $("#username").attr('class','errinput');
                $("#username").attr('placeholder','用户名已存在');
                error_name = true;
            } else {
                error_name = false;
            }
        })
        .fail(function (resp) {

            error_mobile = true;
        })
    }
};
var check_mobile = function() {

    var mobile = $("#mobile").val();
    var mobile_length = mobile.length;
    var re = /^1[345789]\d{9}$/;
    if(re.test(mobile)) {
        error_mobile = false;
        $.ajax({
            type:"get",
            url:host +'users/mobile/' + mobile + '/count/',
            contentType: "application/json",
            headers: {
                "X-CSRFToken": getCookie("csrf_token")
            },
        })
        .done(function(resp){
            if (resp.count > 0) {
                error_mobile = true;
                $("#mobile").attr('placeholder','该手机号码已注册');
            } else {
                error_mobile = false;
            }
        })
        .fail(function (resp) {

            error_mobile = true;
        })

    }
    else {
        error_mobile = true;
        $("#mobile").val('');
        $("#mobile").attr('class','errinput');
        $("#mobile").attr('placeholder','你输入的手机号码有误');
    }
};
var send_sms = function () {
    if(sending_flag == true){
        return;
    }
    check_username();
    check_mobile();
    if (error_name == true || error_mobile == true) {
        sending_flag = false;
        return;
    }

    var num = 60;
    var t = setInterval(() => {

        if (num == 1) {
            // 如果计时器到最后, 清除计时器对象
            clearInterval(t);
            sending_flag = false;
            // 将点击获取验证码的按钮展示的文本回复成原始文本
            $('#sendsms').text('发送');
        } else {
            sending_flag = true;
            num -= 1;
            console.log(num+'秒');
            // 展示倒计时信息
            $('#sendsms').text(num + '秒');
        }
    }, 1000, 60)
};
$(function(){

    $(".log .content2 .register_form_con").submit(function (e) {
        check_username();
        check_mobile();
        e.preventDefault();
        const params = {
            "username": $("#username").val(),
            "mobile": $("#mobile").val(),
            "sms_code": $("#smscode").val(),

            "email": $("#email").val(),
            "password": $("#password").val()
        };
        $.ajax({
            url: host + "users/",
            type: "post",
            contentType: "application/json",
            data: JSON.stringify(params),
            success: function (resp) {
                alert(resp)
            }
        })
    });
    $('#username').blur(function () {
        check_username();
    });
    $('#mobile').blur(function () {
        check_mobile();
    });
    $("#sendsms").click(function () {
        send_sms();
        return false;
    })

});