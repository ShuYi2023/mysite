function toggleFontColor() {

    ele = event.target;
    //console.log(ele);
    if (ele.className=='ycb'){
        sibEle=ele.nextElementSibling;//sibEle, sibling element
    }
    if(ele.className=='ysuper'){
        ele = ele.previousElementSibling;
        sibEle = ele.nextElementSibling;        
    }
    
    //↓坑爹，rgb函数中211和112前面有空格啊, 而且不能带有α通道
    //if (ele.style.backgroundColor == "rgb(245, 211, 112)"){
    //↓这个判断语句还不能用#f6f6f7来写，#f6f6f7是rgb(246, 246, 247)
    //绿色是 rgb(68, 146, 64)    
    if (ele.style.color == 'rgb(246, 246, 247)'){
        ele.style.color="rgb(68, 146, 64)";
        sibEle.style.backgroundColor="rgb(68, 146, 64)";
        }
    else{
        //console.log(ele);
        sibEle.style.backgroundColor = "red";
        ele.style.color = "rgb(246, 246, 247)";
        //sibEle.style.backgroundColor="red";
    }

}

var ycbs = document.querySelectorAll('.ycb');//ycheckbox
//↑注意引号中有个点，表示class
var ysupers = document.querySelectorAll('.ysuper');

for (var i=0;i<ycbs.length;i++){
    ycbs[i].addEventListener('click', toggleFontColor);
    ycbs[i].style.backgroundColor = 'rgb(246, 246, 247)';
    ycbs[i].style.color = 'rgb(246, 246, 247)';
    //ycb[i].style = "backgroud-color: rgb(246, 246, 247); color: rgb(246, 246, 247)";
    ysupers[i].addEventListener('click',toggleFontColor);
}
