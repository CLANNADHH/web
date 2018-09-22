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
$(function(){
    $(".log .content2 .register_form_con").submit(function (e) {
        e.preventDefault();
        alert(123);
        var params = {
            "username": "w"
        };
        $.ajax({
            url: "http://127.0.0.1:8000/register/",
            type: "post",
            contentType: "application/json",
            // headers: {
            //     "X-CSRFToken": getCookie("csrf_token")
            // },
            data: JSON.stringify(params),
            success: function (resp) {
                    alert(resp)
                }
        })
    })

});