import sys

def formatter(number, formater):
    start = 0 
    formatted = ''
    for x in formater.split('-'):
        end = start + len(x)
        formatted =  formatted + number[start:end] + '-'
        start =  end
    formatted =  formatted[:-1]
    return  formatted
    
if __name__ == "__main__":
    result = formatter(sys.argv[1], sys.argv[2])
    print(result)