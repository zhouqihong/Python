%cake base1
 
[base1_x base1_y base1_z]=cylinder(0.8,100);
surf(base1_x,base1_y,base1_z/3+0.5,'facecolor',[94/255 38 /255  18 /255],'linestyle','none');  hold on
  
base1_z_max=max(base1_z/3+0.5);
base1_z_max=base1_z_max(1);
x1_top=0.8*cos(linspace(0,2*pi,1000));
y1_top=0.8*sin(linspace(0,2*pi,1000));
z1_top=ones(size(x1_top))*base1_z_max;
   
fill3(x1_top,y1_top,z1_top,'y', 'facecolor',[138/255 54 /255  15 /255]);

%cake base2
  
[base2_x base2_y base2_z]=cylinder(1,100);
surf(base2_x,base2_y,base2_z/2,'facecolor',[81/255 149/255 72/255],'linestyle','none'); 
  
base2_z_max=max(base2_z/2);
base2_z_max=base2_z_max(1);
x2_top=cos(linspace(0,2*pi,1000));
y2_top=sin(linspace(0,2*pi,1000));
z2_top=ones(size(x2_top))*base2_z_max;
    
fill3(x2_top,y2_top,z2_top,'y', 'facecolor',[152/255  251 /255  152/255]);
   
%cake candles
for i=1:22
  [x_can y_can z_can]=cylinder(0.015,22);
  z_can=z_can/4+.7333;
  x_can=x_can+0.7*cos(i*pi/22*2);
  y_can=y_can+0.7*sin(i*pi/22*2);
  surf(x_can,y_can,z_can,'facecolor',[250/255 2/255  60/255]); axis equal
end
   
%cake text
text(0-0.5, 0.2,0.9,'Yanyan,happy birthday!','FontSize',22,...
  'FontName','Monotype Corsiva','Color',[1 0 0]);
