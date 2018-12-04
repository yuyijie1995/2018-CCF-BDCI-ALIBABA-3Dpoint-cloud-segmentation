pts=csvread('G:\研究生\课题组\比赛\CCF点云分割\DCF_test\DCF_test\pts_test/000d4e61-1203-4819-98ab-afbb619010b0_channelVELO_TOP.csv');
category=csvread('G:\研究生\课题组\比赛\CCF点云分割\DCF_test\DCF_test\category_test/000d4e61-1203-4819-98ab-afbb619010b0_channelVELO_TOP.csv');
% upload1=csvread('J:\11_11\cyc0.9_unknow0.4/000d4e61-1203-4819-98ab-afbb619010b0_channelVELO_TOP.csv');
% upload2=csvread('J:\11_11\gaodu_limit/000d4e61-1203-4819-98ab-afbb619010b0_channelVELO_TOP.csv');
% upload3=csvread('N:\11-11tiaocan\cyc0.8unknow0.3/000d4e61-1203-4819-98ab-afbb619010b0_channelVELO_TOP.csv');
% upload4=csvread('N:\11-11tiaocan\0.4_0.4/000d4e61-1203-4819-98ab-afbb619010b0_channelVELO_TOP.csv');
% upload5=csvread('G:\研究生\课题组\比赛\dcf\11-11tiaocan2\cyc_unknow0.45/000d4e61-1203-4819-98ab-afbb619010b0_channelVELO_TOP.csv');
% upload6=csvread('G:\研究生\课题组\比赛\dcf\DCF_test\DCF_test\upload11_10_wuyuzhi/00d264b8-8008-4135-9c2c-ff696516b328_channelVELO_TOP.csv');
% upload7=csvread('G:\研究生\课题组\比赛\dcf\DCF_test\DCF_test\upload11_10aug/000d4e61-1203-4819-98ab-afbb619010b0_channelVELO_TOP.csv');
% upload8=csvread('G:\研究生\课题组\比赛\dcf\新建文件夹\DCF_test\upload11_10_0.2/000d4e61-1203-4819-98ab-afbb619010b0_channelVELO_TOP.csv');
% upload9=csvread('G:\研究生\课题组\比赛\dcf\新建文件夹\DCF_test\upload11_10_0.3/000d4e61-1203-4819-98ab-afbb619010b0_channelVELO_TOP.csv');
% upload10=csvread('G:\研究生\课题组\比赛\dcf\新建文件夹\DCF_test\upload11_10_0.45/000d4e61-1203-4819-98ab-afbb619010b0_channelVELO_TOP.csv');

intensity=csvread('M:/intensity/000d4e61-1203-4819-98ab-afbb619010b0_channelVELO_TOP.csv');
% picture=imread('C:\Users\louxy126\Desktop\jiancha/0012ac79-75ec-4e36-94dd-1500eb27fda1_channelVELO_TOP.png');
% imshow(picture);
% rectangle('Position',[359 32 26 56],'EdgeColor','g','LineWidth',1.5);
% rectangle('Position',[292 490 24 36],'EdgeColor','g','LineWidth',1.5);
% %category=csvread('M:/category/000d4e61-1203-4819-98ab-afbb619010b0_channelVELO_TOP.csv');
x=pts(:,1);
y=pts(:,2);
z=pts(:,3);

scatter3(x,y,z,'.','black')
% intensity=intensity(:,1);
% category=category(:,1);
DontCare=pts(category==0,:);
cyclist=pts(category==1,:);
tricycle=pts(category==2,:);
smallMot=pts(category==3,:);
bigMot=pts(category==4,:);
pedestrian=pts(category==5,:);
crowds=pts(category==6,:);
unknown=pts(category==7,:);
% 
% DontCare=pts(upload1==0,:);
% cyclist=pts(upload1==1,:);
% tricycle=pts(upload1==2,:);
% smallMot=pts(upload1==3,:);
% bigMot=pts(upload1==4,:);
% pedestrian=pts(upload1==5,:);
% crowds=pts(upload1==6,:);
% unknown=pts(upload1==7,:);
% 
% DontCare=pts(upload2==0,:);
% cyclist=pts(upload2==1,:);
% tricycle=pts(upload2==2,:);
% smallMot=pts(upload2==3,:);
% bigMot=pts(upload2==4,:);
% pedestrian=pts(upload2==5,:);
% crowds=pts(upload2==6,:);
% unknown=pts(upload2==7,:);

