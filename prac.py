
def count_substring(string, sub_string):
    count = 0
    string = list(string)
    sub_string = list(sub_string)
    subs = [string[i:j] for i in range(len(string)) for j in range(i+1,len(string)+1)]
    for x in subs:
        if(x == sub_string):
            count = count+1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)