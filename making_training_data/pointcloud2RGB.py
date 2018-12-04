import os
import numpy as np
import pandas as pd
import glob
import matplotlib.pyplot as plt
import scipy
import skimage #搜索scipy 会出来
from skimage import io
from skimage import morphology
from skimage import measure

category_path='D:\lxy\DFC-pointcloud\data/training/category'
intensity_path='D:\lxy\DFC-pointcloud\data/training/intensity'
pts_path='D:\lxy\DFC-pointcloud\data/training/pts'
outpicture_path='D:\lxy\DFC-pointcloud\data/training/outpicture700500'
outtxt_path='D:\lxy\DFC-pointcloud\data/training/outtxt700500'

size_ROI={}
size_ROI['minX'] = -35; size_ROI['maxX'] = 35; size_ROI['minY'] = -25; size_ROI['maxY'] = 25
size_ROI['minZ'] = -2; size_ROI['maxZ'] = 2

size_cell=0.1
height_thresold=0.05

def removePoints(PointCloud, BoundaryCond):
    minX = BoundaryCond['minX']
    maxX = BoundaryCond['maxX']
    minY = BoundaryCond['minY']
    maxY = BoundaryCond['maxY']
    minZ = BoundaryCond['minZ']
    maxZ = BoundaryCond['maxZ']

    # Remove the point out of range x,y,z
    mask = np.where((PointCloud[:, 0] > minX) & (PointCloud[:, 0] < maxX) & (PointCloud[:, 1] > minY) & (
                PointCloud[:, 1] < maxY) & (PointCloud[:, 2] >= minZ) & (PointCloud[:, 2] <= maxZ))
    PointCloud = PointCloud[mask]
    return PointCloud

