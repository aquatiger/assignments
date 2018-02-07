doformatter = "%r %r %r %r"

print(doformatter % (1, 2, 3, 4))
print(doformatter % ("one", "two", "three", "four"))
print(doformatter % (True, False, False, True))
print(doformatter % (doformatter, doformatter, doformatter, doformatter))
print (doformatter % (
    "I had this thing." + "\n",
    "That you could type up right.\n",
    "But it didn't sing.\n",
    "So I said goodnight.\n"
))
