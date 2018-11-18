var nav=document.getElementById('nav');
var x=nav.offsetTop;
var btns=document.getElementsByClassName('b');
var tabs=document.getElementsByClassName('tab');
var divs=document.getElementsByClassName('div');
var temp=0;

window.onscroll=function(){
    if(window.pageYOffset>x){
    	nav.style.position='fixed';
    	nav.style.top='0px';
  	}else {
    	nav.style.top=x+'px';
    	nav.style.position='absolute';
  	}
}

function change(a , b) {
  console.log(a);
  console.log(b);
  btns[a].disable=true;
  tabs[a].style.backgroundColor='#4451ff';
  divs[b].style.display='none';
  divs[a].style.display='block';
  btns[b].disable=false;
  tabs[b].style.backgroundColor='rgba(27, 112, 17, 0.6)';
  return a;
}

window.onload=function(){
  window.scrollTo(0,1);
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
  btns[0].onclick=function(){temp=change(0,temp);}
  btns[1].onclick=function(){temp=change(1,temp);}
  btns[2].onclick=function(){temp=change(2,temp);}
  btns[3].onclick=function(){temp=change(3,temp);}
  btns[0].disable=true;
}
