#defaul arg: Incase if you're not sending a value to a parameter
#Can set a default value to it
#Example: In the below case for comp we can set 76 default 

def calculate_marks(maths,eng,hindi,comp=76):
    print(f"maths: {maths}")
    print(f"eng: {eng}")
    print(f"hindi: {hindi}")
    print(f"comp: {comp}")
    total=maths+eng+hindi+comp
    print(f"total: {total}")

calculate_marks(34,45,67)