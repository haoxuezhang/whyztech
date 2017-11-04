
$(function(){
	$("a").focus(function(){this.blur();});
	
	$(".HomePro .item a").hover(
		function () {
			$(this).children(".infotxt").stop().fadeTo(300, 1);
			$(this).children(".tit").stop().fadeTo(0, 0);
		}, 
		function () {
			$(this).children(".infotxt").stop().fadeTo(300, 0);
			$(this).children(".tit").stop().fadeTo(0, 1);
		}
	);
	//产品分类
	
	$(".HomeArea li a").hover(
		function () {
			$(this).children(".infotxt").stop().fadeTo(300, 1);
		}, 
		function () {
			$(this).children(".infotxt").stop().fadeTo(300, 0);
		}
	);
	//应用领域	
	
	$(".FloatRight li").hover(function() {
	   $(this).addClass("on");
    },function(){
	   $(this).removeClass("on");
	});
	//右侧飘浮
    
	$('.FloatRight .top').click(function(){$('html,body').animate({scrollTop: '0px'}, 800);});
	//返回顶部
});

//nav
$(".MainNav li").hover(
		function(){
			$(".MainNav .SubNav").hide(); 
			$(".MainNav li span .sele").attr("class","shutAhover");
			$(this).attr("id","nav_hover")
			$("#nav_hover span a").attr("class","sele");
			$("#nav_hover").find(".SubNav").stop().slideDown(); 
		},
		function(){
			
			if($(this).attr("class") != "nav_lishw"){
				$("#nav_hover span .sele").attr("class","");
				$("#nav_hover .SubNav").slideUp();
			}
			$(this).attr("id","")
			$(".MainNav li span .shutAhover").attr("class","sele");
			$(".nav_lishw").find(".SubNav").stop().attr();
			$(".nav_lishw span a").attr("class","sele");
		}
);//

$(document).ready(function(){
	$('.SubNav').eq(4).addClass('disNo');
	$('.SubNav').eq(4).hide(0);
	
})