def makeBVFeature(PointCloud_origin, BoundaryCond, size_cell):  # Discretization：ROI长度（m)/该长度方向上的栅格数，即每个cell的边长
    Height=700
    Width=500
    # Height = np.int(np.floor((BoundaryCond['maxX']-BoundaryCond['minX'])/size_cell))#PYTHON 中 float/float结果不准，例如121.6/0.1=1215.99999999
    # Width = np.int(np.floor((BoundaryCond['maxY']-BoundaryCond['minY'])/size_cell))

    PointCloud = removePoints(PointCloud_origin, BoundaryCond)
    PointCloud[:, 0] = BoundaryCond['maxX'] - PointCloud[:, 0]  # 坐标系统一为左上角
    PointCloud[:, 1] = BoundaryCond['maxY'] - PointCloud[:, 1]

    # PointCloud_grid = np.copy(PointCloud )
    PointCloud[:, 0] = np.int_(np.floor(PointCloud[:, 0] / size_cell))  # np.floor 返回不大于输入参数的最大整数；
    PointCloud[:, 1] = np.int_(
        np.floor(PointCloud[:, 1] / size_cell))  # 将点云坐标转化为栅格坐标，python数组从0开始，所以不用+1，matlab从0开始，所以需要+1

    # sort-3times
    indices = np.lexsort((-PointCloud[:, 2], PointCloud[:, 1], PointCloud[:, 0]))  #  np.lexsort((b,a)) 先对a排序，再对b.排序按x轴(栅格）进行从小到大排列，当x值相同时，按y轴（栅格）从小到大排序，y也相同时，按z从大到小排序
    PointCloud = PointCloud[indices]                                                #  目的是将每个栅格的最大z排在最前面，下面unique时，便只会保留z最大值（排在第一位）的索引

    # Height Map& DensityMap
    heightMap = np.zeros((Height, Width))  # 括号括起来 表示是一个参数，即np.zeros（）的第一个参数是（Height,Width)
    densityMap = np.zeros((Height, Width))
    # _, indices, counts = np.unique(PointCloud[:, 0:2], axis=0, return_index=True, return_counts=True)  # 除去重复的元素，return_index=True表示返回新列表元素在旧列表中的索引,注意0:2含左不含右，即只是指0,1，也就是每个栅格中只保留第一个（z最大的）
    # aa=0
    # for num_cell in range(counts.size):  #遍历每一个存在点的栅格,max_min+单点滤波
    #     linshi=PointCloud[aa:(aa+counts[num_cell]), 0:3]
    #     if len(linshi)==1:
    #         continue
    #     if (max(linshi[:,2])-min(linshi[:,2]))<height_thresold:
    #         PointCloud[aa:(aa + counts[num_cell]), 0:3]=0
    #     aa = aa + counts[num_cell]
    # index=np.where((PointCloud[:, 0] != 0)&(PointCloud[:, 1]  != 0)&(PointCloud[:, 2]  != 0))
    # PointCloud=PointCloud[index]

    _, indices, counts = np.unique(PointCloud[:, 0:2], axis=0, return_index=True, return_counts=True)

    PointCloud_frac = PointCloud[indices]                                                             # counts返回的是每个元素在原始数组出现的次数，这里是每个存在点的栅格中点的数量
    # some important problem is image coordinate is (y,x), not (x,y)
    height_z=np.int(BoundaryCond['maxZ']) - np.int(BoundaryCond['minZ'])
    heightMap[np.int_(PointCloud_frac[:, 0]), np.int_(PointCloud_frac[:, 1])] = (PointCloud_frac[:, 2]+2)/height_z
    heightMap.astype(np.int)
    normalizedCounts = np.minimum(1.0, np.log(counts + 1) / np.log(64))  # 即normalizedCounts最大为1
    densityMap[np.int_(PointCloud_frac[:, 0]), np.int_(PointCloud_frac[:, 1])] = normalizedCounts/1
    densityMap.astype(np.int)
    classMap=np.zeros((Height, Width),dtype=np.int32)
    aaa=0
    for num_cell in range(counts.size):  #遍历每一个存在点的栅格
        linshi=PointCloud[aaa:(aaa+counts[num_cell]), 4]  #该栅格中的所有点
        if np.sum(linshi)==0:
            aaa = aaa + counts[num_cell]  #aaa表示该栅格中点的起始序号
            continue
        num1=np.sum(linshi==1)      #统计每个栅格中各类障碍物点的数量
        num2=np.sum(linshi==2)
        num3=np.sum(linshi==3)
        num4=np.sum(linshi==4)
        num5=np.sum(linshi==5)
        num6=np.sum(linshi==6)
        num7=np.sum(linshi==7)
        cell_label=np.max((num1,num2,num3,num4,num5,num6,num7))
        if cell_label==num5:
            cell_label=5
        elif cell_label==num1:
            cell_label=1
        elif cell_label==num3:
            cell_label=3
        elif cell_label==num6:
            cell_label=6
        elif cell_label==num2:
            cell_label=2
        elif cell_label==num4:
            cell_label=4
        elif cell_label == num7:
            cell_label = 7
        classMap[np.int(PointCloud[aaa, 0]), np.int(PointCloud[aaa, 1])] = cell_label
        aaa = aaa + counts[num_cell]
    classMap = skimage.morphology.dilation(classMap, np.ones((6, 5)))
    classMap = skimage.morphology.closing(classMap, np.ones((6, 5)))
    zero_one=measure.label(classMap,connectivity=2)  #连通区域标记
    object_list = measure.regionprops(zero_one)
    for num_object in object_list:
        min_x,min_y,max_x,max_y=num_object.bbox #栅格图中的x、y与实际图像坐标系中的xy是相反的
        width=max_x-min_x
        height=max_y-min_y
        #idx_ndarry=np.where((classMap[:,0]>=min_x)&(classMap[:,0]<=max_x)&(classMap[:,1]>=min_y)&(classMap[:,1]<=max_y))
        this_object=classMap[min_x:max_x,min_y:max_y]
        index_label=np.where(this_object>0)
        x_ = index_label[0][0]+min_x
        y_ = index_label[1][0]+min_y
        label_object=classMap[x_,y_]
        # 标签转换
        if label_object == 1:
            label_object = 'cyclist'
        elif label_object == 2:
            label_object = 'tricycle'
        elif label_object == 3:
            label_object = 'smallMot'
        elif label_object == 4:
            label_object='bigMot'
        elif label_object == 5:
            label_object='pedestrian'
        elif label_object == 6:
            label_object = 'crowds'
        elif label_object == 7:
            label_object = 'unknown'

        txt=open(outtxt,'a')
        txt.write(str(min_x))
        txt.write(' ')
        txt.write(str(min_y))
        txt.write(' ')
        txt.write(str(width))
        txt.write(' ')
        txt.write(str(height))
        txt.write(' ')
        txt.write(str(label_object))
        txt.write('\n')
        txt.close()
    # io.imshow(classMap_pengzhang)
    # io.show()
    # plt.imshow(classMap)
    # plt.show()
    # x_min,y_min,width,height = cv2.boundingRect(classMap)
    # Intensity Map
    intensityMap = np.zeros((Height, Width))
    indices = np.lexsort((-PointCloud[:, 3], PointCloud[:, 1], PointCloud[:, 0]))  # 按x由小到大，y由小到大， intensity由大到小
    PointCloud_intensity = PointCloud[indices]
    _, indices= np.unique(PointCloud_intensity[:, 0:2], axis=0, return_index=True)  # 只保留每个栅格中intensity最大的点
    PointCloud_max_intensity = PointCloud_intensity[indices]
    intensityMap[np.int_(PointCloud_max_intensity[:, 0]), np.int_(PointCloud_max_intensity[:, 1])] = PointCloud_max_intensity[:, 3]  # 将反射强度放大100倍
    intensityMap.astype(np.int)


    RGB_Map = np.zeros((Height, Width, 3))
    RGB_Map[:, :, 0] = densityMap  # r_map
    # plt.imshow(densityMap)
    # plt.show()
    RGB_Map[:, :, 1] = heightMap  # g_map
    # plt.imshow(heightMap)
    # plt.show()
    RGB_Map[:, :, 2] = intensityMap  # b_map
    # plt.imshow(intensityMap)
    # plt.show()

    grid_picture = RGB_Map[0:Height, 0:Width, :]
    # plt.imshow(grid_picture)
    # plt.show()
    # plt.imsave(outpicture+'R'+'.png', densityMap)
    # plt.imsave(outpicture+'G'+'.png', heightMap)
    # plt.imsave(outpicture+'B'+'.png', intensityMap)
    # plt.imsave(outpicture + 'C' + '.png', classMap)
    plt.imsave(outpicture, grid_picture)
    #return grid_picture

