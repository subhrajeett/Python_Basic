#positional arg: Checks for keyword match and set that value accordingly
def calculate_marks(maths,eng,hindi,comp=76):
    print(f"maths: {maths}")
    print(f"eng: {eng}")
    print(f"hindi: {hindi}")
    print(f"comp: {comp}")
    total=maths+eng+hindi+comp
    print(f"total: {total}") 

calculate_marks(eng=100,maths=98,comp=56,hindi=78)  