import os
import argparse
import shutil

def func(args):
#     ------------- parse command line input args -------------
    ratio = ['cs','bf'] if args.ratio is None else [x.lower() for x in args.ratio]    
    
#     ratio for analysis
    ratio_dict = dict()
    for i in ratio:   
        if i=='cs':
            ratio_dict.update({'calendar':[1,-1]})
        elif i=='bf':
            ratio_dict.update({'butterfly':[1,-2,1]})
        elif i=='bx':
            ratio_dict.update({'box':[1,-1,-1,1]})
            
#     --------------- run analysis ---------------
    for ratio_key, ratio_value in ratio_dict.items():
#         check if png output directory exists
        mmlist = [str(i).zfill(2) for i in list(range(0,13))]
        for mm in mmlist:        
            odirmm = os.path.join(os.getcwd(), ratio_key, mm)
            if not os.path.exists(odirmm):
                os.makedirs(odirmm)

#         copy files to specified month folder
        src = os.path.join(os.getcwd(), ratio_key)
        print(src, 'copy files to specified month folder')       
        for ff in os.listdir(src):
            xx = ff.split('.')
            if len(xx)==5:
                if xx[-1]=='png' and xx[-2] in mmlist:
                    dst = os.path.join(src, xx[-2])
                    shutil.copyfile(os.path.join(src,ff), os.path.join(dst,ff))

def main():
    parser = argparse.ArgumentParser(usage='Copy Files to Month Folder')
    parser.add_argument('-r', '--ratio', nargs='*', action='store')
    args = parser.parse_args()
#     print(args)
    try:
        func(args)
    except Exception as e: 
        print(__file__, '\n', e)  
                                
if __name__ == '__main__':
    main()
    
# cd 'Z:\williamyizhu On My Mac\Documents\workspace\PyAnalysis'
# python .\month_list.py -r cs bf