def show_pc(pc):
    x = pc[:, 0]
    y = pc[:, 1]
    z = pc[:, 2]
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.scatter(x, y, z, marker='.')
    plt.show()

#nb_frame=glob.glob(r'D:\lxy\DFC-pointcloud\data/training/pts/*.csv')

for frame_name in os.listdir(pts_path):
    category_file = pd.read_csv(os.path.join(category_path, frame_name))
    intensity_file = pd.read_csv(os.path.join(intensity_path, frame_name))
    pts_file = pd.read_csv(os.path.join(pts_path, frame_name))
    # category_file = pd.read_csv(os.path.join(category_path,'000d4e61-1203-4819-98ab-afbb619010b0_channelVELO_TOP.csv'))
    # intensity_file = pd.read_csv(os.path.join(intensity_path, '000d4e61-1203-4819-98ab-afbb619010b0_channelVELO_TOP.csv'))
    # pts_file = pd.read_csv(os.path.join(pts_path, '000d4e61-1203-4819-98ab-afbb619010b0_channelVELO_TOP.csv'))
    #category_file = pd.read_csv('D:\lxy\DFC-pointcloud\data/testing\shiyan-pts/000ac4dd-fd8e-43fd-95d2-d8aefc678b23_channelVELO_TOP.csv')
    #PointCloud =np.array(category_file)
    PointCloud = np.hstack((pts_file, intensity_file, category_file))
    file_name = frame_name.split('.')[0]
    outpicture = outpicture_path+'/'+file_name+'.png'
    outtxt= outtxt_path+'/'+file_name+'.txt'
    # if os.path.exists(outtxt):
    #     continue
    #show_pc(PointCloud)
    makeBVFeature(PointCloud, size_ROI, size_cell)