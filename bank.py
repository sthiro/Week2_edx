# Special Requirements => Case-insensitive, no leading whitespaces
# Be sure to give $0 not only for “hello” but also “hello there”, “hello, Newman”, and the like.

#if the greeting starts with an “h” (but not “hello”), output $20
#use str.startswith(prefix[, start[, end]])¶

Greeting = input("Greeting: ").strip().casefold() 
#Small letters and no blank space both side


if "hello" in  Greeting:
    print("0")
elif Greeting.startswith("h"):
    print("$20")
else:
    print("$100")