# try:
#     print(5/0)
#     break
# except:
#     print("Sorry, something went wrong...")
# except (ValueError, ZeroDivisionError):
#     print("Too bad...")

nums = [1,2,3]
vals = nums
del vals[:]
print(vals)