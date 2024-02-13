
# Jake
# 12 February 2024

# list comprehensions 

def main():
    print("hello world")

    list_1 = ["gratian", "monk", "hildegard"]
    list_2 = ["canon", "gratian", "monk"]

    # list comprehensions
    print([word for word in list_1 if word not in list_2])
    
if __name__ == "__main__":
    main()
    