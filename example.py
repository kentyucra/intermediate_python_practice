def merge_the_tools(string, k):
    n = len(string)
    size = k
    k = int(n/k)
    for i in range(k):
        index1 = int(i*size)
        index2 = int((i+1)*size)
        substring = string[index1: index2]
        my_list = []
        dictionary = dict()
        for char in substring:
            if char in dictionary:
                pass
            else:
                dictionary[char] = True
                my_list.append(char)
        
        print(''.join(my_list))
        
        
            
    

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
