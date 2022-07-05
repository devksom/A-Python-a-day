#A program where lst = [10,30,55 ,70, 90] Check the sum of the numbers in the list.
#if they are not equal to 500, add the difference to the list to make the summ 500
#Display the initial sum
#Display the difference added to reach 500
#Print the New list

lst = [10,30,55 ,70, 90]

print(lst)

total=sum(lst)
print("Initial sum of lst is "+ str(total))
if total<500:
    diff=500-total
    total=total+diff
    new_list=lst.append(diff)

print("I added " +str(diff) + " to the list to get " + str(total))
print("Our new List is now "+ str(lst))
print(total)