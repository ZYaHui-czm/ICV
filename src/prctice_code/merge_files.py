def merge_files(filenames , output):
    '''依次打开列表里的文件'''
    for file in filenames:
        try:
            '''逐行读取该文件的内容并写入新文件'''
            with open(file,'r',encoding="utf-8") as f:
                for line in f:
                    with open(output,'a',encoding="utf-8") as o:
                        o.write(line)
            print(f'The {output} was successfully created')
            '''检测该文件是否存在'''
        except FileNotFoundError:
            print(f'{file} Not Found')
    return output

'''运行'''
if __name__ == "__main__":
    print("请输入文件名：")
    '''获取文件名列表'''
    filenames = [x for x in input().split()]
    output = input("输出文件名为：")
    merge_files(filenames,output)