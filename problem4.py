date1 =  input("enter your date (dd/mm/yyyy) :").split("/")
lst = list(date1)
dict1 = {
    "01" : "jan",
    "02" : "feb",
    "03" : "march",
    "04" : "april",
    "05" : "may",
    "06" : "jun",
    "09" : "sept",
    "10" : "oct",
    "11" : "nov",
    "12" : "dec"

}
mon = dict1[lst[1]]

print(f"{lst[0]}/{mon}/{lst[2]}")