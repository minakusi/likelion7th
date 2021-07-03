var n1 = Math.ceil(Math.random()*9);
var n2 = Math.ceil(Math.random()*9);
var r = n1*n2;
var i = 0;
var flag = false;
var correct = 0;
var timer;
var delay = 10;
var clock = delay;
var body = document.body;
var time = document.createElement('div');
time.textContent = 10;
body.append(time);
var question = document.createElement('div');
if(String(n2)[String(n2).length-1] === 2||
String(n2)[String(n2).length-1] === 4||
String(n2)[String(n2).length-1] === 5||
String(n2)[String(n2).length-1] === 9){question.textContent = String(n1)+' 곱하기 '+String(n2)+'는?';}
else{
    question.textContent = String(n1)+' 곱하기 '+String(n2)+'은?';
    }
body.append(question);

var form = document.createElement('form');
body.append(form);
var input = document.createElement('input');
form.append(input);
var button = document.createElement('button');
button.textContent = '입력';
form.append(button);

var result = document.createElement('div');
body.append(result);
var cor = document.createElement('div');
body.append(cor);
var odapchang = document.createElement('div');
body.append(odapchang);
var wrong = document.createElement('div');
body.append(wrong);

if(clock>0){
    clock--;
    timer = setTimeout(1000);
}
console.log(timer);
form.addEventListener('submit', function(event){
    event.preventDefault();
    if(flag){
        return;
    }

    console.log(timer);
    if(r === Number(input.value)){
        result.textContent = '딩동댕!';
        n1 = Math.ceil(Math.random()*9);
        n2 = Math.ceil(Math.random()*9);
        r = n1*n2;
        if(String(n2)[String(n2).length-1] === 2||
        String(n2)[String(n2).length-1] === 4||
        String(n2)[String(n2).length-1] === 5||
        String(n2)[String(n2).length-1] === 9){question.textContent = String(n1)+' 곱하기 '+String(n2)+'는?';}
        else{
            question.textContent = String(n1)+' 곱하기 '+String(n2)+'은?';
        }
        input.value='';
        input.focus();
        correct += 1;
    clearTimeout();
    } else{
        result.textContent='땡!';
        odapchang.textContent = '***오답목록***';
        var div = document.createElement('div');
        div.textContent = String(i+1)+'. '+String(n1)+'x'+String(n2)+' != '+input.value;
        wrong.append(div);
        i +=1 ;
    }
});

