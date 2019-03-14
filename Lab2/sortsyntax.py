


sort() Parameters
By default, sort() doesn't require any extra parameters. However, it has two optional parameters:

reverse - If true, the sorted list is reversed (or sorted in Descending order)
key - function that serves as a key for the sort comparison




Sorting dictionary:


charcount={ch : 0 for ch in [chr(i) for i in range(97, 123)]}


reqdlist=sorted(charcount, key = lambda i : charcount[i],reverse=True)