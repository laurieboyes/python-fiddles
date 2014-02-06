print ("Welcome to TeaMaster 2014")
print ("=========================")

milkAnswer = input("Milk, dear? ")
milk = milkAnswer.upper().startswith("Y")
sugarAnswer = input("Any sugar? ")
sugar = sugarAnswer.upper().startswith("Y")

print("")

if(sugar):
    print("   **")
    print("   **\n")
    
if(milk):
    print("C|-------|")
    print("  \_____/\n")
else:
    print("C|%%%%%%%|")
    print("  \%%%%%/\n")

print("Here you are!")