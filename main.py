def calc_time_for_gunmarks(alpha, reload, gunmarks):

    alphas = [alpha * 0.75, alpha, alpha * 1.25]

    times_needed = []

    i = 0

    for gm in gunmarks:
        counter = 0
        j = 0

        for alpha in alphas:

            done = alpha
            time = 0

            while done < gm:
                time += reload
                done += alpha

            shots = time / reload

            print(f"Inspected gunmark: {gm} for Alpha {alpha} needs {time} seconds equal to {shots} shots!")

            times_needed.append(time)

            j += 1

        i += 1

    return times_needed


# The main method
alpha = 490
reload = 12.5
gunmarks = [2500, 3000, 3750]

times = calc_time_for_gunmarks(alpha, reload, gunmarks)

print(times)
