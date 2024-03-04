# Paul Evans (pevans@sandiego.edu)
# 25 February 2024
import re
def main():
    intro = 'Humanum genus duobis regitur'
    print(intro)
    # regular expression demo for Jake Bayon
    result = re.match('.', intro)
    print(result[0])
    result = re.match('.*', intro)
    print(result[0])
    result = re.match('.*?', intro)
    print(result)
    result = re.split(' ', intro)
    print(result)
    result = re.match('genus.*?duobus', intro)
    print(result)

if __name__ == "__main__":
    main()