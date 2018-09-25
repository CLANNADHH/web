// $(function () {
//
//     $("form").submit(function(e){
//       alert("Submitted");
//     });
//     // $(".readmore").click(function () {
//     //     $(".collection").attr('data-newid');
//     //     var params = {
//     //         "news_id": news_id,
//     //     }
//     //     $.ajax({
//     //         url: "http://api.clannadhh.club:8000/news/",
//     //         type: "get",
//     //         contentType: "application/json",
//     //         headers: {
//     //             "X-CSRFToken": getCookie("csrf_token")
//     //         },
//     //         data: JSON.stringify(params),
//     //         success: function (resp) {
//     //                 alert(resp)
//     //             }
//     //     })
//     // })
//
// })
var username_flag = false;

var check = function() {
    // $("#username").blur(function () {
    //
    // })
    var name = $("#username").val();
    var name_length = name.length;
    if ((name == '用户名') || (name_length < 5)) {
        username_flag = false
        $("#username").val('');
        $("#username").attr('class','errinput');
        $("#username").attr('placeholder','请输入合法的用户名');

    }
    else {
        username_flag = true
    }
};

$(function(){

    $(".log .content2 .register_form_con").submit(function (e) {
        check();
        e.preventDefault();
        const params = {
            "username": "w"
        };
        $.ajax({
            url: "http://127.0.0.1:8000/register/",
            type: "post",
            contentType: "application/json",
            data: JSON.stringify(params),
            success: function (resp) {
                    alert(resp)
                }
        })
    })


});