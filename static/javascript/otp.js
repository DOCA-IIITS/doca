var time=document.getElementById('time');
var rsend=document.getElementById("rsend");
var v=document.getElementById("v");
var min=2;
var sec=0;
var t, s;

rsend.onclick=function(){
  for(var i=1;i<7;i++){
    document.getElementById(i.toString()).value='';
  }
  rsend.disabled=true;
  min=2;
  sec=0;
  time.innerHTML='2 : 00';
  t=setInterval(timer, 1000);
}

function isNum(evt){
    var charCode = (evt.which) ? evt.which : event.keyCode
    if (charCode > 31 && (charCode < 48 || charCode > 57))
        return false;
    return true;
}

function next(ind, event){
  if(event.keyCode==8){
    if(ind!=1){
      ind--;
      var id=ind.toString();
      document.getElementById(id).focus();
    }
    if(!v.disabled){
      v.disabled=true;
    }
  }else{
    if(document.getElementById(ind.toString()).value!=''){
      if(document.getElementById('1').value!='' && document.getElementById('2').value!='' && document.getElementById('3').value!='' && document.getElementById('4').value!='' && document.getElementById('5').value!='' && document.getElementById('6').value!=''){
        v.disabled=false;
      }else{
        ind++;
        var id=ind.toString();
        document.getElementById(id).focus();
      }
    }
  }
}

function timer(){
  if(min == 0 && sec==0){
    clearInterval(t);
    rsend.disabled=false;
  }
  if(sec==0){
    min--;
    sec=60;
  }
  sec--;
  s=sec.toString();
  if(sec<10){
    s='0'+s;
  }
  if(min!=-1){
    time.innerHTML= min.toString()+' : '+s;
  }
}

t=setInterval(timer, 1000);
