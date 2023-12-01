f = open("day6Input.txt", 'r')


with open('day6Input.txt') as f:
    for line in f:
        arr=["","","","","","","","","","","","","",""]
        count=0
        number=0
        for letter in line:
            number+=1
            if ("" in arr) or (len(arr)<14):
                if len(arr)<14:
                    if letter in arr:
                        arr=arr[arr.index(letter)+1:]
                    arr.append(letter)
                elif letter in arr:
                    arr=arr[arr.index(letter)+1:]
                    arr.append(letter)
                else:
                    arr.pop(0)
                    arr.append(letter)
            else:
                print(arr," ",number-1)
                print("lll")
                break

f.close()