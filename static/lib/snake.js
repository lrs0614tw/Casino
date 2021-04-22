//獲取繪製工具
/*
var canvas = document.getElementById("canvas");
var ctx = canvas.getContext("2d");//獲取上下文
ctx.moveTo(0,0);
ctx.lineTo(450,450);*/
var c = document.getElementById("canvas");
var ctx = c.getContext("2d");
/*ctx.beginPath();
ctx.moveTo(0,0);
ctx.lineTo(450,450);
ctx.stroke();
*/

var snake = []; //定義一條蛇，畫蛇的身體
var snakeCount = 6; //初始化蛇的長度
var foodx = 0;
var foody = 0;
var foodColor = 'black';
var togo = 0;
var moveInterval;
var score = 0;


function drawtable() //畫地圖的函式
{


    for (var i = 0; i < 20; i++) //畫豎線
    {
        ctx.strokeStyle = "black";
        ctx.beginPath();
        ctx.moveTo(45 * i, 0);
        ctx.lineTo(45 * i, 900);
        ctx.closePath();
        ctx.stroke();
    }
    for (var j = 0; j < 20; j++) //畫橫線
    {
        ctx.strokeStyle = "black";
        ctx.beginPath();
        ctx.moveTo(0, 45 * j);
        ctx.lineTo(900, 45 * j);
        ctx.closePath();
        ctx.stroke();
    }

    for (var k = 0; k < snakeCount; k++) //畫蛇的身體
    {
        ctx.fillStyle = "#000";
        if (k == snakeCount - 1) {
            ctx.fillStyle = "red"; //蛇頭的顏色與身體區分開
        }
        ctx.fillRect(snake[k].x, snake[k].y, 45, 45); //前兩個數是矩形的起始座標，後兩個數是矩形的長寬。

    }
    //繪製食物	
    ctx.fillStyle = foodColor;
    ctx.fillRect(foodx, foody, 45, 45);
    ctx.fill();


}


function start() //定義蛇的座標
{
    snake = []; //定義一條蛇，畫蛇的身體
    snakeCount = 6; //初始化蛇的長度
    foodx = 0;
    foody = 0;
    foodColor = 'black';
    togo = 0;
    score = 0;
    document.getElementById('Score').innerText = score;

    for (var k = 0; k < snakeCount; k++) {
        snake[k] = { x: k * 45, y: 0 };

    }

    drawtable();
    addfood(); //在start中呼叫新增食物函式

}

function addfood() {
    foodx = Math.floor(Math.random() * 20) * 45; //隨機產生一個0-1之間的數
    foody = Math.floor(Math.random() * 20) * 45;

    for (var k = 0; k < snakeCount; k++) {
        if (foodx == snake[k].x && foody == snake[k].y) //防止產生的隨機食物落在蛇身上
        {
            addfood();
        }
    }


}

function move() {
    switch (togo) {
        case 1:
            snake.push({ x: snake[snakeCount - 1].x - 45, y: snake[snakeCount - 1].y });
            break; //向左走
        case 2:
            snake.push({ x: snake[snakeCount - 1].x, y: snake[snakeCount - 1].y - 45 });
            break;
        case 3:
            snake.push({ x: snake[snakeCount - 1].x + 45, y: snake[snakeCount - 1].y });
            break;
        case 4:
            snake.push({ x: snake[snakeCount - 1].x, y: snake[snakeCount - 1].y + 45 });
            break;
        default:
            snake.push({ x: snake[snakeCount - 1].x + 45, y: snake[snakeCount - 1].y });
    }
    snake.shift(); //刪除陣列第一個元素
    ctx.clearRect(0, 0, 900, 900);
    isEat();
    isDead();
    drawtable();

}


function isEat() //吃到食物後長度加1
{
    if (snake[snakeCount - 1].x == foodx && snake[snakeCount - 1].y == foody) {
        addfood();
        snakeCount++;
        snake.unshift({ x: 45, y: -45 });
        score = score + 100;
        document.getElementById('Score').innerText = score;
        if (score > parseInt(highscore)) {
            document.getElementById('highScore').innerText = score;
            highscore = score;
        }
    }

}

function isDead() {
    if (snake[snakeCount - 1].x > 855 || snake[snakeCount - 1].y > 855 || snake[snakeCount - 1].x < 0 || snake[snakeCount - 1].y < 0) {
        clearInterval(moveInterval);
        document.getElementById('gameover').style.display = 'block';
        document.getElementById('highscoreShow').innerText = '本次得分： ' + score;
        $.ajax({
            'url': '/snakeUpdate',
            'type': 'POST',
            'data': {
                uid: '{{uid}}',
                highscore: highscore,
            },
        }).done(function(data) {
            if (data.status == 200) {
                console.log('a');
            } else if (data.status == 400) {
                alert(data.message);
            }
        })
    }
    for (var i = snakeCount - 2; i--; i >= 0) {
        if (snake[snakeCount - 1].x == snake[i].x && snake[snakeCount - 1].y == snake[i].y) {
            clearInterval(moveInterval);
            document.getElementById('gameover').style.display = 'block';
            document.getElementById('highscoreShow').innerText = '本次得分： ' + score;
            $.ajax({
                'url': '/snakeUpdate',
                'type': 'POST',
                'data': {
                    uid: '{{uid}}',
                    highscore: highscore,
                },
            }).done(function(data) {
                if (data.status == 200) {
                    console.log('a');
                } else if (data.status == 400) {
                    alert(data.message);
                }
            })
        }
    }
}
$("body").on("touchstart", function(e) {　　　　
    e.preventDefault();　　　　
    startX = e.originalEvent.changedTouches[0].pageX, 　　　　startY = e.originalEvent.changedTouches[0].pageY;　　
});　　
$("body").on("touchmove", function(e) {　　　　
    e.preventDefault();　　　　
    moveEndX = e.originalEvent.changedTouches[0].pageX, 　　　　moveEndY = e.originalEvent.changedTouches[0].pageY, 　　　　X = moveEndX - startX, 　　　　Y = moveEndY - startY;

    　　　　
    if (Math.abs(X) > Math.abs(Y) && X > 0 && togo != 1) { togo = 3; }　　　　
    else if (Math.abs(X) > Math.abs(Y) && X < 0 && togo != 3) { togo = 1; }　　　　
    else if (Math.abs(Y) > Math.abs(X) && Y > 0 && togo != 2) { togo = 4; }　　　　
    else if (Math.abs(Y) > Math.abs(X) && Y < 0 && togo != 4) { togo = 2; }　　　　
});

function startgame() {
    document.getElementById('start').style.display = 'none';
    document.getElementById('gameover').style.display = 'none';
    start();
    moveInterval = setInterval(move, 100);
    drawtable();
}