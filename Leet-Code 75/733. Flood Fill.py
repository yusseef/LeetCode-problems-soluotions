class Solution:
    def floodFill(self, image, sr, sc, newColor):
        sourceColor = image[sr][sc]
        if sourceColor != newColor:
            self.colorize(image, sr, sc, sourceColor, newColor)
        return image
    
    def colorize(self, image, sr, sc, sourceColor, newColor):
        if sr<0 or sr>=len(image) or sc<0 or sc>=len(image[0]) or image[sr][sc] != sourceColor:
            return
        image[sr][sc] = newColor
        self.colorize(image, sr-1, sc, sourceColor, newColor) 
        self.colorize(image, sr, sc+1, sourceColor, newColor) 
        self.colorize(image, sr+1, sc, sourceColor, newColor) 
        self.colorize(image, sr, sc-1, sourceColor, newColor) 
