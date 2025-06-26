lst =[1,5,7,3,9,12,6,8]

# def even_val(lst):
#     new_lst = []
#     for i in lst:
#         if i%2==0:
#             new_lst.append(i)
#     return new_lst

# print(even_val(lst))

#filter(function, iterable) filter(...) → list থেকে শুধু সেই সব সংখ্যা রাখে যেগুলো even
#Python-এ filter(), map() ইত্যাদি ফাংশনগুলো সরাসরি list দেয় না কিন্তু list(filter(function, iterable)) → result কে একটা পূর্ণ list বানায়


new_lst = list(filter(lambda x: x%2==0, lst))
print(new_lst)

value = 5
is_even = lambda x: x%2==0
print(is_even(value))