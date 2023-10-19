def is_leap(n):
    return n%4==0 and not(n%100==0 and not(n%400==0))

year = int(input())
print(is_leap(year))