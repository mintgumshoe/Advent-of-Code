# AoC 2015 - Day 2
import os 

with open('input.txt') as file1:
    boxes = file1.readlines()

def calculatePaper(box): 
    bd = box.rstrip().split('x') # Array of the 3 measurements
    
    l = int(bd[0])
    w = int(bd[1])
    h = int(bd[2])
    
    # surface area = (2*l*w) + (2*w*h) + (2*h*l)
    
    # Calc the sides
    side1 = l * w
    side2 = w * h
    side3 = h * l 

    # Find the smallest of these 3
    small = min(side1, side2, side3)

    # Add it up, double it, add the excess, and return it
    return (2 * (side1 + side2 + side3)) + small
  
papertotal = 0
for box in boxes: 
    papertotal += calculatePaper(box)

print(f"Paper required: {papertotal} sq ft")

# Part 2 
def calculateRibbon(box): 
    bd = box.rstrip().split('x') # Array of the 3 measurements, in ascending order
    bd = [ int(x) for x in bd ]
    bd.sort()
    
    a = int(bd[0]) # smallest
    b = int(bd[1])
    c = int(bd[2]) # largest
    
    peri = a + a + b + b 
    area = a * b * c

    return peri + area 
    
ribbontotal = 0
for box in boxes: 
    ribbontotal += calculateRibbon(box)

print(f"Ribbon required: {ribbontotal} ft")
