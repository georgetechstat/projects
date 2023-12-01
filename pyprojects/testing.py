import sys
import operator
from math import sqrt
from argparse import ArgumentParser

class PolygonAnalyzer:
    def __init__(self, filename, print_flag):
        self.filename = filename
        self.print_flag = print_flag
        self.lines = None
        self.grid = None
        self.width = None
        self.height = None
        self.new_grid = None
        self.poly = []
        self.polygons = {}
        self.results = {}
        self.depth_dict = {}

    def parse_arguments(self):
        parser = ArgumentParser()
        parser.add_argument('-print', action='store_true')
        parser.add_argument('--file', dest='filename', required=True)
        args = parser.parse_args()
        self.filename = args.filename
        self.print_flag = args.print

    def read_file(self):
        with open(self.filename) as file:
            self.lines = file.read().splitlines()
            self.lines = list(filter(str.strip, self.lines))

    def process_input(self):
        self.grid = [[] for _ in range(len(self.lines))]
        for i in range(len(self.lines)):
            line = list(filter(str.strip, self.lines[i]))
            self.grid[i] = list(map(int, line))
        self.width = len(self.grid[0])
        self.height = len(self.grid)
        self.new_grid = [[] for _ in range(self.height + 2)]
        for i in range(self.height + 2):
            self.new_grid[i] = [[] for _ in range(self.width + 2)]
            if i == 0 or i == self.height + 1:
                for k in range(self.width + 2):
                    self.new_grid[i][k] = 0
            else:
                for k in range(self.width + 2):
                    if k == 0 or k == self.width + 1:
                        self.new_grid[i][k] = 0
                    else:
                        self.new_grid[i][k] = self.grid[i - 1][k - 1]
        self.grid = self.new_grid[:]
        self.width = len(self.grid[0])
        self.height = len(self.grid)

    def point_inside_polygon(self, x, y, poly):
        n = len(poly)
        inside = False
        p1x, p1y = poly[0]
        for i in range(n + 1):
            p2x, p2y = poly[i % n]
            if min(p1y, p2y) < y <= max(p1y, p2y) and x <= max(p1x, p2x):
                if p1y != p2y:
                    xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                if p1x == p2x or x <= xinters:
                    inside = not inside
            p1x, p1y = p2x, p2y
        return inside

    def polygon_perimeter(self, poly):
        perimeter1 = 0
        perimeter2 = 0
        for i in range(-1, len(poly) - 1):
            if poly[i][0] == poly[i + 1][0] or poly[i][1] == poly[i + 1][1]:
                perimeter1 += abs(poly[i + 1][0] - poly[i][0]) + abs(poly[i + 1][1] - poly[i][1])
            else:
                perimeter2 += abs(poly[i][0] - poly[i + 1][0])
        perimeter1 = round(perimeter1 * 0.4, 1)
        if perimeter1 == 0:
            perimeter = '%s*sqrt(.32)' % (perimeter2)
        else:
            if perimeter2 == 0:
                perimeter = '%s' % (perimeter1)
            else:
                perimeter = '%s + %s*sqrt(.32)' % (perimeter1, perimeter2)
        return perimeter

    def polygon_area(self, poly):
        n = len(poly)
        area = 0.00
        for i in range(n):
            j = (i + 1) % n
            area += poly[i][0] * poly[j][1]
            area -= poly[j][0] * poly[i][1]
        area = abs(area) / 2 * 0.16
        return area

    def poly_rotations(self, poly):
        vertex = []
        for i in range(-1, len(poly) - 1):
            dif1 = ((poly[i][0] - poly[i - 1][0]), (poly[i][1] - poly[i - 1][1]))
            dif2 = ((poly[i + 1][0] - poly[i][0]), (poly[i + 1][1] - poly[i][1]))
            inner_product = (dif1[0] * dif2[0]) + (dif1[1] * dif2[1])
            dif1_length = sqrt(dif1[0] ** 2 + dif1[1] ** 2)
            dif2_length = sqrt(dif2[0] ** 2 + dif2[1] ** 2)
            cos_value = inner_product / (dif1_length * dif2_length)
            new_poly = poly[:]
            new_poly.pop(i)
            area = self.polygon_area(poly)
            new_area = self.polygon_area(new_poly)
            if new_area > area:
                convex = 1
            else:
                convex = 0
            vertex.append((cos_value, convex, dif1_length, dif2_length))
        nb_of_invariant_rotations = 0
        for i in range(1, len(vertex) + 1):
            new_vertex = vertex[len(vertex) - i:len(vertex)] + vertex[:-i]
            if new_vertex == vertex:
                nb_of_invariant_rotations += 1
        return nb_of_invariant_rotations

    def polygon_depth(self, poly):
        depth = 0
        x = poly[0][0]
        y = poly[0][1]
        for i in self.polygons:
            is_point_inside_polygon = self.point_inside_polygon(x, y, self.polygons[i])
            if is_point_inside_polygon:
                depth += 1
        return depth

    def poly_convex(self, area, poly):
        convex = 'yes'
        if len(poly) != 3:
            for i in range(len(poly)):
                new_poly = poly[:]
                new_poly.pop(i)
                new_area = self.polygon_area(new_poly)
                if new_area > area:
                    convex = 'no'
                    break
        return convex

    def get_polygons(self, poly):
        points_not_vertex = []
        for i in range(-1, len(poly) - 1):
            dif1 = ((poly[i][0] - poly[i - 1][0]), (poly[i][1] - poly[i - 1][1]))
            dif2 = ((poly[i + 1][0] - poly[i][0]), (poly[i + 1][1] - poly[i][1]))
            if dif1 == dif2:
                points_not_vertex.append(poly[i])
        for i in points_not_vertex:
            poly.remove(i)
        return poly
