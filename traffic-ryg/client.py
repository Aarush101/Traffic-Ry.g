import modules
from modules.traffic import Traffic
from modules.fireDetection import FireDetect

class main:
    def __init__(self) -> None:

        while True:
            print('What do you want to do?\n1.Fire Detection\n2.Infrastructural\n (ENTER Q TO QUIT)')
            choice=input("Enter your choice:")
            if choice == '1':
                F = FireDetect()
                print("---------------")
                print()
            
            elif choice == '2':
                tf = Traffic()
                tf.rndShuffle("mock")
                tf.sampleGeneraton("shuffled")
                tf.speedGen()
                tf.conges_check()
                print("---------------")
                print()
            
            elif choice.lower() == 'q':
                print("Quiting....")
                print("---------------")
                print()
                break

            
            else:
                print("Enter Valid Input.")
                print("---------------")
                print()



if __name__ == "__main__":
    m = main()