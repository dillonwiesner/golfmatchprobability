import csv

def calculateWinProb(points, holesLeft):
    # individual hole outcome probabilities. assume holes are independent events. next step is to incorporate an
    # ELO type mode to update these probabilities as match progresses
    W = .29
    T = .42
    L = .29

    # update for next recursive call
    newHolesLeft = holesLeft - 1
    pointsWithWin = points + 1
    pointsWithTie = points + .5
    pointsWithLoss = points

    # probability player will win the match this hole
    winThisHole = 0
    if points == 9:
        winThisHole = W + T
    elif points == 8.5:
        winThisHole = W

    # if match is already over probability of winning this hole is 0
    if points + holesLeft <= 9 or points > 9:
        return 0
    # otherwise add probability of winning this hole to probabilities of winning next hole conditional on W, L, or T
    else:
        return winThisHole + calculateWinProb(pointsWithWin, newHolesLeft)*W + \
               calculateWinProb(pointsWithTie, newHolesLeft)*T +\
               calculateWinProb(pointsWithLoss, newHolesLeft)*L

def calculateTieProb(points, holesLeft):
    # individual hole outcome probabilities. assume holes are independent events. next step is to incorporate an
    # ELO type mode to update these probabilities as match progresses
    W = .29
    T = .42
    L = .29

    # update for next recursive call
    newHolesLeft = holesLeft - 1
    pointsWithWin = points + 1
    pointsWithTie = points + .5
    pointsWithLoss = points

    # probability match will end in a tie this hole
    endInTieThisHole = 0
    if points == 9 and holesLeft == 1:
        endInTieThisHole = L
    elif points == 8.5 and holesLeft == 1:
        endInTieThisHole = T
    elif points == 8 and holesLeft == 1:
        endInTieThisHole = W
    # probably not necessary since initialized above but being safe
    else:
        endInTieThisHole = 0

    # if match cannot end in tie
    if points + holesLeft < 9 or points > 9:
        return 0
    # otherwise add probability of tying this hole to probabilities of tying next hole conditional on W, L, or T
    else:
        return endInTieThisHole + calculateTieProb(pointsWithWin, newHolesLeft) * W + \
               calculateTieProb(pointsWithTie, newHolesLeft) * T + \
               calculateTieProb(pointsWithLoss, newHolesLeft) * L

# main program
if __name__ == '__main__':
    titles = ["points", "holes left", "win probability", "tie probability"]
    initialStates = []
    writeRows = []

    # read in csv created from google sheet data with
    with open('startingconditions.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                initialStates.append([float(row[0]), float(row[1])])
                line_count += 1

    # for every starting condition calculate probability of win loss and tie
    counter = 0
    for state in initialStates:
        print("State " + str(counter) + ": " + str(state))
        counter += 1
        points = state[0]
        holesLeft = state[1]
        winProb = calculateWinProb(points, holesLeft)
        tieProb = calculateTieProb(points, holesLeft)
        row = [points, holesLeft, winProb, tieProb]
        writeRows.append(row)

    # write to csv
    with open('probabilities.csv', mode='w') as probabilities:
        probabilities_writer = csv.writer(probabilities, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        probabilities_writer.writerow(titles)

        for row in writeRows:
            probabilities_writer.writerow(row)







