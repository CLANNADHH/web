
var host = "http://api.clannadhh.club:8000/";
// var host = "http://127.0.0.1:8000/";

$(function () {
    $(".register").click(function () {
        location.href = "http://www.clannadhh.club/register.html"
    });
    $(".login").click(function () {
        location.href = "http://www.clannadhh.club/login.html"
    });
    $(".message").click(function () {
        $(".blog").css("display","none");
        $("#editor").css("display","block")
    });
    $(".newslist").click(function () {
        $(".blog").css("display","none");
        $("#editor").css("display","none");
        $("#news_box").css("display","block");
        GetNewsList();
    });
    $(".news_refresh").click(function () {
        GenerNewsFile()
    });
    //原因：新添加的结构是不能获取事件，必须通过父级去完成事件。
    //假如父级也是动态添加，那就要一层一层的网上找。建议直接写body就行了
    $('body').delegate('.read_blog','click',function(){

        pk = $(this).parent().parent().find('.read_blog').attr('id');
        GetBlogData(pk);
        //更新完数据滚动条到顶部
        $('html,body').animate({scrollTop: 0}, 500);
    })
});

$(function () {
    UpdateBlogListData()
});

function UpdateBlogListData() {
    $.ajax({
        type:"get",
        url:host + "blog/list",
        contentType: "application/json",
        // headers: {
        //     "X-CSRFToken": getCookie("csrf_token")
        // },
    })
    .done(function(data){
        if (data != null) {
            // $(".bloglist").html("");
            for(var i=0;i<data.length;i++){
                var news = data[i];
                var content = '';
                var blog_id = String(news.id);
                var id_str = 'id='+blog_id + '>';
                content += '<div class="bloglist"> <span ></span>';
                content += '<h2><a href="javascript:;' + blog_id +'" class="read_blog"' + id_str + news.title + '</a></h2>';
                content += '<p class="datetime">' + news.pub_date+'</p>';
                content += '<ul class="topimg">';
                content += '<img src="images/2011714152744924.jpg">';
                content += '</ul>';
                content += '<ul class="content">';
                content += '<p>' + news.digest + '</p>';
                content += '</ul>\n' + '<p class="read"><a href="javascript:;" class="read_blog">阅读>></a></p></div>';
                $(".blog").append(content);
            }
        }
        //添加请求成功之后返回的数据
    })
}

function GetBlogData(pk) {
    console.log(pk);
    $.ajax({

        type:"get",
        url:host + "blog/"+pk,
        contentType: "application/json",
        // headers: {
        //     "X-CSRFToken": getCookie("csrf_token")
        // },
    })
    .done(function(data){
        if (data != null) {
            $(".bloglist").remove();
            var content = '';
            console.log(data['content']);
            content += '<div class="bloglist">';
            content += '<h2> <a>'+ data['title'] + '</a></h2>';
            content += '<p class="datetime">' + data['pub_date']+'</p>';
            content += '<ul class="topimg">';
            // content += '<img src="images/2011714152744924.jpg">';
            content += '</ul>';
            content += '<ul class="content">';
            content += '<p>' + data['content'] + '</p>';
            content += '</ul>\n' + '<p class="read"><a href="/" >返回首页>></a></p></div>';
            $(".blog").append(content);
        }
        //添加请求成功之后返回的数据
    })
}

function GenerNewsFile() {
    $.ajax({

        type:"get",
        url:host + "newslist/create/",
        contentType: "application/json",
    })
    .done(function(data){
        GetNewsList()
    })
}


function GetNewsList() {

    $.ajax({

        type:"get",
        url:host + "newslist/",
        contentType: "application/json",
        // headers: {
        //     "X-CSRFToken": getCookie("csrf_token")
        // },
    })
    .done(function(data){
        console.log(data)
        if (data != null) {
            // 清除 div内容
            $(".news_box_in").empty();
            var category_count = 0;
            for(var i=0;i<data.length;i++) {

                var content = '';
                var news = data[i];
                if(category_count%10 == 0){
                    content += '<hr>'
                }
                content += "<li><span>";
                content += '[' + news['c'] + ']</span><span class="time_right">';
                content += news['p']+ '</span>';
                content += "</span><a href="+ news['l'] +">" + news['t'];
                content += '</li>';
                category_count += 1;
                $(".news_box_in").append(content);
            }
        }
        //添加请求成功之后返回的数据
    })
}