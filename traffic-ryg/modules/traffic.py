import pandas as pd 
import numpy as np
from .consts import DISTANCES


class Traffic:
    def __init__(self):
        self.places = []

    def rndShuffle(self, filename):
        df = pd.read_csv(f"assets/{filename}.csv")
        shuffled = df.sample(frac = 1, random_state= 1).reset_index()
        shuffled.to_csv("assets/shuffled.csv")

    def sampleGeneraton(self, filename):
        _ = []
        while (sum(_)<1500):
            X = np.random.randint(70, 140)
            _.append(X)
        
        _.pop()
        cum = [sum(_[0:i:1]) for i in range(0, len(_))]
        cum.pop(0)

        df = pd.read_csv(f"assets/{filename}.csv")
        usedPlaces = []
        for i in range(0, len(cum)):
            if i == 0:
                sample = df[0:cum[i]]
            else:
                sample = df[cum[i-1]:cum[i]]
            
            while True:
                placeName = chr(np.random.randint(97, 122))
                if placeName not in usedPlaces:
                    break 

            flyChoice = np.random.choice([0, 1])
            underChoice = np.random.choice([0, 1])

            sample['Place'] = placeName
            sample['Has_Flyover'] = flyChoice
            sample['Has_Underpass'] = underChoice

            sample = sample.reset_index()

            sample.to_csv(f"assets/place-{placeName}.csv")
            self.places.append(f"assets/place-{placeName}.csv")

    def speed(self, nodeOneTime, nodeTwoTime, distance):
        # return (abs(nodeTwoTime - nodeOneTime))/ distance
        return distance / (abs(nodeTwoTime - nodeOneTime))

    def avg_speed(self, l):
        return sum(l) / len(l)

    def timeConvert(self, time):
        if not(time == "nan"):
            # print(time)
            hours, mins, secs = map(int, time.split(":"))
            return hours + (mins / 60 ) + (secs / 3600)
        else:
            return 0

    def speedGen(self):
        print(self.places)
        for place in self.places:
            averages = []
            df = pd.read_csv(place)
            speed_list=[]
            for index in df.index:
                row = df.iloc[index]
                # print(row)
                for i in range(6):
                    for j in range(i+1, 6):

                        nodeOne = row[f"time_node_{i+1}"]
                        nodeTwo = row[f"time_node_{j+1}"]

                        s = self.speed(self.timeConvert(str(nodeOne)), self.timeConvert(str(nodeTwo)), DISTANCES[i, j])
                        row[f'speed_{i}_{j}'] = s
                        if s!=float('inf'):
                            speed_list.append(s)
                averages.append(self.avg_speed(speed_list))
            df['avg_speed'] = averages
            df.to_csv(place)
            print(f"Average Speed Calculated and Pushed into dataset. - {place}")
    
    def conges_check(self):
        pass

    def debugReset(self):
        pass              
