
BASE_PAY = 51382.78

def main():
    first_name, last_name, job_class, education_level, merit_rating, service_rank, service_years = user_input()

    job_percent = job_class_percentage(job_class)
    education_percent = education_percentage(education_level)
    merit_percent = merit_percentage(merit_rating)
    service_percent = service_percentage(service_rank)

    final_salary = calculate_salary(job_percent, education_percent, merit_percent, service_percent, service_years)

    print("\n" + first_name + " " + last_name + ", \n")
    print("Welcome to Google Inc! Based on your job classification as " + job_class + ", your education")
    print("level of " + education_level + ", your " + merit_rating + " merit rating, and your " + str(service_years) + " years of experience as a")
    print(service_rank + ", your salary is $" + f"{final_salary:,.2f}" + ". \n")
    print("Regards, \n")
    print("Google")

def user_input():
    print("Welcome to the Google Salary Calculator!")
    first_name = input("Please enter your First Name: ")
    last_name = input("Please enter your Last Name: ")
    job_class = input("Please enter your Job Classification (New Hire, Manager, Programmer, Senior Dev, Executive): ")
    education_level = input("Please enter your Education Level (High School, Junior College, College, Masters, PhD): ")
    merit_rating = input("Please enter your Merit Ranking (Poor, Good, Excellent): ")
    service_rank = input("Please enter your Service Rank Name (New Hire – 0-5 yrs, Journeyman – 6-10 yrs, Senior – 11+ yrs): ")
    service_years = int(input("Please enter the number of years you have worked here: "))
    return first_name, last_name, job_class, education_level, merit_rating, service_rank, service_years

def job_class_percentage(job_class):
    if job_class == "New Hire":
        return 0.50
    if job_class == "Manager":
        return 0.70
    if job_class == "Programmer":
        return 0.90
    if job_class == "Senior Dev":
        return 1.10
    if job_class == "Executive":
        return 1.30


def education_percentage(education_level):
    if education_level == "High School":
        return 0.40
    if education_level == "Junior College":
        return 0.65
    if education_level == "College":
        return 0.80
    if education_level == "Masters":
        return 0.95
    if education_level == "PhD":
        return 1.10

def merit_percentage(merit_rating):
    if merit_rating == "Poor":
        return 0.00
    if merit_rating == "Good":
        return 0.10
    if merit_rating == "Excellent":
        return 0.25

def service_percentage(service_rank):
    if service_rank == "New Hire":
        return 0.03
    if service_rank == "Journeyman":
        return 0.05
    if service_rank == "Senior":
        return 0.07

def calculate_salary(job_percent, education_percent, merit_percent, service_percent, years):
    return (BASE_PAY * job_percent) + (BASE_PAY * education_percent) + (BASE_PAY * merit_percent) + (BASE_PAY * service_percent * years)


if __name__ == "__main__":
    main()