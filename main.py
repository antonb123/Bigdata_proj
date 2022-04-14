from math import sqrt
import pandas as pd


def main():
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)

    male_df = pd.read_csv('male.csv')
    male_skimmed = male_df[['stature', 'weightkg', 'chestcircumference', 'waistcircumference']]
    male_skimmed.to_csv('male_skimmed.csv')
    male_skimmed_with_size = pd.read_csv("male_skimmed.csv")
    male_skimmed_with_size.drop(male_skimmed_with_size.columns[0], axis=1, inplace=True)

    female_df = pd.read_csv('female.csv')
    female_skimmed = female_df[['stature', 'weightkg', 'chestcircumference', 'waistcircumference']]
    female_skimmed.to_csv('female_skimmed.csv')
    female_skimmed_with_size = pd.read_csv('female_skimmed.csv')
    female_skimmed_with_size.drop(female_skimmed_with_size.columns[0], axis=1, inplace=True)

    m_sizes = []
    for chest, waist in zip(male_skimmed_with_size['chestcircumference'], male_skimmed_with_size['waistcircumference']):
        if chest <= 880:
            if waist <= 730:
                m_sizes.append('xs')
            else:
                m_sizes.append('s')
        elif chest <= 960:
            if waist <= 810:
                m_sizes.append('s')
            else:
                m_sizes.append('m')
        elif chest <= 1040:
            if waist <= 890:
                m_sizes.append('m')
            else:
                m_sizes.append('l')
        elif chest <= 1120:
            if waist <= 970:
                m_sizes.append('l')
            else:
                m_sizes.append('xl')
        elif chest <= 1240:
            if waist <= 1090:
                m_sizes.append('xl')
            else:
                m_sizes.append('xxl')
        elif chest <= 1360:
            if waist <= 1210:
                m_sizes.append('xxl')
            else:
                m_sizes.append('xxxl')
        elif chest <= 1480:
            if waist <= 1330:
                m_sizes.append('xxxl')
            else:
                m_sizes.append('xxxxl')

    male_skimmed_with_size['size'] = m_sizes

    f_sizes = []
    for chest, waist in zip(female_skimmed_with_size['chestcircumference'], female_skimmed_with_size['waistcircumference']):
        if chest <= 830:
            if waist <= 670:
                f_sizes.append('xs')
            else:
                f_sizes.append('s')
        elif chest <= 900:
            if waist <= 740:
                f_sizes.append('s')
            else:
                f_sizes.append('m')
        elif chest <= 970:
            if waist <= 810:
                f_sizes.append('m')
            else:
                f_sizes.append('l')
        elif chest <= 1040:
            if waist <= 880:
                f_sizes.append('l')
            else:
                f_sizes.append('xl')
        elif chest <= 1140:
            if waist <= 980:
                f_sizes.append('xl')
            else:
                f_sizes.append('xxl')
        elif chest <= 1240:
            if waist <= 1140:
                f_sizes.append('xxl')
            else:
                f_sizes.append('xxxl')
        elif chest <= 1340:
            if waist <= 1240:
                f_sizes.append('xxxl')
            else:
                f_sizes.append('xxxxl')

    female_skimmed_with_size['size'] = f_sizes

    sex = input("Are you a male or female? Press 0 for male or 1 for female: ")
    user_length = int(input("Enter your length in mm: "))
    user_weight = int(input("Enter your weight in hg: "))
    nearest_neighbor = []

    if sex == 0:
        for length, weight in zip(male_skimmed_with_size['stature'], male_skimmed_with_size['weightkg']):
            delta_y = user_length - length
            delta_x = user_weight - weight
            hypotenuse = sqrt(delta_y ** 2 + delta_x ** 2)
            nearest_neighbor.append(hypotenuse)
    else:
        for length, weight in zip(female_skimmed_with_size['stature'], female_skimmed_with_size['weightkg']):
            delta_y = user_length - length
            delta_x = user_weight - weight
            hypotenuse = sqrt(delta_y ** 2 + delta_x ** 2)
            nearest_neighbor.append(hypotenuse)

    if sex == 0:
        male_skimmed_with_size['Nearest_neighbor'] = nearest_neighbor
    else:
        female_skimmed_with_size['Nearest_neighbor'] = nearest_neighbor

    if sex == 0:
        print(male_skimmed_with_size.sort_values(by=['Nearest_neighbor']).head(10))

        j = male_skimmed_with_size.sort_values(by=['Nearest_neighbor']).head(10)
        print(j.iat[0, 4], "is the t-shirt size you are looking for")
    else:
        print(female_skimmed_with_size.sort_values(by=['Nearest_neighbor']).head(10))

        j = female_skimmed_with_size.sort_values(by=['Nearest_neighbor']).head(10)
        print(j.iat[0, 4], "is the t-shirt size you are looking for")


if __name__ == '__main__':
    main()
