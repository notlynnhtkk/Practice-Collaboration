#! /Users/linnhtet/anaconda3/bin/python

def rearrange_name(full_name):
    # Split the full name into Last Name and First Name
    last_name, first_name = full_name.split(', ')

    # Rearrange and format the names
    new_name = f"{first_name} {last_name}"

    return new_name

# Get input from the user
input_name = input("Enter a name in 'Last Name, First Name' format: ")

# Call the function to rearrange the name
output_name = rearrange_name(input_name)

# Display the result
print(f"Input Name: {input_name}")
print(f"Output Name: {output_name}")
