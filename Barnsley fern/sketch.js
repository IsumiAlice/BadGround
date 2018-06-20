let x = 0;
let y = 0;

function setup() {
  createCanvas(400, 400);
  background(0);
}

function fun(x, y){

}

function draw() {
  stroke(227, 249, 247);
  strokeWeight(1);

  for (var i = 0; i < 100; i++){
    var px = map(x, -2.182, 2.6558, 0, width);
    var py = map(y, 0, 9.9983, height, 0);

    point(px, py);

    // translate(width/2, height);
    // console.log(x, y);
    // console.log(px, py);

    let next_x;
    let next_y;
    let r = random(1);
    if (r < 0.01){
      next_x =  0;
      next_y =  0.16 * y;
    }
    else if (r < 0.86){
      next_x =  0.85 * x + 0.04 * y;
      next_y = -0.04 * x + 0.85 * y + 1.6;
    }
    else if (r < 0.93){
      next_x =  0.20 * x - 0.26 * y;
      next_y =  0.23 * x + 0.22 * y + 1.6;
    }
    else{
      next_x = -0.15 * x + 0.28 * y;
      next_y =  0.26 * x + 0.24 * y + 0.44;
    }

    x = next_x;
    y = next_y;
  }
}
