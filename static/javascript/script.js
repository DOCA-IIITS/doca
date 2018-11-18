var nav=document.getElementById('nav');
var ss_div=document.getElementById('ss');
var x=nav.offsetTop;
var y=ss_div.offsetTop;
var arr=["url('https://medici.miodottore.it/hubfs/IT/Medico_stretta_di_mano.jpg?t=1538357353863')",
        "url('http://www.remedy247.net/images/slide-health-2.jpg')",
        "url('http://template53236.motopreview.com/mt-demo/53200/53236/mt-content/uploads/2015/03/mt-0017-about-slider1.jpg')",
        "url('http://lifehomecenter.com/mt-demo/53200/53236/mt-content/uploads/2015/03/mt-0017-about-slider2.jpg')",
        "url('https://lh3.googleusercontent.com/l7sbc686quwpelzNeBr4gAoE4n-yON6v8wqEAikJwIQfdfN1NcaqdxWHNb8dgq_TndIb0vqAON0=w1920-h642-no')"];
var text=[
'Your <b>Health is</b> always in the <br><b>first place</b><br><hr><span class="text">We provide you with constant service, we are always here for you</span>',
'Bringing the <b>future of healthcare</b><br><hr><span class="text">Connected with many amazing hospitals, ensuring advanced healthcare is made personal</span>',
'<b>Passionate</b> about medicine...<br><b>Compassionate</b> about People<br><hr><span class="text">Not just beter healthcare, but a beter healthcare experience. Healing hands, Caring hearts </span>',
'A <b>family of hospitals</b> for <b>your family</b><br><hr><span class="text">We show doctors of your choice. Beter doctors and  beter care, all found around you</span>',
'Experience <b>services, memorable</b> for life<br><hr><span class="text">Besides appointing a docter, we also provide various other services convinient and efficient</span>'
];
var i=1;
var txt=document.getElementById('content');
txt.innerHTML=text[0];

window.onload=function(){
  window.scrollTo(0,1);
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}

window.onscroll=function(){
    if(window.pageYOffset>x){
    	nav.style.position='fixed';
    	nav.style.top='0px';
  	}else {
    	nav.style.top=x+'px';
    	nav.style.position='absolute';
      ss_div.style.top=y+'px';
      nav.style.position='absolute';
  	}
}

function slides(){
  txt.style.color='black';
  if(i==5){
    i=0;
  }
  ss_div.style.background=arr[i];
  ss_div.style.backgroundSize='cover';
  txt.innerHTML=text[i];
  i++;
}

var t=setInterval(slides , 8000);
