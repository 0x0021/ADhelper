<head>
  <meta charset="utf-8">
  <title>AD账号服务</title>
  <meta name="renderer" content="webkit">
  <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
  <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
  <link rel="stylesheet" href="/layui/css/layui.css"  media="all">
  <!-- 注意：如果你直接复制所有代码到本地，上述css路径需要改成你本地的 -->
</head>

<style>
body{ text-align:center;font-size:28px;font-family:Arial,"微软雅黑"; } 
.div{ margin:0 auto; width:250px; height:100px;} 
<!-- css注释：为了观察效果设置宽度 边框 高度等样式 --> 
</style>

<script src="/layui/layui.js" charset="utf-8"></script>
<script src="https://g.alicdn.com/dingding/dingtalk-jsapi/2.10.3/dingtalk.open.js"></script>
<script>
//获取免登码
var code = '';
dd.ready(function() {
    dd.runtime.permission.requestAuthCode({
        corpId: "ding5128377a430e46aaee0f45d8e4f7c288", // 企业id
        onSuccess: function (info) {
            code = info.code // 通过该免登授权码可以获取用户身份
			//document.getElementById("myDiv").innerHTML=code;
        }
		});
});
</script>

<div>请选择所需的服务</div>
<fieldset class="layui-elem-field site-demo-button">
  <br>
  <div class="div">
    <button type="button" class="layui-btn layui-btn-lg layui-btn-radius" data-type="unlockaccount">解锁账号</button>
  </div>
  <div class="div">
    <button type="button" class="layui-btn layui-btn-lg layui-btn-radius" data-type="resetpassword"">重置密码</button>
  </div>
<div id='hide' style = "display : none " class="layui-progress layui-progress-big" lay-filter="loading" lay-showPercent="true">
  <div class="layui-progress-bar" lay-percent="0%"></div>
</div>

<div id="myDiv"></div>

<script>
layui.use('element', function(){
  var $ = layui.jquery;
  element = layui.element; //激活element模块
  //触发事件
  var active = {
	//解锁账号
    unlockaccount: function(othis){
	//显示进度条
	document.getElementById("hide").style.display = "block";
	document.getElementById("myDiv").innerHTML="请稍等片刻";
	
      var DISABLED = 'layui-btn-disabled';
      if(othis.hasClass(DISABLED)) return;
      //模拟loading,最大90%
      var n = 0, timer = setInterval(function(){
        n = n + Math.random()*10|0;  
		// |0 把数值转为32位二进制并舍弃小数进行位或运行,达到向下取整效果,最大有效范围2^32/2-1
        if(n>90){
          n = 90;
          clearInterval(timer);
          othis.removeClass(DISABLED);
        }
        element.progress('loading', n+'%');
      }, 50+Math.random()*100);
    othis.addClass(DISABLED);
	//发送请求
	var xmlhttp;
	if (window.XMLHttpRequest)
	{
		//  IE7+, Firefox, Chrome, Opera, Safari 浏览器执行代码
		xmlhttp=new XMLHttpRequest();
	}
	else
	{
		// IE6, IE5 浏览器执行代码
		xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
	}
	xmlhttp.onreadystatechange=function()
	{
		if (xmlhttp.readyState==4 && xmlhttp.status==200)
		{
			document.getElementById("myDiv").innerHTML=xmlhttp.responseText;
			element.progress('loading', '100%')
		}
	}
	xmlhttp.open("POST","./ADhelper.php",true);
	xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
	xmlhttp.send("type=unlockaccount&code="+code);
	  
    },
	
	//重置密码
	resetpassword: function(othis){
	
	document.getElementById("hide").style.display = "block";
	document.getElementById("myDiv").innerHTML="请稍等片刻";
	
      var DISABLED = 'layui-btn-disabled';
      if(othis.hasClass(DISABLED)) return;
      //模拟loading,最大90%
      var n = 0, timer = setInterval(function(){
        n = n + Math.random()*10|0;  
        if(n>90){
          n = 90;
          clearInterval(timer);
          othis.removeClass(DISABLED);
        }
        element.progress('loading', n+'%');
      }, 100+Math.random()*100);
      
      othis.addClass(DISABLED);
	  
	var xmlhttp;
	if (window.XMLHttpRequest)
	{
		//  IE7+, Firefox, Chrome, Opera, Safari 浏览器执行代码
		xmlhttp=new XMLHttpRequest();
	}
	else
	{
		// IE6, IE5 浏览器执行代码
		xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
	}
	xmlhttp.onreadystatechange=function()
	{
		if (xmlhttp.readyState==4 && xmlhttp.status==200)
		{
			document.getElementById("myDiv").innerHTML=xmlhttp.responseText;
			element.progress('loading', '100%')
		}
	}
	xmlhttp.open("POST","./ADhelper.php",true); 
	xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
	xmlhttp.send("type=resetpassword&code="+code);
	}
  };
  
  $('.layui-btn-radius').on('click', function(){
    var othis = $(this), type = $(this).data('type');
    active[type] ? active[type].call(this, othis) : '';
  });
});
</script>



