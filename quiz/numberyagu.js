var numhubo;
var numanswer;
function choice(){
    numhubo = [1,2,3,4,5,6,7,8,9];
    numdab = [];
    for(var i=0;i<4;i++){
        var select = numhubo.splice(Math.floor(Math.random()*(9-i)),1)[0];
        numdab.push(select);
    }
}
var playernum = prompt("플레이어의 수를 적어주세요!");
var turn = 0;
var life = [];
choice();

for(var j=0;j<playernum;j+=1){
    life.push([j,3,1,[]]);
}

console.log(life);
var body = document.body;
var player = document.createElement('h1');
player.textContent = String(life[turn%playernum][0]+1)+'님의 '+String(life[turn%playernum][2])+'번째 턴입니다.';
body.append(player);
var result = document.createElement('h2');
body.append(result);
var sb = document.createElement('h2');
body.append(sb);
var form = document.createElement('form');
body.append(form);
var input = document.createElement('input');
form.append(input);
input.type = 'text';
input.maxLength = 4;
var button = document.createElement('button');
button.textContent = '입력';
form.append(button);
var passbtn = document.createElement('button');
passbtn.textContent = '패스';
body.append(passbtn);
var list = document.createElement('div');
body.append(list);
var flag = false;
console.log()
console.log(numdab);
form.addEventListener('submit', function(event){
    event.preventDefault();
    list.textContent = '';
    if(flag){
         return;
    }
    else if(life[turn%playernum][2] < 4){
    player.textContent = String(life[(turn+1)%playernum][0]+1)+'님의 '+String(life[(turn+1)%playernum][2])+'번째 턴입니다.';
    var answer = input.value;
    if(answer === numdab.join('')){
        player.textContent = String(life[turn%playernum][0]+1)+'님 홈런!';
        result.textContent = '';
        input.value='';
        input.focus();
        flag=true;
        setTimeout(function(){
            location.reload();
        }, 1000);
    } else{
        var answerarr = answer.split('');
        var strike = 0;
        var ball = 0;
        life[turn%playernum][2]++;
        if(life[turn%playernum][2] === 4){
            result.textContent = String(life[turn%playernum][0]+1)+'님 탈락!';
            life.splice(turn%playernum,1);
            playernum--;
            turn-=3;
            input.value='';
            input.focus();
            if(playernum === 0){
                player.textContent = '모두 탈락! 정답은 '+numdab.join(',')+'입니다!';
                result.textContent='';
                input.value='';
                sb.textContent = '';
                flag = true;
                setTimeout(function(){
                    location.reload();
                }, 1000);
            }
            for(var k=0;k<life[(turn+1)%playernum][3].length;k++){
                var div = document.createElement('div');
                div.textContent = life[(turn+1)%playernum][3][k];
                list.append(div);
            }

        } else{
            console.log(answerarr);
            for(var i=0;i<=3;i+=1){
                if(Number(answerarr[i])===numdab[i]){
                    strike +=1;
                } else if(numdab.indexOf(Number(answerarr[i]))>-1){
                    ball +=1;
                }
            }
            sb.textContent = strike+'스트라이크, '+ball+'볼';
            life[turn%playernum][3].push(answerarr.join('')+' '+strike+'스트라이크, '+ball+'볼');
            for(var k=0;k<life[(turn+1)%playernum][3].length;k++){
                var div = document.createElement('div');
                div.textContent = life[(turn+1)%playernum][3][k];
                list.append(div);
            }
            input.value='';
            input.focus();
        }
    }
    } else{
        turn++;
        player.textContent = String(life[(turn+1)%playernum][0]+1)+'님의 '+String(life[(turn+1)%playernum][2])+'번째 턴입니다.';    
        console.log(turn);
    }
    turn++;
    console.log(life,turn,playernum, numanswer);
});

passbtn.addEventListener('click', function(e){
    e.preventDefault();
    if(life[turn%playernum][1]>0){
        life[turn%playernum][1]--;
        player.textContent = String(life[(turn+1)%playernum][0]+1)+'님의 '+String(life[(turn+1)%playernum][2])+'번째 턴입니다.';
        turn++;
    } else{
        result.textContent = '패스 횟수를 다 썼습니다!';
    }
    console.log(life);
});