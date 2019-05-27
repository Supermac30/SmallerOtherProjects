function preload() {
  song = loadSound('music.mp3')
  collide = loadSound('hit.wav')
  shoot = loadSound('shoot.wav')
}

function setup() {
  var cnv = createCanvas(400, 400)
  var x = (windowWidth - width) / 2;
  var y = (windowHeight +40 - height) / 2;
  cnv.position(x, y);
  song.play()
}

var Tx1 = 0
var Ty1 = 185
var Tx2 = 0
var Ty2 = 215
var Tx3 = 40
var Ty3 = 200

var stage = 4

// try starting at stage 0, changing line 103, to get a cool mode

var time = 0
var timeleft = 0

var shots = []
var enemies = []

var hit = 0

function draw() {
  time += 1
  timeleft += 1
  background(0, 0, 0)

  fill(61, 61, 59)
  textSize(15)
  text("Level: " + (stage - 3) + "    " + "Hits: " + hit + "    " + "Time: " + (int)(timeleft / 30), 0, 15)

  fill(8, 25, 114)
  triangle(Tx1, Ty1, Tx2, Ty2, Tx3, Ty3)


  // start movement
  if (keyIsDown(87) && Ty1-5 >= 0) { //moves up
    Ty1 -= 5
    Ty2 = Ty1 + 30
    Ty3 = Ty1 + 15
  }
  if (keyIsDown(83) && Ty1+35 <= height) { // moves down
    Ty1 += 5
    Ty2 = Ty1 + 30
    Ty3 = Ty1 + 15
  }
  if (keyIsDown(65) && Tx1-5 >= 0) { // moves left
    Tx1 -= 5
    Tx2 = Tx1
    Tx3 = Tx1 + 40
  }
  if (keyIsDown(68) && Tx1+45 <= width) { //moves right
    Tx1 += 5
    Tx2 = Tx1
    Tx3 = Tx1 + 40
  }
  // end movement

  /*
   * shots are fired then moved
   * if the shot is out of bounds it is not kept in shots
   */
  temp = [];
  for (let i = 0; i < shots.length; i++) {
    curX = shots[i][0]
    curY = shots[i][1]
    if (curX > width || collision(i)) {
      continue
    }
    fill(255, 255, 255)
    ellipse(curX, curY, 12, 12)
    temp.push([curX + 10, curY])
  }
  shots = temp.slice()

  // checks if it is time to add an enemy
  if ((int)(60 / stage) < (int)(time / 3)) {
    time = 0
    buildEnemy()
  }

  // builds all enemies
  // removes out of bounds enemies
  temp = []
  for (let i = 0; i < enemies.length; i++) {
    curX = enemies[i][0]
    curY = enemies[i][1]
    if (curX < 0) {
      continue
    }
    fill(37, 147, 25)
    ellipse(curX, curY, 50, 50)
    temp.push([curX - (int)(stage / 2) - 1, curY])
    
    //checks if an enemy is hit
    var dx1 = Tx1 - enemies[i][0]  
    var dx2 = Tx2 - enemies[i][0]  
    var dx3 = Tx3 - enemies[i][0]  
    var dy1 = Ty1 - enemies[i][1]  
    var dy2 = Ty2 - enemies[i][1]  
    var dy3 = Ty3 - enemies[i][1]  
    if ( sqrt(sq(dx1)+sq(dy1)) < radius){
      gameover()
    }
    else if ( sqrt(sq(dx2)+sq(dy2)) < radius){
      gameover()
    }
    else if ( sqrt(sq(dx3)+sq(dy3)) < radius){
      gameover()
    }
  }
  enemies = temp.slice()

  // increases the difficulty
  if (hit > sq(stage - 3)) {
    stage += 1
  } // remove the -3 and start when stage = 0 for a cool mode


}

function keyPressed() {
  if (keyCode == 32) {
    shoot.play()
    shots.push([Tx3, Ty3]) //shoots a bullet
  }
  if (keyCode == 82){
    hit = 0
    enemies = []
    shots = []
    stage = 4
    timeleft = 0
    loop()
  }
}

function buildEnemy() {
  enemies.push([width, (int)(random(height))])
}

function collision(loc) {
  for (let i = 0; i < enemies.length; i++) {
    var enX = enemies[i][0]
    var enY = enemies[i][1]
    var curX = shots[loc][0]
    var curY = shots[loc][1]
    var dist = sqrt(sq(curX - enX) + sq(curY - enY))
    if (dist <= 31) {
      enemies.splice(i, 1)
      collide.play()
      hit += 1
      return true
    }
  }
  return false
}
    
const radius = 25
    
function gameover(){
  fill(244, 223, 66)
  textSize(50)
  text("Game Over", 50, 200)
  textSize(25)
  text("You scored " + hit + " points", 50, 250)
  text("press r to restart", 50, 280)
  noLoop()
}
