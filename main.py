def calc_time_for_gunmarks(tank):

    gun = tank[0]
    alpha = tank[1]
    reload = tank[2]
    gunmarks = tank[3]

    alphas = [alpha * 0.75, alpha, alpha * 1.25]

    times_needed = []

    if gun == "single":

        for gm in gunmarks:

            times = []

            for alpha in alphas:

                deal = []

                done = alpha
                time = 0

                while done < gm:
                    time += reload
                    done += alpha

                shots = time / reload

                print(f"Inspected gunmark: {gm} for Alpha {alpha} needs {time} seconds equal to {shots} shots!")

                deal.append(time)
                deal.append(shots)

                times.append(deal)

            times_needed.append(times)
    elif gun == "magazine":
        print("is magazine")
    elif gun == "autoreload":
        print("is autoreload")
    else:
        print(f"unknown gun type {gun}")

    return times_needed


# The main method
tank1 = ["single", 490, 12.5, [2500, 3000, 3750]]
tank2 = ["magazine", 280, 3, [2500, 3000, 3750], 4, 38.5]
tank3 = ["autoreload", 280, 2.5, [2500, 3000, 3750], 3, [10.5, 8.7, 6.5]]

tank1.append(calc_time_for_gunmarks(tank1))
tank2.append(calc_time_for_gunmarks(tank2))
tank3.append(calc_time_for_gunmarks(tank3))

print(tank1)
print(tank2)
print(tank3)
