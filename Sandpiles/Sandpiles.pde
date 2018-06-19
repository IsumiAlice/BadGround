// https://youtu.be/diGjw5tghYU
// can be faster, will make it

int[][] sandpiles;

void setup() {
  size(300, 300);
  sandpiles = new int[width][height];
  sandpiles[width/2][height/2] = 1000000000;
}

void topple() {
  int[][] nextpiles = new int[width][height];  
  for (int x = 0; x < width; x++) {
    for (int y = 0; y < height; y++) {
      int num = sandpiles[x][y];
      if (num < 4) {
        nextpiles[x][y] = sandpiles[x][y];
      }
    }
  }

  for (int x = 0; x < width; x++) {
    for (int y = 0; y < height; y++) {
      int num = sandpiles[x][y];
      if (num >= 4) {
        nextpiles[x][y] += (num - 4);
        if (x+1 < width)
          nextpiles[x+1][y]++;
        if (x-1 >= 0)
          nextpiles[x-1][y]++;
        if (y+1 < height) 
          nextpiles[x][y+1]++;
        if (y-1 >= 0) 
          nextpiles[x][y-1]++;
      }
    }
  }

  sandpiles = nextpiles;
}

void render() {
  loadPixels();
  for (int x = 0; x < width; x++) {
    for (int y = 0; y < height; y++) {
      int num = sandpiles[x][y];
      color col = color(#a900b8);
      if (num == 0) {
        col = color(#ceb6f0);
      } else if (num == 1) {
        col = color(#b7bbf0);
      } else if (num == 2) {
        col = color(#c7ea97);
      } else if (num == 3) {
        col = color(#c4f3ef);
      }

      pixels[x+y*width] = col;
    }
  }

  updatePixels();
}


void draw() {
  render(); 
  for (int i = 0; i < 100; i++) {
    topple();
  }
}
