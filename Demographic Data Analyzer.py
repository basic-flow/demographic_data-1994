import pandas as pd


def calculate_demographic_data(print_data=True):
    df = pd.read_csv('adult.data.csv')


    race_count = pd.Series(df["race"].value_counts())

    average_age_men = round(df[df['sex']== 'Male']['age'].mean(),1)

    
    percentage_bachelors = round((len(df[df['education']== 'Bachelors'])/ len(df['education']))*100,1)

    
    higher_education = len(df[((df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')) & (df['salary'] == '>50K')]) 
    
    lower_education = len(df[((df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate')) & (df['salary'] == '>50K')]) 

    higher_education_rich = round((higher_education/ len(df[((df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate'))]))*100,1)
    lower_education_rich = round((lower_education / len(df[((df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate'))]))*100,1)

    min_work_hours = df['hours-per-week'].min()

    num_min_workers = len(df[(df['hours-per-week'] == 1) & (df['salary'] == '>50K')])

    rich_percentage = round((num_min_workers/len(df[(df['hours-per-week'] == 1)]))*100,1)

    highest_earning_country = round((df[(df['salary']== '>50K')]['native-country'].value_counts()/df['native-country'].value_counts())*100,1).sort_values(ascending= False).index[0]
    highest_earning_country_percentage = round((df[(df['salary']== '>50K')]['native-country'].value_counts()/df['native-country'].value_counts())*100,1).sort_values(ascending= False)[0]

    
    top_IN_occupation = df[(df['salary']== '>50K') & (df['native-country'] == 'India')]['occupation'].value_counts().index[0]

    if print_data:
        print('\n------------------------------------------------------\n',"Number of each race:\n", race_count,'\n------------------------------------------------------\n') 
        print("Average age of men:", average_age_men,'\n------------------------------------------------------\n')
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%",'\n------------------------------------------------------\n')
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%",'\n------------------------------------------------------\n')
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%",'\n------------------------------------------------------\n')
        print(f"Min work time: {min_work_hours} hours/week",'\n------------------------------------------------------\n')
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%",'\n------------------------------------------------------\n')
        print("Country with highest percentage of rich:", highest_earning_country,'\n------------------------------------------------------\n')
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%",'\n------------------------------------------------------\n')
        print("Top occupations in India:", top_IN_occupation,'\n------------------------------------------------------\n')

    return {
        'race_count': race_count ,
        'average_age_men': average_age_men,
        
        'percentage_bachelors': percentage_bachelors,
        
        'higher_education_rich': higher_education_rich,
        
        'lower_education_rich': lower_education_rich,
        
        'min_work_hours': min_work_hours,
        
        'rich_percentage': rich_percentage,
        
        'highest_earning_country': highest_earning_country,
        
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        
        'top_IN_occupation': top_IN_occupation
    }
print(calculate_demographic_data())
