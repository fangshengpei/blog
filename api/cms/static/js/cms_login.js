/**
 * 
 * @authors Your Name (you@example.org)
 * @date    2017-05-28 23:02:45
 * @version $Id$
 */

// $(document).ready(function)
// {
// 	$(function() {
// 		$(".captcha").click(function() {
// 			console.log('这是测试js');	
// 		});
// 	});
// };
$(document).ready(function() {
	$(".captcha").click(function() {
		// 获得当前的验证码图片的src
		var old_src=$(this).attr('src');
		// console.log(old_url);
		//更换src就能达到刷新图片的目的
		// 产生随机的参数
		var src=old_src+'?xx'+Math.random();
		// console.log(src);
		$(this).attr('src',src);
	});
})