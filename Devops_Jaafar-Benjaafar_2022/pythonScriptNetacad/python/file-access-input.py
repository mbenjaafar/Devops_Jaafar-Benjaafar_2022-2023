file = open("devices.txt","a")
while True:
    newItem = input("Enter device name")
    if newItem == "exit":
        file.close()
        print("All done!")
        break
    file.write(newItem + "\n")