% DontCare=pts(upload3==0,:);
% cyclist=pts(upload3==1,:);
% tricycle=pts(upload3==2,:);
% smallMot=pts(upload3==3,:);
% bigMot=pts(upload3==4,:);
% pedestrian=pts(upload3==5,:);
% crowds=pts(upload3==6,:);
% unknown=pts(upload3==7,:);
% 
% 
% DontCare=pts(upload4==0,:);
% cyclist=pts(upload4==1,:);
% tricycle=pts(upload4==2,:);
% smallMot=pts(upload4==3,:);
% bigMot=pts(upload4==4,:);
% pedestrian=pts(upload4==5,:);
% crowds=pts(upload4==6,:);
% unknown=pts(upload4==7,:);
% 
scatter(cyclist(:,1),cyclist(:,2),'.','r')
hold on 
scatter(tricycle(:,1),tricycle(:,2),'.','black')
hold on 
scatter(smallMot(:,1),smallMot(:,2),'.','g')
hold on 
scatter(bigMot(:,1),bigMot(:,2),'.','g')
hold on 
scatter(pedestrian(:,1),pedestrian(:,2),'.','y')
hold on 
scatter(crowds(:,1),crowds(:,2),'.','y')
hold on 
scatter(unknown(:,1),unknown(:,2),'.','m')
hold on 
axis([-80, 80, -60, 60]);
% 
% DontCare=pts(category==0,:);
% cyclist=pts(category==1,:);
% tricycle=pts(category==2,:);
% smallMot=pts(category==3,:);
% bigMot=pts(category==4,:);
% pedestrian=pts(category==5,:);
% crowds=pts(category==6,:);
% unknown=pts(category==7,:);
% 
% 
% scatter(cyclist(:,1),cyclist(:,2),'.','r')
% hold on 
% scatter(tricycle(:,1),tricycle(:,2),'.','r')
% hold on 
% scatter(smallMot(:,1),smallMot(:,2),'.','g')
% hold on 
% scatter(bigMot(:,1),bigMot(:,2),'.','g')
% hold on 
% scatter(pedestrian(:,1),pedestrian(:,2),'.','y')
% hold on 
% scatter(crowds(:,1),crowds(:,2),'.','y')
% hold on 
% scatter(unknown(:,1),unknown(:,2),'.','m')
% hold on 
% axis([-45, 45, -30, 30]);
% scatter3(pts(:,1),pts(:,2),pts(:,3),'.','k')

% for num=1:size(pts,1)
%     scatter(pts(num,1),pts(num,2),'.','r')
% %     scatter3(pts(num,1),pts(num,2),pts(num,3),'.','r')
%     hold on
% end
% % 黑色：DontCare 红色：cyclist 绿色：smallMot 黄色：pedestrian 紫红：unknown
% scatter3(DontCare(:,1),DontCare(:,2),DontCare(:,3),'.','k')

% scatter3(0,10,0,'*','r')
hold on 
scatter3(cyclist(:,1),cyclist(:,2),cyclist(:,3),'.','r')
hold on 
scatter3(tricycle(:,1),tricycle(:,2),tricycle(:,3),'.','r')
hold on 
scatter3(smallMot(:,1),smallMot(:,2),smallMot(:,3),'.','g')
hold on 
scatter3(bigMot(:,1),bigMot(:,2),bigMot(:,3),'.','g')
hold on 
scatter3(pedestrian(:,1),pedestrian(:,2),pedestrian(:,3),'.','y')
hold on 
scatter3(crowds(:,1),crowds(:,2),crowds(:,3),'.','y')
hold on 
scatter3(unknown(:,1),unknown(:,2),unknown(:,3),'.','m')
hold on 
scatter3(DontCare(:,1),DontCare(:,2),DontCare(:,3),'.','black')