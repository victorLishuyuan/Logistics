var username=""
var usercode=""
var cookies=document.cookie.split(";");
for(var i=0;i<cookies.length;i++){
	if(cookies[i].split("=")[0]=="electdata-user-cookie"){
		loginStatus = true;
		username = unescape(cookies[i].split("=")[1].split(",")[1]);
		usercode = unescape(cookies[i].split("=")[1].split(",")[0]);
	}
}
$("#user_ID").text(username)
function getCookie(name) 
{ 
    var arr,reg=new RegExp("(^| )"+name+"=([^;]*)(;|$)");
 
    if(arr=document.cookie.match(reg))
 
        return unescape(arr[2]); 
    else 
        return null; 
}
function initTableHeight(){
    //拿到父窗口的centerTabs高度(这是iframe子页面拿到父窗口元素的方法，需要根据自己项目所使用的框架自行修改元素的id)
    var panelH = $("#mainTabs", parent.document).height();
    var height = panelH - 240;
    return height;
}
function outLogin() {
	var date = new Date()
		date.setTime(date.getTime() - 1);
	   var cval=getCookie("electdata-user-cookie"); 
	    if(cval!=null) 
	        document.cookie= "electdata-user-cookie" + "="+cval+";expires="+date.toGMTString(); 
	    parent.window.location = "/electdata-front/login.html";
}