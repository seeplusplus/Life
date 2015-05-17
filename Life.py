#  Copyright 2015 Caleb Webber
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

from math import sqrt, pow, floor

class Board:
    LiveChar = '*'
    DeadChar = '.'
    def __init__(self, _width, _height, _seed=[]):
        self.Width = _width
        self.Height = _height
        self.Living = []
        self.Initialized = False
        if (len(_seed) > 0):
            self.seed(_seed)
        
    def seed(self, _seed):
        if (type(_seed) != list):
            raise ValueError
        for i in _seed:
            if (not i in self.Living) & (self.is_point(i)):
                self.Living.append(i)
            elif not self.is_point(i):
                raise IndexError("Point {} is not located in board of {} width and {} height".format(i, self.Width, self.Height))
        self.Initialized = True

    def is_point(self, point):
        return (point[0] <= (self.Width - 1)) and (point[1] <= (self.Height - 1)) and (point[0] != -1 and point[1] != -1)

    def Print(self):
        for i in range(0, self.Height):
            line = ''
            for j in range(0, self.Width):
                if [j,i] in self.Living:
                    line += Board.LiveChar
                else:
                    line += Board.DeadChar
            print(line)
    @staticmethod
    def atob_distance(a_point, b_point):
        return sqrt(pow((b_point[0] - a_point[0]),2) + pow((b_point[1] - a_point[1]),2))
    
    @staticmethod
    def GetSurroundingPoints(x,y):
        if type(x) != int or type(y) != int:
            raise TypeError("Arguments not of valid types")
        newList = []
        for i in range(x - 1, x + 2):
            for j in range(y -1, y + 2):
                newList.append([i,j])
        return newList

    @staticmethod
    def Process(board):
        evalPoints = []
        for point in board.Living:
            for surrounding_point in board.GetSurroundingPoints(point[0], point[1]):
                if not surrounding_point in evalPoints and board.is_point(surrounding_point):
                    evalPoints.append(surrounding_point)
        
        copyEval = list(evalPoints)
        for point in evalPoints:
            neighbor_count = 0
            for l_points in board.Living:
                if point != l_points and floor(Board.atob_distance(point,l_points)) <= 1:
                    neighbor_count += 1
            if point in board.Living:
                if neighbor_count < 2 or neighbor_count > 3:
                    copyEval.remove(point)
            elif neighbor_count != 3:
                copyEval.remove(point)
        board.Living = copyEval