# Welcome to my git repo for Advent of Code 2022!
 In here I will be documenting my experience with the Advent of code, day by day.
 I hope this will prove useful and I'll be able to look back on this in the future

## Day 1
Phew been a while since I've done Python, especially file management
Managed to get it done though, found an implementation that I really liked:

'''python
    f=open('day1Input.txt','r')
    with open('day1Input.txt') as f:
        lines = [line.rstrip() for line in f]
    f.close()
'''

so i slightly edited it, because it was too advanced for the purpose I needed it for.

I did fail part 2 initially, only because I forgot to make it push all values below down. After fixing that, I passed it.


