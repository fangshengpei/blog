/**
 * 
 * @authors Your Name (you@example.org)
 * @date    2017-05-26 17:19:32
 * @version $Id$
 */
$(document).ready(function() {
	
		//获得当前的url
		var c_url=window.location.href;
		//判断当前的url，再给指定的li添加active类
		c_index=0;
		if(c_url.indexOf('add_article')>0){
			c_index=1;	
		}else{
			c_index=0;
		}
		var ulTag=$('.menu-ul');
		ulTag.children().eq(c_index).addClass('active').siblings().removeClass('active');
	//导航栏，当点击进入别的选项时，添加所选择的的页面的active类，去掉当前页面的active
});
