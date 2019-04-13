$(function () {
    $('.add').click(function () {

        //转换为整形
        num = parseInt($('.num_show').val())
        price = parseFloat($('#price').html())

        num += 1;

        money = price*num

        // alert(money)
        //重新赋值
        $('.num_show').val(num)

        $('#money').html(money.toFixed(2)+'元')

    })

    $('.minus').click(function () {

        num = $('.num_show').val()
        price = $('#price').html()

        num -= 1;

        if (num <= 1){
             num = 1
        }

        money = price * num


        $('.num_show').val(num)
        $('#money').html(money.toFixed(2)+'元')


    })

    // 点击加入购物车
    $('#add_cart').click(function () {
        // alert('123')
    //    获取商品id 和 数量
        num = parseInt($('.num_show').val())
        goods_id = $(this).next().val()
        // alert(goods_id)
        $.get('/cart/cart_handle',{'num':num,'id':goods_id},function (data) {
            if(data.ret==1){
                alert('商品加入购物车成功!!!')
            }
        })
        

    })







})