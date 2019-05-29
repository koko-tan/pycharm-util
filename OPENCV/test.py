# 题目
# 列表中[1,1,1,1] 表示 1的串，
# 求只包含0和1的list中最长1的串的开始和结束的 Index
# 例如
# list = [0,0,0,1,1,1,1,1,1,0,0,0,0,1,1,1,0,0,0]
# 中包含两个1的串，最长1的串就是
# idx_start = 3
# idx_end = 8
#
# 如果没有，就返回
# idx_start = -1
# idx_end = -1




def TEST_DO_NOT_CHANGE(in_list):
    idx_start = -1  
    idx_end = -1    
    ########## 下面可以改动
    start = -1
    end = -1
    maxLen = 0
    for i in range(len(in_list)):
        if in_list[i] == 1:
            if start == -1:
                start = i
                end = i
            else:
                end += 1
        else:
            if start != -1:
                temp = end - start + 1
                if temp > maxLen:
                    maxLen = temp
                    idx_start = start
                    idx_end = end
                    start = -1
                    end = -1
    #下面这个判断用于处理末尾最后一位是1的情况
    #如果不加这个判断，那么最后一串连续的1无论有多长，
    #都无法进入上面的else更新idx_start和idx_end
    if end - start + 1 > maxLen:
        idx_start = start
        idx_end = end
    ########## 上面可以改动    
    return idx_start, idx_end


if __name__ == "__main__":
    list = [0,0,0,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,0]
    print(TEST_DO_NOT_CHANGE(list))
    list = [0,0,0,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1]
    print(TEST_DO_NOT_CHANGE(list))