def main():
    rank = 0
    number = int(input(""))
    while (number > 0):
      number = number//10
      rank = rank + 1
    print (rank)

if __name__ == '__main__':
    main()
