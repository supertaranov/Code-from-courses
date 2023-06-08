# Zoom challenged Flash to a fair duel in the form of a race around a magnetar. 
# If he lost, this neutron star would charge up and destroy the world, 
# so Flash decided not to risk it for no reason, and asked his friend Cisco Ramon 
# if it made sense to accept the challenge. Cisco received data that Zoom's speed was n, and Flash's speed is k.

# Write a program that should output Cisco's answer to Flash's question.

# Input Data Format:
# The input to the program is two integers n and k, the speed of Zoom and Flash.

# Output data format:
# If Zoom is faster than Flash output "NO", if Flash is faster than Zoom output "YES", 
# if their speeds are equal output "Don't know".

n, k, = int(input()), int(input())

if n < k:
    print('YES')
elif n > k:
    print('NO')
elif n == k:
    print("Don't know")