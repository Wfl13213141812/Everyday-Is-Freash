$(function(){
	// 2：========================================
	//封装点击前后更新前端页面的函数
	function cart_info(id,num,xiaoji,obj){
		$.ajax({
			'url':'/cart/cart_edit',
			'data':{'id':id,'num':num},
			'method':'get',
			'async':false,
			'success':function (data) {
				if (data.ret == 1){
					$(obj).parents('.cart_list_td').find('.num_show').val(num);
					$(obj).parents('.cart_list_td').find('.col07').html(xiaoji.toFixed(2)+'元');
					// 调用函数更新前端总价总数内容
					update_front_info()
				}
            }
		})
	}

	// 4：=================================
	//更新前端购物车总价与总数
	 function update_front_info(){
		total = 0;
		zongji = 0;
		// 利用each 便利
		 $('.cart_list_td').each(function () {
			 if ($(this).find('.danxuan').prop('checked') == false){
			return true;
			// return true 跳过本次循环，return false 结束循环
			}
			else
			{
				total += parseInt($(this).find('.num_show').val());
				zongji += parseFloat($(this).find('.col07').html());
			}

         })
		 // 将累加后的结果 返回前端
		 $('#total').html(total);
		 $('#zongji').html(zongji.toFixed(2)+'元');
		 $('.total_count1').html(total);
	 }





	// 1：======================================
	// 点击加号使商品数量增加
	$('.add').click(function () {
		//获取商品现有数量 商品id 以及 用户id
		num = parseInt($(this).parents('.cart_list_td').find('.num_show').val());
		xiaoji = parseInt($(this).parents('.cart_list_td').find('.col05').html());
		id = parseInt($(this).parents('.cart_list_td').find('.danxuan').val());

		// alert(num)
		// alert(xiaoji)
		// alert(id)
		//数量加1 小计改变
		num+=1;
		xiaoji = xiaoji*num

		obj = this

		cart_info(id,num,xiaoji,obj)
    });

	// 3：======================================
	//	点击减号
	$('.minus').click(function () {
		num = parseInt($(this).parents('.cart_list_td').find('.num_show').val());
    	id = parseInt($(this).parents('.cart_list_td').find('.danxuan').val());
		xiaoji = parseInt($(this).parents('.cart_list_td').find('.col05').html());

		// alert(num)
		// alert(id)
		// alert(xiaoji)
		num -= 1
		if (num<=1){
			num = 1
		}
		xiaoji = num * xiaoji

		obj = this
		cart_info(id,num,xiaoji,obj)


	});


	// 5：=================================
	// 修改框内数字实现内容的改变
	$('.num_show').change(function () {
		num = parseInt($(this).parents('.cart_list_td').find('.num_show').val())
		xiaoji = parseInt($(this).parents('.cart_list_td').find('.col05').html())
		id = parseInt($(this).parents('.cart_list_td').find('.danxuan').val())

		alert(num)

		xiaoji = xiaoji * num
		obj = this
		cart_info(id,num,xiaoji,obj)

    })

	// 6:===========================
	// 复选框发生改变
    $('.danxuan').change(function () {
		// 调用函数0-2，更新前端总数和总价
		update_front_info();
    });

	//7:==========================================
	// 复选框发生改变
    $('.quanxuan').click(function () {
    	check = this.checked;
    	alert(check)
     	$('.danxuan').each(function () {
     	//	把全选狂的checked 属性 赋给每一个单选区
			this.checked = check;
        })
		//更新前端信息
		update_front_info()
    });

    // 8：===============================
    // 删除购物车

	$('.delete_cart').cleck(function () {
		//获取商品 id
		$(this).parent('.cart_list_td').find('.danxuan').val();

		obj = this;
		alert('abc')
		$.get('/cart/del_cart',{'id':id},function (data) {
			if (data.ret ==1)
			{
				$(obj).parents('.cart_list_td').remove()
			}

        })

    })





})