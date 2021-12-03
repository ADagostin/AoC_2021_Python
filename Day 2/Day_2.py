# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def P1():
    with open('c:\\Users\\Andre\\Desktop\\Data.txt') as f:
        Instructions=f.readlines()
        Horizontal=0
        Depth=0
        for Single_Instruction in Instructions:
            Direction, Dir_Mag = Single_Instruction.split()
            Dir_Mag = int(Dir_Mag)
            if Direction == "forward":
                Horizontal+=Dir_Mag
            if Direction == 'up':
                Depth-=Dir_Mag
            if Direction == 'down':
                Depth+=Dir_Mag
    print (Horizontal*Depth)

def P2():
    with open('c:\\Users\\Andre\\Desktop\\Data.txt') as f:
        Instructions=f.readlines()
        Horizontal=0
        Depth=0
        Aim=0
        for Single_Instruction in Instructions:
            Direction, Dir_Mag = Single_Instruction.split()
            Dir_Mag = int(Dir_Mag)
            if Direction == "forward":
                Horizontal+=Dir_Mag
                Depth+=Aim*Dir_Mag
            if Direction == 'up':
                Aim-=Dir_Mag
            if Direction == 'down':
                Aim+=Dir_Mag
    print (Horizontal*Depth)

