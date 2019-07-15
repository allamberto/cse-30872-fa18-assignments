#!/usr/bin/env python3
import sys

def can_see(GT, BT):
    GT = sorted(GT)
    BT = sorted(BT)
    for count, player in enumerate(BT):
        if player <= GT[count]:
            return False
    return True


if __name__ == '__main__':
    teams = []
    for line in sys.stdin:
        team = [int(x) for x in line.split(" ")]
        teams.append(team)

        if(len(teams) % 2 == 0):
            BT = teams.pop()
            GT = teams.pop()
            if can_see(GT, BT):
                print('Yes')
            else:
                print('No')
