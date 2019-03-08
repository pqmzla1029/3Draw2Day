clc
clear all
close all

x = xlsread('text.xlsx',1,'A1:A2711');
y = xlsread('text.xlsx',1,'B1:B2711');
z = xlsread('text.xlsx',1,'C1:C2711');

scatter3(x,y,z)