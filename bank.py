text = input("Приветствие: ")
if text.startswith("здравствуйте"):
    print("$0")
elif text.startswith("з"):
    print("$20")
else:
    print("$100")
