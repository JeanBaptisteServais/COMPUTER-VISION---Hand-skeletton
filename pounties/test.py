a = [([(85, 72), (78, 57), (78, 50), (75, 44)], 'I'),
     ([(74, 79), (61, 68), (53, 65), (46, 62)], 'M'),
     ([(64, 90), (57, 82), (50, 75), (46, 72)], 'An'),
     ([(61, 104), (50, 100), (43, 96), (36, 93)], 'a'),
     ([(99, 97), (113, 89), (123, 79), (130, 68)], 'thumb')]


#((82, 103), (99, 97))

last = [(82, 103)]

aa = []
for i in a:
    if i[1] == "thumb":
        i = last + i[0]
    aa.append(i)


bb = []
bb.append(aa[-1])
for i in aa[:-1]:
    bb.append(i[0])

b = [j for i in bb for j in i]


c = []
for i in range(len(b)):
    if i == 0:
        c.append((b[0], b[1]))
    else:
        if i < len(b) -1:
            c.append((b[i], b[i + 1]))
print(c)


def retreatement_points(palm_center, points_sorted):

    reput_center_palm = []
    for i in points_sorted:
        if i[1] == "thumb":
            i = palm_center + i[0]
        reput_center_palm.append(i)

    put_finger_order = []
    put_finger_order.append(reput_center_palm[-1])
    put_finger_order += [i[0] for i in reput_center_palm[:-1]]

    all_points = [j for i in put_finger_order for j in i]

    reorganize_by_pair = []
    for i in range(len(all_points)):
        if i == 0:
            reorganize_by_pair.append((all_points[0], all_points[1]))
        else:
            if i < len(all_points) -1:
                reorganize_by_pair.append((all_points[i], all_points[i + 1]))

    return reorganize_by_pair


points_sorted = [([(85, 72), (78, 57), (78, 50), (75, 44)], 'I'),
     ([(74, 79), (61, 68), (53, 65), (46, 62)], 'M'),
     ([(64, 90), (57, 82), (50, 75), (46, 72)], 'An'),
     ([(61, 104), (50, 100), (43, 96), (36, 93)], 'a'),
     ([(99, 97), (113, 89), (123, 79), (130, 68)], 'thumb')]

palm_center = [(82, 103)]

a = retreatement_points(palm_center, points_sorted)
print(a)







