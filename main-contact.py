from pyscript import display, document # pyright: ignore[reportMissingImports]

location = "67 Ramen St., Greenhills San Juan City, Philippines" #string
numbers = ["+63 912 345 6789", "+63 987 654 3210"] #list
emails = ["admin@rumiyeons.com", "support@rumiyeons.com"] #list
business_hours = 'Open 10:00 - 22:00 ;)' #string


#displaying everything :p
display(f'Location: {location}', target="location-info")
display(f'Contact Numbers:\n' + '\n'.join(numbers), target="contact-numbers")
display(f'Emails:\n' + '\n'.join(emails), target="email-addresses")
display(business_hours, target="resto-hours")