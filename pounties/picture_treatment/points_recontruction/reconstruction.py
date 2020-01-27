
"""Here's librairy treatment"""
import cv2
import ast
import math
import numpy as np
from scipy.spatial import distance as dist

"""Here's csv treatment"""
from utils_reconstruction import csv_files
from utils_reconstruction import recuperate_data_in_csv


"""Here's data treatment"""
from utils_reconstruction import collect_distances
from utils_reconstruction import *



def recuperate_data(csv_names):

    """Recuperate data"""
    data_csv = recuperate_data_in_csv(csv_names)
    return data_csv


def Treatement_passation(points, ratio):

    """Treatement of our passation point to reconstruct
    Recuperate distance, scale and angulus."""

    #Distance of thumb, index .. annular and ratio (scale).
    passation_distance, passation_scale = collect_distances(points, ratio)

    #Collect points like (15, 5) -> 15 to right, 5 to top.
    x_y_absice = collect_points(points)

    #Atan of angle.
    passation_angles = points_to_angle(x_y_absice)

    #Search none detection points.
    searching_points = what_we_need_to_search(passation_distance)
    print(searching_points, "\n")

    info_passation = passation_distance, passation_scale,\
                     passation_angles, searching_points

    return info_passation

def compare_passation_data(data_csv, passation_distance, passation_angles, passation_scale):

    """Begenning to compare passation and data csv."""

    liste_informations_angle = []
    liste_informations_distance = []

    for data in data_csv:

        """Treatment data."""
        #Recuperate distance of thumb, index ... annular and ratio.
        data_distance, data_scale = collect_distances(data[0], data[1])

        #Collect points like (15, 5) -> 15 to right, 5 to top.
        points_data = collect_points(data[0])

        #Atan of angle.
        angle_data = points_to_angle(points_data)

        #Define ratio to normalise distance beetween
        #CSV data and data passation.
        norm = determine_ratio(data_scale, passation_scale)

        """Recup data."""

        #Make a difference beetween data and passation (distance and angle).
        distance = proximum_distance(passation_distance, data_distance, norm)
        angle = proximum_distance(passation_angles, angle_data, 1)


        """Stock data."""

        #Append it to appropriate list.
        liste_informations_distance.append(distance)
        liste_informations_angle.append(angle)


    return liste_informations_distance, liste_informations_angle, norm




def minimum_distance_angle(liste_informations_distance, liste_informations_angle,
                            searching_points):

    """Search the minimum (distance angle) for rebuilt phax"""

    #Make a melting of dist, angle as [liste_info, angle].
    distance_angle = melting_angle_distance(liste_informations_distance,
                           liste_informations_angle, searching_points)

    #Make sum of informations.
    sum_dist_angle = recuperate_sum_distance_angle(distance_angle)

    #Recuperate minimum sum beetween passation and data.
    minimum_distance_angle = recuperate_minimum_distance_dist_angle(sum_dist_angle)

    dico_final_dst_angle = put_informations_to_dictionnary(minimum_distance_angle)

    return dico_final_dst_angle


def minimum_finger_distance():

    """Search the minimum distance from finger not found"""

    #Recuperate fingers data interest == (None detection in passation).
    fingers = recuperate_fingers_interest(liste_informations_distance, searching_points)

    #Make sum from phaxs finger(s).
    sum_distance_finger = make_sum_finger_interest(fingers)

    #Recuperate minimum distance beetween finger's data
    #and finger passation.
    #ex search index -> dist of thumb and major.
    minimum_finger = minimum_fingers(sum_distance_finger)

    dico_final_finger = put_informations_to_dictionnary(minimum_finger)

    print(dico_final_finger)

def remplacing_passation_points(searching_points, dico_final_dst_angle, norm, points, data_csv):

    """Replace old points to new points"""

    #phax = fingers_points(finger, points_data, points_to_change, norm)

    dico_for_liste = {"t" :0, "i" : 1, "m" : 2, "an" : 3, "a" : 4}
    for k, v in searching_points.items():
        if searching_points[k] != ["None"]:
            print(k, v)
            if dico_final_dst_angle[k] != []:
                print(dico_final_dst_angle[k])
                points = phax_points(k, norm, data_csv, dico_final_dst_angle[k], v, points)

##
##            if dico_final_finger[k] != []:
##                print(dico_final_finger[k])
##                points = fingers_points(k, data_csv[dico_final_finger[k]][0], points, norm)


    blank_image1 = np.zeros((500, 500, 3), np.uint8)
    [cv2.circle(blank_image1, (j[0], j[1]) , 2, (0, 0, 255), 2) for i in points for j in i]

    #cv2.imshow("blanck", blank_image1)
    #cv2.waitKey(0)








def reconstruction(points, ratio, image):

    data_csv = recuperate_data(1)

    info_passation = Treatement_passation(points, ratio)

    passation_distance, passation_scale,\
    passation_angles, searching_points = info_passation

##    print(passation_distance)
##    print(passation_angles)
##    print(searching_points)

    liste_informations_distance, liste_informations_angle, norm\
    = compare_passation_data(data_csv, passation_distance, passation_angles, passation_scale)



    dico_final_dst_angle = minimum_distance_angle(liste_informations_distance,
                                                  liste_informations_angle, searching_points)
    print(dico_final_dst_angle)

    
    remplacing_passation_points(searching_points, dico_final_dst_angle, norm, points, data_csv)

    print(data_csv[33])



if __name__ == "__main__":


    image = "a"
    points = [((0, 0), (0, 0)), ((97, 105), (115, 94)), ((115, 94), (122, 79)), ((122, 79), (126, 69)), ((0, 0), (0, 0)), ((86, 76), (83, 55)), ((83, 55), (83, 47)), ((83, 47), (83, 40)), ((0, 0), (0, 0)), ((75, 79), (68, 55)), ((0, 0), (0, 0)), ((0, 0), (0, 0)), ((0, 0), (0, 0)), ((0, 0), (0, 0)), ((0, 0), (0, 0)), ((0, 0), (0, 0)), ((0, 0), (0, 0)), ((51, 98), (44, 91)), ((44, 91), (40, 94)), ((40, 94), (41, 90))]
    ratio = (31, 31, 113, 109)

    reconstruction(points, ratio, image)
    













