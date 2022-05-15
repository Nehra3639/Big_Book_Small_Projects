# Print the horizontal number labels

print('---------------------------------------------------------------------------------------')
print('---N---|---0---|---1---|---2---|---3---|---4---|---5---|---6---|---7---|---8---|---9---|')
print('---------------------------------------------------------------------------------------')


# Display each row of products:
for number1 in range(0, 11):

    # Print the vertical numbers labels:
    print(str(number1).rjust(6), end='')

    # Print a separating bar:
    print(' | ', end='')

    # Print the product followed by a space:
    for number2 in range(0, 10):
        print(str(number1 * number2).rjust(3), end='')
        print('   |'*1, end=' ')

    # Finish the row by printing a newline
    print('')
