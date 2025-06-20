# lst =[1,2,2,3,3,4,5,6,6]
#avoid duplicates
# lst =set(lst)
# lst = list(lst)
# print(lst)

#reverse- list[start:stop:step] [::-1] slicing-এর মাধ্যমে list-কে পেছন দিক থেকে এক এক করে নিয়ে নতুন list বানায়।

# lst = lst[::-1]
# print(lst)

#check palindrome
# a ='madam'
# b = a[::-1] #reverse
# print(a==b)

#list comprehension
#{key: value for item in iterable} এটা হলো Python-এর একটি সংক্ষিপ্ত উপায় dictionary তৈরি করার জন্য।

# lst =[1,2,2,3,3,4,5,6,6]
# dictt={item:lst.count(item) for item in lst}
# print(dictt)

#enumerate(lst) হচ্ছে Python-এর একটা ফাংশন, যেটা প্রতিটি element-এর index এবং value দুটোই দেয়।
#for i, j in enumerate(lst):
    #print(f"Index = {i}, Value = {j}")

lst =[1,5,7,3,9,12,6,8]
value =5

new_lst=[i for i,j in enumerate(lst) if j>value]
print(new_lst)