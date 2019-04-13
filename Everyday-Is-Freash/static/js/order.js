$(function () {
    $('#order_btn').click(function () {
    // 获取支付方式和cart_ids
        pay = $('.pay_style_con input:checked').val();
        ids_str = $('#ids_str').val();

        //获取csrf_token 的值
        // csrf_val = $(this).next().val();
        // alert(csrf_val)
        //POST 方式传参若后端使用了 防盗链装饰器在此则不用再获取csrf 的值并传入
        //POST 方式传参 切记 传至的 url 最后要添加  反斜杠 /
        //POST 方式必须传参必须使用防盗链 传递名称必须为  csrfmiddlewaretoken
        $.post('/order/order_handle/',{'pay':pay, 'ids_str': ids_str},function (data) {
            if (data.ret == 1){
                window.location = '/user/order';
            }
            else {
                alert('订单处理失败!!!')
            }
        })

    })

})