# If a yearly reduction of a certain percent is included, this function calculates the real monthly rate
def calculate_reduced_monthly_rate(monthly_interest_rate, yearly_interest_reduction):
    annual_interest_rate = calculate_annual_rate(monthly_interest_rate)  # Convert monthly to annual
    reduced_annual_interest_rate = annual_interest_rate - yearly_interest_reduction  # Apply yearly reduction
    return ((1 + reduced_annual_interest_rate) ** (1 / 12)) - 1  # Convert annual back to monthly

# Calculates the annual interest rate from the given monthly interest rate
def calculate_annual_rate(monthly_rate):
    return ((1 + monthly_rate) ** 12) - 1

# Calculates the monthly payment
def calculate_monthly_payment(principal, monthly_interest_rate, term_months):
    return (principal * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -term_months) # Calculate monthly payment

# Calculates and prints the statistics for each month's payment
def calculate_interest_and_principal(principal, monthly_interest_rate, term_months, monthly_payment):
    print(f"For {principal} principal, {term_months} months of term and {monthly_interest_rate:.6f}% monthly interest rate ")
    print(f"Monthly Payment: {monthly_payment:.2f}")
    print(f"Total Payment: {(monthly_payment * term_months):.2f}")
    interest_paid = 0
    principal_paid = 0
    remaining_principal = principal
    for i in range(term_months):
        interest_this_month = remaining_principal * monthly_interest_rate # Calculate interest of the month
        interest_paid += interest_this_month # Calculate total paid interest
        principal_this_month = monthly_payment - interest_this_month # Calculate total paid principal
        principal_paid += principal_this_month # Calculate total paid principle so far
        remaining_principal -= principal_this_month # Calculate remaining principal debt
        print(f"Month {i+1}: Interest Paid: {interest_this_month:.2f}, Total Interest Paid: {interest_paid:.2f}, Principal Paid: {principal_this_month:.2f}, Total Principle Paid: {principal_paid:.2f} Remaining Principal: {remaining_principal:.2f}")

# Takes principal(amount of loan), monthly_interest_rate, and yearly rate reduction and calculates everything related to the loan
def main(principal, term_months, monthly_interest_rate, yearly_rate_reduction=0):
    monthly_interest_rate = monthly_interest_rate / 100
    print(monthly_interest_rate)
    if yearly_rate_reduction != 0:
        yearly_rate_reduction = yearly_rate_reduction / 100
        monthly_interest_rate = calculate_reduced_monthly_rate(monthly_interest_rate, yearly_rate_reduction)
    monthly_payment = calculate_monthly_payment(principal, monthly_interest_rate, term_months)
    calculate_interest_and_principal(principal, monthly_interest_rate, term_months, monthly_payment)

principal = 2500000
monthly_interest_rate = 0.69
yearly_reduction = 0.25
term_months = 180
main(principal, term_months, monthly_interest_rate, yearly_reduction)