# 数据集在../data/中，结果存放在../all/中
import os
import sys
from shutil import copyfile
import re


def dataprepare(ifilepath = '../data',ofilepath = '../all'):
    if os.path.exists(ofilepath):
        print('数据集已创建，无需再次创建')
        return
    if not os.path.exists(ifilepath):
        print('错误，源数据集不存在\n')
        sys.exit()
    os.makedirs(ofilepath)
    os.makedirs(os.path.join(ofilepath, 'train_all'))
    os.makedirs(os.path.join(ofilepath, 'train'))
    os.makedirs(os.path.join(ofilepath, 'val'))
    prepare_Market(ifilepath,ofilepath)
    prepare_DukeMTMC(ifilepath, ofilepath)
    prepare_CUHK03(ifilepath, ofilepath)


def prepare_Market(ifilepath = '../data',ofilepath = '../all'):
    ipath = os.path.join(ifilepath, 'Market-1501')
    if not os.path.exists(ipath):
        print('Market-1501数据集不存在\n')
        return
    print('******处理Market-1501中******')
    extract_market(os.path.join(ipath,'bounding_box_train'),os.path.join(ofilepath,'train_all'))
    extract_market(os.path.join(ipath,'query'),os.path.join(ofilepath,'train_all'))
    extract_market(os.path.join(ipath,'bounding_box_test'),os.path.join(ofilepath,'val'),'val')
    print('******Market-1501处理完成******')

def extract_market(src_path, dst_dir,sg='train'):
    img_names = os.listdir(src_path)
    count = 0
    # 定义正则表达式，数字_c数字
    pattern = re.compile(r'([-\d]+)_c(\d)')
    for img_name in img_names:
        # 判断是否是jpg格式的图片
        if '.jpg' not in img_name:
            continue
        # pid: 每个人的标签编号 1
        # _  : 摄像头号 2
        ID = img_name.split('_')
        pid, _ = map(int, pattern.search(img_name).groups())
        # 去掉没用的图片
        if pid == 0 or pid == -1:
            continue
        dst = os.path.join(dst_dir,ID[0])
        if not os.path.exists(dst):
            if sg == 'val':
                if count >= 300:
                    continue
            os.makedirs(dst)
            count = count + 1
        copyfile(os.path.join(src_path, img_name), os.path.join(dst, img_name))

def prepare_DukeMTMC(ifilepath = '../data',ofilepath = '../all'):
    ipath = os.path.join(ifilepath, 'DukeMTMC-reID')
    if not os.path.exists(ipath):
        print('DukeMTMC-reID数据集不存在\n')
        return
    print('******处理DukeMTMC中******')
    extract_dukemtmc(os.path.join(ipath,'bounding_box_train'),os.path.join(ofilepath,'train_all'))
    extract_dukemtmc(os.path.join(ipath,'query'),os.path.join(ofilepath,'train_all'))
    extract_dukemtmc(os.path.join(ipath,'bounding_box_test'),os.path.join(ofilepath,'val'),'val')
    print('******DukeMTMC处理完成******')

def extract_dukemtmc(src_path, dst_dir,sg='train'):
    img_names = os.listdir(src_path)
    count = 0
    # 定义正则表达式，数字_c数字
    pattern = re.compile(r'([-\d]+)_c(\d)')
    for img_name in img_names:
        # 判断是否是jpg格式的图片
        if '.png' not in img_name and '.jpg' not in img_name:
            continue
        ID = img_name.split('_')
        # pid: 每个人的标签编号 1
        # _  : 摄像头号 2
        pid, _ = map(int, pattern.search(img_name).groups())
        dst = os.path.join(dst_dir,str(pid + 1501))
        if not os.path.exists(dst):
            if sg == 'val':
                if count >= 300:
                    continue
            os.makedirs(dst)
            count = count + 1
        copyfile(os.path.join(src_path, img_name), os.path.join(dst, img_name))


def prepare_CUHK03(ifilepath = '../data',ofilepath = '../all'):
    ipath = os.path.join(ifilepath, 'CUHK03-np')
    if not os.path.exists(ipath):
        print('CUHK03数据集不存在\n')
        return
    print('******处理CUHK03中******')
    inpath = os.path.join(ipath,'detected')
    extract_cuhk03(os.path.join(inpath,'bounding_box_train'),os.path.join(ofilepath,'train_all'))
    extract_cuhk03(os.path.join(inpath,'query'),os.path.join(ofilepath,'train_all'))
    extract_cuhk03(os.path.join(inpath,'bounding_box_test'),os.path.join(ofilepath,'val'),'val')
    inpath = os.path.join(ipath, 'labeled')
    extract_cuhk03(os.path.join(inpath, 'bounding_box_train'), os.path.join(ofilepath, 'train_all'))
    extract_cuhk03(os.path.join(inpath, 'query'), os.path.join(ofilepath, 'train_all'))
    extract_cuhk03(os.path.join(inpath, 'bounding_box_test'), os.path.join(ofilepath, 'val'),'val')
    print('******CUHK03处理完成******')

def extract_cuhk03(src_path, dst_dir, sg='train'):
    img_names = os.listdir(src_path)
    count = 0
    # 定义正则表达式，数字_c数字
    pattern = re.compile(r'([-\d]+)_c(\d)')
    for img_name in img_names:
        # 判断是否是jpg格式的图片
        if '.png' not in img_name and '.jpg' not in img_name:
            continue
        ID = img_name.split('_')
        # pid: 每个人的标签编号 1
        # _  : 摄像头号 2
        pid, _ = map(int, pattern.search(img_name).groups())
        dst = os.path.join(dst_dir,str(pid + 8641))
        if not os.path.exists(dst):
            if sg == 'val':
                if count >= 300:
                    continue
            os.makedirs(dst)
            count = count + 1
        copyfile(os.path.join(src_path, img_name), os.path.join(dst, img_name))

if __name__ == '__main__':
    inputfile = '../data'
    outputfile = '../all'
    dataprepare(inputfile,outputfile)

